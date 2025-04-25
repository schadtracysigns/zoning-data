// SignageApp.swift

import SwiftUI

@main
struct SignageApp: App {
    var body: some Scene {
        WindowGroup {
            SignageHomeView()
        }
    }
}

struct SignageHomeView: View {
    @State private var zipCode: String = ""
    @State private var selectedZone: String = "Retail"
    @State private var selectedSignType: String = "Monument"
    @State private var zoningInfo: [String: String] = [:]
    @State private var errorMessage: String? = nil

    let zones = ["Retail", "Commercial", "Residential"]
    let signTypes = ["Channel Letters", "Monument", "Pylon"]

    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    Image("schadtracy_logo")
                        .resizable()
                        .scaledToFit()
                        .frame(height: 60)

                    Text("Welcome to the Schad Tracy Signage Zoning App")
                        .font(.headline)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)

                    Text("Signage Zoning Finder")
                        .font(.title2)
                        .bold()

                    TextField("Enter ZIP Code", text: $zipCode)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .keyboardType(.numberPad)
                        .padding(.horizontal)

                    Button("Check Zoning") {
                        fetchZoningData()
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
                    .padding(.horizontal)

                    Picker("Zone", selection: $selectedZone) {
                        ForEach(zones, id: \.\self) { Text($0) }
                    }
                    .pickerStyle(SegmentedPickerStyle())
                    .padding(.horizontal)

                    Picker("Sign Type", selection: $selectedSignType) {
                        ForEach(signTypes, id: \.\self) { Text($0) }
                    }
                    .pickerStyle(SegmentedPickerStyle())
                    .padding(.horizontal)

                    if !zoningInfo.isEmpty {
                        VStack(alignment: .leading, spacing: 8) {
                            ForEach(zoningInfo.sorted(by: >), id: \.key) { key, value in
                                VStack(alignment: .leading) {
                                    Text("\(key):")
                                        .font(.subheadline)
                                        .bold()
                                    Text(value)
                                        .font(.footnote)
                                }
                            }
                        }
                        .padding()
                    } else if let error = errorMessage {
                        Text(error)
                            .foregroundColor(.red)
                            .padding()
                    }
                }
                .padding()
            }
            .navigationTitle("Zoning Lookup")
        }
    }

    func fetchZoningData() {
        guard let url = URL(string: "https://schadtracysigns.github.io/zoning-data/burnsville.json") else {
            errorMessage = "Invalid URL"
            return
        }

        URLSession.shared.dataTask(with: url) { data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    self.errorMessage = "Request error: \(error.localizedDescription)"
                    return
                }

                guard let data = data else {
                    self.errorMessage = "No data received."
                    return
                }

                do {
                    let decoded = try JSONDecoder().decode([String: [String: [String: [String: [String: String]]]]].self, from: data)
                    if let city = decoded["burnsville"]?["55306"]?[selectedZone]?[selectedSignType] {
                        self.zoningInfo = city
                        self.errorMessage = nil
                    } else {
                        self.zoningInfo = [:]
                        self.errorMessage = "No zoning info found for the selected options."
                    }
                } catch {
                    self.errorMessage = "Decoding error: \(error.localizedDescription)"
                }
            }
        }.resume()
    }
}
