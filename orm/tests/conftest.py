import pytest
from sqlalchemy import create_engine, distinct
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database

from cfg.engine import db_url

import orm.models
from orm.models.main import Base
from orm.consts.protocol_type import ProtocolType


@pytest.mark.order(1)
@pytest.fixture(scope='class')
def session():
    test_engine = create_engine(db_url)
    TestSession = sessionmaker(test_engine)
    session = TestSession()
    yield session
    session.close()


@pytest.mark.order(2)
@pytest.fixture(scope='class', autouse=True)
def clear_db_before_usage():
    if database_exists(db_url):
        drop_database(db_url)
    create_database(db_url)
    test_engine = create_engine(db_url)
    Base.metadata.create_all(test_engine)


@pytest.mark.order(3)
@pytest.fixture(scope='class', autouse=True)
def h_labels(session):
    label_names = ['HASH_USD', 'FUND_DEFI']
    label_notionals = ['USDT', 'USDT']

    for label_name, label_notional in zip(label_names, label_notionals):
        label = orm.models.HubLabels(
            h_label_name=label_name,
            h_label_notional=label_notional
        )
        session.add(label)
        session.commit()


@pytest.mark.order(4)
@pytest.fixture(scope='class', autouse=True)
def h_protocols(session):
    protocol_names = ['uniswap', 'balancer', 'cake']
    protocol_types = [ProtocolType.DEX, ProtocolType.STAKING, ProtocolType.SYNTHS]

    for protocol_name, protocol_type in zip(protocol_names, protocol_types):
        protocol = orm.models.HubProtocols(
            h_protocol_name=protocol_name,
            h_protocol_type=protocol_type
        )
        session.add(protocol)
        session.commit()


@pytest.mark.order(5)
@pytest.fixture(scope='class', autouse=True)
def h_chains(session):
    network_names = ['eth', 'bsc', 'opt']
    network_ids = [1, 2, 3]
    network_endpoints = ['eth.endpoint', 'bsc.endpoint', 'opt.endpoint']

    for network_name, network_id, network_endpoint in zip(network_names, network_ids, network_endpoints):
        chain = orm.models.HubChains(
            h_network_name=network_name,
            h_network_id=network_id,
            h_network_endpoint=network_endpoint
        )
        session.add(chain)
        session.commit()


@pytest.mark.order(6)
@pytest.fixture(scope='class', autouse=True)
def h_tokens(session):
    token_symbols = ['USDC', 'USDT', 'DAI', 'FRAX']
    token_decimals = [6, 18, 18, 18]

    for token_symbol, token_decimal in zip(token_symbols, token_decimals):
        token = orm.models.HubTokens(
            h_token_symbol=token_symbol,
            h_token_decimals=token_decimal
        )
        session.add(token)
        session.commit()


@pytest.mark.order(7)
@pytest.fixture(scope='class', autouse=True)
def h_addresses(session):
    addresses = [
        'USDCUSDT_uniswap_eth_address',
        'USDCUSDT_uniswap_bsc_address',
        'USDCDAI_uniswap_eth_address',
        'DAIFRAX_balancer_eth_address',
        'DAIUSDT_balancer_opt_address',
        'DAIUSDC_balancer_eth_address',
        'DAIUSDT_cake_bsc_address',
        'USDC_eth_address',
        'USDC_bsc_address',
        'USDT_eth_address',
        'USDT_bsc_address',
        'USDT_opt_address',
        'DAI_eth_address',
        'DAI_opt_address',
        'DAI_bsc_address',
        'FRAX_eth_address',
        'HASH_USD_bsc_address',
        'HASH_USD_eth_address',
        'HASH_USD_opt_address',
        'FUND_DEFI_bsc_address',
        'FUND_DEFI_eth_address',
        'FUND_DEFI_opt_address'
    ]

    for address in addresses:
        instance = orm.models.HubAddresses(
            h_address=address
        )
        session.add(instance)
        session.commit()


@pytest.mark.order(8)
@pytest.fixture(scope='class', autouse=True)
def h_abis(session):
    abi_lists = [
        'USDCUSDT_uniswap_eth_abi',
        'USDCUSDT_uniswap_bsc_abi',
        'USDCDAI_uniswap_eth_abi',
        'DAIFRAX_balancer_eth_abi',
        'DAIUSDT_balancer_opt_abi',
        'DAIUSDC_balancer_eth_abi',
        'DAIUSDT_cake_bsc_abi',
        'ERC20_abi'
    ]

    for abi_list in abi_lists:
        abi = orm.models.HubAbis(
            h_abi_list=abi_list
        )
        session.add(abi)
        session.commit()


