


















'''




this is a good example of how to use my mixer





Suppose we want to mix, for example: (water, stone, air).

We must arrange these objects in sequential order. For example:



{

"water" : 0

"stone" : 1

"air"   : 2

}


Then we create a range from 0 to 2 .


Then we place only the number 2 in position i_number_of_element__minus_1__0_i .



and then we have many mix :
    
    
    [] : nothing 
    
    [0] : ["water"]
    
    [1] : ["stone"]
    
    [2] : ["air"]
    
    [0, 0] : ["water", "water"]
    
    [1, 0] : ["stone", "water"]
    
    
    ...
    
    and so on 
    
    



we allways start from : 
    
    
    [] : nothing 
    
    




if you want to use it do like this :
    
    
    
    
    import i_my_mixer_1_i
    
    
    
    i_list_0_i = []
    
    
    i_number_of_element__minus_1__0_i = 2
    
    
    
    i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    
    
    
    
    
    

if you want to start from a point . like for example :
    
    
    [0, 0, 0]
    
    


do like that :
    
    
    
    
    
    import i_my_mixer_1_i
    
    
    
    i_number_of_element__minus_1__0_i = 2
    
    
    
    i_list_0_i = [0, 0, 0] # right here you do the init . condition : all( [ (  0 <= i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i ) for i_counter_0_i in range(0, len(i_list_0_i)) ] )
    
    
    
    
    i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    

    









'''
























































































import copy








def i_next_step_0_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 0 .
    
    
    
    '''
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i += 1
            
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(0)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_1_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 1 .
    
    
    
    '''
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i -= 1
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, 0)
        
        
        
        
    
    return i_list_0_i











def i_next_step_2_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 2 .
    
    
    
    '''
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i += 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if (i_list_0_i[i_counter_0_i] >= 0):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_element__minus_1__0_i)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_3_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 3 .
    
    
    
    '''
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i -= 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if (i_list_0_i[i_counter_0_i] >= 0):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_element__minus_1__0_i)
        
        
        
        
    
    return i_list_0_i













