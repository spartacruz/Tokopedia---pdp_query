# Tokopedia---pdp_query
A script to retrive information from tokopedia pdp

Just download the repo and make some modify on ``request gql_PDP_v02_with vpn.py``. Change the ``parent_dir`` directory based on your environtment.

To use this script, you need to provide ``1_nama_toko.txt`` (store name) & ``2_storeKeyPDP.txt``
Each sku product have a unique ``storeKeyPDP``

Have a look on this tokopedia sku link : https://www.tokopedia.com/onemed/aseptic-gel-500ml-refill-onemed

It contains : (tld/domain)/(nama_toko)/(storeKeyPDP).
Then, you could input it on txt file separately.

For mass query, i suggest you to use Nord-vpn to prevent blocking.
I used Nord-vpn + combined with another script https://github.com/kboghe/NordVPN-switcher that helps you to switch to another network after several query.


Will generate json file that contain all product_sku information on a PDP page. Later on, you could use this service https://data.page/ to transform it into tabular format.

NB:

*This code could be used as long as there is no significant change on tokopedia API

*Do with your own risk.

*I suggest for testing purpose only.
