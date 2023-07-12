---
title: "Stanley Rother"
date: 2023-07-12T09:10:11-05:00
draft: true
---

{{< rawhtml >}}

<!-- <script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script> -->
<style>
    /* 
 * Always set the map height explicitly to define the size of the div element
 * that contains the map. 
 */
#map {
  height: 400px;
}
</style>

<h3>My Google Maps Demo</h3>
<!--The div element for the map -->
<div id="map"></div>

<!-- prettier-ignore -->
<script>(g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})
    ({key: window.GOOGLE_API_KEY, v: "beta"});</script>

<script>
    // Initialize and add the map
let map;
let geocoder;

async function initMap() {
  // The location of Uluru
  const position = { lat: -25.344, lng: 131.031 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  const {Geocoder} = await google.maps.importLibrary("geocoding");



  let geocoder = new Geocoder();

  geocoder.geocode(
      {"address": "700+Southeast+89th+Street,+Oklahoma+City,+OK"},
      function(results, status) {
          console.log(results); console.log(status);
            // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 4,
    center: results[0].geometry.location,
    mapId: "DEMO_MAP_ID",
  });
//     // The marker, positioned at Uluru
//   const marker = new AdvancedMarkerElement({
//     map: map,
//     position: results[0].geometry.location,
//     title: "Uluru",
//   });
    // The marker, positioned at Uluru
  const marker2 = new AdvancedMarkerElement({
    map: map,
    position: {lat: 35.376906, lng: -97.502884},
    title: "Uluru",
  });
    })


}

initMap();
</script>

{{< /rawhtml >}}



# Holy Trinity Catholic Church

Holy Trinity Catholic Church, Missouri Avenue, Okarche, OK, USA

Bl. Stanley Rother was a parishioner at Holy Trinity Catholic Church, where he received his sacraments and studied at Holy Trinity Catholic School.
[More details](https://www.holytrinityok.org/)


# Blessed Stanley Rother Shrine

Blessed Stanley Rother Shrine, Southeast 89th Street, Oklahoma City, OK, USA

The shrine was dedicated on February 17, 2023 with the Most Rev. Paul S. Coakley, Archbishop of Oklahoma City presiding.  The service was attended by 37 bishops, 147 priests, and hundreds of other religious and pilgrims.
[More details](https://www.rothershrine.org/)

