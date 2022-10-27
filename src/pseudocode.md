## Test Driven Developement

### Using the evercraft documentation create Tests 

<!-- 1. ) Create test to make sure the character exists by asserting the character is not equal to None
2. ) Create Test for create name by asserting the name is not equal to None 
3. ) Create test for character name by setting the new name to a variable 
3. A) variable name is now equal to the name of the character then asserting the character name is not equal to None
3. B) set the variable name of character2 by running through the same function 
4. ) Check to make sure you can change names by updating the name of the character after creation 
4a. A) set character you are changing to a variable and then set the new name equal to a variable as well
4. ) add new character name to the current name and push
5.  ) set alignment (you will need to always send both name and alignment every time you create the character)
6.  ) Creating a character give it an ac rating, default to 10 
6.  A) After creating a character can the ac be updated to a different number
7.  ) Create a character and make a health to 5
7.  A) Can a character damage another characeter and change the health by 1
7.  B) Can a character damage another character with a critical hit and do more damage
7.  C) Can a character damage another player   -->


## Refactored PseudoCode
## when creating Character in all test's must be referenced with Character('name', 'alignment')

1.  ✓ ) inside the def __init__ (self, name, alignment) 
1. ✓ B) set self(name, alignment, ac, health, is_alive, dex, str, wis, chr, con, int and atribute)
2. ✓ ) test case assert that Character() does not equal None 
3. ✓ ) test case assert that Character name does not equal None
4. ✓ ) Test case assert name == custom name for two custom Characters ( 1 & 2)
5. ✓ ) Test case set name to Character1.name / set Character.name to new custom name assert that Character.name does not equal "name'
6. ✓ ) Test case assert that Character alignment does not equal None
7. ✓ ) Test case assert that Character ac does not equal None
8.  ✓ ) test case create Character then add to Chacter.ac then assert that Character.ac does not equal base Character.ac 
9. ✓ ) Test case assert that Character.health does not equal None
9. ✓ ) Test case create two unique Characters then assert that when the Dice_roll is above the ac the targeted Character hit equal True
10. ✓ ) Test case create two unique Charatcers then assert that when the Dice_roll is below the ac of the targeted Character hit equals false 
11. ✓ ) Test case create two unique Characters then assert that when Dice_roll is above targeted Character.ac then the targeted chacter.health does not equal full health (5)
12.✓  ) Test case does the same thing as the attack_hit but if Dice_roll === 20 then assert that health equals 3
13. ✓ ) Test case when Character is attacked and health = 0 the assert that character.is_alive == flase
14. ✓ ) Test case Create Character and assert that character.dex == 10
15. ✓ ) Test case to check for the Modifiers / create Character 'Sims mcBirdman'
15. ✓  A) Sims McBirdman.dex == 14 assert Sims McBirdman.modifiers == 2
15. ✓ B) Sims McBirdman.dex == 19 assert Sims McBirdman.modifiers == 4
16. ✓ ) Test case to check for negative Modifiers / create Character 'Afda'
16. ✓ A) Afda.dex == 7 assert Afda.modifiers == -2
16. ✓ B) Afda.dex == 4 assert Afda.Modifiers == -3
16. ✓ C) Afda.dex == 3 assert Afda.Modifiers == -5



 ## Iteration 2

1. ✓ Make a subclass off character for each "class"
2. ✓ Update the new things 
###### &emsp;
3. ✓ Fighter
* ✓ 3a. Health increases by 10 points per level
* &emsp; Edit the level_up function
* ✓ 3b. Attack increases by 1 every level
* &emsp; Edit the attack function
###### &emsp;
4. ✓ Rogue
* ✓ 4a. Does triple damage on crits
* &emsp; Editing the attack function
* ✓ 4b. Ignores opponents dex mod for AC
* &emsp; Edit the attack function
* ✓ 4c. Adds dex mod for damage
* &emsp; Edit the attack function
* ✓ 4d. Cannot be a good character
* &emsp; Change the character alignment to Neutral if given good
###### &emsp;
5. Monk
* 5a. ✓ Gets 6 HP per level
* &emsp; Edit the level_up function
* 5b. ✓ Does base 3 damage per attack
* &emsp; Change the damage in the attack method
* 5c. ✓ Adds Wis mod to AC in addition to Dex
* &emsp; Changes update_character to add Wis mod to AC
* 5d. ✓ attack roll increased by 1  2nd, 3rd level
* &emsp; Add it the dice_mod variable
###### &emsp;
6. Paladin
* ✓  6a Gets 8 HP per level
* &emsp; Edit the level_up function
* ✓ 6b +2 damage to Evil Characters
* &emsp; Edit the attack, check if enemy.alignment contains "Evil" or 'evil'
* ✓ 6c Does triple damage on crit
* &emsp; Edit the attack function for crits
* ✓ 6d Attack roll increase by 1 every level
* &emsp; Edit the attack function
* ✓ 6e Can only have Good alignment
* &emsp; Set the alignment to good. 

## Iteration Three Races

1. ✓ Character can have a race 
2. ✓ Character can have the race changed
3. ✓ Character with a class can change race
4. ✓ Orc changes stats to get modifier
6. ✓ Orc changes stats to negative modifier
5. ✓ Orc AC changed
7. ✓ Dwarf race exits
8. ✓ Dwarf modifiers change 
9. ✓ Dwarf doubled constitution modifier on health gain
10. ✓ Dwarf gets +2 against orc
11. ✓ Dwarf does not get +2 against non-orc
12. ✓ Elf gets modifiers changed
13. ✓ Elf Crit range changes
14. ✓ Elf gets AC against orc attacks
15. ✓ Elf doesn't get AC when not attacked 
16. ✓ Halfling stats get changed
17. ✓ Halfling armor increase when attackee is not halfling
18. ✓ Halfling armor doesn't increase when attackee is halfling
19. ✓ Halfling cannot have Evil alignment
20. ✓ Halfling cannot have evil alignment

## Iteration Four Equipment 

1. ✓ Equipment exits
2. ✓ Character knows equipment
3. ✓ Character can equip item
4. ✓ Character stats change
5. ✓ Character's stats decrease on unequip
6. ✓ Character can equip item and then equip other item, stats change accordingly
7. ✓ Item creates attributes if they don't exist 
8. ✓ Charcter klass
9. ✓ Daniel done with Evercraft
10. ✓ Estus done with Evercraft
11. ✓ Roll Dice
12. ✓ Choas race
13. ✓ Roll dice on hit
