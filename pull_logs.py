import meraki
# ################################################ PARAMETERS ##########################################################
# Configure you API Key and Organization Name below. One thousand logs per page (maximum).
# ######################################################################################################################
API_KEY = 'MERAKIAPIKEY'
organization_id = 'Organization Name'
devices = ['appliance', 'wireless', 'switch']
perpage = "1000"
# ################################################ PARAMETERS ##########################################################
# start_date = '2021-03-09T00:00:00.526Z'
# end_date = '2021-06-09T23:59:59.526Z'
networks = []


def pull_organization_id():
    dashboard = meraki.DashboardAPI(API_KEY)
    response = dashboard.organizations.getOrganizations()
    print(response)
    for dicti in response:
        name = dicti["name"]
        if name == organization_id:
            org_id = dicti["id"]
            print("#################################################")
            print(name + "\n" + "Organization ID: " + org_id)
            print("#################################################")
            return org_id
        else:
            continue


def pull_organization_networks(ident):
    net_dictionary = {}
    dashboard = meraki.DashboardAPI(API_KEY)
    response = dashboard.organizations.getOrganizationNetworks(ident, total_pages='all')
    print(response)
    for network in response:
        name = network['name']
        n_id = network['id']
        net_dictionary[name] = n_id
    print(net_dictionary)
    return net_dictionary


def export_device_events(nids, devs, pp):
    network_list = []
    name_list = []
    dashboard = meraki.DashboardAPI(API_KEY)
    for n in nids:
        network_list.append(nids[n])
        name_list.append(n)
        # print(network_list)
    for net in range(len(network_list)):
        for d in devs:
            try:
                response = dashboard.networks.getNetworkEvents(network_list[net], total_pages='all', productType=d,
                                                               perPage=pp)
                print(response)
                filename = name_list[net] + "_" + d + "_" + "network_events.txt"
                saveoutput = open(filename, "a+")
                readoutput = response
                saveoutput.write(str(readoutput))
            except:
                print("ERROR")


def execute_export():
    org_id = pull_organization_id()
    net = pull_organization_networks(org_id)
    export_device_events(net, devices, perpage)


execute_export()
