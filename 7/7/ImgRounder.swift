//
//  ImgRounder.swift
//  7
//
//  Created by Filip Telescu on 2018-05-19.
//  Copyright © 2018 team24seven. All rights reserved.
//

import Foundation

import UIKit

class ImgRounder: UIViewController {
    

    @IBOutlet weak var imgCiara: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        imgCiara.layer.cornerRadius = imgCiara.frame.size.width / 2
        imgCiara.clipsToBounds = true
    }

}
