# Colony notebook, episode 1 (RimWorld 1.7, Cassandra / Rough, tile 254174)

Started through the vanilla setup pages (site + pawns chosen, see bridge-manual "New game"). Temperate forest, large hills,
tile avg 22C (seasonal 9..35C), growing all year. Day 2, winter: nights ~4C.

COLONISTS
- Kena (Human424) Shooting 13!!, Construction 7!, Crafting 5, Artistic 6. Bolt-action rifle. Main shooter + builder. Can't cook/plant/mine/social/animals.
- Mila (Human514) Cooking 11!!, Medicine 9!, Plants 8!. Plasteel knife (shooting is poor, ShootingAccuracy -1). Cook + grower + doctor.
- Nicole (Human3718) Social 10!!, Shooting 7!!, Intellectual 6!, Medicine 6. Revolver. 2nd shooter, researcher, negotiator, backup doctor.

BASE
- Barracks x111-119 z144-150 (63 cells, 28C from the campfire -> "slept hot" -4): 3 beds z150, SimpleResearchBench [112,145], Campfire [117,146], stockpile "main" Important. Door [115,143] into the storeroom.
- Storeroom x111-119 z136-142 (shares the barracks south wall): stockpile "store", Table1x2c [117,139] + 2 stools, HandTailoringBench [113,137]. West door [110,139] = the only outside entrance.
- Rally [113,144,3,2] inside barracks by the door. Steel spike traps [105,137] [105,141] flanking the entrance lane.
- ButcherSpot [106,150] outside (bill Forever). Horseshoes pin [107,141].
- Fields: rice1 [103,134,7,6] (sown day 1), cotton1 [103,127,7,5].
- Ancient ruin (tomb, sarcophagi) right east of base x122-131 z131-144: harmless. Tomb with 4 AncientCryptosleepCaskets at [157,53]: keep away.

STOCKS day 2: wood ~400 (dropping into walls), steel ~1100, components 30, silver 800, industrial medicine 30, survival meals ~45, leather 27.

PROBLEMS / NEXT
1. Warm clothes: winter, only 27 leather, 1 animal on the map. Buy apparel from the first trader; jacket bills once >=70 cloth/leather.
2. Mood ~53: awful barracks -7 (split into bedrooms this season), slept-hot -4 (heater on a thermostat once power exists).
3. Defense: barricades outside [110,139] after a stonecutter; turrets later. First Cassandra raid expected ~day 5-10.
4. Research: Batteries -> SolarPanels -> Pemmican -> Smithing.

DAY 3 manhunter swan attacked Mila at [90,169] (2 scratches + bite, bleeding); Kena+Nicole shot it from ~[107,141]. Mila self-tend on (NormalOrWorse; tend order to Nicole was not offered). Bite = 30% infection: re-check in 12h.
DORMANT MECHS at [158-163,60-67] near the cryptosleep tomb: Cyclops (charge blaster) + 2 Pikemen, duty SleepForever. Never send anyone there (hunting/foraging/mining radius!).

DAY ~6 (3/2) DISASTER + RESET. Steward hunting job designated a caravan donkey -> Kena shot it, tribe 家族聯盟的路 hostile (-92). Then a 垃圾人 raider set the wooden workshop on fire while I ignored the raid alert ("x0"). Workshop, stonecutter, research bench, table, rice crop, wind turbine burned. New colonist Hector (Shooting 9, Mining 11, revolver). OWNER: steward fully OFF (config.local.yaml steward.enabled false); I set priorities and designations by hand. Vanilla already rescues (Doctor) and fights fire in the home area.

GOALS (small, check each wake; tick when state proves it)
G1 [now] nobody starves: food_days > 3. Berries+healroot designated (14), hunt 2 alpacas ~[133,240] (Hector), resow rice1 when Growing runs. Downed pawns get fed by hand if nobody does it.
G2 [today] barracks is a room again: slate walls z143 x116-120 + x120 z144-150 + [113,151], wood door [115,143], 4th bed [111,145]. Proof: room_digest shows Barracks, blueprints 0.
G3 [2 days] no colonist breaks: moods > 35. Table+stools inside, pain heals with bed rest.
G4 [after G1-G3] storage out of the bedroom: separate stone storeroom; campfire replaced by a stove in its own kitchen; bedrooms later.
Rule I break most: every check = run rim_look (full picture), never a narrow query; any danger != None -> name every hostile.