'''






javascript' ' '


function i_next_step_0_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    
    /*
        
        this is everything number 0 .
        
    */
    
    
    
    let i_counter_0_i = 0;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    while ( (i_counter_0_i < i_list_0_i.length) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i ) 
        {
            
            i_list_0_i[i_counter_0_i] = 0;
            
            
            i_counter_0_i++;
            
            
        }
        
        else 
        {
            
            i_list_0_i[i_counter_0_i] += 1;
            
            
            if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i ) 
            {
                
                
                i_semaphore_of_add_0_i = false;
                
                
            }
            
        }
        
    }
    
    if (i_semaphore_of_add_0_i === true) 
    {
        
        
        i_list_0_i.push(0);
        
        
    }
    
    
    
    
    return i_list_0_i;
    
    
    
}





function i_next_step_1_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    /*
        
        this is everything number 1 .
        
    */
    
    
    
    let i_counter_0_i = i_list_0_i.length - 1;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    
    
    while ( (i_counter_0_i >= 0) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        
        if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i ) 
        {
            
            
            i_list_0_i[i_counter_0_i] = 0;
            
            
            i_counter_0_i--;
            
            
        }
        
        else 
        {
            
            i_list_0_i[i_counter_0_i] += 1;
            
            if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i ) 
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }

    if (i_semaphore_of_add_0_i === true) 
    {
        
        i_list_0_i.unshift(0);
        
    }
    
    
    
    return i_list_0_i;
    
    
}




function i_next_step_2_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    
    /*
        
        this is everything number 2 .
        
    */
    
    
    
    let i_counter_0_i = 0;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    
    while ( (i_counter_0_i < i_list_0_i.length) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        
        if (i_list_0_i[i_counter_0_i] <= 0) 
        {
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i++;
            
            
        }

        else 
        {
            
            
            i_list_0_i[i_counter_0_i] -= 1;
            
            
            if (i_list_0_i[i_counter_0_i] >= 0) 
            {
            
                
                i_semaphore_of_add_0_i = false;
                
                
            }
            
        }
        
    }
    
    if (i_semaphore_of_add_0_i === true) 
    {
        
        
        i_list_0_i.push(i_number_of_element__minus_1__0_i);
        
        
    }
    
    
    return i_list_0_i;
    
    
    
}






function i_next_step_3_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    /*
        
        this is everything number 3 .
        
    */
    
    
    let i_counter_0_i = i_list_0_i.length - 1;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    
    while ( (i_counter_0_i >= 0) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        
        if (i_list_0_i[i_counter_0_i] <= 0) 
        {
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i--;
            
            
        }

        else 
        {
            
            
            i_list_0_i[i_counter_0_i] -= 1;
            
            
            if (i_list_0_i[i_counter_0_i] >= 0) 
            {
                
                
                i_semaphore_of_add_0_i = false;
                
                
            }
            
        }
        
    }
    
    if (i_semaphore_of_add_0_i === true) 
    {
        
        
        i_list_0_i.unshift(i_number_of_element__minus_1__0_i);
        
        
    }
    
    
    return i_list_0_i;
    
    
}





' ' '









java' ' '






import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_0_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 0 .
            
        */
        
        int i_counter_0_i = 0;
        
        boolean i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i < i_list_0_i.size() ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) > i_number_of_element__minus_1__0_i ) 
            {
                
                i_list_0_i.set(i_counter_0_i, 0);
                
                i_counter_0_i++;
                
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) + 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) <= i_number_of_element__minus_1__0_i ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add(0);
            
        }
        
        return i_list_0_i;
        
    }
    
}











import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_1_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 1 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.size() - 1;
        
        boolean i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) > i_number_of_element__minus_1__0_i ) 
            {
                
                i_list_0_i.set(i_counter_0_i, 0);
                
                i_counter_0_i--;
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) + 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) <= i_number_of_element__minus_1__0_i ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add(0, 0);
            
        }
        
        return i_list_0_i;
        
    }
    
}










import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_2_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 2 .
            
        */
        
        
        int i_counter_0_i = 0;
        
        boolean i_semaphore_of_add_0_i = true;
        
        
        while ( ( i_counter_0_i < i_list_0_i.size() ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) <= 0 ) 
            {
                
                i_list_0_i.set( i_counter_0_i, i_number_of_element__minus_1__0_i );
                
                i_counter_0_i++;
                
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) - 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) >= 0 ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add(i_number_of_element__minus_1__0_i);
            
        }
        
        return i_list_0_i;
        
    }
    
}








import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_3_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 3 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.size() - 1;
        
        boolean i_semaphore_of_add_0_i = true;
        
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) <= 0 ) 
            {
                
                i_list_0_i.set( i_counter_0_i, i_number_of_element__minus_1__0_i );
                
                i_counter_0_i--;
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) - 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) >= 0 ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add( 0, i_number_of_element__minus_1__0_i );
            
        }
        
        return i_list_0_i;
        
    }
    
}










' ' '










csharp' ' '






using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    public static List<int> i_next_step_0_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 0 .
            
        */
        
        
        int i_counter_0_i = 0;
        
        bool i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i < i_list_0_i.Count ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i )
            {
                
                i_list_0_i[i_counter_0_i] = 0;
                
                i_counter_0_i++;
                
            }
            else
            {
                
                
                i_list_0_i[i_counter_0_i] += 1;
                
                if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Add(0);
            
        }
        
        
        return i_list_0_i;
        
    }
    
}






using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    
    public static List<int> i_next_step_1_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 1 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.Count - 1;
        
        bool i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i )
            {
                
                i_list_0_i[i_counter_0_i] = 0;
                
                i_counter_0_i--;
                
                
            }
            else
            {
                
                i_list_0_i[i_counter_0_i] += 1;
                
                if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Insert(0, 0);
            
        }
        
        return i_list_0_i;
        
    }
    
}









using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    public static List<int> i_next_step_2_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 2 .
            
        */
        
        
        int i_counter_0_i = 0;
        
        bool i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i < i_list_0_i.Count ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] <= 0 )
            {
                
                i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
                
                
                i_counter_0_i++;
                
                
            }
            else
            {
                
                i_list_0_i[i_counter_0_i] -= 1;
                
                if ( i_list_0_i[i_counter_0_i] >= 0 )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Add(i_number_of_element__minus_1__0_i);
            
        }
        
        
        return i_list_0_i;
        
    }
    
}









using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    public static List<int> i_next_step_3_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 3 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.Count - 1;
        
        
        bool i_semaphore_of_add_0_i = true;
        
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] <= 0 )
            {
                
                i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
                
                
                i_counter_0_i--;
                
                
            }
            else
            {
                
                i_list_0_i[i_counter_0_i] -= 1;
                
                if ( i_list_0_i[i_counter_0_i] >= 0 )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Insert( 0, i_number_of_element__minus_1__0_i );
            
        }
        
        return i_list_0_i;
        
    }
    
}







' ' '










Rust' ' '





fn i_next_step_0_i( i_list_0_i: &mut Vec<u64>, i_number_of_element__minus_1__0_i: u64 ) -> &mut Vec<u64> 
{
    
    
    /*
        
        this is everything number 0 .
        
    */
    
    
    
    let mut i_counter_0_i: usize = 0;
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    while ( ( i_counter_0_i < i_list_0_i.len() ) && ( i_semaphore_of_add_0_i == true ) ) 
    {
        
        if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i )
        {
            
            i_list_0_i[i_counter_0_i] = 0;
            
            i_counter_0_i += 1;
            
        }
        else 
        {
            
            i_list_0_i[i_counter_0_i] += 1;
            
            if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i )  
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    
    if ( i_semaphore_of_add_0_i == true )
    {
        
        i_list_0_i.push(0);
        
    }
    
    return i_list_0_i;
    
}










fn i_next_step_1_i( i_list_0_i: &mut Vec<u64>, i_number_of_element__minus_1__0_i: u64 ) -> &mut Vec<u64> 
{
    
    
    /*
        
        this is everything number 1 .
        
    */
    
    
    let mut i_counter_0_i: isize = i_list_0_i.len() as isize - 1;
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) ) 
    {
        
        
        if ( i_list_0_i[i_counter_0_i as usize] > i_number_of_element__minus_1__0_i ) 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] = 0;
            
            
            i_counter_0_i -= 1;
            
            
        }
        else 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] += 1;
            
            
            if ( i_list_0_i[i_counter_0_i as usize] <= i_number_of_element__minus_1__0_i )
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    
    if ( i_semaphore_of_add_0_i == true ) 
    {
        
        i_list_0_i.insert(0, 0);
        
    }
    
    return i_list_0_i;
    
}










fn i_next_step_2_i( i_list_0_i: &mut Vec<i64>, i_number_of_element__minus_1__0_i: i64 ) -> &mut Vec<i64> 
{
    
    
    /*
        
        this is everything number 2 .
        
    */
    
    
    
    
    let mut i_counter_0_i: usize = 0;
    
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    
    while ( ( i_counter_0_i < i_list_0_i.len() ) && ( i_semaphore_of_add_0_i == true ) ) 
    {
        
        
        if ( i_list_0_i[i_counter_0_i] <= 0 ) 
        {
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i += 1;
            
            
        }
        else 
        {
            
            i_list_0_i[i_counter_0_i] -= 1;
            
            if ( i_list_0_i[i_counter_0_i] >= 0 ) 
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    if ( i_semaphore_of_add_0_i == true ) 
    {
        
        i_list_0_i.push( i_number_of_element__minus_1__0_i );
        
    }
    
    return i_list_0_i;
    
}







fn i_next_step_3_i( i_list_0_i: &mut Vec<i64>, i_number_of_element__minus_1__0_i: i64 ) -> &mut Vec<i64> 
{
    
    
    /*
        
        this is everything number 3 .
        
    */
    
    
    let mut i_counter_0_i: isize = i_list_0_i.len() as isize - 1;
    
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    
    
    while ( (i_counter_0_i >= 0) && (i_semaphore_of_add_0_i == true) ) 
    {
        
        if ( i_list_0_i[i_counter_0_i as usize] <= 0 ) 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i -= 1;
            
            
            
        }
        else 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] -= 1;
            
            if ( i_list_0_i[i_counter_0_i as usize] >= 0 )
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    if ( i_semaphore_of_add_0_i == true )
    {
        
        i_list_0_i.insert( 0, i_number_of_element__minus_1__0_i );
        
    }
    
    
    return i_list_0_i;
    
}










' ' ' 












'''













