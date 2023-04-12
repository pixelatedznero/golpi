def create(pattern: bytes, x_dim: int) -> tuple:
    return (pattern, x_dim)


class Stills :

    block = (b'''
**
**
'''.replace(b'''
''', b''), 2)    

    beehive = (b'''
 ** 
*  *
 ** 
'''.replace(b'''
''', b''), 4)
    
    circle = (b'''
 ** 
*  *
*  *
 ** 
'''.replace(b'''
''', b''), 4)
    
    loaf = (b'''
 ** 
*  *
 * *
  * 
'''.replace(b'''
''', b''), 4)
    
    double_loaf = (b'''
 **  
*  * 
* * *
 *  *
  ** 
'''.replace(b'''
''', b''), 5)
    
    boat = (b'''
** 
* *
 * 
'''.replace(b'''
''', b''), 3)
    
    tub = (b'''
 *
* *
 * 
'''.replace(b'''
''', b''), 3)

class Oscillators :

    blinker = (b'''
***
'''.replace(b'''
''', b''), 3)
    
    quadruple_blinker = (b'''
  ***  
       
*     *
*     *
*     *
       
  ***  
'''.replace(b'''
''', b''), 7)
    
    double_blinker = (b'''
 ***
*   
*   
*   
'''.replace(b'''
''', b''), 4)

    toad = (b'''
 ***
*** 
'''.replace(b'''
''', b''), 4)

    beacon = (b'''
**  
*   
   *
  **
'''.replace(b'''
''', b''), 4)

    pulsar = (b'''
  ***   ***  
             
*    * *    *
*    * *    *
*    * *    *
  ***   ***  
             
  ***   ***  
*    * *    *
*    * *    *
*    * *    *
             
  ***   ***  
'''.replace(b'''
''', b''), 15)

    pentadecathlon = (b'''
 * 
 * 
***
   
   
***
 * 
 * 
 * 
 * 
***
   
   
***
 * 
 * 
'''.replace(b'''
''', b''), 3)

    bill_gosper = (b'''
    **      **    
   * *      * *   
   *          *   
** *          * **
** * *  **  * * **
   * * *  * * *   
   * * *  * * *   
** * *  **  * * **
** *          * **
   *          *   
   * *      * *
    **      **    
'''.replace(b'''
''', b''), 18)

class Spaceships :

    glider = (b'''
 * 
  *
***
'''.replace(b'''
''', b''), 3)
    
    light = (b'''
*  * 
    *
*   *
 ****
'''.replace(b'''
''', b''), 5)
    
    middle = (b'''
 *****
*    *
     *
*   * 
  *   
'''.replace(b'''
''', b''), 6)
    
    heavy = (b'''
 ******
*     *
      *
*    * 
  **   
'''.replace(b'''
''', b''), 7)

class Colonizers :

    r_pentonimo = (b'''
 **
** 
 * 
'''.replace(b'''
''', b''), 3)

class Others :
    
    glider_collision = (b'''
  *      
* *      
 **      
         
         
      ** 
      * *
      *  
'''.replace(b'''
''', b''), 9)
    
    def generate_crown(base_size = 7, crawn_type = "double") :
        if base_size % 2 == 0 :
            Exception("The size of the base of the crown must be odd.")
        if crawn_type != "double" and crawn_type != "quadruple" :
            Exception("The type of the crown must be 'double' or 'quadruple'.")
        
        if crawn_type == "double" :
            spacing = int(((base_size - 7) + 2) / 2)
            final = ' '
            rest = int(base_size / 2)
            do = 0
            while do < int(base_size / 2) :
                char = 0
                for _ in range(rest) :
                    final += ' '
                    char += 1
                final += '*'
                char += 1
                while base_size - rest > char :
                    final += ' *'
                    char += 2
                for _ in range(rest) :
                    final += ' '
                    char += 1
                rest -= 1
                do += 1
            for _ in range(base_size) :
                final += '*'
            for _ in range(spacing) :
                for _ in range(base_size) :
                    final += ' '
            final += "".join(reversed(final))
            final = bytes(final, "utf-8")
                        
        return final

"""
unclassified, unnamed or to draw :
- _____ = (b' **
            * *
            ** '  => Stills
            
- _____ = (b'** **
            ** **
              *  '  => Other



 ***
*  *
*
**


      *      !
     * *     !
    * * *    !
    *****    !
  **     **  !
 * *  *  * * !
* ** * * ** *!
 * *  *  * * !
  **     **  !
    *****    !
    * * *    !
     * *     !
      *      !
"""