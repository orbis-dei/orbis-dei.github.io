---
title: "Stanley Rother"
date: 2023-07-12T09:10:11-05:00
---

{{< rawhtml >}}

<style>
    /* 
 * Always set the map height explicitly to define the size of the div element
 * that contains the map. 
 */
#map {
  height: 400px;
}
</style>

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
  const position = {lat: 35.375800, lng: -97.49750};
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    zoom: 8,
    center: position,
    mapId: "DEMO_MAP_ID",
  });
    // The marker, positioned at Uluru
    // The marker, positioned at Uluru
  const marker2 = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Uluru",
  });


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

