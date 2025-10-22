# 11.8. Decluttering codes from View Controller (Recommended Read)

If you noticed, we have 281 lines of code in ViewController.swift. It appears to be a jumble of code. And in many ways, it's hard to read when you'll return to it after a week.

We can utilize protocols and extensions to break the code into multiple files, making it more modular.

## Separating the API calls from the Controller

Let's first separate the code we used to call the Contacts API. The methods we have related to the Contacts API are:

* getAllContacts()
* addANewContact(contact: Contact)
* getContactDetails(name: String)

### Defining a Protocol for the API Calls

So, let's write a protocol where we will declare the methods we will use to call the Contacts API. Let's create a new Swift file ContactsProtocol.swift, inside the 'Contact API Configs' folder.

```swift
//
//  ContactsProtocol.swift
//  App11
//
//  Created by Sakib Miazi on 5/29/23.
//

import Foundation

protocol ContactsProtocol{
    func getAllContacts()
    func addANewContact(contact: Contact)
    func getContactDetails(name: String)
}
```

### Adopting the Protocol

Awesome, now that we have a protocol, let's create another Swift file, ContactsAPICalls.swift, in the MainScreen folder. Import UIKit and Alamofire in this file. Let's write the following code in the file:

```swift
//
//  ContactsAPICalls.swift
//  App11
//
//  Created by Sakib Miazi on 5/29/23.
//

import Foundation
import UIKit
import Alamofire

extension ViewController: ContactsProtocol{
    
}
```

In the above code, we use the extension magic to adopt the ContactsProtocol from ViewController. Now, it's time to move the methods from ViewController.swift to ContactsAPICalls.swift.

{% code lineNumbers="true" %}
```swift
//
//  ContactsAPICalls.swift
//  App11
//
//  Created by Sakib Miazi on 5/29/23.
//

import Foundation
import UIKit
import Alamofire

extension ViewController:ContactsProtocol{
    //MARK: get all contacts call: getall endpoint...
    func getAllContacts(){
        if let url = URL(string: APIConfigs.baseURL + "getall"){
            AF.request(url, method: .get).responseData(completionHandler: { response in
                //MARK: retrieving the status code...
                let status = response.response?.statusCode
                
                switch response.result{
                case .success(let data):
                    //MARK: there was no network error...
                    
                    //MARK: status code is Optional, so unwrapping it...
                    if let uwStatusCode = status{
                        switch uwStatusCode{
                            case 200...299:
                            //MARK: the request was valid 200-level...
                                self.contactNames.removeAll()
                                let decoder = JSONDecoder()
                                do{
                                    let receivedData =
                                        try decoder
                                        .decode(ContactNames.self, from: data)
                                    for item in receivedData.contacts{
                                        self.contactNames.append(item.name)
                                    }
                                    self.mainScreen.tableViewContacts.reloadData()
                                }catch{
                                    print("JSON couldn't be decoded.")
                                }
                                break
                    
                            case 400...499:
                            //MARK: the request was not valid 400-level...
                                print(data)
                                break
                    
                            default:
                            //MARK: probably a 500-level error...
                                print(data)
                                break
                    
                        }
                    }
                    break
                    
                case .failure(let error):
                    //MARK: there was a network error...
                    print(error)
                    break
                }
            })
        }
    }
    
    //MARK: get details of a contact...
    func getContactDetails(name: String){
        print(name)
        if let url = URL(string: APIConfigs.baseURL+"details"){
            AF.request(url, method: .get, parameters: ["name":name])
                .responseData(completionHandler: { response in
                //MARK: retrieving the status code...
                let status = response.response?.statusCode
                
                switch response.result{
                case .success(let data):
                    print(data)
                    //MARK: there was no network error...
                    
                    //MARK: status code is Optional, so unwrapping it...
                    if let uwStatusCode = status{
                        switch uwStatusCode{
                            case 200...299:
                            //MARK: the request was valid 200-level...
                                let decoder = JSONDecoder()
                                do{
                                    let receivedData = try decoder.decode(Contact.self, from: data)
                                    print(receivedData)
                                    self.showDetailsInAlert(data: receivedData)
                                }catch{

                                }
                                break
                    
                            case 400...499:
                            //MARK: the request was not valid 400-level...
                                print(data)
                                break
                    
                            default:
                            //MARK: probably a 500-level error...
                                print(data)
                                break
                    
                        }
                    }
                    break
                    
                case .failure(let error):
                    //MARK: there was a network error...
                    print(error)
                    break
                }
            })
        }
    }
    
    //MARK: add a new contact call: add endpoint...
    func addANewContact(contact: Contact){
        if let url = URL(string: APIConfigs.baseURL+"add"){
            
            AF.request(url, method:.post, parameters:
                        [
                            //MARK: we can unwrap them here since we made sure they are not null above...
                            "name": contact.name,
                            "email": contact.email,
                            "phone": contact.phone
                        ])
                .responseString(completionHandler: { response in
                    //MARK: retrieving the status code...
                    let status = response.response?.statusCode
                    
                    switch response.result{
                    case .success(let data):
                        //MARK: there was no network error...
                        
                        //MARK: status code is Optional, so unwrapping it...
                        if let uwStatusCode = status{
                            switch uwStatusCode{
                                case 200...299:
                                //MARK: the request was valid 200-level...
                                self.getAllContacts()
                                self.clearAddViewFields()
                                    break
                        
                                case 400...499:
                                //MARK: the request was not valid 400-level...
                                    print(data)
                                    break
                        
                                default:
                                //MARK: probably a 500-level error...
                                    print(data)
                                    break
                        
                            }
                        }
                        break
                        
                    case .failure(let error):
                        //MARK: there was a network error...
                        print(error)
                        break
                    }
                })
        }else{
            //alert that the URL is invalid...
        }
    }
}

```
{% endcode %}

### The file structure of the project now looks like this:

<figure><img src="../.gitbook/assets/Screenshot 2023-05-29 at 2.32.25 PM (1).png" alt=""><figcaption></figcaption></figure>

Now, the code is more modular and more manageable.

**Note: You can make it even more modular by putting the table view protocol codes into a separate file from the ViewController.**

{% file src="../.gitbook/assets/App11_modular (2).zip" %}

