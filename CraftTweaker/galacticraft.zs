# Thermal Foundation
val redprint = <thermalfoundation:diagram_redprint>;

# Applied Energistics 2
val sky_stone = <appliedenergistics2:sky_stone_block>;

# Galacticraft
val moon_rock = <galacticraftcore:basic_block_moon:4>;
val titanium = <ore:ingotTitanium>;

# Galacticraft: Dungeon bricks
val moon = <galacticraftcore:basic_block_moon:14>;
val mars = <galacticraftplanets:mars:7>;
val venus1 = <galacticraftplanets:venus:4>;
val venus2 = <galacticraftplanets:venus:5>;

recipes.addShaped("CT_GC_MoonBuggy", <galacticraftcore:schematic>, [
  [sky_stone, moon_rock, sky_stone],
  [moon_rock, redprint, moon_rock],
  [sky_stone, moon_rock, sky_stone],
]);

recipes.addShaped("CT_GC_Tier2Rocket", <galacticraftcore:schematic:1>, [
  [sky_stone, moon, sky_stone],
  [moon, redprint, moon],
  [sky_stone, moon, sky_stone],
]);

recipes.addShaped("CT_GC_Tier3Rocket", <galacticraftplanets:schematic>, [
  [sky_stone, mars, sky_stone],
  [mars, redprint, mars],
  [sky_stone, mars, sky_stone],
]);

recipes.addShaped("CT_GC_CargoRocket", <galacticraftplanets:schematic:1>, [
  [sky_stone, venus1, sky_stone],
  [venus1, redprint, venus1],
  [sky_stone, venus1, sky_stone],
]);

recipes.addShaped("CT_GC_AstroMiner", <galacticraftplanets:schematic:2>, [
  [sky_stone, titanium, sky_stone],
  [titanium, redprint, titanium],
  [sky_stone, titanium, sky_stone],
]);
