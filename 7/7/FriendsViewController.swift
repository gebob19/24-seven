//
//  FriendsViewController.swift
//  7
//
//  Created by Brennan Gebotys on 2018-05-26.
//  Copyright © 2018 team24seven. All rights reserved.
//

import UIKit
import Alamofire

class FriendsViewController: UIViewController {

    var token:String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let params: Parameters = ["token": token]
        
        Alamofire.request("http://127.0.0.1:8000/user/friends/", method: .post, parameters: params, encoding: JSONEncoding.default).responseJSON { response in
            if let status = response.response?.statusCode {
                switch(status) {
                case 200:
                    //success
                    break
                default:
                    print("error with status: \(status)")
                    return
                }
            }
            print(response)
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