@pytest.mark.order(9)
@pytest.fixture(scope='class', autouse=True)
def l_protocols_chains(session):
    h_protocols = session.query(orm.models.HubProtocols).all()
    h_chains = session.query(orm.models.HubChains).all()

    for h_protocol in h_protocols:
        for h_chain in h_chains:
            l_protocol_chain = orm.models.LinkProtocolsChains(
                h_protocol_id=h_protocol.h_protocol_id,
                h_chain_id=h_chain.h_chain_id
            )
            session.add(l_protocol_chain)
            session.commit()

    xcom = session.query(
        orm.models.LinkProtocolsChains,
        orm.models.HubProtocols,
        orm.models.HubChains
    ).join(
        orm.models.HubProtocols,
        orm.models.LinkProtocolsChains.h_protocol_id == orm.models.HubProtocols.h_protocol_id,
        isouter=True
    ).join(
        orm.models.HubChains,
        orm.models.LinkProtocolsChains.h_chain_id == orm.models.HubChains.h_chain_id,
        isouter=True
    ).all()
    return xcom


@pytest.mark.order(10)
@pytest.fixture(scope='class', autouse=True)
def l_addresses_chains(session):
    h_addresses = session.query(orm.models.HubAddresses).all()
    h_chains = session.query(orm.models.HubChains).all()

    for h_address in h_addresses:
        for h_chain in h_chains:
            if h_chain.h_network_name.lower() in h_address.h_address.lower():
                l_address_chain = orm.models.LinkAddressesChains(
                    h_address_id=h_address.h_address_id,
                    h_chain_id=h_chain.h_chain_id
                )
                session.add(l_address_chain)
                session.commit()

    xcom = session.query(
        orm.models.LinkAddressesChains,
        orm.models.HubAddresses,
        orm.models.HubChains
    ).join(
        orm.models.HubAddresses,
        orm.models.LinkAddressesChains.h_address_id == orm.models.HubAddresses.h_address_id,
        isouter=True
    ).join(
        orm.models.HubChains,
        orm.models.LinkAddressesChains.h_chain_id == orm.models.HubChains.h_chain_id,
        isouter=True
    ).all()
    return xcom


@pytest.mark.order(11)
@pytest.fixture(scope='class', autouse=True)
def l_addresses_abis_chains(session, l_addresses_chains):
    h_abis = session.query(orm.models.HubAbis).all()

    for h_abi in h_abis:
        for l_address_chain in l_addresses_chains:
            h_hetwork_name = l_address_chain[2].h_network_name
            h_address = l_address_chain[1].h_address

            # pools
            if h_abi.h_abi_list[:-4] == h_address[:-8] and h_hetwork_name in h_abi.h_abi_list:
                l_address_abi_chain = orm.models.LinkAddressesAbisChains(
                    l_address_chain_id=l_address_chain[0].l_address_chain_id,
                    h_abi_id=h_abi.h_abi_id
                )

                session.add(l_address_abi_chain)
                session.commit()

            # tokens
            elif h_address[:-12].lower() not in ('hash_usd', 'fund_defi') and \
                    h_abi.h_abi_list == 'ERC20_abi' and len(h_address) < 20:
                l_address_abi_chain = orm.models.LinkAddressesAbisChains(
                    l_address_chain_id=l_address_chain[0].l_address_chain_id,
                    h_abi_id=h_abi.h_abi_id
                )
                session.add(l_address_abi_chain)
                session.commit()

    xcom = session.query(
        orm.models.LinkAddressesAbisChains,
        orm.models.LinkAddressesChains,
        orm.models.HubChains,
        orm.models.HubAddresses
    ).join(
        orm.models.LinkAddressesChains,
        orm.models.LinkAddressesAbisChains.l_address_chain_id == orm.models.LinkAddressesChains.l_address_chain_id,
        isouter=True
    ).join(
        orm.models.HubAddresses,
        orm.models.LinkAddressesChains.h_address_id == orm.models.HubAddresses.h_address_id,
        isouter=True
    ).join(
        orm.models.HubChains,
        orm.models.LinkAddressesChains.h_chain_id == orm.models.HubChains.h_chain_id,
        isouter=True
    ).all()

    return xcom


