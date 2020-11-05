from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SettingsCredSnmpV3SuccessGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``Collector:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceName:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceType:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string
    
    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string
    
    |  ``Network:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "Collector",
                  "DeviceID",
                  "DeviceName",
                  "DeviceType",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceAssurance",
                  )

    
    
    
    
    
    
    
    
    
    
    