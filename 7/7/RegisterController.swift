//
//  RegisterController.swift
//  7
//
//  Created by Brennan Gebotys on 2018-05-21.
//  Copyright © 2018 team24seven. All rights reserved.
//

import UIKit
import Alamofire

class RegisterController: UIViewController {

    @IBOutlet weak var emailInput: LoginTextField!
    @IBOutlet weak var passwordInput: LoginTextField!
    @IBOutlet weak var passwordConfirmInput: LoginTextField!
    @IBOutlet weak var errorOutput: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func register(_ sender: Any) {
        if (passwordInput.text == passwordConfirmInput.text) {
            let params: Parameters = ["email": (string: emailInput.text),
                                      "password": (string: passwordInput.text),
                                      "firstName": (string: "Gebobby"),
                                      "lastName": (string: "Bobby")]
            
            Alamofire.request("http://localhost:8000/register", method: .post, parameters: params,
                              encoding: JSONEncoding.default).responseJSON { response in
                if let status = response.response?.statusCode {
                    switch (status) {
                    case 200:
                        // success
                        break
                    default:
                        print("Error with status: \(status)")
                        return
                    }
                }
                
                if let result = response.result.value {
                    let respJSON = result as! NSDictionary
                    if let err = respJSON["err"] {
                        self.errorOutput.text = err as! String
                    } else if let token = respJSON["token"] {
                        // pass token to this vc
                        let vc = self.storyboard?.instantiateViewController(withIdentifier: "explore") as! UITabBarController
                        self.present(vc, animated: true, completion: nil)
                    }
                }
            }
        } else {
            errorOutput.text = "passwords do not match"
        }
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
