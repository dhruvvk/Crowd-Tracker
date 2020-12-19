//
//  LocationView.swift
//  Crowd Tracker
//
//  Created by Dhruv Vikram Krishna on 12/19/20.
//

import SwiftUI

struct LocationView: View {
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 16)
                .fill(Color(.white))
                .frame(width: 350, height: 90, alignment: .center)
            
            Text("NOT CURRENTLY IN ANY BUILDING")
                .font(.system(size: 16, weight: .bold))
                .foregroundColor(Color(red: 0.18, green: 0.31, blue: 0.44, opacity: 1.0))
        }
    }
}

struct LocationView_Previews: PreviewProvider {
    static var previews: some View {
        LocationView()
    }
}
