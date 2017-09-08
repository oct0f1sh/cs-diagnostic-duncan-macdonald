//: Playground - noun: a place where people can play

import UIKit

class Car {
    var numWheels: Int = 4
    var make: String = "Car"
    var model: String = "Fast"
    var color: String
    var topSpeed: Int = 10
    
    init(color: String) {
        self.color = color
    }
    
    func honk() {
        print("Beep Beep!")
    }
    
    func description() {
        print("Number of wheels: \(numWheels)\nMake: \(make)\nModel: \(model)\nColor: \(color)\nTop Speed: \(topSpeed)")
    }
}