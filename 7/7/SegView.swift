//
//  SegView.swift
//  7
//
//  Created by Filip Telescu on 2018-06-02.
//  Copyright © 2018 team24seven. All rights reserved.
//

import Foundation
import UIKit

class SegView: UIViewController {
    
    
    
    @IBOutlet var allLbl: UILabel!
    
    @IBOutlet var seg: UISegmentedControl!
    
    @IBAction func ValueChanged(_ sender: UISegmentedControl) {
        
        if seg.selectedSegmentIndex == 0 //first
        {
            allLbl.text = "First is selected"
        }
        else if seg.selectedSegmentIndex == 1 //second
        {
            allLbl.text = "Second is selected"
        }
        else if seg.selectedSegmentIndex == 2 //third
        {
            allLbl.text = "Third is selected"
        }

    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}