def i_next_step_4_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
   
   
   
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
   
   
   
   
   
   
    ''' 
    
    
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i += 1
            
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        if (len(i_list_0_i) == 0):
            
            i_list_0_i.append(0)
            
        else:
            
            i_list_0_i.append(i_number_of_first_appear_0_i)
        
        
        
        
        
    
    return i_list_0_i










def i_next_step_5_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    '''
    
    
        
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i -= 1
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        if (len(i_list_0_i) == 0):
            
            
            i_list_0_i.append(0)
            
            
        else:
            
            
            i_list_0_i.insert(0, i_number_of_first_appear_0_i)
            
        
        
        
    
    return i_list_0_i











def i_next_step_6_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    
    '''
    
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    
    '''
    
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    i_semaphore_of_add_1_i = False
    
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True) and (i_semaphore_of_add_1_i == False)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i += 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if ((i_list_0_i[i_counter_0_i] >= 0)):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
            
            
            
            
            if ((i_list_0_i[i_counter_0_i] < i_number_of_first_appear_0_i) and (i_counter_0_i == len(i_list_0_i) - 1) and (len(i_list_0_i) > 1)):
                
                
                
                i_semaphore_of_add_1_i = True
                
                
                
                i_semaphore_of_add_0_i = True
                
                
            
            
            
        
    
    
    
    
    if (i_semaphore_of_add_1_i == True):
    
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_0_i)):
            
            
            
            i_list_0_i[i_counter_1_i] = i_number_of_element__minus_1__0_i
            
            
            
            i_counter_1_i += 1
            
            
            
    
    
    
    
    
    
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_element__minus_1__0_i)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_7_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    
    
    '''
    
    
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    i_semaphore_of_add_1_i = False
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True) and (i_semaphore_of_add_1_i == False)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
        
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
                
            
            
            i_counter_0_i -= 1
                
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            
            
            
            
            if ((i_list_0_i[i_counter_0_i] >= 0)):
            
                
                
                
                i_semaphore_of_add_0_i = False
                
                
                
                
                
                
                
            
            
            
            if ((i_list_0_i[i_counter_0_i] < i_number_of_first_appear_0_i) and (i_counter_0_i == 0) and (len(i_list_0_i) > 1)):
                
                
                
                i_semaphore_of_add_1_i = True
                
                
                
                i_semaphore_of_add_0_i = True
                
                
                
                
            
            
        
     
    
    
    
    if (i_semaphore_of_add_1_i == True):
    
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_0_i)):
            
            
            i_list_0_i[i_counter_1_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_1_i += 1
            
            
            
    
    
    
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_element__minus_1__0_i)
        
        
        
        
    
    return i_list_0_i




























def i_check_if_repetition_exist_0_i(i_list_0_i):
    
    
    
    i_semaphore_of_result_0_i = False
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_result_0_i == False)):
        
        
        i_counter_of_repetition_0_i = 0
        
        
        i_counter_1_i = i_counter_0_i
        
        
        while ((i_counter_1_i < len(i_list_0_i))):
            
            
            if (i_list_0_i[i_counter_1_i] == i_list_0_i[i_counter_0_i]):
                
                
                i_counter_of_repetition_0_i += 1
                
                
            
            
            i_counter_1_i += 1
            
        
        
        
        if (i_counter_of_repetition_0_i > 1):
            
            
            i_semaphore_of_result_0_i = True
            
            
        
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
    i_element_that_repeats_0_i = i_counter_0_i - 1
    
    
    
    return [i_semaphore_of_result_0_i, i_element_that_repeats_0_i]
    
    
    





def i_main_0_i():
    
    
    
    i_max_number_0_i = 9
    
    
    
    i_number_of_loop_0_i = 1500
    
    
    
    i_list_0_i = []
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = []
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < i_number_of_loop_0_i):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_1_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_2_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        
        i_list_3_i = i_next_step_3_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    
    
    
    i_semaphore_of_result_0_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_0_i)
    
    
    
    i_semaphore_of_result_1_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_1_i)
    
    
    
    i_semaphore_of_result_2_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_2_i)
    
    
    
    i_semaphore_of_result_3_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_3_i)
    
    
    
    
    
    i_list_of_semaphores_of_result_0_i = [
                    
                    
                    i_semaphore_of_result_0_i,
                    
                    
                    i_semaphore_of_result_1_i,
                    
                    
                    i_semaphore_of_result_2_i,
                    
                    
                    i_semaphore_of_result_3_i,
                    
                    
                    
                    ]
    
    
    
    
    print(f"\n\n\n    i_list_of_semaphores_of_result_0_i = {i_list_of_semaphores_of_result_0_i} .\n\n\n")
    
    
    
    
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    i_number_of_first_appear_0_i = 1
    
    
    
    i_list_0_i = []
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = []
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < i_number_of_loop_0_i):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_4_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_5_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_6_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        
        i_list_3_i = i_next_step_7_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    
    
    
    i_semaphore_of_result_0_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_0_i)
    
    
    
    i_semaphore_of_result_1_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_1_i)
    
    
    
    i_semaphore_of_result_2_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_2_i)
    
    
    
    i_semaphore_of_result_3_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_3_i)
    
    
    
    
    i_list_of_semaphores_of_result_0_i = [
                    
                    
                    i_semaphore_of_result_0_i,
                    
                    
                    i_semaphore_of_result_1_i,
                    
                    
                    i_semaphore_of_result_2_i,
                    
                    
                    i_semaphore_of_result_3_i,
                    
                    
                    
                    ]
    
    
    
    
    print(f"\n\n\n    i_list_of_semaphores_of_result_0_i = {i_list_of_semaphores_of_result_0_i} .\n\n\n")
    
    
    
    
    
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    











