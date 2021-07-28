Compile to .pyc
Chuck into "C:\games\World_of_Tanks\res_mods\1.13.0.1\scripts\client\gui\mods"
Run game
Login
Open settings
Then in python.log you'll see it


files with "mod_" prefix are loaded and run by game after it loads, but before login
files without prefix are loaded manually (with "import" clause)


access_token only available when player is logged in, so you can't get it in script root scope, gotta attach to some user event
"showSettingsWindow" selected because it was easy to guess where I had to click to invoke it just from name alone

suspect that clan page is in "in-game", it looks to be an embedded webpage which complicates things
access_token is stored in client.gui.wgcg.states, but going by how its accessed you should get it from client.gui.wgcg.web_controller which is injected as IWebController
all asynchronous so you gotta make wrapper function just to call it

test victim is client.gui.shop.getShopProductInfo because I am not very familiar with clan stuff, and it was easy to find
It seems that both clan and shop use same access token, you can easily check if its the case with WireShark
 

WoTAPIPy.py - this is the 'glue logic'
Test_Submodule.py - this is where you can do stuff with access_token

HOW THIS WAS DETERMINED
grep'ed for "access_token", found out its stored in "AccessTokenData" class
grep'ed for " AccessTokenData", found out "getAccessTokenData" method
grep'ed for "getAccessTokenData", found nice example in "getShopProductInfo"

decorators ("@blahblah" directives above methods) were copied verbosely from donor code, as dependency injection is required to get instance of "WebController" and if one has to stay all of them might as well