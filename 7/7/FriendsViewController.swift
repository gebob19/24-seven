//
//  FriendsViewController.swift
//  7
//
//  Created by Brennan Gebotys on 2018-05-26.
//  Copyright © 2018 team24seven. All rights reserved.
//

import UIKit
import Alamofire
import SocketIO

class FriendsViewController: UIViewController {

    
  
    
    
    @IBOutlet var lbl: UILabel!
    
    
    @IBOutlet var seg: UISegmentedControl!
    
    
    @IBAction func ValueChanged(_ sender: Any) {
        if seg.selectedSegmentIndex == 0 //first
        {
            lbl.text = "First is selected"
        }
        else if seg.selectedSegmentIndex == 1 //second
        {
            lbl.text = "Second is selected"
        }
        else if seg.selectedSegmentIndex == 2 //third
        {
            lbl.text = "Third is selected"
        }
    }
    
    var token:String = ""
    var socket:SocketIOClient!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // connect socket
        var manager = SocketManager(socketURL: URL(string: "http://127.0.0.1:8080")!, config: [.log(true), .connectParams(["token": token])])
        self.socket = manager.defaultSocket
        self.setSocketEvents()
        self.socket.connect()
        // get user's friends from server
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
    
    private func setSocketEvents() {
        self.socket.on(clientEvent: .connect) { data, ack in
            print("Socket Connected!")
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
