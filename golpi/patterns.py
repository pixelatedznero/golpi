class Stills :
    block = b'''**
              **'''
    beehive = b''' ** 
                *  *
                 ** '''
    circle = b''' ** 
               *  *
               *  *
                ** '''
    loaf = b''' ** 
             *  *
              * *
               * '''
    double_loaf = b''' **  
                    *  * 
                    * * *
                     *  *
                      ** '''
    boat = b'''** 
             * *
              * '''
    tub = b''' *
            * *
             * '''

class Oscillators :
    blinker = b'''***'''
    quadruple_blinker = b'''  ***  
                                 
                          *     *
                          *     *
                          *     *
                                 
                            ***  '''
    double_blinker = b''' ***
                       *   
                       *   
                       *   '''
    toad = b''' ***
             *** '''
    beacon = b'''**  
               *
                  *
                 **'''
    pulsar = b'''  ***   ***  
                            
               *    * *    *
               *    * *    *
               *    * *    *
                 ***   ***  
                            
                 ***   ***  
               *    * *    *
               *    * *    *
               *    * *    *
                            
                 ***   ***  '''
    pentadecathlon = b''' * 
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
                        * '''
    bill_gosper = b'''    **      **    
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
                        **      **    '''

class Spaceships :
    glider = b''' * 
                 *
               ***'''
    light = b'''*  * 
                  *
              *   *
               ****'''
    middle = b''' *****
               *    *
                    *
               *   * 
                 *   '''
    heavy = b''' ******
              *     *
                    *
              *    * 
                **   '''

class Colonizers :
    r_pentonimo = b''' **
                    ** 
                     * '''

class Others :
    double_blinker = b''' ***
                       *   
                       *   
                       *   '''
    glider_collision = b'''  *      
                         * *      
                          **      
                                  
                                  
                               ** 
                               * *
                               *  '''
    def generate_crown(base_size = 7, crawn_type = "double") :
        if base_size % 2 == 0 :
            raise Exception("The size of the base of the crown must be odd.")
        if crawn_type != "double" and crawn_type != "quadruple" :
            raise Exception("The type of the crown must be 'double' or 'quadruple'.")
        
        if crawn_type == "double" :
            spacing = int(((base_size - 7) + 2) / 2)
            final = ""
            rest = int(base_size / 2)
            do = 0
            while do < int(base_size / 2) :
                char = 0
                for _ in range(rest) :
                    final += " "
                    char += 1
                final += "*"
                char += 1
                while base_size - rest > char :
                    final += " *"
                    char += 2
                for _ in range(rest) :
                    final += " "
                    char += 1
                rest -= 1
                do += 1
            for _ in range(base_size) :
                final += "*"
            for _ in range(spacing) :
                for _ in range(base_size) :
                    final += " "
            final += "".join(reversed(final))
            final = bytes(final, "utf-8")
                        
        return final


"""
unclassified, unnamed or to draw :
- _____ = b''' **
              * *
              ** '''  => Stills
            
- _____ = b'''** **
              ** **
                *  '''  => Other
"""