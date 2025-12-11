#WEAPONS COMPLETED.(ADD AS DEEMED NESSESSARY)
#Weapons
#Plane types
planes = {
  "diveBomber":{
    "weaponName":"Dive bombers","weaponType":"Plane",
    "weaponDamage":400,"attackAmount":4,
    "weaponHealth":400,"accuracy":25,"loaded":False}, 
  "torpedoBomber":{
    "weaponName":"Torpedo bombers","weaponType":"Plane",
    "weaponDamage":1000,"attackAmount":2,
    "weaponHealth":300,"accuracy":10,"loaded":False}
}
#Primary weapon types
battleshipArnament = {
  "cannon20in":{
    "weaponName":"20in Cannon","weaponType":"Primary",
    "weaponDamage":700,"attackAmount":2,
    "weaponHealth":400,"accuracy":20,"loaded":False},
  "cannon18in":{
    "weaponName":"18in Cannon","weaponType":"Primary",
    "weaponDamage":500,"attackAmount":3,
    "weaponHealth":300,"accuracy":15,"loaded":False},
  "cannon14in":{
    "weaponName":"14in Cannon","weaponType":"Primary",
    "weaponDamage":300,"attackAmount":4,
    "weaponHealth":400,"accuracy":25,"loaded":False}
}
cruiserArnament = {
  "cannon14in" : {
    "weaponName":"14in Cannon","weaponType":"Primary",
    "weaponDamage":500,"attackAmount":2,
    "weaponHealth":400,"accuracy":25,"loaded":False},
  "cannon12in":{
    "weaponName":"12in Cannon","weaponType":"Primary",
    "weaponDamage":300,"attackAmount":3,
    "weaponHealth":400,"accuracy":30,"loaded":False},
  "cannon10in":{
    "weaponName":"10in Cannon","weaponType":"Primary",
    "weaponDamage":200,"attackAmount":4,
    "weaponHealth":200,"accuracy":35,"loaded":False}
}
destroyerArnament = {
  "cannon10in":{
    "weaponName":"10in Cannon","weaponType":"Primary",
    "weaponDamage":200,"attackAmount":2,
    "weaponHealth":300,"accuracy":50,"loaded":True},
  "torpedo":{
    "weaponName":"Torpedo","weaponType":"Primary",
    "weaponDamage":1000,"attackAmount":1,
    "weaponHealth":100,"accuracy":10,"loaded":True}
}
submarineArnament = {
  "torpedo":{
    "weaponName":"Torpedo","weaponType":"Primary",
    "weaponDamage":1000,"attackAmount":1,
    "weaponHealth":100,"accuracy":10,"loaded":False}
}
#Secondary weapon types
secondaryArnament = {
  "cannon8in" : {
    "weaponName":"8in Cannon","weaponType":"Secondary",
    "weaponDamage":80,"attackAmount":2,
    "weaponHealth":200,"accuracy":20,"loaded":True},
  "cannon6in" : {
    "weaponName":"6in Cannon","weaponType":"Secondary",
    "weaponDamage":50,"attackAmount":2,
    "weaponHealth":250,"accuracy":20,"loaded":True}
}
#Flak weapon types 
flak = {
  "heavyFlak" : {
    "weaponName":"Heavy Flak","weaponType":"AA",
    "weaponDamage":50,"attackAmount":2,
    "weaponHealth":100,"accuracy":50,"loaded":True},
  "mediumFlak" : {
    "weaponName":"Medium Flak","weaponType":"AA",
    "weaponDamage":20,"attackAmount":5,
    "weaponHealth":200,"accuracy":40,"loaded":True},
  "lightFlak" : {
    "weaponName":"Light Flak","weaponType":"AA",
    "weaponDamage":10,"attackAmount":20,
    "weaponHealth":100,"accuracy":35,"loaded":True}
}

#Ships #WORK ON THIS.
carrier = {
  "name":"Carrier","health":5000,"size":"large",
  "Pweapon":planes,"PweaponNumber":2,
  "Sweapon":secondaryArnament,"SweaponNumber":4, 
  "AAweapon":flak,"AAweaponNumber":12}
battleship = {
  "name":"Battleship","health":7000,"size":"large",
  "Pweapon":battleshipArnament,"PweaponNumber":3,
  "Sweapon":secondaryArnament, "SweaponNumber":10, 
  "AAweapon":flak, "AAweaponNumber":10}
cruiser = {
  "name":"Cruiser","health":4000,"size":"Medium",
  "Pweapon":cruiserArnament,"PweaponNumber":4,
  "Sweapon":secondaryArnament,"SweaponNumber":8, 
  "AAweapon":flak, "AAweaponNumber":16}
destroyer = {
  "name":"Destroyer","health":3000,"size":"small",
  "Pweapon":destroyerArnament,"PweaponNumber":2,
  "Sweapon":secondaryArnament,"SweaponNumber":2, 
  "AAweapon":flak,"AAweaponNumber":6}
submarine = {
  "name":"Submarine","health":2000,"size":"Small",
  "Pweapon":submarineArnament,"PweaponNumber":4,
  "Sweapon":secondaryArnament,"SweaponNumber":1, 
  "AAweapon":flak, "AAweaponNumber":2}

#Enemy ship
testTarget = {
  "name":"Test Target","health":500,"size":"Small",
  "Pweapon":destroyerArnament,"PweaponNumber":1,
  "Sweapon":secondaryArnament,"SweaponNumber":2, 
  "AAweapon":flak, "AAweaponNumber":4
}
ecarrier = {
  "name":"Carrier","health":5000,"size":"large",
  "Pweapon":planes,"PweaponNumber":2,
  "Sweapon":secondaryArnament,"SweaponNumber":4, 
  "AAweapon":flak,"AAweaponNumber":12}
ebattleship = {
  "name":"Battleship","health":7000,"size":"large",
  "Pweapon":battleshipArnament,"PweaponNumber":3,
  "Sweapon":secondaryArnament, "SweaponNumber":10, 
  "AAweapon":flak, "AAweaponNumber":10}
ecruiser = {
  "name":"Cruiser","health":4000,"size":"Medium",
  "Pweapon":cruiserArnament,"PweaponNumber":4,
  "Sweapon":secondaryArnament,"SweaponNumber":8, 
  "AAweapon":flak, "AAweaponNumber":16}
edestroyer = {
  "name":"Destroyer","health":3000,"size":"small",
  "Pweapon":destroyerArnament,"PweaponNumber":2,
  "Sweapon":secondaryArnament,"SweaponNumber":2, 
  "AAweapon":flak,"AAweaponNumber":6}
esubmarine = {
  "name":"Submarine","health":2000,"size":"Small",
  "Pweapon":submarineArnament,"PweaponNumber":4,
  "Sweapon":secondaryArnament,"SweaponNumber":1, 
  "AAweapon":flak, "AAweaponNumber":2}










