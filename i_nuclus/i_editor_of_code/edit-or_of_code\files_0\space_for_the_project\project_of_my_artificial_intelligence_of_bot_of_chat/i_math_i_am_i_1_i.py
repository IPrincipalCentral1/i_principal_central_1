

















global i


i = {}



i["principal-central"] = "i am here"


i["i am i"] = True

if (i["i am i"] == True):



    import os

    import time
    
    import sys
    
    import importlib 
    
    
    
    
    
    
    
    
    i_cwd_0_i = os.path.dirname(os.path.abspath(__file__))
    
    
    i_path_0_i = os.path.dirname(i_cwd_0_i)
    
    
    i_path_1_i = os.path.join(i_path_0_i, "project_of_my_math")
    
    
    sys.path.append(i_path_1_i)
    
    
    
    
    # start section of parametter :
    
    # ------------------------------------------------------------------
    
    
    
    
    latest_type_of_int = "int64_t"
    
    
    
    number_of_bit_max_of_the_processor = "64"
    
    
    
    i_encoding_0_i = "latin-1"
    
    
    
    # end section of parametter :
    
    # ------------------------------------------------------------------
    
    
    
    
    
    
    
    
    
    
    

    def read_i(file):

        # lit le entier depuit le fichier 'file'

        i = 0

        try:

            with open(file, "r") as f_:

                i = int(f_.read(os.path.getsize(file)))

        except:

            semaphore = True

        return i

    
    
    
    
        
    def i_functon_of_preparing_0_i(number_of_digit_after_the_floating_point_):
        
        
        i_file_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_runner_of_my_math_1_i.py")
        
        
        i_file_0_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_runner_of_my_math_1_0_i.py")
        
        
        
        with open(i_file_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            i_content_0_i = f_.read(os.path.getsize(i_file_0_i))
            
            
            
        
        
        
        i_content_0_i = i_content_0_i.replace("_____number_of_digit_after_the_floating_point_____", str(number_of_digit_after_the_floating_point_))
        
        
        
        i_content_0_i = i_content_0_i.replace("_____latest_type_of_int_____", str(latest_type_of_int))
        
        
        
        i_content_0_i = i_content_0_i.replace("_____number_of_bit_max_of_the_processor____", str(number_of_bit_max_of_the_processor))
        
        
        
        
        with open(i_file_0_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_content_0_i)
            
            
            
        
        
    
    
    
    
    def my_max(a, b):

        # renvoi le max de 'a' et 'b'

        if (a <= b):

            return b

        else:

            return a

    def my_min(a, b):

        # renvoi le min de 'a' et 'b'

        if (a >= b):

            return b

        else:

            return a


    def my_abs(a):

        # calcule le abs de 'a'

        if (a < 0):

            return -a

        else:

            return a



    def my_puissance(a, n):

        # calcule la puissance 'a' de 'n'

        m = 1

        if (n > 0):

            i = 0

            while (i < n):

                m = m * a

                i += 1

        elif (n == 0):

            m = 1

        elif (n < 0):

            i = 0

            while (i < (-n)):

                m = m * (1 / a)

                i += 1

        return m



    def my_div(a, b, number_of_digit_after_the_floating_point_):

        # calcule  'a' / 'b' avec 'number_of_digit_after_the_floating_point_' nombre de numereau apres la vergule

        m = 0

        if (a < 0):

            a = -a

        if (b < 0):

            b = -b

        i = 0
        
        q = 1
        
        while (q < a):
            
            q = q * 10
            
            i += 1

        while (i > -1):

            while (m * b < a):

                # m = m - my_puissance(a=10, n=(i))

                m = m + q

                # print("i = ", i, " . m = ", m, " . a = ", a, " . m * b = ", m * b)

            if (m * b > a):

                m = m - q

                i -= 1
                
                q = my_puissance(a=10, n=i)
                            
            else:
                
                break


            # print("1 . i = ", i, " . m = ", m)

        # print("finished . 1")

        k = 0

        m1 = 0

        if ((number_of_digit_after_the_floating_point_ > 0) and (m * b != a)):

            d1 = my_puissance(a=10, n=number_of_digit_after_the_floating_point_)

            m1 = m * d1

            i = number_of_digit_after_the_floating_point_

            while (i > -1):

                d2 = my_puissance(a=10, n=i)

                while ((m1 + k) * b < a * d1):

                    k = k + d2

                if ((m1 + k) * b == a * d1):

                    break

                else:

                    k = k - d2

                i -= 1
                
        i = 0
        
        while (my_puissance(a=10, n=i) <= k):
            
            i += 1
            
        #if (i == 0):
            
        #    i = 1

        # print("finale . m = ", m, " .  (m * b == a) = ", (m * b == a), " . (m1 + k) * b == a * my_puissance(a=10, n=number_of_digit_after_the_floating_point_) = ", (m1 + k) * b == a * my_puissance(a=10, n=number_of_digit_after_the_floating_point_))


        return [m, k, number_of_digit_after_the_floating_point_ - i]

    def conv_chr_int(c):

        # convertie un caractere à un chiffre

        n = 0

        if (len(c) == 1):

            if (c == "0"):

                n = 0

            elif (c == "1"):

                n = 1

            elif (c == "2"):

                n = 2

            elif (c == "3"):

                n = 3

            elif (c == "4"):

                n = 4

            elif (c == "5"):

                n = 5

            elif (c == "6"):

                n = 6

            elif (c == "7"):

                n = 7

            elif (c == "8"):

                n = 8

            elif (c == "9"):

                n = 9

        return n

    def str_to_int(s):

        # convertie un string à un integer

        erreur = False

        num = 0

        i = -1

        r = True

        p = 0

        s_ = ""

        r_ = True

        t = 1

        while ((i < len(s)) and (r_)):

            i += 1

            if ((s[i] == "+") or (s[i] == "-")):

                if (s[i] == "-"):

                    t = -t

            else:

                r_ = False



        while ((i < len(s)) and (r)):

            if (not ((s[i] == "0") or (s[i] == "1") or (s[i] == "2") or (s[i] == "3") or (s[i] == "4") or (s[i] == "5") or 
                (s[i] == "6") or (s[i] == "7") or (s[i] == "8") or (s[i] == "9") or (s[i] == "."))):

                r = False

            if (s[i] == "."):

                p += 1

            if ((r) and (p == 0)):

                s_ += s[i]

            i += 1

        if ((i < len(s)) or (p > 1)):

            erreur = True


        if (not (erreur)):

            i = len(s_) - 1

            q = 1

            while (i >= 0):

                num += conv_chr_int(c=s_[i]) * q

                i -= 1

                q *= 10


            num = num * t
        

        return [erreur, num]


    def conv_int_chr(p):

        # convertie un integer à un chr

        c = ""

        if ((p < 10) and (p >= 0)):

            if (p == 0):

                c = "0"

            elif (p == 1):

                c = "1"

            elif (p == 2):

                c = "2"

            elif (p == 3):

                c = "3"

            elif (p == 4):

                c = "4"

            elif (p == 5):

                c = "5"

            elif (p == 6):

                c = "6"

            elif (p == 7):

                c = "7"

            elif (p == 8):

                c = "8"

            elif (p == 9):

                c = "9"

        return c
        


    def my_puissance_1(l, n, number_of_digit_after_the_floating_point_):

        # calcule la puissance 'l' de 'n' avec 'number_of_digit_after_the_floating_point_' nombre de numereau apres la vergule

        # 'a3' c'est le nombre de zero avent 'a2' : 'a1', 0{'a3'}'a2'

        a1 = l[0]

        a2 = l[1]

        a3 = l[2]
        
        a4 = l[3]

        m = [0, 0, number_of_digit_after_the_floating_point_ - 1, 1]

        if (n > 0):

            a = a1 * a4

            f = False

            if (a2 != 0):

                s_ = str(a2)

                if ((number_of_digit_after_the_floating_point_ < len(str(a2))) or (a3 > 0)):

                    s_ = ""

                    s = str(a2)

                    i = 0

                    while (i < a3):

                        s_ += "0"

                        i += 1

                    # print("s_ = ", s_)

                    i = 0

                    while (i < len(s)):

                        s_ += s[i]

                        i += 1

                # print("a1 = ", a1, " . s_ = ", s_, " . len(s_) = ", len(s_), " . a3 = ", a3)

                a = int(str(a1 * a4) + s_)


                f = True

            if (not f):

                x = my_puissance(a=a, n=n)

                if (x < 0):
                    
                    a4 = -1
                    
                    x = -x
                    
                else:
                    
                    a4 = 1

                m = [x, 0, number_of_digit_after_the_floating_point_ - 1, a4]

                #print("m = ", m, " . a = ", a)

            else:

                i = 0

                m1 = 1

                while (i < n):

                    m1 = m1 * a

                    i += 1

                #print("i = ", i, " . m1 = ", m1, " . len(str(m1)) = ", len(str(m1)), " . a = ", a, " . len(str(a)) = ", len(str(a)))

                l1 = my_div(a=m1, b=my_puissance(a=10, n=(n * number_of_digit_after_the_floating_point_)), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
                
                #print("l1 = ", l1)
                

                if (m1 < 0):
                    
                    a4 = -1
                    
                else:
                    
                    a4 = 1
                
                m = []
                
                i = 0
                
                while (i < len(l1)):
                    
                    m.append(l1[i])
                    
                    i += 1
                    
                m.append(a4)

        elif (n == 0):

            m = [1, 0, number_of_digit_after_the_floating_point_ - 1, 1]

        return m


    def liste_number_of_digit_after_the_floating_point__to_n_1(l, number_of_digit_after_the_floating_point_):
        
        # renvoi le nombre de 'l' compatible avec numba
        
        m = 0
        
        if (number_of_digit_after_the_floating_point_ > 0):
        
            m = l[0] * my_puissance(a=10, n=number_of_digit_after_the_floating_point_)
        
            m += l[1]
        
        else:
            
            m = l[0] * 10
            
            m += l[1]
        
        m = m * l[3]
        
        return m



    def n_to_liste_number_of_digit_after_the_floating_point__1(n, number_of_digit_after_the_floating_point_):

        # transform une liste 'l' en numereau 'n' compatible avec numba
        
        a4 = 1
        
        #print("n = ", n)
        
        if (n < 0):
            
            a4 = -1
            
            n = -n
        
        a = my_div(a=n, b=my_puissance(a=10, n=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=1)
        
        a1 = a[0]
        
        a2 = n - (a1 * my_puissance(a=10, n=number_of_digit_after_the_floating_point_))
        
        #print("a = ", a, " . a1 = ", a1, " . a2 = ", a2)
        
        i = 0
        
        while (my_puissance(a=10, n=i) <= a2):
            
            i += 1
            
        if (i == 0):
            
            i = 1
            
        a3 = number_of_digit_after_the_floating_point_ - i
        
        return [a1, a2, a3, a4]
        
        



    def my_puissance_2(l, n, number_of_digit_after_the_floating_point_):
        
        # compatible avec numba

        # calcule la puissance 'l' de 'n' avec 'number_of_digit_after_the_floating_point_' nombre de numereau apres la vergule

        # 'a3' c'est le nombre de zero avent 'a2' : 'a1', 0{'a3'}'a2'

        d = liste_number_of_digit_after_the_floating_point__to_n_1(l=l, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        d = my_puissance(a=d, n=n)
        
        t = 1
        
        if (l[3] == -1):
        
            t = my_puissance(a=-1, n=n)

        # d1 = my_div(a=d, b=my_puissance(a=10, n=((n - 1) * number_of_digit_after_the_floating_point_)), number_of_digit_after_the_floating_point_=1)

        d1 = [d // my_puissance(a=10, n=((n - 1) * number_of_digit_after_the_floating_point_))]

        d = d1[0]

        d2 = n_to_liste_number_of_digit_after_the_floating_point__1(n=d, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2[3] = t
        
        return d2


    def n_de_my_puissance_1(L, number_of_digit_after_the_floating_point_):

        # renvoi le 'int(s)' pour my_puissance_1

        i = len(str(L))

        s = str(L)

        while (i < number_of_digit_after_the_floating_point_):

            s += "0"

            i += 1

        return int(s)




    def mod(a, b):

        # retourne le mode 'a' à 'b'

        r = my_div(a=a, b=b, number_of_digit_after_the_floating_point_=1)

        r2 = r[0] * b

        r3 = a - r2

        return r3




    def pgcd(a, b):

        # trouve le PGCD entre 'a' et 'b'

        r0 = a

        r1 = b

        r2 = 0
        
        r = mod(a=r0, b=r1)

        while (r != 0):

            r2 = r
            
            r0 = r1

            r1 = r2
            
            r = mod(a=r0, b=r1)

        return r1


    def ppcm(a, b):

        # trouve le ppcm entre 'a' et 'b'

        a1 = my_div(a=a * b, b=pgcd(a=a, b=b), number_of_digit_after_the_floating_point_=1)
        
        return a1[0]




    def ent(a):
        
        # retourne le nombre entier de 'a'
        
        i = 0
        
        while (my_puissance(a=10, n=i) <= a):
            
            i += 1
            
        d = 0
        
        while (i > -1):
        
            while (d < a):
            
                d += my_puissance(a=10, n=i)
            
            if (d > a):
                
                d -= my_puissance(a=10, n=i)
                
                i -= 1
                
            else:
                
                break
            
            
        return d

    def s_ent(s):
        
        # renvoi le coté entier de numero 's'

        i = 0
        
        s_ = ""
        
        while ((i < len(s)) and (s[i] != ".")):
            
            s_ += s[i]
            
            i += 1
        
        return s_


    def generer_number_of_digit_after_the_floating_point_(n):

        # genere 'number_of_digit_after_the_floating_point_' superieur ou egale à 'n'

        o = 2

        if (mod(a=n, b=2) == 0):

            o = n

        else:

            o = n + 1


        return o


    def my_racine(a, n):

        # calcule le racine 'a' de 'n'

        m = 0.0

        if (n == 1):

            m = a

        elif ((a < 0) and (mod(a=n, b=2) == 0)):

            m = 0.0

        elif (n > 1):

            i = 0

            while (i < 11):

                while (my_puissance(a=m, n=n) < a):

                    m = m + my_puissance(a=10, n=(-i))

                if (my_puissance(a=m, n=n) == a):

                    break

                else:

                    m = m - my_puissance(a=10, n=(-i))

                    i += 1

                # print("m = ", m)

        return m



    def liste_number_of_digit_after_the_floating_point__to_n(l, number_of_digit_after_the_floating_point_):

        # renvoi le nombre de 'l'

        s_ = ""
        
        moin = ""
        
        #print("l = ", l)
        
        if (l[3] == -1):
            
            moin = "-"
            
        
        if (number_of_digit_after_the_floating_point_ == len(str(l[1])) + l[2]):
            
            #print("hello 1 .")
            
            if (l[1] != 0):

                s = str(l[1])

                if (l[2] != 0):
                    
                    #print("hello 2 .")

                    i = 0

                    while (i < l[2]):

                        s_ += "0"

                        i += 1
                        
                    #print("h 2 . i = ", i, " . s_ = ", s_)

                i = 0

                while (i < len(s)):

                    s_ += s[i]

                    i += 1
                    
                #print("h 3 . s_ = ", s_)

            else:

                i = 0

                while (i < number_of_digit_after_the_floating_point_):

                    s_ += "0"

                    i += 1

        else:
            
            i = 0
            
            while (i < my_min(a=l[2], b=number_of_digit_after_the_floating_point_)):
                
                s_ += "0"
                
                i += 1
                
            ss = str(l[1])
            
            j = 0
            
            while ((j < len(ss)) and (i < number_of_digit_after_the_floating_point_)):
                
                s_ += ss[j]
                
                j += 1
                
                i += 1
                

        return int(moin + str(l[0]) + s_)    


    def my_inferieur_1(l1, l2, number_of_digit_after_the_floating_point_):

        # inferieur : <

        res = False

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        if (d1 < d2):

            res = True

        else:

            res = False

        return res


    def my_superieur_1(l1, l2, number_of_digit_after_the_floating_point_):

        # superieur : >

        res = False

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        if (d1 > d2):

            res = True

        else:

            res = False

        return res



    def my_egale_1(l1, l2, number_of_digit_after_the_floating_point_):

        # egale : =

        res = False

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        if (d1 == d2):

            res = True

        else:

            res = False

        return res


    def n_to_liste_number_of_digit_after_the_floating_point_(n, number_of_digit_after_the_floating_point_):

        # transform une liste 'l' en numereau 'n'

        n1 = str(n)
        
        n2 = n1
        
        moin = False
        
        a1 = 0

        a2 = 0

        a3 = 0
        
        a4 = 1

        
        if (n < 0):
            
            moin = True
            
            a4 = -1
            
            n = -n
            
            i = 1
            
            n2 = ""
            
            while (i < len(n1)):
                
                n2 += n1[i]
                
                i += 1

        
        if (number_of_digit_after_the_floating_point_ < len(n2)):

            
            s = ""

            i = 0

            while (i < len(n2) - number_of_digit_after_the_floating_point_):

                s += n2[i]

                i += 1

            # print("1 . s = ", s)

            if (s != ""):

                a1 = int(s)


            a3 = 0

            while ((i < len(n2)) and (n2[i] == "0")):

                a3 += 1

                i += 1

            if (i == len(n2)):

                a3 -= 1

            s = ""

            while (i < len(n2)):

                s += n2[i]

                i += 1

            if (s != ""):

                # print("2 . s = ", s)

                a2 = int(s)

        else:

            a1 = 0

            a2 = n

            a3 = number_of_digit_after_the_floating_point_ - len(str(a2))
            
        return [a1, a2, a3, a4]


    def my_div_1(l_a, l_b, number_of_digit_after_the_floating_point_):

        # my_division 'l_a' / 'l_b'

        #print("l_a = ", l_a, " . l_b = ", l_b)

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        #print("d1 = ", d1, " . d2 = ", d2)

        d3 = my_div(a=d1, b=d2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)



        d = 1

        if (l_a[3] * l_b[3] <= 0):

            d = -1
            
        l = []
        
        i = 0
        
        while (i < len(d3)):
            
            l.append(d3[i])
            
            i += 1
            
        l.append(d)
        
        #print("l = ", l)
            
        #print("d1 = ", d1, " . d2 = ", d2, " . d3 = ", d3)

        return l


    def my_multip_1(l_a, l_b, number_of_digit_after_the_floating_point_):

        # my_multiplication  'l_a' * 'l_b'

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d3 = d1 * d2
        
        mo = 1
        
        if (d3 < 0):
            
            d3 = -d3
            
            mo = -1

        
        d4 = n_to_liste_number_of_digit_after_the_floating_point__1(n=d3, number_of_digit_after_the_floating_point_=(number_of_digit_after_the_floating_point_ * 2))


        d4[3] = mo

        return d4


    def my_moin_1(l_a, l_b, number_of_digit_after_the_floating_point_):

        # my_moin  'l_a' - 'l_b'

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d3 = d1 - d2

        d4 = n_to_liste_number_of_digit_after_the_floating_point__1(n=d3, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        return d4


    def my_plus_1(l_a, l_b, number_of_digit_after_the_floating_point_):

        # my_plus  'l_a' + 'l_b'

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d2 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l_b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d3 = d1 + d2

        d4 = n_to_liste_number_of_digit_after_the_floating_point__1(n=d3, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        return d4


    def my_racine_1(l, n, number_of_digit_after_the_floating_point_):

        # calcule  'l' R 'b' avec 'number_of_digit_after_the_floating_point_' nombre de numereau apres la vergule

        m = [0, 0, number_of_digit_after_the_floating_point_ - 1, 1]

        d = 0

        d1 = liste_number_of_digit_after_the_floating_point__to_n(l=l, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        #print("1 . d1 = ", d1 , " . len(str(d1)) = ", len(str(d1)))    

        d1 = d1 * my_puissance(a=10, n=((n - 1) * number_of_digit_after_the_floating_point_))

        #print("2 . d1 = ", d1 , " . len(str(d1)) = ", len(str(d1)))
        
        mo = 1
        
        if (d1 < 0):
        
            d1 = -d1

            mo = -1

        i = 0

        while (-1 < i):

            i = 0

            o = d

            t = 0

            # print("m = ", m, " . n = ", n, " _ = ", my_puissance(a=m, n=n))

            while (my_puissance(a=d, n=n) < d1):

                if (t < 10):

                    d = d + my_puissance(a=10, n=i)

                    t += 1
                    
                else:
                    
                    t = 0
                    
                    d = o
                    
                    i += 1

                #print("i = ", i, " . t = ", t, " . d = ", d, " . my_puissance(a=d, n=n) = ", my_puissance(a=d, n=n), " . d1 = ", d1)

            #print("i = ", i, " . m = ", m, " . d = ", d, " . len(str(d)) = ", len(str(d)), " . len(str(d1)) = ", len(str(d1)), " . d1 = ", d1, " . _ = ", (my_puissance(a=d, n=n) > d1))

            if (my_puissance(a=d, n=n) > d1):

                d = d - my_puissance(a=10, n=i)

                i -= 1

            # if (i < 0):
            #
            #     break
            #
            # # print("1 . i = ", i, " . m = ", m)
            #
            # i = 0

        m = n_to_liste_number_of_digit_after_the_floating_point_(n=d, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        if (mod(a=n, b=2) == 1):
            
            m[3] = mo

        return m



    def my_racine_2(l, n, number_of_digit_after_the_floating_point_):

        # compatible avec numba

        # calcule  'l' R 'b' avec 'number_of_digit_after_the_floating_point_' nombre de numereau apres la vergule

        m = [0, 0, number_of_digit_after_the_floating_point_ - 1, 1]

        d = 0

        d1 = liste_number_of_digit_after_the_floating_point__to_n_1(l=l, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        d1 = d1 * my_puissance(a=10, n=((n - 1) * number_of_digit_after_the_floating_point_))
        
        mo = 1
        
        if (d1 < 0):
        
            d1 = -d1

            mo = -1

        i = n * number_of_digit_after_the_floating_point_
        
        q = my_puissance(a=10, n=i)

        while (q <= d1):
            
            q = q * 10
            
            i += 1

        o = 0

        while (-1 < i):

            o = my_puissance(a=d, n=n)
            
            # print("m = ", m, " . n = ", n, " _ = ", my_puissance(a=m, n=n))

            while (o < d1):
                
                d = d + my_puissance(a=10, n=i)

                o = my_puissance(a=d, n=n)

                # print("i = ", i, " . m = ", m, " . d = ", d)

            # print("i = ", i, " . m = ", m, " . d = ", d, " . len(str(d)) = ", len(str(d)), " . len(d1) = ", len(str(d1)), " . d1 = ", d1, " . _ = ", (my_puissance(a=d, n=n) == d1))

            if (o > d1):

                d = d - my_puissance(a=10, n=i)

                i -= 1
                
            else:
                
                break

            
        m = n_to_liste_number_of_digit_after_the_floating_point__1(n=d, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        if (mod(a=n, b=2) == 1):
            
            m[3] = mo

        return m






    def s_n_to_liste_number_of_digit_after_the_floating_point_(s, number_of_digit_after_the_floating_point_):

        # transforme 's' en liste_number_of_digit_after_the_floating_point_

        a1 = 0

        a2 = 0

        a3 = 0
        
        a4 = 1

        point = False

        s1 = ""

        i = 0

        while ((i < len(s)) and ((s[i] == '+') or (s[i] == '-'))):

            if (s[i] == '-'):
                
                a4 = -a4
                
            i += 1

        #print("_1 . s1 = ", s1)

        while ((i < len(s)) and (s[i] != '.')):

            s1 += s[i]

            i += 1

        #print("s1 = ", s1, " . s = ", s)

        if ((i < len(s)) and (s[i] == '.')):

            point = True

            i += 1

        #print("1 . s1 = ", s1, " . point = ", point, " . s = ", s)

        if (s1 != ""):

            a1 = int(s1)
            
            # if (a1 < 0):
                
            #     a4 = -1
                
            #     a1 = -a1


        a3 = 0

        j = 0

        while ((i < len(s)) and (s[i] == "0") and (a3 < number_of_digit_after_the_floating_point_)):

            a3 += 1

            i += 1

            j += 1

        if ((a3 > 0) and ((i == len(s)) or (a3 == number_of_digit_after_the_floating_point_))):

            a3 -= 1

        s1 = ""

        while ((i < len(s)) and (j < number_of_digit_after_the_floating_point_)):

            s1 += s[i]

            i += 1

            j += 1

        # print("2 . s1 = ", s1, " . j = ", j)

        if (j < number_of_digit_after_the_floating_point_):

            if ((point) and (s1 != "") and (int(s1) != 0)):

                while (j < number_of_digit_after_the_floating_point_):

                    s1 += "0"

                    j += 1

            else:

                a2 = 0

                a3 = number_of_digit_after_the_floating_point_ - 1

        if (s1 != ""):

            # print("3 . s1 = ", s1, " . len(s1) = ", len(s1))

            a2 = int(s1)


        return [a1, a2, a3, a4]

    def liste_number_of_digit_after_the_floating_point__to_s_n(l, number_of_digit_after_the_floating_point_):

        # transforme une liste_number_of_digit_after_the_floating_point_ 'l' en s

        #d = liste_number_of_digit_after_the_floating_point__to_n(l=l, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        #print("l = ", l, " . d = ", d)


        s = ""

        
        #sd = str(d)

        # t = len(sd) - number_of_digit_after_the_floating_point_

        # # print("t = ", t)

        # while (i < t):

        #     s += sd[i]

        #     i += 1

        # if (s == ""):

        #     s = "0"

        # if (s == "-"):
            
        #     s = "-0"

        # s += "."

        # while (i < len(sd)):

        #     s += sd[i]

        #     i += 1


        
        s = str(l[0])
        
        if (l[3] == -1):
            
            s = "-" + s
            
        #if (l[1] != 0):
            
        s += "."
            
        i = 0
        
        while (i < l[2]):
            
            s += "0"
            
            i += 1
            
        s += str(l[1])
        

        return s



    def i_comparator_0_i(s1, i_operator_0_i, s2, number_of_digit_after_the_floating_point_):
        
        
        
        i_result_0_i = False
        
        
        
        i_functon_of_preparing_0_i(number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        
        i_file_a_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_a_0_i.txt")
        
        
        i_file_b_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_b_0_i.txt")
        
        
        i_file_of_operator_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_operator_0_i.txt")
        
        
        i_file_of_result_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_result_0_i.txt")
        
        
        
        with open(i_file_a_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(s1)
            
            
            
        
        
        with open(i_file_b_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(s2)
            
            
        
        
        with open(i_file_of_operator_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_operator_0_i)
            
            
        
        
        
        
        import i_runner_of_my_math_1_0_i
        
        importlib.reload(i_runner_of_my_math_1_0_i)
        
        
        
        
        i_runner_of_my_math_1_0_i.i_main_0_i()
        
        
        
        
        
        
        with open(i_file_of_result_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            i_content_of_result_0_i = f_.read(os.path.getsize(i_file_of_result_0_i))
            
            
        
        
        
        if (i_content_of_result_0_i == "true"):
            
            
            i_result_0_i = True
            
            
        elif (i_content_of_result_0_i == "false"):
            
            
            i_result_0_i = False
            
            
            
        
        return i_result_0_i
        
        


    
    
    def i_greater_1_i(s1, s2, number_of_digit_after_the_floating_point_):
        
        
        i_v_0_i = i_comparator_0_i(s1=s1, i_operator_0_i=">=", s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        i_v_1_i = i_comparator_0_i(s1=s1, i_operator_0_i="==", s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        if ((i_v_0_i == True) and (i_v_1_i == False)):
            
            
            return True
            
            
        else:
            
            
            return False
            
            
        
        
    
    def i_inferior_1_i(s1, s2, number_of_digit_after_the_floating_point_):
        
        
        i_v_0_i = i_comparator_0_i(s1=s1, i_operator_0_i=">=", s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        
        if ((i_v_0_i == False)):
            
            
            return True
            
            
        else:
            
            
            return False
            
            
        
    
    
    def i_equal_1_i(s1, s2, number_of_digit_after_the_floating_point_):
        
        
        
        i_v_1_i = i_comparator_0_i(s1=s1, i_operator_0_i="==", s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        if ((i_v_1_i == True)):
            
            
            return True
            
            
        else:
            
            
            return False
            
            
        
        
    
    
    
    
    
    def my_superieur_s_n_1(s1, s2, number_of_digit_after_the_floating_point_):
    
        return my_superieur_1(l1=s_n_to_liste_number_of_digit_after_the_floating_point_(s=s1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l2=s_n_to_liste_number_of_digit_after_the_floating_point_(s=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
    
    
    
    def my_inferieur_s_n_1(s1, s2, number_of_digit_after_the_floating_point_):
    
        return my_inferieur_1(l1=s_n_to_liste_number_of_digit_after_the_floating_point_(s=s1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l2=s_n_to_liste_number_of_digit_after_the_floating_point_(s=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
    
    
    
    def my_egale_s_n_1(s1, s2, number_of_digit_after_the_floating_point_):
    
    
        return my_egale_1(l1=s_n_to_liste_number_of_digit_after_the_floating_point_(s=s1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l2=s_n_to_liste_number_of_digit_after_the_floating_point_(s=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
    
    
    
    
    




    def cos_sin(alpha_1):

        # calcule le cos et le sin de 'alpha_1'

        alpha = alpha_1 / math.pi

        x = 0

        y = 0

        a = mod(a=alpha, b=(1 / 2))

        if (a == 0):

            x = 1

            y = 0

        else:

            x = my_racine(a=(1 - (1 / (my_puissance(a=((1 / (2 * a)) - 1), n=2) + 1))), n=2)

            y = my_racine(a=(1 / (my_puissance(a=((1 / (2 * a)) - 1), n=2) + 1)), n=2)

        b = int(alpha / (1 / 2))

        c = mod(a=b, b=4)

        if (c == 0):

            # 1er care

            x = x

            y = y

        elif (c == 1):

            # 2eme care

            x_ = x

            x = -y

            y = x_

        elif (c == 2):

            # 3eme care

            x = -x

            y = -y

        elif (c == 3):

            # 4eme care

            x_ = x

            x = y

            y = -x_

        return [x, y]



    def cocos_cosin(x, y):

        # calcule le alpha_1

        r = 0

        if ((x >= 0) and (y >= 0)):

            # 1er care

            r = 0

        elif ((x <= 0) and (y >= 0)):

            # 2eme care

            r = 1

        elif ((x <= 0) and (y <= 0)):

            # 3eme care

            r = 2

        elif ((x >= 0) and (y <= 0)):

            # 4eme care

            r = 3

        x = my_abs(a=x)

        y = my_abs(a=y)

        return (((y * math.pi) / (2 * (x + y))) + (r * math.pi))



    def plus_one_in_l_c(l_c, l, n):

        # n_comence_par_0

        # plus 1 avec la liste l_c

        the_max_number = len(l_c)

        i = n

        l[i] += 1

        if (l[i] == the_max_number):

            l[i] = 0

            i += 1

            # print(" - l = ", l, " . i = ", i)

            if (len(l) < i + 1):

                l.append(0)

                # print("- l = ", l)

            else:

                plus_one_in_l_c(l_c=l_c, l=l, n=i)


    def list_l_c_to_s(l_c, l):

        # transforme l à s par l_c

        s = ""

        i = 0

        while (i < len(l)):

            t = l[i]

            s = l_c[t] + s

            # print("t = ", t, " . s = ", s, " . i = ", i)

            i += 1

        return s

    def from_int_to_list_l_c(l_c, n):

        # transforme n à une liste l depuit l_c

        l = [0]

        i = 0

        while (i < n):

            plus_one_in_l_c(l_c=l_c, l=l, n=0)

            i += 1

        return l


    def check_parentheses(s):

        # check si les parentheses sont correcte

        r = False

        i = 0

        t = 0
        
        g = False

        g_ = ""

        while (i < len(s)):
            
            if ((s[i] == '"') or (s[i] == '\'')):
                
                if (((i - 1 > -1) and (s[i - 1] != '\\')) or (i == 0)):
                
                    if (g_ == ""):
                    
                        g_ = s[i]
                    
                        g = True

                    elif (g_ == s[i]):
                        
                        g_ = ""
                        
                        g = False
            
            if (not g):

                if (s[i] == '('):

                    t += 1

                elif (s[i] == ')'):

                    t -= 1

            i += 1

        if (t == 0):

            r = True

        else:

            r = False

        return r


    def ajoute_parentheses(s, a, b):

        # ajoute deux parentheses à a et b

        s_ = ""

        if ((a < b) and (b < len(s))):

            i = 0

            while (i < a):

                s_ += s[i]

                i += 1

            s_ += "("

            while (i < b):

                s_ += s[i]

                i += 1

            s_ += ")"

            while (i < len(s)):

                s_ += s[i]

                i += 1

        return s_



    def is_numereau(s):

        # check si s contien un numereau

        i = 0

        res = True
        
        if ((len(s) > 0) and (s[0] == '.')):
            
            res = False
        
        else:

            while ((i < len(s)) and ((s[i] == '+') or (s[i] == '-'))):

                i += 1

            if (len(s) == i):

                res = False

            o = 0

            while ((i < len(s)) and (res)):

                if (((s[i] == '0') or (s[i] == '1') or (s[i] == '2') or (s[i] == '3') or (s[i] == '4') or (s[i] == '5') or
                    (s[i] == '6') or (s[i] == '7') or (s[i] == '8') or (s[i] == '9') or (s[i] == '.')) and (o < 2)):

                    res = True

                else:

                    res = False

                if (s[i] == '.'):

                    o += 1

                # print("i = ", i, " . s[i] = ", s[i], " . o = ", o)

                i += 1

        if ((res) and (s[len(s) - 1] == '.')):
            
            res = False


        return [res, o]





    def supprime_espace(s):

        # supprime tout les espaces de s

        s_ = ""

        g = False
        
        g_ = ""

        i = 0

        while (i < len(s)):

            if ((s[i] == '"') or (s[i] == '\'')):
                
                if ((i == 0) or ((i - 1 > -1) and (s[i - 1] != '\\'))):
                    
                    if (g_ == ""):
                        
                        g = True
                        
                        g_ = s[i]
                        
                    elif (g_ == s[i]):
                        
                        g_ = ""
                        
                        g = False
                        

            if (not g):

                if (s[i] != ' '):

                    s_ += s[i]

            else:
                
                s_ += s[i]

            i += 1

        return s_


    def s_to_liste(s):

        # transforme s en liste l

        l = []

        erreur = False

        s = supprime_espace(s=s)

        i = 0

        s_ = ""

        while ((i < len(s)) and (not erreur)):

            if ((s[i] == '(') or (s[i] == ')') or (s[i] == '*') or (s[i] == '+') or (s[i] == '/') or (s[i] == '-') or
                    (s[i] == '^') or (s[i] == 'R') or (s[i] == 'r')):

                if ((s_ != '') and (is_numereau(s_)[0])):

                    erreur = False

                elif (s_ != ''):

                    erreur = True

                # print("i = ", i, " . s[i] = ", s[i], " . s_ = ", s_, " . erreur = ", erreur)

                if ((s_ != '')):

                    l.append(s_)

                l.append(s[i])

                s_ = ""

            else:

                s_ += s[i]

            i += 1

        if ((len(s) > 0) and (s_ != "")):

            if (not (is_numereau(s=s_)[0])):

                erreur = True

            l.append(s_)

        return [erreur, l]



    def s_to_numereau(s):

        # transforme s à un numereau

        res = 0

        s = supprime_espace(s=s)

        if (is_numereau(s=s)[0]):

            t = 1

            i = 0

            while ((i < len(s)) and ((s[i] == '+') or (s[i] == '-'))):

                if (s[i] == '+'):

                    t = t

                elif (s[i] == '-'):

                    t = -t

                i += 1

            # print("s = ", s, " . t = ", t)

            s_1 = ""

            o = False

            while ((i < len(s)) and (not o)):

                if (s[i] == '.'):

                    o = True

                else:

                    s_1 += s[i]

                    i += 1

            s_2 = ""

            if (o):

                i += 1

                while (i < len(s)):

                    s_2 += s[i]

                    i += 1

            if (s_1 != ""):

                res = int(s_1)

            if ((s_2 != "") and (int(s_2) != 0)):

                res += int(s_2) / my_puissance(a=10, n=len(s_2))

            # print("s_1 = ", s_1, " . s_2 = ", s_2, " . res = ", res)

            res = res * t

        return res


    def assemble(l, n):

        # asemble deux element 'n' et 'n + 1' dans la liste l

        m = []

        # print("assemblage")

        if (n < len(l)):

            i = 0

            while (i < n):

                m.append(l[i])

                i += 1

            t = ""

            t += l[i]

            if (i + 1 < len(l)):

                i += 1

                t += l[i]

            m.append(t)

            i += 1

            while (i < len(l)):

                m.append(l[i])

                i += 1

        return m


    def check_erreur(l):

        # check les erreur de la liste l

        erreur = False

        i = 0

        while ((i < len(l)) and (not erreur)):

            # print("l[i] = ", l[i])

            if ((l[i] == '+') or (l[i] == '-')):

                if ((i == 0) and (i + 1 < len(l)) and (is_numereau(s=l[i + 1])[0])):

                    l = assemble(l=l, n=i)

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and ((l[i - 1] == "*") or (l[i - 1] == "/") or
                        (l[i - 1] == "^") or (l[i - 1] == "R") or (l[i - 1] == "r") or (l[i - 1] == "+") or (l[i - 1] == "-")) and
                    (is_numereau(s=l[i + 1])[0])):

                    l = assemble(l=l, n=i)

                    erreur = False


                elif ((i > 0) and (l[i - 1] == '(') and (i + 1 < len(l)) and (is_numereau(s=l[i + 1])[0])):

                    l = assemble(l=l, n=i)

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (is_numereau(s=l[i - 1])[0]) and ((l[i + 1] == "+") or (l[i + 1] == "-"))):

                    erreur = False

                elif ((i > 0) and (l[i - 1] == '(') and (i + 1 < len(l)) and (l[i + 1] == '(')):

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (is_numereau(s=l[i - 1])[0]) and (is_numereau(s=l[i + 1])[0])):

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (l[i - 1] == ')') and (l[i + 1] == '(')):

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (l[i - 1] == ')') and (is_numereau(s=l[i + 1])[0])):

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (is_numereau(s=l[i - 1])[0]) and (l[i + 1] == '(')):

                    erreur = False

                else:

                    erreur = True

            elif ((l[i] == '*') or (l[i] == '/') or (l[i] == 'R') or (l[i] == "r") or (l[i] == '^')):

                if ((i > 0) and (i + 1 < len(l)) and (is_numereau(s=l[i - 1])[0]) and (is_numereau(s=l[i + 1])[0])):

                    erreur = False
                    
                elif ((i > 0) and (i + 1 < len(l)) and ((l[i + 1] == "+") or (l[i + 1] == "-"))):
                    
                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (is_numereau(s=l[i - 1])[0]) and (l[i + 1] == '(')):

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (l[i - 1] == ')') and (is_numereau(s=l[i + 1])[0])):

                    erreur = False

                elif ((i > 0) and (i + 1 < len(l)) and (l[i - 1] == ')') and (l[i + 1] == '(')):

                    erreur = False

                else:

                    erreur = True

            elif (l[i] == ')'):

                if ((i + 1 < len(l)) and (l[i + 1] == '(')):

                    erreur = True

                elif ((i + 1 < len(l)) and (l[i + 1] != "+") and (l[i + 1] != "-") and (l[i + 1] != "*")
                    and (l[i + 1] != "/") and (l[i + 1] != "^") and (l[i + 1] != "R") and (l[i + 1] != "r") and (l[i + 1] != ')')):

                    erreur = True


            elif (l[i] == '('):

                if ((i - 1 > -1) and (l[i - 1] == ')')):

                    erreur = True

                elif ((i - 1 > -1) and (l[i - 1] != "+") and (l[i - 1] != "-") and (l[i - 1] != "*")
                    and (l[i - 1] != "/") and (l[i - 1] != "^") and (l[i - 1] != "R") and (l[i - 1] != "r") and (l[i - 1] != '(')):

                    erreur = True

            elif (is_numereau(s=l[i])):

                if ((i - 1 > -1) and (l[i - 1] != "+") and (l[i - 1] != "-") and (l[i - 1] != "*")
                        and (l[i - 1] != "/") and (l[i - 1] != "^") and (l[i - 1] != "R") and (l[i - 1] != "r") and (l[i - 1] != '(')):
                    erreur = True

                if ((i + 1 < len(l)) and (l[i + 1] != "+") and (l[i + 1] != "-") and (l[i + 1] != "*")
                        and (l[i + 1] != "/") and (l[i + 1] != "^") and (l[i + 1] != "R") and (l[i + 1] != "r") and (l[i + 1] != ')')):
                    erreur = True

            #print("check_erreur . i = ", i, " . l[i] = ", l[i], " . erreur = ", erreur)

            i += 1

        return [erreur, l]


    def calcule(a, o, b):

        # clacule les deux nombre a et b avec l'operateur o

        res = 0

        erreur = False

        if (o == '+'):

            res = s_to_numereau(s=a) + s_to_numereau(s=b)

        elif (o == '-'):

            res = s_to_numereau(s=a) - s_to_numereau(s=b)

        elif (o == '*'):

            res = s_to_numereau(s=a) * s_to_numereau(s=b)

        elif (o == '/'):

            if (s_to_numereau(s=b) == 0):

                erreur = True

            else:

                res = s_to_numereau(s=a) / s_to_numereau(s=b)

        elif (o == '^'):

            t = is_numereau(s=b)

            if ((t[0]) and (t[1] == 0)):

                t_1 = s_to_numereau(s=b)

                t_2 = s_to_numereau(s=a)

                if ((t_1 < 0) and (t_2 == 0)):

                    erreur = True

                elif ((t_1 == 0) and (t_2 == 0)):

                    erreur = True

                else:

                    res = my_puissance(a=s_to_numereau(s=a), n=s_to_numereau(s=b))

            elif (t[0]):

                i = 0

                while (b[i] != '.'):

                    i += 1

                i += 1

                s = ""

                while (i < len(b)):

                    s += b[i]

                    i += 1

                if (int(s) == 0):

                    t_1 = s_to_numereau(s=b)

                    t_2 = s_to_numereau(s=a)

                    if ((t_1 < 0) and (t_2 == 0)):

                        erreur = True

                    elif ((t_1 == 0) and (t_2 == 0)):

                        erreur = True

                    else:

                        res = my_puissance(a=s_to_numereau(s=a), n=s_to_numereau(s=b))

                else:

                    erreur = True

            else:

                erreur = True

        elif ((o == 'R') or (o == 'r')):

            t = is_numereau(s=b)

            h1 = s_to_numereau(s=a)

            h = s_to_numereau(s=b)

            if ((h1 < 0) and (mod(a=h, b=2) == 0)):

                erreur = True

            elif ((t[0]) and (t[1] == 0) and (h > 0)):

                res = my_racine(a=s_to_numereau(s=a), n=s_to_numereau(s=b))

            elif ((t[0]) and (h > 0)):

                i = 0

                while (b[i] != '.'):

                    i += 1

                i += 1

                s = ""

                while (i < len(b)):

                    s += b[i]

                    i += 1

                if (int(s) == 0):

                    res = my_racine(a=s_to_numereau(s=a), n=s_to_numereau(s=b))

                else:

                    erreur = True


            else:

                erreur = True

        return [erreur, res]


    def calcule_1(a, o, b, number_of_digit_after_the_floating_point_):

        # clacule les deux nombre a et b avec l'operateur o

        res = ""

        erreur = False

        # print("l_a = ", s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_))

        # print("l_b = ", s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_))

        #print("a = ", a, " . b = ", b, " . o = ", o)

        res_1 = []

        if (o == '+'):

            res_1 = my_plus_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '-'):

            res_1 = my_moin_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '*'):

            res_1 = my_multip_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '/'):

            s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            if ((s_b[0] == 0) and (s_b[1] == 0)):

                erreur = True

            else:

                res_1 = my_div_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '^'):

            t = is_numereau(s=b)
            
            b_ = s_to_numereau(s=b)
            
            #print("b_ = ", b_)

            if ((t[0]) and (t[1] == 0) and (b_ >= 0)):

                s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                s_a = s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                if ((s_b[0] < 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                    erreur = True

                elif ((s_b[0] == 0) and (s_b[1] == 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                    erreur = True

                else:

                    res_1 = my_puissance_1(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            elif ((t[0]) and (b_ >= 0)):

                i = 0

                while (b[i] != '.'):

                    i += 1

                i += 1

                s = ""

                while (i < len(b)):

                    s += b[i]

                    i += 1

                if (int(s) == 0):

                    s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    s_a = s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    if ((s_b[0] < 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                        erreur = True

                    elif ((s_b[0] == 0) and (s_b[1] == 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                        erreur = True

                    else:

                        res_1 = my_puissance_1(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                        res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                else:
                    
                    
                    s = b.split(".")
                    
                    a1 = s[0] + s[1]
                    
                    b1 = my_puissance(a=10, n=len(s[1]))
                    
                    d = pgcd(a=int(a1), b=b1)
                    
                    a2 = int(a1) / d
                    
                    b2 = b1 / d
                    
                    #print("a2 = ", a2, " . b2 = ", b2)
                    
                    res_1 = my_puissance_1(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=a2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    res_1 = my_racine_1(l=res_1, n=b2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)


                    #erreur = True

            else:

                erreur = True

        elif ((o == 'R') or (o == 'r')):

            t = is_numereau(s=b)

            s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            s_a = s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            # if ((h1 < 0) and (mod(a=h, b=2) == 0)):
            #
            #     erreur = True

            if ((t[0]) and (t[1] == 0) and (s_b[0] > 0)):

                if ((s_a[0] < 0) and (mod(a=s_b[0], b=2) == 0)):

                    erreur = True

                else:

                    res_1 = my_racine_1(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            elif ((t[0]) and (s_b[0] > 0)):

                i = 0

                while (b[i] != '.'):

                    i += 1

                i += 1

                s = ""

                while (i < len(b)):

                    s += b[i]

                    i += 1

                if (int(s) == 0):

                    if ((s_a[0] < 0) and (mod(a=s_b[0], b=2) == 0)):

                        erreur = True

                    else:

                        res_1 = my_racine_1(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                        res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                else:

                    erreur = True

            else:

                erreur = True

        # print("res_1 = ", res_1)

        return [erreur, res]



    def calcule_2(a, o, b, number_of_digit_after_the_floating_point_):

        # clacule les deux nombre a et b avec l'operateur o

        res = ""

        erreur = False

        # print("l_a = ", s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_))

        # print("l_b = ", s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_))

        #print("a = ", a, " . b = ", b, " . o = ", o)

        res_1 = []

        if (o == '+'):

            res_1 = my_plus_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '-'):

            res_1 = my_moin_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '*'):

            res_1 = my_multip_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '/'):

            s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            if ((s_b[0] == 0) and (s_b[1] == 0)):

                erreur = True

            else:

                res_1 = my_div_1(l_a=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), l_b=s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

        elif (o == '^'):

            t = is_numereau(s=b)
            
            #b_ = s_to_numereau(s=b)
            
            b_ = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
            
            #print("b_ = ", b_)

            if ((t[0]) and (t[1] == 0) and (b_[3] >= 0)):

                s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                s_a = s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                if ((s_b[0] < 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                    erreur = True

                elif ((s_b[0] == 0) and (s_b[1] == 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                    erreur = True

                else:

                    res_1 = my_puissance_2(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

            elif ((t[0]) and (b_[3] >= 0)):

                i = 0

                while (b[i] != '.'):

                    i += 1

                i += 1

                s = ""

                while (i < len(b)):

                    s += b[i]

                    i += 1

                if (int(s) == 0):

                    s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    s_a = s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    if ((s_b[0] < 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                        erreur = True

                    elif ((s_b[0] == 0) and (s_b[1] == 0) and (s_a[0] == 0) and (s_a[1] == 0)):

                        erreur = True

                    else:

                        res_1 = my_puissance_2(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                        res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                else:

                    
                    s = b.split(".")
                    
                    a1 = s[0] + s[1]
                    
                    b1 = my_puissance(a=10, n=len(s[1]))
                    
                    d = pgcd(a=int(a1), b=b1)
                    
                    a2 = my_div(a=int(a1), b=d, number_of_digit_after_the_floating_point_=1)
                    
                    b2 = my_div(a=b1, b=d, number_of_digit_after_the_floating_point_=1)

                    res_1 = my_puissance_2(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=a2[0], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    # print("a2 = ", a2, " . b2 = ", b2, " . res_1 = ", res_1)

                    number_v_0 = b2[0]

                    if (not ((res_1[3] < 0) and ((mod(a=number_v_0, b=2) == 0)))):
                    
                        #print("a2 = ", a2, " . b2 = ", b2)
                        

                        res_1 = my_racine_2(l=res_1, n=b2[0], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                        res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    else:

                        erreur = True

                    #erreur = True

            else:

                erreur = True

        elif ((o == 'R') or (o == 'r')):


            v_0 = b.split(".")

            if (not ((my_inferieur_s_n_1(s1=a, s2="0", number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point) == True) and ((v_0[0][-1] == "0") or (v_0[0][-1] == "2") or (v_0[0][-1] == "4") or (v_0[0][-1] == "6") or (v_0[0][-1] == "8")))):

                t = is_numereau(s=b)

                s_b = s_n_to_liste_number_of_digit_after_the_floating_point_(s=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                s_a = s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                # if ((h1 < 0) and (mod(a=h, b=2) == 0)):
                #
                #     erreur = True

                if ((t[0]) and (t[1] == 0) and (s_b[0] > 0)):

                    if ((s_a[0] < 0) and (mod(a=s_b[0], b=2) == 0)):

                        erreur = True

                    else:

                        res_1 = my_racine_2(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                        res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                elif ((t[0]) and (s_b[0] > 0)):

                    i = 0

                    while (b[i] != '.'):

                        i += 1

                    i += 1

                    s = ""

                    while (i < len(b)):

                        s += b[i]

                        i += 1

                    if (int(s) == 0):

                        if ((s_a[0] < 0) and (mod(a=s_b[0], b=2) == 0)):

                            erreur = True

                        else:

                            res_1 = my_racine_2(l=s_n_to_liste_number_of_digit_after_the_floating_point_(s=a, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_), n=s_to_numereau(s=b), number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                            res = liste_number_of_digit_after_the_floating_point__to_s_n(l=res_1, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                    else:

                        erreur = True

                else:

                    erreur = True

            else:

                erreur = True


        # print("res_1 = ", res_1)

        return [erreur, res]

    
        
    
    def i_add_2_i(i_string_a, i_string_b, number_of_digit_after_the_floating_point_):
        
        
        i_functon_of_preparing_0_i(number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        
        i_file_a_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_a_0_i.txt")
        
        
        i_file_b_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_b_0_i.txt")
        
        
        i_file_of_operator_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_operator_0_i.txt")
        
        
        i_file_of_result_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_result_0_i.txt")
        
        
        
        with open(i_file_a_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_a)
            
            
            
        
        
        with open(i_file_b_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_b)
            
            
        
        
        with open(i_file_of_operator_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write("+")
            
            
        
        
        
        
        import i_runner_of_my_math_1_0_i
        
        importlib.reload(i_runner_of_my_math_1_0_i)
        
        
        
        
        i_runner_of_my_math_1_0_i.i_main_0_i()
        
        
        
        
        
        
        
        with open(i_file_of_result_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            i_content_of_result_0_i = f_.read(os.path.getsize(i_file_of_result_0_i))
            
            
        
        
        
        return i_content_of_result_0_i
        
    
    
    def i_sub_2_i(i_string_a, i_string_b, number_of_digit_after_the_floating_point_):
        
        
        
        i_functon_of_preparing_0_i(number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        
        i_file_a_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_a_0_i.txt")
        
        
        i_file_b_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_b_0_i.txt")
        
        
        i_file_of_operator_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_operator_0_i.txt")
        
        
        i_file_of_result_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_result_0_i.txt")
        
        
        
        with open(i_file_a_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_a)
            
            
            
        
        
        with open(i_file_b_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_b)
            
            
        
        
        with open(i_file_of_operator_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write("-")
            
            
        
        
        
        
        import i_runner_of_my_math_1_0_i
        
        importlib.reload(i_runner_of_my_math_1_0_i)
        
        
        
        
        i_runner_of_my_math_1_0_i.i_main_0_i()
        
        
        
        
        
        
        
        with open(i_file_of_result_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            i_content_of_result_0_i = f_.read(os.path.getsize(i_file_of_result_0_i))
            
            
        
        
        
        return i_content_of_result_0_i
        
        
        
    
    
    def i_mult_2_i(i_string_a, i_string_b, number_of_digit_after_the_floating_point_):
        
        
        
        i_functon_of_preparing_0_i(number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        
        i_file_a_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_a_0_i.txt")
        
        
        i_file_b_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_b_0_i.txt")
        
        
        i_file_of_operator_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_operator_0_i.txt")
        
        
        i_file_of_result_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_result_0_i.txt")
        
        
        
        with open(i_file_a_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_a)
            
            
            
        
        
        with open(i_file_b_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_b)
            
            
        
        
        with open(i_file_of_operator_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write("*")
            
            
        
        
        
        
        import i_runner_of_my_math_1_0_i
        
        importlib.reload(i_runner_of_my_math_1_0_i)
        
        
        
        
        i_runner_of_my_math_1_0_i.i_main_0_i()
        
        
        
        
        
        
        
        with open(i_file_of_result_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            i_content_of_result_0_i = f_.read(os.path.getsize(i_file_of_result_0_i))
            
            
        
        
        
        return i_content_of_result_0_i
        
        
        
    
    
    def i_div_2_i(i_string_a, i_string_b, number_of_digit_after_the_floating_point_):
        
        
        
        i_functon_of_preparing_0_i(number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
        
        
        
        i_file_a_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_a_0_i.txt")
        
        
        i_file_b_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_b_0_i.txt")
        
        
        i_file_of_operator_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_operator_0_i.txt")
        
        
        i_file_of_result_0_i = os.path.join(i_path_0_i, "project_of_my_math", "i_space_of_calcul_0_i", "i_file_of_result_0_i.txt")
        
        
        
        with open(i_file_a_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_a)
            
            
            
        
        
        with open(i_file_b_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write(i_string_b)
            
            
        
        
        with open(i_file_of_operator_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            
            f_.write("/")
            
            
        
        
        
        
        import i_runner_of_my_math_1_0_i
        
        importlib.reload(i_runner_of_my_math_1_0_i)
        
        
        
        
        i_runner_of_my_math_1_0_i.i_main_0_i()
        
        
        
        
        
        
        
        with open(i_file_of_result_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            i_content_of_result_0_i = f_.read(os.path.getsize(i_file_of_result_0_i))
            
            
        
        
        
        return i_content_of_result_0_i
        
        
        
        
    
    
    
    def i_check_0_i(i_result_0_i):
        
        
        i_binary_result_0_i = False
        
        
        i_counter_0_i = 0
        
        while ((i_counter_0_i < len(i_result_0_i)) and (i_result_0_i[i_counter_0_i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
                    
                    ".", "+", "-", ))):
                    
            
            
            
            i_counter_0_i += 1
            
            
            
        
        
        if (i_counter_0_i >= len(i_result_0_i)):
            
            
            i_binary_result_0_i = False
            
            
        else:
            
            
            i_binary_result_0_i = True
            
        
        
        return i_binary_result_0_i
        
        
    
    
    
    def calcule_3(a, o, b, number_of_digit_after_the_floating_point_):
    
        # clacule les deux nombre a et b avec l'operateur o
    
        i_result_0_i = ""
    
        i_error_0_i = False
    
    
        if (o == '+'):
            
            i_result_0_i = i_add_2_i(i_string_a=a, i_string_b=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
            
        elif (o == '-'):
            
            i_result_0_i = i_sub_2_i(i_string_a=a, i_string_b=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
            
        elif (o == '*'):
            
            i_result_0_i = i_mult_2_i(i_string_a=a, i_string_b=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
            
        elif (o == '/'):
            
            i_result_0_i = i_div_2_i(i_string_a=a, i_string_b=b, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
            
            
        
        
        i_error_0_i = i_check_0_i(i_result_0_i=i_result_0_i)
        
        
        print(f"i_hello_0_i . i_result_0_i = {i_result_0_i} . i_error_0_i = {i_error_0_i} .")
        
        
        
        
        return [i_error_0_i, i_result_0_i]
    
    
    


    def trouv(l, n):

        # trouve la fin de parenthese par devan depuit 'n' dans la liste 'l'

        i = 0

        if ((n > -1) and (n < len(l)) and (l[n] == '(')):

            i = n + 1

            t = 1

            while ((i < len(l)) and (t != 0)):

                if (l[i] == '('):

                    t += 1

                elif (l[i] == ')'):

                    t -= 1

                # print("i = ", i, " . l[i] = ", l[i], " . t = ", t)

                i += 1

            if (t == 0):

                i -= 1

        else:

            i = len(l)


        return i

    def trouv_(l, n):

        # trouve la fin de parenthese par deriere

        i = 0

        if ((n > -1) and (n < len(l)) and (l[n] == ')')):

            i = n - 1

            t = 1

            while ((i > -1) and (t != 0)):

                if (l[i] == ')'):

                    t += 1

                elif (l[i] == '('):

                    t -= 1

                # print("i = ", i, " . l[i] = ", l[i], " . t = ", t)

                i -= 1

            if (t == 0):

                i += 1

        else:

            i = -1

        return i


    def mot(l, n):

        # donne la position des deux extrimité depuit l'operateur à l'indice n

        a = n - 1

        b = n + 1

        if ((n > 0) and (l[n - 1] == ')')):

            a = trouv_(l=l, n=n - 1)

        if ((n + 1 < len(l)) and (l[n + 1] == '(')):

            b = trouv(l=l, n=n + 1)

        return [a, b]


    def parentheser(l, a, b):

        # mais les parentheses dans la liste 'l' dans 'a' et 'b'

        m = []

        erreur = False

        c = 0

        # print("a = ", a, " . b = ", b)

        if (a - 1 > -1):

            c = trouv(l=l, n=a - 1)

        if ((b + 1 < len(l)) and (c == b + 1)):

            m = l

        elif ((a < b) and (b < len(l))):

            i = 0

            while (i < a):

                m.append(l[i])

                i += 1

            m.append("(")

            while (i < b + 1):

                m.append(l[i])

                i += 1

            m.append(")")

            while (i < len(l)):

                m.append(l[i])

                i += 1

        else:

            erreur = True

        return [m, erreur]


    def trouv_c(l, c, n):

        # trouve le caractere c dans la liste l

        i = n

        while ((i < len(l)) and (l[i] != c)):

            i += 1

        return i


    def insert_l(l, s, a, b):

        # insert la chaine s à la position [a, b] de la liste l

        m = []

        i = 0

        while (i < a):

            m.append(l[i])

            i += 1

        m.append(s)

        i = b + 1

        while (i < len(l)):

            m.append(l[i])

            i += 1

        return m


    def avec_signe(s):
        
        # differencie le signe de numero
        
        i = 0
        
        t = 1
        
        while ((i < len(s)) and ((s[i] == '+') or (s[i] == '-'))):
            
            if (s[i] == '-'):
                
                t = -t
                
            i += 1
            
        s_ = ""
        
        while (i < len(s)):
            
            s_ += s[i]
            
            i += 1
            
        t_ = ""
        
        if (t == -1):
            
            t_ = "-"
                
        
            
        return [t_, s_]

    def parentheser_l(l):

        # mais les parentheses dans la liste 'l'

        erreur = False

        if (len(l) > 1):

            i = 0

            while (i < len(l)):

                a = trouv_c(l=l, c='^', n=i)

                b = trouv_c(l=l, c='R', n=i)

                c = my_min(a=a, b=b)

                if (c < len(l)):

                    t = mot(l=l, n=c)

                    h = parentheser(l=l, a=t[0], b=t[1])

                    # print("a = ", a, " . b = ", b, " . c = ", c, " . t = ", t, " . h = ", h, " . l[c] = ", l[c])

                    if (not h[1]):

                        l = h[0]

                    else:

                        erreur = True

                i = c + 2

            i = 0

            while (i < len(l)):

                a = trouv_c(l=l, c='*', n=i)

                b = trouv_c(l=l, c='/', n=i)

                c = my_min(a=a, b=b)

                if (c < len(l)):

                    t = mot(l=l, n=c)

                    h = parentheser(l=l, a=t[0], b=t[1])

                    # print("a = ", a, " . b = ", b, " . c = ", c, " . t = ", t, " . h = ", h, " . l[c] = ", l[c])

                    if (not h[1]):

                        l = h[0]

                    else:

                        erreur = True

                i = c + 2

            i = 0

            while (i < len(l)):

                a = trouv_c(l=l, c='+', n=i)

                b = trouv_c(l=l, c='-', n=i)

                c = my_min(a=a, b=b)

                if (c < len(l)):

                    t = mot(l=l, n=c)

                    h = parentheser(l=l, a=t[0], b=t[1])

                    # print("a = ", a, " . b = ", b, " . c = ", c, " . t = ", t, " . h = ", h, " . l[c] = ", l[c])

                    if (not h[1]):

                        l = h[0]

                    else:

                        erreur = True

                i = c + 2

        elif (len(l) == 1):

            #l = [s_to_numereau(s=l[0])]

            if (is_numereau(s=l[0])[0]):

                a = avec_signe(s=l[0])
                
                s = a[0] + a[1]
                
                l = ["(", s, ")"]
                
            else:
                
                erreur = True

        return [erreur, l]

    def liste_to_s(l):
        
        #trensforme une liste 'l' à une chaine 's'
        
        i = 0
        
        s = ""
        
        while (i < len(l)):
            
            s += l[i]
            
            i += 1
            
        return s


    def check_parenthese_l(l):

        # check les parenthese de la liste 'l'

        h = liste_to_s(l=l)

        u = check_parentheses(s=h)

        # print("h = ", h, " . u = ", u)

        return u


    def calculatrice(s, l_, n):

        # calcule le resultat de s

        erreur = False

        d = []

        if (n == 0):

            s = supprime_espace(s=s)

            u = check_parentheses(s=s)

            # print("calc . u = ", u)

            m = s_to_liste(s=s)

            if (not m[0]):

                t = check_erreur(l=m[1])

                if (not t[0]):

                    l = t[1]

                    f = parentheser_l(l=l)

                    if (not f[0]):

                        d = f[1]

                        t = trouv_c(l=d, c=')', n=0)

                        while ((t < len(d)) and (not erreur)):

                            t_ = trouv_(l=d, n=t)

                            k = 0

                            if (t_ == t - 4):

                                r = calcule(a=d[t - 3], o=d[t - 2], b=d[t - 1])

                                if (not r[0]):

                                    k = r[1]

                                    # print("1 . d = ", d)

                                else:

                                    erreur = True

                            else:

                                if (is_numereau(s=d[t - 1][0])):

                                    k = s_to_numereau(s=d[t - 1])

                                else:

                                    erreur = True

                            d = insert_l(l=d, s=str(k), a=t_, b=t)

                            p = check_erreur(l=d)

                            d = p[1]

                            # print("2 . d = ", d)

                            t = trouv_c(l=d, c=')', n=0)

                    else:

                        erreur = True

                else:

                    erreur = True

            else:

                erreur = True

        elif (n == 1):

            u = check_parenthese_l(l=l_)

            # print("calc . u = ", u)

            if (u):

                t = check_erreur(l=l_)

                # print("calc . t = ", t)

                if (not t[0]):

                    l = t[1]

                    f = parentheser_l(l=l)

                    # print("calculatrice . f = ", f)

                    if (not f[0]):

                        d = f[1]

                        t = trouv_c(l=d, c=')', n=0)

                        while ((t < len(d)) and (not erreur)):

                            t_ = trouv_(l=d, n=t)

                            k = 0

                            if (t_ == t - 4):

                                r = calcule(a=d[t - 3], o=d[t - 2], b=d[t - 1])

                                if (not r[0]):

                                    k = r[1]

                                    # print("calculatrice . d = ", d)

                                else:

                                    erreur = True

                            else:

                                if (is_numereau(s=d[t - 1])[0]):

                                    # print("d[t - 1] = ", d[t - 1])

                                    k = s_to_numereau(s=d[t - 1])

                                else:

                                    erreur = True

                            d = insert_l(l=d, s=str(k), a=t_, b=t)

                            p = check_erreur(l=d)

                            d = p[1]

                            # print("calc  2 . d = ", d)

                            t = trouv_c(l=d, c=')', n=0)

                    else:

                        erreur = True

                else:

                    erreur = True

            else:

                erreur = True

        return [erreur, d]


    def calculatrice_1(s, l_, n, number_of_digit_after_the_floating_point_, e):

        # calcule le resultat de s

        erreur = False

        d = []

        if (n == 0):

            s = supprime_espace(s=s)

            u = check_parentheses(s=s)

            if (e):

                print("calc . u = ", u)

            if (u):

                m = s_to_liste(s=s)

                if (e):

                    print("m = ", m)

                if (not m[0]):

                    t = check_erreur(l=m[1])

                    if (e):
                    
                        print("calcu . len(t[1]) = ", len(t[1]), " . t = ", t)

                    if (not t[0]):

                        l = t[1]

                        f = parentheser_l(l=l)

                        if (e):
                        
                            print("calcul . f = ", f)

                        if (not f[0]):

                            d = f[1]

                            t = trouv_c(l=d, c=')', n=0)

                            while ((t < len(d)) and (not erreur)):

                                t_ = trouv_(l=d, n=t)

                                k = 0

                                if (t_ == t - 4):

                                    r = calcule_1(a=d[t - 3], o=d[t - 2], b=d[t - 1], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                                    if (not r[0]):

                                        k = r[1]

                                        # print("1 . d = ", d)

                                    else:

                                        erreur = True

                                elif (t_ == t - 2):

                                    if (is_numereau(s=d[t - 1][0])):

                                        k = d[t - 1]

                                    else:

                                        erreur = True

                                else:
                                    
                                    erreur = True

                                if (not erreur):

                                    d = insert_l(l=d, s=k, a=t_, b=t)

                                    p = check_erreur(l=d)

                                    if (not erreur):

                                        erreur = p[0]

                                    d = p[1]

                                    if (e):
                                    
                                        print("calcul . d = ", d)

                                    t = trouv_c(l=d, c=')', n=0)

                        else:

                            erreur = True

                    else:

                        erreur = True

                else:

                    erreur = True

            else:
                
                erreur = True

        elif (n == 1):

            u = check_parenthese_l(l=l_)

            if (e):

                print("calc . u = ", u)

            if (u):

                t = check_erreur(l=l_)

                if (e):
                
                    print("calc . t = ", t)

                if (not t[0]):

                    l = t[1]

                    f = parentheser_l(l=l)

                    if (e):
                    
                        print("calculatrice . f = ", f)

                    if (not f[0]):

                        d = f[1]

                        t = trouv_c(l=d, c=')', n=0)

                        while ((t < len(d)) and (not erreur)):

                            t_ = trouv_(l=d, n=t)

                            k = 0

                            if (t_ == t - 4):

                                r = calcule_1(a=d[t - 3], o=d[t - 2], b=d[t - 1], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                                if (not r[0]):

                                    k = r[1]

                                    # print("calculatrice . d = ", d)

                                else:

                                    erreur = True

                            elif (t_ == t - 2):

                                if (is_numereau(s=d[t - 1])[0]):

                                    # print("d[t - 1] = ", d[t - 1])

                                    k = d[t - 1]

                                else:

                                    erreur = True

                            else:
                                
                                erreur = True
                            
                            if (not erreur):
                            
                            
                                d = insert_l(l=d, s=k, a=t_, b=t)

                                p = check_erreur(l=d)

                                if (not erreur):
            
                                    erreur = p[0]

                                d = p[1]

                                if (e):
                                
                                    print("calc  2 . d = ", d)

                                t = trouv_c(l=d, c=')', n=0)

                    else:

                        erreur = True

                else:

                    erreur = True

            else:

                erreur = True

        # if (len(d) == 1):
            
        #     d[0] = str(d[0])

        return [erreur, d]



    def calculatrice_2(s, l_, n, number_of_digit_after_the_floating_point_, e):

        # calcule le resultat de s

        erreur = False

        d = []

        if (n == 0):

            s = supprime_espace(s=s)

            u = check_parentheses(s=s)

            if (e):

                print("calc . u = ", u)

            if (u):

                m = s_to_liste(s=s)

                if (e):

                    print("m = ", m)

                if (not m[0]):

                    t = check_erreur(l=m[1])

                    if (e):
                    
                        print("calcu . len(t[1]) = ", len(t[1]), " . t = ", t)

                    if (not t[0]):

                        l = t[1]

                        f = parentheser_l(l=l)

                        if (e):
                        
                            print("calcul . f = ", f)

                        if (not f[0]):

                            d = f[1]

                            t = trouv_c(l=d, c=')', n=0)

                            while ((t < len(d)) and (not erreur)):

                                t_ = trouv_(l=d, n=t)

                                k = 0

                                if (t_ == t - 4):

                                    r = calcule_2(a=d[t - 3], o=d[t - 2], b=d[t - 1], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                                    if (not r[0]):

                                        k = r[1]

                                        # print("1 . d = ", d)

                                    else:

                                        erreur = True

                                elif (t_ == t - 2):

                                    if (is_numereau(s=d[t - 1][0])):

                                        k = d[t - 1]

                                    else:

                                        erreur = True

                                else:
                                    
                                    erreur = True

                                if (not erreur):

                                    d = insert_l(l=d, s=k, a=t_, b=t)

                                    p = check_erreur(l=d)

                                    if (not erreur):

                                        erreur = p[0]

                                    d = p[1]

                                    if (e):
                                    
                                        print("calcul . d = ", d)

                                    t = trouv_c(l=d, c=')', n=0)

                        else:

                            erreur = True

                    else:

                        erreur = True

                else:

                    erreur = True

            else:
                
                erreur = True

        elif (n == 1):

            u = check_parenthese_l(l=l_)

            if (e):

                print("calc . u = ", u)

            if (u):

                t = check_erreur(l=l_)

                if (e):
                
                    print("calc . t = ", t)

                if (not t[0]):

                    l = t[1]

                    f = parentheser_l(l=l)

                    if (e):
                    
                        print("calculatrice . f = ", f)

                    if (not f[0]):

                        d = f[1]

                        t = trouv_c(l=d, c=')', n=0)

                        while ((t < len(d)) and (not erreur)):

                            t_ = trouv_(l=d, n=t)

                            k = 0

                            if (t_ == t - 4):

                                r = calcule_2(a=d[t - 3], o=d[t - 2], b=d[t - 1], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)

                                if (not r[0]):

                                    k = r[1]

                                    # print("calculatrice . d = ", d)

                                else:

                                    erreur = True

                            elif (t_ == t - 2):

                                if (is_numereau(s=d[t - 1])[0]):

                                    # print("d[t - 1] = ", d[t - 1])

                                    k = d[t - 1]

                                else:

                                    erreur = True

                            else:
                                
                                erreur = True
                            
                            if (not erreur):
                            
                            
                                d = insert_l(l=d, s=k, a=t_, b=t)

                                p = check_erreur(l=d)

                                if (not erreur):
            
                                    erreur = p[0]

                                d = p[1]

                                if (e):
                                
                                    print("calc  2 . d = ", d)

                                t = trouv_c(l=d, c=')', n=0)

                    else:

                        erreur = True

                else:

                    erreur = True

            else:

                erreur = True

        # if (len(d) == 1):
            
        #     d[0] = str(d[0])



        #if (erreur == False):

            #counter_0 = len(d[0]) - 1

            #while ((counter_0 > 0) and (d[0][counter_0] != ".") and (d[0][counter_0] == "0")):

                #counter_0 -= 1


            #if (d[0][counter_0] == "."):

                #counter_0 += 1


                #d_ = [d[0][:counter_0 + 1]]


                ## print(f"d = {d} . d_ = {d_} .")


                #d = d_


        return [erreur, d]





    
    
    def calculatrice_3(s, l_, n, number_of_digit_after_the_floating_point_, e):
    
        # calcule le resultat de s
    
        erreur = False
    
        d = []
    
        if (n == 0):
    
            s = supprime_espace(s=s)
    
            u = check_parentheses(s=s)
    
            if (e):
    
                print("calc . u = ", u)
    
            if (u):
    
                m = s_to_liste(s=s)
    
                if (e):
    
                    print("m = ", m)
    
                if (not m[0]):
    
                    t = check_erreur(l=m[1])
    
                    if (e):
                    
                        print("calcu . len(t[1]) = ", len(t[1]), " . t = ", t)
    
                    if (not t[0]):
    
                        l = t[1]
    
                        f = parentheser_l(l=l)
    
                        if (e):
                        
                            print("calcul . f = ", f)
    
                        if (not f[0]):
    
                            d = f[1]
    
                            t = trouv_c(l=d, c=')', n=0)
    
                            while ((t < len(d)) and (not erreur)):
    
                                t_ = trouv_(l=d, n=t)
    
                                k = 0
    
                                if (t_ == t - 4):
    
                                    r = calcule_3(a=d[t - 3], o=d[t - 2], b=d[t - 1], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
    
                                    if (not r[0]):
    
                                        k = r[1]
    
                                        # print("1 . d = ", d)
    
                                    else:
    
                                        erreur = True
    
                                elif (t_ == t - 2):
    
                                    if (is_numereau(s=d[t - 1][0])):
    
                                        k = d[t - 1]
    
                                    else:
    
                                        erreur = True
    
                                else:
                                    
                                    erreur = True
    
                                if (not erreur):
    
                                    d = insert_l(l=d, s=k, a=t_, b=t)
    
                                    p = check_erreur(l=d)
    
                                    if (not erreur):
    
                                        erreur = p[0]
    
                                    d = p[1]
    
                                    if (e):
                                    
                                        print("calcul . d = ", d)
    
                                    t = trouv_c(l=d, c=')', n=0)
    
                        else:
    
                            erreur = True
    
                    else:
    
                        erreur = True
    
                else:
    
                    erreur = True
    
            else:
                
                erreur = True
    
        elif (n == 1):
    
            u = check_parenthese_l(l=l_)
    
            if (e):
    
                print("calc . u = ", u)
    
            if (u):
    
                t = check_erreur(l=l_)
    
                if (e):
                
                    print("calc . t = ", t)
    
                if (not t[0]):
    
                    l = t[1]
    
                    f = parentheser_l(l=l)
    
                    if (e):
                    
                        print("calculatrice . f = ", f)
    
                    if (not f[0]):
    
                        d = f[1]
    
                        t = trouv_c(l=d, c=')', n=0)
    
                        while ((t < len(d)) and (not erreur)):
    
                            t_ = trouv_(l=d, n=t)
    
                            k = 0
    
                            if (t_ == t - 4):
    
                                r = calcule_3(a=d[t - 3], o=d[t - 2], b=d[t - 1], number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_)
    
                                if (not r[0]):
    
                                    k = r[1]
    
                                    # print("calculatrice . d = ", d)
    
                                else:
    
                                    erreur = True
    
                            elif (t_ == t - 2):
    
                                if (is_numereau(s=d[t - 1])[0]):
    
                                    # print("d[t - 1] = ", d[t - 1])
    
                                    k = d[t - 1]
    
                                else:
    
                                    erreur = True
    
                            else:
                                
                                erreur = True
                            
                            if (not erreur):
                            
                            
                                d = insert_l(l=d, s=k, a=t_, b=t)
    
                                p = check_erreur(l=d)
    
                                if (not erreur):
            
                                    erreur = p[0]
    
                                d = p[1]
    
                                if (e):
                                
                                    print("calc  2 . d = ", d)
    
                                t = trouv_c(l=d, c=')', n=0)
    
                    else:
    
                        erreur = True
    
                else:
    
                    erreur = True
    
            else:
    
                erreur = True
    
        # if (len(d) == 1):
            
        #     d[0] = str(d[0])
    
    
    
        #if (erreur == False):
    
            #counter_0 = len(d[0]) - 1
    
            #while ((counter_0 > 0) and (d[0][counter_0] != ".") and (d[0][counter_0] == "0")):
    
                #counter_0 -= 1
    
    
            #if (d[0][counter_0] == "."):
    
                #counter_0 += 1
    
    
                #d_ = [d[0][:counter_0 + 1]]
    
    
                ## print(f"d = {d} . d_ = {d_} .")
    
    
                #d = d_
    
    
        return [erreur, d]
    
    
    
    
    
    
    
    









    # Z = a + i * b
        
        
        
    def invers_cos(a, b, number_of_digit_after_the_floating_point_1, type_of_angle=""):
    
        if (type_of_angle == "degree"):
        
            str_type = "90"
    
        elif (type_of_angle == "grad"):
        
            str_type = "100"
        

        else:
    
            str_type = ""
    
    
    
                
        str_result = ""
        
        operation = f"({a} ^ 2 + {b} ^ 2)"
        
        
        
        m_1 = calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
             
             
        if (m_1[0] == False):
        
            
                
            s1 = m_1[1][0]
            
            s2 = "1"
            
            
            
            bool_0 = my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
            
            if (bool_0 == True):
                    
            
                        
                s1 = a
                
                s2 = "0"
                
                
                  
                m_1 = calculatrice_2(s=a, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                
                if (m_1[0] == False):
                
                    s1 = f"{m_1[1][0]}"     
                    
                    
                    a = f"{m_1[1][0]}"     
                
                
                #print(f"s1 = {s1}")
                
                bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
                
                if (bool_0 == True):
                
                    a = f"({a} * -1)"
                
                
                m_1 = calculatrice_2(s=a, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)  
                  
                        
                if (m_1[0] == False):
                
                    a = f"{m_1[1][0]}"     
                
                
                #print(f"i_hello . a = {a}")
                        
                s1 = b
                
                s2 = "0"
                
                
                  
                m_1 = calculatrice_2(s=s1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                
                if (m_1[0] == False):
                
                    s1 = f"{m_1[1][0]}"     
                
                
                
                
                bool_1 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
                
                
                if (bool_1 == True):
            
                            
                    b = f"({b} * -1)"
                
                
                m_1 = calculatrice_2(s=b, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)  
                  
                        
                if (m_1[0] == False):
                
                    b = f"{m_1[1][0]}"
                
                
            
            
                str_0 = f"((1 - {a}) R 2)"
                
                str_1 = f"((1 - ((1 - {a} ^ 2) R 2)) R 2)"
            
                str_result = f"({str_0} / ({str_0} + {str_1}))"
            
            
            
                #print(f"i_hello . bool_0 = {bool_0} . bool_1 = {bool_1} .")
            
                if ((bool_0 == False) and (bool_1 == False)):
                
                    pass
                    
                elif ((bool_0 == True) and (bool_1 == False)):
            
                    str_result = f"((2) - {str_result})"
            
                elif ((bool_0 == True) and (bool_1 == True)):
                
                    str_result = f"({str_result} - (2))"
            
                        
                elif ((bool_0 == False) and (bool_1 == True)):
                
                    str_result = f"((4) - {str_result})"
                
                #print(f"str_result = {str_result}")
                
            
            
            
                if (str_type != ""):
                
                    str_result += f" * {str_type}"
            
                
                
    
    
        return str_result
        
        
        
        
        
    def invers_sin(a, b, number_of_digit_after_the_floating_point_1, type_of_angle=""):
    
                
        if (type_of_angle == "degree"):
        
            str_type = "90"
        
        elif (type_of_angle == "grad"):
        
            str_type = "100"
              

        else:
        
            str_type = ""
        
        
        str_result = ""
        
        operation = f"({a} ^ 2 + {b} ^ 2)"
        
        
        m_1 = calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
             
             
        if (m_1[0] == False):
        
            
                           
                 
                 
            s1 = m_1[1][0]
                             
            s2 = "1"
            
            
            
            bool_0 = my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
            
            if (bool_0 == True):
            
                
                    
                     
                      
                        
                s1 = a
                
                s2 = "0"
                
                
                  
                m_1 = calculatrice_2(s=s1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                
                if (m_1[0] == False):
                
                    s1 = f"{m_1[1][0]}"     
                
                
                bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
                
                if (bool_0 == True):
                
                    a = f"({a} * -1)"
                
                
                m_1 = calculatrice_2(s=a, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)  
                  
                        
                if (m_1[0] == False):
                
                    a = f"{m_1[1][0]}"     
                
                  
                        
                s1 = b
                
                s2 = "0"
                
                
                  
                m_1 = calculatrice_2(s=s1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                
                if (m_1[0] == False):
                
                    s1 = f"{m_1[1][0]}"     
                
                
                
                
                bool_1 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
                
                
                if (bool_1 == True):
                
                            
                    b = f"({b} * -1)"
                
                
                m_1 = calculatrice_2(s=b, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)  
                  
                        
                if (m_1[0] == False):
                
                    b = f"{m_1[1][0]}"
                
                
                        
                str_a = f"((1 - {b} ^ 2) R 2)"
                    
                str_0 = f"((1 - {str_a}) R 2)"
                
                str_1 = f"((1 - ((1 - {str_a} ^ 2) R 2)) R 2)"
                
                str_result = f"({str_0} / ({str_0} + {str_1}))"
                     
                     
                     
                        
                if ((bool_0 == False) and (bool_1 == False)):
                
                    pass
                    
                elif ((bool_0 == True) and (bool_1 == False)):
                
                    str_result = f"((2) - {str_result})"
                
                elif ((bool_0 == True) and (bool_1 == True)):
                
                    str_result = f"({str_result} - (2))"
                
                        
                elif ((bool_0 == False) and (bool_1 == True)):
                
                    str_result = f"((4) - {str_result})"
                
                     
                     
                     
                        
                if (str_type != ""):
                
                    str_result += f" * {str_type}"
                
                
                
                
        return str_result
        
        
        
        
        
    def invers_cos_1(a, number_of_digit_after_the_floating_point_1, type_of_angle=""):
    
        if (type_of_angle == "degree"):
        
            str_type = "90"
    
        elif (type_of_angle == "grad"):
        
            str_type = "100"
        
    
        else:
    
            str_type = ""
    
    
    
                
        s1 = a
        
        s2 = "0"
        
        
          
        m_1 = calculatrice_2(s=s1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        if (m_1[0] == False):
        
            s1 = f"{m_1[1][0]}"     
        
        
        bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
        
        
        if (bool_0 == True):
        
            a = f"({a} * -1)"
        
        
        m_1 = calculatrice_2(s=a, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)  
          
                
        if (m_1[0] == False):
        
            a = f"{m_1[1][0]}"     
        
          
            
    
    
        str_0 = f"((1 - {a}) R 2)"
        
        str_1 = f"((1 - ((1 - {a} ^ 2) R 2)) R 2)"
    
        str_result = f"({str_0} / ({str_0} + {str_1}))"
    
    
    
    
    
        if (str_type != ""):
        
            str_result += f" * {str_type}"
    
        
        
    
    
        return str_result
        
        
        
        
        
    def invers_sin_1(b, number_of_digit_after_the_floating_point_1, type_of_angle=""):
    
                
        if (type_of_angle == "degree"):
        
            str_type = "90"
        
        elif (type_of_angle == "grad"):
        
            str_type = "100"
              
    
        else:
        
            str_type = ""
        
        
        
             
                
        s1 = b
        
        s2 = "0"
        
        
          
        m_1 = calculatrice_2(s=s1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        if (m_1[0] == False):
        
            s1 = f"{m_1[1][0]}"     
        
        
        
        
        bool_1 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
        
        
        
        if (bool_1 == True):
        
                    
            b = f"({b} * -1)"
        
        
        m_1 = calculatrice_2(s=b, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)  
          
                
        if (m_1[0] == False):
        
            b = f"{m_1[1][0]}"
        
        
                
        str_a = f"((1 - {b} ^ 2) R 2)"
            
        str_0 = f"((1 - {str_a}) R 2)"
        
        str_1 = f"((1 - ((1 - {str_a} ^ 2) R 2)) R 2)"
        
        str_result = f"({str_0} / ({str_0} + {str_1}))"
             
             
            
             
             
                
        if (str_type != ""):
        
            str_result += f" * {str_type}"
        
        return str_result
        
        
        
        
    
    
    
    
    
    def cos(alpha_, number_of_digit_after_the_floating_point_1, type_of_angle=""):
    
    
                 
        if (type_of_angle == "degree"):
        
            str_type = "360"
            
            str_type_1 = "90"
        
        elif (type_of_angle == "grad"):
        
            str_type = "400"
            
            str_type_1 = "100"

        else:
        
            str_type = ""
        
        
                
                
        m_1 = calculatrice_2(s=alpha_, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        if (m_1[0] == False):
        
            alpha_ = f"{m_1[1][0]}"     
        
        
        
        
        #print(f"before = {str_type}")



        m_1 = calculatrice_2(s=str_type, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)


        if (m_1[0] == False):

            str_type = f"{m_1[1][0]}"     



        #print(f"after = {str_type}")
        
        
        #print(f"alpha_ = {alpha_}")
        
        position_at_lest = 0.0
        
        alpha = f"{alpha_}"     
    
        if (str_type != ""):
            
        
                        
                        
            
            
            
            # extracting the value of the angle from dividing by the number of circles that are there .
            
            
            # Then extract the first quarter of the circle. The value here expresses 90 degree by 1.0
            
            
            
            
            s1 = alpha_
            
            s2 = str_type
            

            
            bool_3 = my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
            
                        
            alpha_1 = f"({alpha_} / {str_type})"
            
            alpha_2 = ""
            
            alpha_3 = alpha_
            
            
            if (bool_3 == True):
                
            
                alpha_1 = f"({alpha_} / {str_type})"
            
                #print(f"i_hello . alpha_1 = {alpha_1}")
            
                alpha_2 = ""
            
                alpha_3 = alpha_
            
                m = calculatrice_2(s=alpha_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
    
                if (m[0] == False):
                
                                        
                    s1 = m[1][0]
                    
                    s2 = str_type
                    
                    str_number_0 = ""
                    
                    counter_0 = 0
                    
                    while ((counter_0 < len(s1)) and (s1[counter_0] != ".")):
                    
                        
                        str_number_0 += s1[counter_0]
                        
                        counter_0 += 1
                    
                    
                    
                    alpha_2 = f"({alpha_} - ({str_number_0} * {str_type}))"
                    
                    #print(f"alpha_2 = {alpha_2}")
    
                    m_1 = calculatrice_2(s=alpha_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                    
                    if (m_1[0] == False):
    
                        alpha_3 = f"{m_1[1][0]}"     
                
                
            
            alpha_2 = f"({alpha_3} / {str_type})"
            
            
            alpha_4 = f"({alpha_3} / ({str_type} / 4))"
            
            alpha_2 = alpha_4
            
            
            #print(f"i_hello . alpha_2 = {alpha_2}")
                    
                    
                    
            m_2 = calculatrice_2(s=alpha_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_2[0] == False):
            
                alpha = f"{m_2[1][0]}"
            
                
                
                
                
                
                
            # filter_0 
                
            
            
            
            
            
            
            
            
            position_at_lest = 0.0
            
            
                
                
                    
            m_1 = calculatrice_2(s=alpha, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_1[0] == False):
            
                alpha = f"{m_1[1][0]}"     
            
            
                     
            
            s1 = alpha
            
            s2 = "1"
            
            
  
            m_1 = calculatrice_2(s=s2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_1[0] == False):
            
                s2 = f"{m_1[1][0]}"     
            
            
            
                        
            #print(f"alpha = {alpha}")
            
            bool_4 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
            
            if (bool_4 == True):
            
                position_at_lest = 0.0
                
            else:
            
    
                s1 = alpha
                
                s2 = "2"
                
                                
                #s2 = f"{str_type} * 0.5"
                
                            
                m_1 = calculatrice_2(s=s2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                
                if (m_1[0] == False):
                
                    s2 = f"{m_1[1][0]}"     
                
                
                
                bool_4 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
                            
                
                if (bool_4 == True):
                
                    position_at_lest = 0.25
                    
                    
                    
                    alpha = f"((2) - {alpha})"
                    
                    
                else:
                
                    s1 = alpha
                    
                    s2 = "3"
                    
                                        
                                    
                    #s2 = f"{str_type} * 0.75"
                    
                                
                    m_1 = calculatrice_2(s=s2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                    
                    
                    if (m_1[0] == False):
                    
                        s2 = f"{m_1[1][0]}"     
                    
                    
                    bool_4 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                    
                                
                    
                    if (bool_4 == True):
                    
                        position_at_lest = 0.5
                        
                        
                        alpha = f"({alpha} - (2))"
                        
                        
                    else:
                    
                        position_at_lest = 0.75
            
                        
                        alpha = f"((4) - {alpha})"
            
            
            #print(f"alpha = {alpha}")
            
            
            m_2 = calculatrice_2(s=alpha, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_2[0] == False):
            
                alpha = f"{m_2[1][0]}"
            
        
        
        # Now we have the quadrant of the angle in the circle . The angle is expressed by a value between 0.0 and 1.0 
        
        
        
        
        
        
        
        
        
        
        
        # Now if alpha == 1.0 . that mean 90 degree . it mean the cos = 0.0 .
        
        
        #print(f"final : alpha = {alpha}")
        
        s1 = alpha
        
        s2 = "1"
        


        bool_0 = my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
        #print(f"bool_0 = {bool_0} . alpha = {alpha}")
        
            
        if (bool_0 == True):
        
            return "0.0"
            
        else:
            
            
            # if alpha != 1.0 . Let's start the account .
            
            

            #print(f"final : alpha = {alpha}")


            # those are in the equation :  a * (x ^ 2) + b * (x) + c == 0 . i extracted this equation from invers_cos .

            # a ==> str_a ; b ==> str_b ; c ==> str_c ; and x represent cos 


            str_a = f"((1 - {alpha}) ^ 4 + {alpha} ^ 4)"
            
            str_b = f"(-2 * ((1 - {alpha}) ^ 4) + 2 * ({alpha} ^ 2) * ((1 - {alpha}) ^ 2))"
        
            str_c = f"(({alpha} ^ 4) + ((1 - {alpha}) ^ 4) - 2 * ({alpha} ^ 2) * ((1 - {alpha}) ^ 2) - ({alpha} ^ 4))"
        
            
            
            # delta = b ^ 2 - 4 * a * c
            
            
            delta = f"(({str_b} ^ 2) - 4 * {str_a} * {str_c})"
            
            
            
            m = calculatrice_2(s=delta, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m[0] != True):
                
                
                # Now Let's test if (delta < 0)
                
                
                
                s1 = m[1][0]
                
                s2 = "0"
                
                
                
                bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
    
                #print(f"bool_0 = {bool_0}")
                
                
                if (bool_0 == False):
                
                    
                    # if (delta < 0) == False . Let's start the account .
                    
                    
                    #print(f"delta >= 0")    
                    
                    delta = m[1][0]
                    
                    
                    
                    s1 = delta
                    
                    s2 = "0"
                    
                    
                    
                    bool_1 = my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                          
                    
                    if (bool_1 == False):
                
                
                        # if (delta == 0) == False . Let's do the 2 solution a_1 and a_2 .
                    
                    
                        a_1 = f"((-{str_b} + ({delta} R 2)) / (2 * {str_a}))"
                        
                        
                        a_2 = f"((-{str_b} - ({delta} R 2)) / (2 * {str_a}))"
                    
                        
                        
                        m_1 = calculatrice_2(s=a_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                        #print(f"m_1 = {m_1}")
                
                                        
                        m_2 = calculatrice_2(s=a_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                        
                        #print(f"m_2 = {m_2}")
                        
                        
                        
                        
                        if ((m_2[0] == False) and (m_1[0] == False)):
        
                            
                            # Now when there is 2 choise . Let's chose The closest solution to alpha . it mean when invers_cos make alpha it while be The Chosen One .
        
                            
                            str_0 = invers_cos_1(a=m_1[1][0], number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point_1, type_of_angle=type_of_angle)
        
        
                            str_1 = invers_cos_1(a=m_2[1][0], number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point_1, type_of_angle=type_of_angle)
        
                            m_3 = calculatrice_2(s=str_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
                            m_4 = calculatrice_2(s=str_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        
                            #print(f"invers : m_3 = {m_3} . m_4 = {m_4}")
        
        
        
        
                            v_0 = f"((({m_3[1][0]} - {alpha_}) ^ 2) R 2)"
        
        
                            m_5 = calculatrice_2(s=v_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
                                                        
                            
                            v_1 = f"((({m_4[1][0]} - {alpha_}) ^ 2) R 2)"
                            
                            
                            m_6 = calculatrice_2(s=v_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                            
                            
        
        
                            # right here the choise between the 2 solution from delta . i chose The closest one to what i want .
                            
                            
        
                            s1 = m_5[1][0]
                            
                            s2 = m_6[1][0]
                            
                            
                            
                            bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                                
                                
                                
                            #print(f"(m_5 < m_6 ) == {bool_0}")
        
        


                            if (bool_0 == True):
                            
                               
                                # right here i chose the first one .    
                               
                                v_3 = f"({m_1[1][0]})"
                                
                                
                                # right here i chose if it is positive or negative . relative to the position in the circle .
                                
                                if ((position_at_lest == 0.25) or ((position_at_lest == 0.5))):
                                
                                
                                    v_3 =  f"({v_3} * -1)"


                                elif ((position_at_lest == 0.0) or ((position_at_lest == 0.75))):
                                
    
                                    v_3 = v_3
                                    
                                
                                m_6 = calculatrice_2(s=v_3, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                                
        
        
                                if (m_6[0] == False):
        
                                    return f"{m_6[1][0]}"
                                


                            else:
                            
                            
                                
                                # right here i chose the second one .    
                            
                                                                
                                v_3 = f"({m_2[1][0]})"
                                
                                
                                # right here i chose if it is positive or negative . relative to the position in the circle .
                                
                                
                                if ((position_at_lest == 0.25) or ((position_at_lest == 0.5))):
                                
                                
                                    v_3 =  f"({v_3} * -1)"
                                
                                
                                elif ((position_at_lest == 0.0) or ((position_at_lest == 0.75))):
                                
                                
                                    v_3 = v_3
                                    
                                
                                m_6 = calculatrice_2(s=v_3, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                                
                                
                                
                                if (m_6[0] == False):
                                
                                    return f"{m_6[1][0]}"
                                
                                
                                

                    
                    
                    else:
                    
                        
                        # Now if (delta == 0) == true . i chose just one solution .
                    
                    
                    
                        #print(f"delta == 0")
                                                
                        
                        a_1 = f"((-{str_b} + ({delta} R 2)) / (2 * {str_a}))"
                        
                        
                        a_2 = f"((-{str_b} - ({delta} R 2)) / (2 * {str_a}))"
                        
                        
                        
                        m_1 = calculatrice_2(s=a_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                        
                        #print(f"m_1 = {m_1}")
                        
                                        
                        m_2 = calculatrice_2(s=a_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                        
                        #print(f"m_2 = {m_2}")
                        
                        
                        
                        if ((m_2[0] == False) and (m_1[0] == False)):
                        
                        
                            # i chose if it is positive or negative . relative to the position in the circle .                                
                            
                            if ((position_at_lest == 0.25) or ((position_at_lest == 0.5))):
                            
                                v_0 = f"({m_2[1][0]} * -1)"
                                
                                m_6 = calculatrice_2(s=v_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                            
                                return f"{m_6[1][0]}"
                            
                            elif ((position_at_lest == 0.0) or ((position_at_lest == 0.75))):
                            
                                return f"{m_2[1][0]}"
                            
                            
                        

                else:
                
                    
                    pass
                    
                    #print(f"delta < 0")    
            
            
        
        return ""
        
        
        
        
        
        
        
        
        
        
        
        
        
    def sin(alpha_, number_of_digit_after_the_floating_point_1, type_of_angle=""):
    
    


        str_result = ""

                
                 
        if (type_of_angle == "degree"):
        
            str_type = "360"
            
            str_type_1 = "90"
        
        elif (type_of_angle == "grad"):
        
            str_type = "400"
            
            str_type_1 = "100"
        
        else:
        
            str_type = ""
        
        
                
                
        m_1 = calculatrice_2(s=alpha_, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        if (m_1[0] == False):
        
            alpha_ = f"{m_1[1][0]}"     
        
        
        
        
        #print(f"before = {str_type}")
        
        
        
        m_1 = calculatrice_2(s=str_type, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        if (m_1[0] == False):
        
            str_type = f"{m_1[1][0]}"     
        
        
        
        #print(f"after = {str_type}")
        
        
        #print(f"alpha_ = {alpha_}")
        
        position_at_lest = 0.0
        
        alpha = f"{alpha_}"     
        
        if (str_type != ""):
            
        
                        
                        
            
            
            
            # extracting the value of the angle from dividing by the number of circles that are there .
            
            
            # Then extract the first quarter of the circle. The value here expresses 90 degree by 1.0
            
            
            
            
            s1 = alpha_
            
            s2 = str_type
            
        
            
            bool_3 = my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
            
                        
            alpha_1 = f"({alpha_} / {str_type})"
            
            alpha_2 = ""
            
            alpha_3 = alpha_
            
            
            if (bool_3 == True):
                
            
                alpha_1 = f"({alpha_} / {str_type})"
            
                #print(f"i_hello . alpha_1 = {alpha_1}")
            
                alpha_2 = ""
            
                alpha_3 = alpha_
            
                m = calculatrice_2(s=alpha_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
                if (m[0] == False):
                
                                        
                    s1 = m[1][0]
                    
                    s2 = str_type
                    
                    str_number_0 = ""
                    
                    counter_0 = 0
                    
                    while ((counter_0 < len(s1)) and (s1[counter_0] != ".")):
                    
                        
                        str_number_0 += s1[counter_0]
                        
                        counter_0 += 1
                    
                    
                    
                    alpha_2 = f"({alpha_} - ({str_number_0} * {str_type}))"
                    
                    #print(f"alpha_2 = {alpha_2}")
        
                    m_1 = calculatrice_2(s=alpha_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                    
                    if (m_1[0] == False):
        
                        alpha_3 = f"{m_1[1][0]}"     
                
                
            
            alpha_2 = f"({alpha_3} / {str_type})"
            
            
            alpha_4 = f"({alpha_3} / ({str_type} / 4))"
            
            alpha_2 = alpha_4
            
            
            #print(f"i_hello . alpha_2 = {alpha_2}")
                    
                    
                    
            m_2 = calculatrice_2(s=alpha_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_2[0] == False):
            
                alpha = f"{m_2[1][0]}"
            
                
                
                
                
                
                
            # filter_0 
                
            
            
            
            
            
            
            
            
            position_at_lest = 0.0
            
            
                
                
                    
            m_1 = calculatrice_2(s=alpha, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_1[0] == False):
            
                alpha = f"{m_1[1][0]}"     
            
            
                     
            
            s1 = alpha
            
            s2 = "1"
            
            
          
            m_1 = calculatrice_2(s=s2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_1[0] == False):
            
                s2 = f"{m_1[1][0]}"     
            
            
            
                        
            #print(f"alpha = {alpha}")
            
            bool_4 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
            
            if (bool_4 == True):
            
                position_at_lest = 0.0
                
            else:
            
        
                s1 = alpha
                
                s2 = "2"
                
                                
                #s2 = f"{str_type} * 0.5"
                
                            
                m_1 = calculatrice_2(s=s2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                
                if (m_1[0] == False):
                
                    s2 = f"{m_1[1][0]}"     
                
                
                
                bool_4 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
                            
                
                if (bool_4 == True):
                
                    position_at_lest = 0.25
                    
                    
                    
                    alpha = f"((2) - {alpha})"
                    
                    
                else:
                
                    s1 = alpha
                    
                    s2 = "3"
                    
                                        
                                    
                    #s2 = f"{str_type} * 0.75"
                    
                                
                    m_1 = calculatrice_2(s=s2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                    
                    
                    if (m_1[0] == False):
                    
                        s2 = f"{m_1[1][0]}"     
                    
                    
                    bool_4 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                    
                                
                    
                    if (bool_4 == True):
                    
                        position_at_lest = 0.5
                        
                        
                        alpha = f"({alpha} - (2))"
                        
                        
                    else:
                    
                        position_at_lest = 0.75
            
                        
                        alpha = f"((4) - {alpha})"
            
            
            #print(f"alpha = {alpha}")
            
            
            m_2 = calculatrice_2(s=alpha, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m_2[0] == False):
            
                alpha = f"{m_2[1][0]}"
            
        
        
        # Now we have the quadrant of the angle in the circle . The angle is expressed by a value between 0.0 and 1.0 
        
        
        
        
        
        
        
        
        
        
        
        # Now if alpha == 1.0 . that mean 90 degree . it mean the cos = 0.0 .
        
        
        #print(f"final : alpha = {alpha}")
        
        s1 = alpha
        
        s2 = "1"
        
        
        
        bool_0 = my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
            
        #print(f"bool_0 = {bool_0} . alpha = {alpha}")
        
            
        if (bool_0 == True):
        
            str_result = "0.0"
            
        else:
            
            
            # if alpha != 1.0 . Let's start the account .
            
            
        
            #print(f"final : alpha = {alpha}")
        
        
            # those are in the equation :  a * (x ^ 2) + b * (x) + c == 0
        
            # a ==> str_a ; b ==> str_b ; c ==> str_c ; and x represent cos 
        
        
            str_a = f"((1 - {alpha}) ^ 4 + {alpha} ^ 4)"
            
            str_b = f"(-2 * ((1 - {alpha}) ^ 4) + 2 * ({alpha} ^ 2) * ((1 - {alpha}) ^ 2))"
        
            str_c = f"(({alpha} ^ 4) + ((1 - {alpha}) ^ 4) - 2 * ({alpha} ^ 2) * ((1 - {alpha}) ^ 2) - ({alpha} ^ 4))"
        
            
            
            # delta = b ^ 2 - 4 * a * c
            
            
            delta = f"(({str_b} ^ 2) - 4 * {str_a} * {str_c})"
            
            
            
            m = calculatrice_2(s=delta, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
            
            
            if (m[0] != True):
                
                
                # Now Let's test if (delta < 0)
                
                
                
                s1 = m[1][0]
                
                s2 = "0"
                
                
                
                bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                
        
                #print(f"bool_0 = {bool_0}")
                
                
                if (bool_0 == False):
                
                    
                    # if (delta < 0) == False . Let's start the account .
                    
                    
                    #print(f"delta >= 0")    
                    
                    delta = m[1][0]
                    
                    
                    
                    s1 = delta
                    
                    s2 = "0"
                    
                    
                    
                    bool_1 = my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                          
                    
                    if (bool_1 == False):
                
                
                        # if (delta == 0) == False . Let's do the 2 solution a_1 and a_2 .
                    
                    
                        a_1 = f"((-{str_b} + ({delta} R 2)) / (2 * {str_a}))"
                        
                        
                        a_2 = f"((-{str_b} - ({delta} R 2)) / (2 * {str_a}))"
                    
                        
                        
                        m_1 = calculatrice_2(s=a_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                
                        #print(f"m_1 = {m_1}")
                
                                        
                        m_2 = calculatrice_2(s=a_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                        
                        #print(f"m_2 = {m_2}")
                        
                        
                        
                        
                        if ((m_2[0] == False) and (m_1[0] == False)):
        
                            
                            # Now when there is 2 choise . Let's chose The closest solution to alpha . it mean when invers_cos make alpha it while be The Chosen One .
        
                            
                            str_0 = invers_cos_1(a=m_1[1][0], number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point_1, type_of_angle=type_of_angle)
        
        
                            str_1 = invers_cos_1(a=m_2[1][0], number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point_1, type_of_angle=type_of_angle)
        
                            m_3 = calculatrice_2(s=str_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
                            m_4 = calculatrice_2(s=str_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        
                            #print(f"invers : m_3 = {m_3} . m_4 = {m_4}")
        
        
        
        
                            v_0 = f"((({m_3[1][0]} - {alpha_}) ^ 2) R 2)"
        
        
                            m_5 = calculatrice_2(s=v_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
                                                        
                            
                            v_1 = f"((({m_4[1][0]} - {alpha_}) ^ 2) R 2)"
                            
                            
                            m_6 = calculatrice_2(s=v_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                            
                            
        
        
                            # right here the choise between the 2 solution from delta . i chose The closest one to what i want .
                            
                            
        
                            s1 = m_5[1][0]
                            
                            s2 = m_6[1][0]
                            
                            
                            
                            bool_0 = my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1)
                                
                                
                                
                            #print(f"(m_5 < m_6 ) == {bool_0}")
        
        
        
        
                            if (bool_0 == True):
                            
                               
                                # right here i chose the first one .    
                               
                                v_3 = f"({m_1[1][0]})"
                                
                                
                                # right here i chose if it is positive or negative . relative to the position in the circle .
                                
                                if ((position_at_lest == 0.25) or ((position_at_lest == 0.5))):
                                
                                
                                    v_3 =  f"({v_3} * -1)"
        
        
                                elif ((position_at_lest == 0.0) or ((position_at_lest == 0.75))):
                                
        
                                    v_3 = v_3
                                    
                                
                                m_6 = calculatrice_2(s=v_3, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                                
        
        
                                if (m_6[0] == False):
        
                                    str_result = f"{m_6[1][0]}"
                                
        
        
                            else:
                            
                            
                                
                                # right here i chose the second one .    
                            
                                                                
                                v_3 = f"({m_2[1][0]})"
                                
                                
                                # right here i chose if it is positive or negative . relative to the position in the circle .
                                
                                
                                if ((position_at_lest == 0.25) or ((position_at_lest == 0.5))):
                                
                                
                                    v_3 =  f"({v_3} * -1)"
                                
                                
                                elif ((position_at_lest == 0.0) or ((position_at_lest == 0.75))):
                                
                                
                                    v_3 = v_3
                                    
                                
                                m_6 = calculatrice_2(s=v_3, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                                
                                
                                
                                if (m_6[0] == False):
                                
                                    str_result = f"{m_6[1][0]}"
                                
                                
                                
        
                    
                    
                    else:
                    
                        
                        # Now if (delta == 0) == true . i chose just one solution .
                    
                    
                    
                        #print(f"delta == 0")
                                                
                        
                        a_1 = f"((-{str_b} + ({delta} R 2)) / (2 * {str_a}))"
                        
                        
                        a_2 = f"((-{str_b} - ({delta} R 2)) / (2 * {str_a}))"
                        
                        
                        
                        m_1 = calculatrice_2(s=a_1, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                        
                        #print(f"m_1 = {m_1}")
                        
                                        
                        m_2 = calculatrice_2(s=a_2, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                        
                        #print(f"m_2 = {m_2}")
                        
                        
                        
                        if ((m_2[0] == False) and (m_1[0] == False)):
                        
                        
                            # i chose if it is positive or negative . relative to the position in the circle .                                
                            
                            if ((position_at_lest == 0.25) or ((position_at_lest == 0.5))):
                            
                                v_0 = f"({m_2[1][0]} * -1)"
                                
                                m_6 = calculatrice_2(s=v_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
                            
                                str_result = f"{m_6[1][0]}"
                            
                            elif ((position_at_lest == 0.0) or ((position_at_lest == 0.75))):
                            
                                str_result = f"{m_2[1][0]}"
                            
                            
                        
        
                else:
                
                    
                    pass
                    
                    #print(f"delta < 0")    
            
            
        
        
        # right here i chose sin . because : sin = ((1 - cos ^ 2) R 2)
           
                
        operation = f"((1 - {str_result} ^ 2) R 2)"
        
        
        m_2 = calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_1, e=False)
        
        
        
        if (m_2[0] == False):
        
        
            
            # right here i chose if it is positive xor negative . relative to the position in the circle .
                         
            if ((position_at_lest == 0.0) or ((position_at_lest == 0.25))):
            
                return f"{m_2[1][0]}"
            
            elif ((position_at_lest == 0.5) or ((position_at_lest == 0.75))):
            
                return f"({m_2[1][0]} * -1)"




        



        return ""













    if __name__ == "__main__":




        oper = "((10) ^ 2.5)"
        
                
        number_of_digit_after_the_floating_point = 20
        
        
        
        #oper = invers_cos(a="(1 / (2))")
        
        
        oper = invers_sin(a="0", b="-1000", number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point, type_of_angle="")
        
        
        
        #oper += " * 90"
       
        
        print(f"oper = {oper}")
        
        
        m = calculatrice_2(s=oper, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
        
        
        print(f"m = {m}")
        
        
        
        
        alpha = "(1 / 2) * 8"
        
        
        alpha += " * 90"
        
        
        alpha = "60"
        
        
        print(f"operation_of_alpha = {alpha}")
        
        
                
        str_0 = cos(alpha_=alpha, number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point, type_of_angle="degree")
        
        
        print(f"\n\n cos = {str_0} .\n\n")
        
        
                
        str_1 = sin(alpha_=alpha, number_of_digit_after_the_floating_point_1=number_of_digit_after_the_floating_point, type_of_angle="degree")
        
        
        print(f"\n\n sin = {str_1} .\n\n")
        
        
        
        t1 = time.time()

        m = calculatrice_2(s=oper, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
        
        t2 = time.time()
        
        print("oper = '", oper, "' . m = ", m, " . number_of_digit_after_the_floating_point_ = ", number_of_digit_after_the_floating_point, " . time = ", t2 - t1)



        s1 = "2.0"

        s2 = "-2.0"


        print(s1, ">", s2, " = ", my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point))

        print(s1, "==", s2, " = ", my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point))

        print(s1, "<", s2, " = ", my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point))



    
    
    
        
        
        print("\n" * 10)
        
        
        number_of_digit_after_the_floating_point_ = 10

        i_operation_0_i = "1/6"


        t1 = time.time()

        m = calculatrice_3(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point_, e=False)

        t2 = time.time()

        print("i_operation_0_i = '", i_operation_0_i, "' . m = ", m, " . number_of_digit_after_the_floating_point_ = ", number_of_digit_after_the_floating_point_, " . time = ", t2 - t1)

        
        
        
        
        print("\n" * 10)
        
        




        #s1 = "-2.0"

        #s2 = "2.0"


        #print("( s1 : ", s1, " ) > ", " ( s2 : ", s2, " ) = ", i_greater_1_i(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point))

        #print("( s1 : ", s1, " ) <",  " ( s2 : ", s2, " ) = ", i_inferior_1_i(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point))

        #print("( s1 : ", s1, " ) ==",  " ( s2 : ", s2, " ) = ", i_equal_1_i(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point))


        
        
        








                

                

                
                

                

                
                

                