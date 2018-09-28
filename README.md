# folium-jsbutton

Add a button that executes JavaScript. Add's EasyButton and FontAwesome to the map.

# Installation

    pip install folium-jsbutton

or from git

    pip install git+https://github.com/prinsherbert/folium-jsbutton.git



# Example

    import folium

    from folium_jsbutton import JsButton

    m = folium.Map((50, 6), tiles='stamentoner', zoom_start=4)

    JsButton(
        title='<i class="fas fa-crosshairs"></i>',function="""
        function(btn, map) {
            map.setView([42.3748204, -71.1161913],5);
            btn.state('zoom-to-forest');
        }
        """).add_to(m)


    JsButton(
        title='<i class="fas fa-crosshairs"></i>',function="""
        function(btn, map) {
            map.setView([42.3748204, 71.1161913],5);
            btn.state('zoom-to-forest');
        }
        """).add_to(m)

    m

[result](example.html)