@pytest.mark.order(12)
@pytest.fixture(scope='class', autouse=True)
def l_addresses_labels_chains(session, l_addresses_chains):
    h_labels = session.query(orm.models.HubLabels).all()

    for h_label in h_labels:
        for l_address_chain in l_addresses_chains:
            h_address = l_address_chain[1].h_address

            if h_label.h_label_name in h_address:
                l_address_label_chain = orm.models.LinkAddressesLabelsChains(
                    l_address_chain_id=l_address_chain[0].l_address_chain_id,
                    h_label_id=h_label.h_label_id
                )
                session.add(l_address_label_chain)
                session.commit()

    xcom = session.query(
        orm.models.LinkAddressesLabelsChains
    ).all()
    return xcom


@pytest.mark.order(13)
@pytest.fixture(scope='class', autouse=True)
def l_addresses_abis_tokens_chains(session, l_addresses_abis_chains):
    h_tokens = session.query(orm.models.HubTokens).all()

    for h_token in h_tokens:
        for l_address_abi_chain in l_addresses_abis_chains:
            h_address = l_address_abi_chain[3].h_address

            if h_address[:-12] == h_token.h_token_symbol:
                l_address_abi_token_chain = orm.models.LinkAddressesAbisTokensChains(
                    l_address_abi_chain_id=l_address_abi_chain[0].l_address_abi_chain_id,
                    h_token_id=h_token.h_token_id
                )
                session.add(l_address_abi_token_chain)
                session.commit()

    xcom = session.query(
        orm.models.LinkAddressesAbisTokensChains,
        orm.models.HubTokens
    ).join(
        orm.models.HubTokens,
        orm.models.LinkAddressesAbisTokensChains.h_token_id == orm.models.HubTokens.h_token_id,
        isouter=True
    ).all()
    return xcom


@pytest.mark.order(14)
@pytest.fixture(scope='class', autouse=True)
def l_addresses_abis_tokens_protocols_chains(
        session,
        l_protocols_chains,
        l_addresses_abis_tokens_chains,
        l_addresses_abis_chains
):
    hash_table = dict()

    for l_protocol_chain in l_protocols_chains:
        h_protocol_name = l_protocol_chain[1].h_protocol_name
        h_network_name = l_protocol_chain[2].h_network_name

        if h_network_name not in hash_table:
            hash_table[h_network_name] = dict()
        if h_protocol_name not in hash_table[h_network_name]:
            hash_table[h_network_name][h_protocol_name] = dict()

        for l_address_abi_token_chain in l_addresses_abis_tokens_chains:
            h_token_symbol = l_address_abi_token_chain[1].h_token_symbol
            for l_address_abi_chain in l_addresses_abis_chains:
                h_address = l_address_abi_chain[3].h_address
                if h_protocol_name in h_address and h_network_name in h_address and h_token_symbol in h_address:

                    if h_address not in hash_table[h_network_name][h_protocol_name]:
                        hash_table[h_network_name][h_protocol_name][h_address] = list()
                    if h_token_symbol not in hash_table[h_network_name][h_protocol_name][h_address]:
                        hash_table[h_network_name][h_protocol_name][h_address].append(h_token_symbol)

                        l_address_abi_token_protocol_chain = orm.models.LinkAddressesAbisTokensProtocolsChains(
                            l_protocol_chain_id=l_protocol_chain[0].l_protocol_chain_id,
                            l_address_abi_chain_id=l_address_abi_chain[0].l_address_abi_chain_id,
                            l_address_abi_token_chain_id=l_address_abi_token_chain[0].l_address_abi_token_chain_id
                        )

                        session.add(l_address_abi_token_protocol_chain)
                        session.commit()

    xcom = session.query(
        orm.models.LinkAddressesAbisTokensProtocolsChains
    ).all()
    return xcom


# TODO
@pytest.mark.order(15)
@pytest.fixture(scope='class', autouse=True)
def l_addresses_abis_tokens_protocols_labels_chains(
        session,
        l_addresses_abis_tokens_protocols_chains,
        l_addresses_labels_chains
):

    for l_address_abi_token_protocol_chain in l_addresses_abis_tokens_protocols_chains:
        for l_address_label_chain in l_addresses_labels_chains:
            l_address_abi_token_protocol_label_chain = orm.models.LinkAddressesAbisTokensProtocolsLabelsChains(
                l_address_abi_token_protocol_chain_id=l_address_abi_token_protocol_chain.l_address_abi_token_protocol_chain_id,
                l_address_label_chain_id=l_address_label_chain.l_address_label_chain_id
            )
            session.add(l_address_abi_token_protocol_label_chain)
            session.commit()


@pytest.mark.usefixtures()
class TestFixtures:

    def test_fixture(self, session):
        assert True
