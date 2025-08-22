import random
from tamagoshi import Tamagoshi

class Dragao(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.fogo = 100
    
    def cuspirFogo(self):
        self.energia -= 10
        self.tedio += 2
        self.fogo -=10
        
        self.historico.append(f"{self.nome} cuspiu fogo!")
        print("""\033[31m
                                 -==\\                          `//~\\   ~~~~`---.___.-~~      \n
                             ______-==|                         | |  \\           _-~`         \n
                       __--~~~  ,-/-==\\                        | |   `\        ,'             \n
                    _-~       /'    |  \\                      / /      \      /               \n
                  .'        /       |   \\                    /' /        \   /'                \n
                 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                  \n
                /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   \n
                                  \_|      /        _) | ;  ),   __--~~                        \n
                                    '~~--_/      _-~/- |/ \   '-~ \                            \n
                                   {\__--_/}    / \\_>-|)<__\      \                           \n
                                   /'   (_/  _-~  | |__>--<__|      |                          \n
                                  |   _/) )-~     | |__>--<__|      |                          \n
                                  / /~ ,_/       / /__>---<__/      |                          \n
                                 o-o _//        /-~_>---<__-~      /                           \n
                                 (^(~          /~_>---<__-      _-~                            \n
                                ,/|           /__>--<__/     _-~                               \n
                             ,//('(          |__>--<__|     /                  .----_          \n
                            ( ( '))          |__>--<__|    |                 /' _---_~\        \n
                         `-)) )) (           |__>--<__|    |               /'  /     ~\`\      \n
                        ,/,'//( (             \__>--<__\    \            /'  //        ||      \n
                      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       \n
                    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  \n
                  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    \n
                   ;'( ')/ ,)(                              ~~~~~~~~~~                         \n
                  ' ') '( (/                                                                   \n
                    '   '  `                                          \n
                                    
              """)
        print(f"{self.nome} soltou fogo!\nFogo restante: {self.fogo}")
        
    def rugir(self):
        self.energia -= 1
        self.tedio -= 2
        
        self.historico.append(f"{self.nome} rugiu ferozmente!")
        
        print("""
              \033[32m
                       /                            )\n
                      (                             |\\n
                     /|                              \\\n
                    //                                \\\n
                   ///                                 \|\n
                  /( \                                  )\\n
                  \\  \_                               //)\n
                   \\  :\__                           ///\n
                    \\     )                         // \\n
                     \\:  /                         // |/\n
                      \\ / \                       //  \\n
                       /)   \   ___..-'           (|  \_|\n
                      //     /   _.'              \ \  \\n
                     /|       \ \________          \ | /\n
                    (| _ _  __/          '-.       ) /.'\n
                     \\ .  '-.__            \_    / / \\n
                      \\_'.     > --._ '.     \  / / /\n
                       \ \      \     \  \     .' /.'\n
                        \ \  '._ /     \ )    / .' |\n
                         \ \_     \_   |    .'_/ __/\n
                          \  \      \_ |   / /  _/ \_\n
                           \  \       / _.' /  /     \\n
                           \   |     /.'   / .'       '-,_\n
                            \   \  .'   _.'_/             \\n
               /\    /\      ) ___(    /_.'           \    |\n
              | _\__// \    (.'      _/               |    |\n
              \/_  __  /--'`    ,                   __/    /\n
              (_ ) /b)  \  '.   :            \___.-'_/ \__/\n
              /:/:  ,     ) :        (      /_.'__/-'|_ _ /\n
             /:/: __/\ >  __,_.----.__\    /        (/(/(/\n
            (_(,_/V .'/--'    _/  __/ |   /\n
             VvvV  //`    _.-' _.'     \   \\n
               n_n//     (((/->/        |   /\n
               '--'         ~='          \  |\n
                                          | |_,,,\n
                                          \  \  /\n
              """)
        print("RAAAAAAAAAAHHHHHHHHHH")
    
    def voarAlto(self):
        self.energia -= 15
        self.tedio -= 5
        
        self.historico.append(f"{self.nome} voou alto nos céus!")

        print("""
              \033[32m
                               ___====-_  _-====___\n
                       _--^^^#####//      \\#####^^^--\n_
                    _-^##########// (    ) \\##########^-_\n
                   -############//  |\^^/|  \\############-\n
                 _/############//   (@::@)   \\############\_\n
                /#############((     \\//     ))#############\\n
               -###############\\    (oo)    //###############-\n
              -#################\\  / VV \  //#################-\n
             -###################\\/      \//###################-\n
            _#/|##########/\######(   /\   )######/\##########|\#_\n
            |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|\n
            `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '\n
               `   `  `      `   / | |  | | \   '      '  '   '\n
                                (  | |  | |  )\n
                               __\ | |  | | /__\n
                              (vvv(VVV)(VVV)vvv)\n
              """)
        print(f"{self.nome} voou alto!\nEnergia: {self.energia}")

class Hipogrifo(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.respeito = 100
        
        if self.respeito < 20:
            self.saude -= 15
            
    def voar(self):
        self.energia -= 20
        self.respeito += 10
        
        self.historico.append(f"{self.nome} voou majestosamente!")
        print("""
              \033[93m
                        //           //\n
                       ///          ///\n
                      ////         ////\n
                      |////       /////\n
                      |))//;     /)))//;\n
                     /)))))/;   /)))))/;\n
                 .---`,))))/;  /)))))))/;\n
             __--\/6-  \`))/; |)))))))/;\n
            (----/    \\\``;  |))))))/;\n
               ~/-\  \\\\\``   \))))))/;\n
                   \\\\\\\\`    |)))))/;\n
                   |\\\\\\\\___/))))))/;__-------.\n
                   //////|  %%_/))))))/;           \___,\n
                  |||||||\   \%%%%VLK;:              \_. \\n
                  |\\\\\\\\\                        |  | |\n
                   \\\\\\\                          |  | |\n
                    |\\\\               __|        /   / /\n
                    | \\__\     \___----  |       |   / /\n
                    |    / |     >     \   \      \  / /\n
                    |   /  |    /       \   \      >/ /  ,,\n
                    |   |  |   |         |   |    // /  //,\n
                    |   |  |   |         |   |   /| |   |\\,\n
                 _--'   _--'   |     _---_---'  |  \ \__/\|/\n
                (-(-===(-(-(===/    (-(-=(-(-(==/   \____/\n
              """)
        
        print(f"{self.nome} voou pelos céus!\nRespeito: {self.respeito}, Energia: {self.energia}")
        
    def planar(self):
        self.energia += 5
        
        self.historico.append(f"{self.nome} planou suavemente pelo ar.")
        print("""
              \033[93m
                .-')          _\n
               (`_^ (    .----`/\n
                ` )  \_/`   __/     __,\n
                __{   |`  __/      /_/\n
               / _{    \__/ '--.  //\n
               \_> \_\  >__/    \((\n
                    _/ /` _\_   |))\n
                   /__(  /______/`\n
              """)
        print(f"{self.nome} planou!\nEnergia: {self.energia}")
        
    def cumprimentar(self):
        cumprimento = ["respeitoso", "desrespeitoso"]
        
        aleatorio = random.choices(cumprimento)
        print(f"Você está cumprimentando {self.nome}")
        
        if aleatorio == 1:
            print(f"Você cumprimentou {self.nome} respeitosamente")
            print("""
                  \033[93m
                        .-')          _\n
                       (`_^ (    .----`/\n
                        ` )  \_/`   __/     __,\n
                          {   |`  __/      /_/\n
                          {    \__/ '--.  //\n
                           \_\  >__/    \((\n
                          _/_/ /` _\_   |))\n
                         /_/__(  /______/\n
                  """)
        else:
            print(f"Você cumprimentou {self.nome} desrespeitosamente")
            print("""
                  \033[93m
                                            _______\n
                                 ______,---'__,---'\n
                             _,-'---_---__,---'\n
                      /_    (,  ---____',\n
                     /  ',,   `, ,-'\n
                    ;/)   ,',,_/,'\n
                    | /\   ,.'//\\n
                    `-` \ ,,'    `.\n
                         `',   ,-- `.\n
                         '/ / |      `,         _\n
                         //'',.\_    .\\      ,{==>-\n
                      __//   __;_`-  \ `;.__,;'\n
                    ((,--,) (((,------;  `--'\n
                    ```  '   ```\n
                  """)


class Camaleao(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.camuflagem = 100
        
    def camuflar(self):
        if self.camuflagem > 0:
            self.camuflagem -= 10
            self.tedio -= 2
            self.historico.append(f"{self.nome} se camuflou e ficou protegido.")
            
            print("""
                                          _       _._\n
                           _,,-''' ''-,_ }'._''.,_.=._\n
                        ,-'      _ _    '        (  @)'-,\n
                      ,'  _..==;;::_::'-     __..----'''}\n
                     :  .'::_;==''       ,'',: : : '' '}\n
                    }  '::-'            /   },: : : :_,'\n
                   :  :'     _..,,_    '., '._-,,,--\'    _\n
                  :  ;   .-'       :      '-, ';,__\.\_.-'\n
                 {   '  :    _,,,   :__,,--::',,}___}^}_.-'\n
                 }        _,'__''',  ;_.-''_.-'\n
                :      ,':-''  ';, ;  ;_..-'\n
            _.-' }    ,',' ,''',  : ^^\n
            _.-''{    { ; ; ,', '  :\n
                  }   } :  ;_,' ;  }\n
                   {   ',',___,'   '\n
                    ',           ,'\n
                      '-,,__,,-'\n
          """)
            print(f"{self.nome} se camuflou!\nCamuflagem restante: {self.camuflagem}")
        else:
            print(f"{self.nome} está sem energia para se camuflar!")

    def pegarInseto(self):
        self.alimentar()
        print("""
                                          _       _._\n
                           _,,-''' ''-,_ }'._''.,_.=._\n
                        ,-'      _ _    '        (  @)'-,\n
                      ,'  _..==;;::_::'-     __..----'''____________________________________________MOSCA\n
                     :  .'::_;==''       ,'',: : : '' '}\n
                    }  '::-'            /   },: : : :_,'\n
                   :  :'     _..,,_    '., '._-,,,--\'    _\n
                  :  ;   .-'       :      '-, ';,__\.\_.-'\n
                 {   '  :    _,,,   :__,,--::',,}___}^}_.-'\n
                 }        _,'__''',  ;_.-''_.-'\n
                :      ,':-''  ';, ;  ;_..-'\n
            _.-' }    ,',' ,''',  : ^^\n
            _.-''{    { ; ; ,', '  :\n
                  }   } :  ;_,' ;  }\n
                   {   ',',___,'   '\n
                    ',           ,'\n
                      '-,,__,,-'\n
          """)
        self.historico.append(f"{self.nome} pegou um inseto.")
        print(f"{self.nome} pegou um inseto!\nFome: {self.fome}")
        
    def esconder(self):
        if self.camuflagem > 20:
            self.energia -= 10
            self.camuflagem -= 20
            
            self.historico.append(f"{self.nome} se escondeu habilmente.")
            print(f"{self.nome} se escondeu!\nEnergia: {self.energia}, Camuflagem: {self.camuflagem}")
        else:
            print(f"{self.nome} não pode se esconder agora!")
            

