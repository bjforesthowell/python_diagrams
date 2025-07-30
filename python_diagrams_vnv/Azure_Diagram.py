from diagrams import Cluster, Diagram, Edge
import diagrams.azure.network
import diagrams.azure.general
import diagrams.azure.compute
import diagrams.k8s.group

with Diagram("Bryn_Neil_Azure", direction="TB", show=False):

    Azure_Subscriptions = diagrams.azure.general.Subscriptions("Azure Subscriptions")
    Azure_Public_IP = diagrams.azure.network.PublicIpAddresses("Azure Public IP")
    Azure_Virtual_Network_Gateway = diagrams.azure.network.VirtualNetworkGateways("Azure Virtual Network Gateway")
    Azure_Virtual_Networks = diagrams.azure.network.VirtualNetworks("Azure Virtual Networks")
    Azure_Subnets = diagrams.azure.network.Subnets("Azure Subnets")
    Azure_Resource_Groups = diagrams.azure.general.Resourcegroups("Azure Resource Groups")
    
    Azure_Subscriptions - Edge(color="blue", style="bold") \
    - Azure_Public_IP - Edge(color="blue", style="bold") \
    - Azure_Virtual_Network_Gateway - Edge(color="blue", style="bold") \
    - Azure_Virtual_Networks - Edge(color="blue", style="bold") \
    - Azure_Subnets - Edge(color="blue", style="bold") \
    - Azure_Resource_Groups

    with Cluster("Azure_SNC_Resource_Group"):
        ghes_azure_appliance = diagrams.azure.compute.VM("GitHub Enterprise Server")
        
        ghes_storage_disk = diagrams.azure.compute.Disks("Detached Storage \n Disk")
        ghes_os_disk = diagrams.azure.compute.Disks("OS Disk")
        ghes_vnic = diagrams.azure.network.NetworkInterfaces("Virtual NIC")
        ghes_nsg = diagrams.azure.network.NetworkSecurityGroupsClassic("Network Security Group")
        
        aks_cluster = diagrams.azure.compute.KubernetesServices("AKS Cluster")
        jfrog_namespace = diagrams.k8s.group.NS("JFrog \n Namespace")
        runner_controller_namespace = diagrams.k8s.group.NS("Runner Controller \n Namespace")
        runner_scale_set_namespace = diagrams.k8s.group.NS("Runner Scale Set \n Namespace")
        
        name_spaces = [jfrog_namespace, 
                        runner_controller_namespace, 
                        runner_scale_set_namespace]
        
        Azure_Resource_Groups >> ghes_azure_appliance
        Azure_Resource_Groups >> aks_cluster
        
        ghes_azure_appliance >> ghes_os_disk
        ghes_azure_appliance >> ghes_vnic >> ghes_nsg
        ghes_azure_appliance >> ghes_storage_disk
        
        aks_cluster >> name_spaces
        