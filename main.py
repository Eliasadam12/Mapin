import customtkinter as ctk
from tkintermapview import TkinterMapView

# Ρύθμιση εμφάνισης (Dark Mode)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MapApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ρυθμίσεις Παραθύρου
        self.title("Mapin - Desktop App")
        self.geometry("1000x700")

        # Create Grid Layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ----------------- Top Bar (Αναζήτηση & Επιλογές) -----------------
        self.top_frame = ctk.CTkFrame(self, corner_radius=10)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Entry για Αναζήτηση
        self.search_entry = ctk.CTkEntry(
            self.top_frame, 
            placeholder_text="Εισάγετε τοποθεσία (π.χ. Αθήνα, Θεσσαλονίκη)...", 
            width=350
        )
        self.search_entry.pack(side="left", padx=10, pady=10)
        self.search_entry.bind("<Return>", lambda event: self.search_location())

        # Κουμπί Αναζήτησης
        self.search_button = ctk.CTkButton(
            self.top_frame, 
            text="🔍 Αναζήτηση", 
            command=self.search_location
        )
        self.search_button.pack(side="left", padx=5, pady=10)

        # Επιλογή Τύπου Χάρτη (Normal / Satellite)
        self.map_type_option = ctk.CTkOptionMenu(
            self.top_frame, 
            values=["OpenStreetMap", "Google Normal", "Google Satellite"],
            command=self.change_map_type
        )
        self.map_type_option.pack(side="right", padx=10, pady=10)

        # ----------------- Map View Widget -----------------
        self.map_widget = TkinterMapView(self, corner_radius=10)
        self.map_widget.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        # Αρχική Τοποθεσία (Ελλάδα - Αθήνα)
        self.map_widget.set_position(37.9838, 23.7275)
        self.map_widget.set_zoom(8)

        # Προσθήκη αρχικής πινέζας
        self.map_widget.set_marker(37.9838, 23.7275, text="Αθήνα")

    def search_location(self):
        address = self.search_entry.get()
        if address:
            # Αυτόματη αναζήτηση τοποθεσίας και τοποθέτηση marker
            self.map_widget.set_address(address, marker=True)

    def change_map_type(self, new_map: str):
        if new_map == "Mapin Satellite":
            self.map_widget.set_tile_server(
                "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", 
                max_zoom=22
            )
        elif new_map == "Mapin Normal":
            self.map_widget.set_tile_server(
                "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}", 
                max_zoom=22
            )
        else:
            self.map_widget.set_tile_server(
                "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
            )

if __name__ == "__main__":
    app = MapApp()
    app.mainloop()