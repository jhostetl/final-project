import requests
import json
from bs4 import BeautifulSoup
import sqlite3

DBNAME = 'weather2.db'

#AIRPORT_LIST = ["KAAA","KAAF","KAAO","KAAS","KAAT","KABE","KABI","KABQ","KABR","KABY","KACB","KACJ","KACK","KACP","KACQ","KACT","KACV","KACY","KACZ","KADC","KADG","KADH","KADM","KADS","KADT","KADU","KADW","KAEG","KAEJ","KAEL","KAEX","KAFF","KAFJ","KAFK","KAFN","KAFO","KAFP","KAFW","KAGC","KAGO","KAGR","KAGS","KAGZ","KAHC","KAHH","KAHN","KAHQ","KAIA","KAIB","KAID","KAIG","KAIK","KAIO","KAIT","KAIV","KAIY","KAIZ","KAJG","KAJO","KAJR","KAJZ","KAKH","KAKO","KAKQ","KAKR","KALB","KALI","KALK","KALM","KALN","KALO","KALS","KALW","KALX","KAMA","KAMG","KAMN","KAMT","KAMW","KANB","KAND","KANE","KANJ","KANK","KANP","KANQ","KANW","KANY","KAOC","KAOH","KAOO","KAOV","KAPA","KAPC","KAPF","KAPG","KAPH","KAPN","KAPT","KAPV","KAQO","KAQP","KAQR","KAQW","KARA","KARB","KARG","KARM","KARR","KART","KARV","KARW","KASD","KASE","KASG","KASH","KASJ","KASL","KASN","KAST","KASW","KASX","KASY","KATA","KATL","KATS","KATW","KATY","KAUG","KAUH","KAUM","KAUN","KAUO","KAUS","KAUW","KAVC","KAVK","KAVL","KAVO","KAVP","KAVQ","KAVX","KAWG","KAWM","KAWO","KAXA","KAXH","KAXN","KAXQ","KAXS","KAXV","KAXX","KAYS","KAYX","KAZC","KAZE","KAZO","KAZU","KBAB","KBAC","KBAD","KBAF","KBAK","KBAM","KBAN","KBAX","KBAZ","KBBB","KBBD","KBBG","KBBP","KBBW","KBCB","KBCE","KBCK","KBCT","KBDE","KBDG","KBDH","KBDJ","KBDL","KBDN","KBDQ","KBDR","KBDU","KBEC","KBED","KBEH","KBFA","KBFD","KBFE","KBFF","KBFI","KBFK","KBFL","KBFM","KBFR","KBFW","KBGD","KBGE","KBGF","KBGM","KBGR","KBHB","KBHC","KBHK","KBHM","KBID","KBIE","KBIF","KBIH","KBIL","KBIS","KBIV","KBIX","KBJC","KBJI","KBJJ","KBJN","KBKD","KBKE","KBKF","KBKL","KBKN","KBKS","KBKT","KBKV","KBKW","KBKX","KBLF","KBLH","KBLI","KBLM","KBLU","KBLV","KBMC","KBMG","KBMI","KBML","KBMQ","KBMT","KBNA","KBNG","KBNL","KBNO","KBNW","KBOI","KBOK","KBOS","KBOW","KBPG","KBPI","KBPK","KBPP","KBPT","KBQK","KBQR","KBRD","KBRL","KBRO","KBRY","KBST","KBTA","KBTF","KBTL","KBTM","KBTN","KBTP","KBTR","KBTV","KBTY","KBUB","KBUF","KBUM","KBUR","KBUU","KBUY","KBVI","KBVN","KBVO","KBVS","KBVU","KBVX","KBVY","KBWC","KBWD","KBWG","KBWI","KBWP","KBXA","KBXG","KBXK","KBXM","KBYG","KBYH","KBYI","KBYS","KBYY","KBZN","KCAD","KCAE","KCAG","KCAK","KCAO","KCAR","KCAV","KCBE","KCBF","KCBG","KCBK","KCBM","KCCA","KCCB","KCCO","KCCR","KCCY","KCDA","KCDC","KCDD","KCDH","KCDI","KCDK","KCDN","KCDR","KCDS","KCDW","KCEA","KCEC","KCEF","KCEK","KCEU","KCEV","KCEW","KCEY","KCEZ","KCFD","KCFE","KCFJ","KCFS","KCFT","KCFV","KCGC","KCGE","KCGF","KCGI","KCGS","KCGZ","KCHA","KCHD","KCHK","KCHN","KCHO","KCHQ","KCHS","KCHT","KCHU","KCIC","KCID","KCII","KCIN","KCIR","KCIU","KCJJ","KCJR","KCKA","KCKB","KCKC","KCKF","KCKI","KCKM","KCKN","KCKP","KCKV","KCLE","KCLI","KCLK","KCLL","KCLM","KCLR","KCLS","KCLT","KCLW","KCMA","KCMH","KCMI","KCMR","KCMX","KCMY","KCNC","KCNH","KCNI","KCNK","KCNM","KCNO","KCNP","KCNU","KCNW","KCNY","KCOD","KCOE","KCOF","KCOI","KCOM","KCON","KCOQ","KCOS","KCOT","KCOU","KCPC","KCPK","KCPM","KCPR","KCPS","KCPT","KCPU","KCQA","KCQB","KCQC","KCQF","KCQM","KCQW","KCQX","KCRE","KCRG","KCRO","KCRP","KCRQ","KCRS","KCRT","KCRW","KCRX","KCRZ","KCSB","KCSG","KCSM","KCSQ","KCSV","KCTB","KCTJ","KCTK","KCTY","KCTZ","KCUB","KCUH","KCUL","KCUT","KCVG","KCVH","KCVK","KCVN","KCVO","KCVS","KCVX","KCWA","KCWC","KCWF","KCWI","KCWS","KCWV","KCXE","KCXL","KCXO","KCXP","KCXU","KCXW","KCXY","KCYO","KCYS","KCYW","KCZD","KCZG","KCZK","KCZL","KCZT","KDAA","KDAB","KDAF","KDAG","KDAL","KDAN","KDAW","KDAY","KDBN","KDBQ","KDCA","KDCU","KDCY","KDDC","KDDH","KDEC","KDED","KDEH","KDEN","KDEQ","KDET","KDEW","KDFI","KDFW","KDGL","KDGW","KDHN","KDHT","KDIJ","KDIK","KDKB","KDKK","KDKR","KDKX","KDLC","KDLF","KDLH","KDLL","KDLN","KDLO","KDLS","KDLZ","KDMA","KDMN","KDMO","KDMW","KDNL","KDNN","KDNS","KDNV","KDOV","KDPA","KDPG","KDPL","KDQH","KDRA","KDRI","KDRO","KDRT","KDRU","KDSM","KDSV","KDTA","KDTG","KDTL","KDTN","KDTO","KDTS","KDTW","KDUA","KDUC","KDUG","KDUH","KDUJ","KDUX","KDVK","KDVL","KDVN","KDVO","KDVP","KDVT","KDWH","KDWU","KDXE","KDXR","KDXX","KDXZ","KDYA","KDYB","KDYL","KDYR","KDYS","KDYT","KDZJ","KEAG","KEAN","KEAR","KEAT","KEAU","KEBG","KEBS","KECG","KECS","KECU","KEDC","KEDE","KEDG","KEDJ","KEDN","KEDU","KEDW","KEED","KEEN","KEEO","KEET","KEFC","KEFD","KEFK","KEFT","KEFW","KEGE","KEGI","KEGQ","KEGT","KEGV","KEHA","KEHO","KEHR","KEIK","KEIW","KEKA","KEKM","KEKN","KEKO","KEKQ","KEKS","KEKX","KEKY","KELA","KELD","KELK","KELM","KELN","KELO","KELP","KELY","KELZ","KEMM","KEMP","KEMT","KEMV","KEND","KENL","KENV","KENW","KEOE","KEOK","KEOP","KEOS","KEPG","KEPH","KEPM","KEQA","KEQY","KERI","KERR","KERV","KERY","KESC","KESF","KESN","KEST","KESW","KETB","KETC","KETN","KEUF","KEUG","KEUL","KEVB","KEVM","KEVU","KEVV","KEVW","KEVY","KEWB","KEWK","KEWN","KEWR","KEXX","KEYE","KEYF","KEYQ","KEYW","KEZF","KEZI","KEZM","KEZS","KEZZ","KFAF","KFAM","KFAR","KFAT","KFAY","KFBG","KFBL","KFBR","KFBY","KFCA","KFCH","KFCI","KFCM","KFCS","KFCT","KFCY","KFDK","KFDR","KFDW","KFDY","KFEP","KFES","KFET","KFFA","KFFC","KFFL","KFFM","KFFO","KFFT","KFFZ","KFGX","KFHB","KFHR","KFHU","KFIG","KFIT","KFKA","KFKL","KFKN","KFKR","KFKS","KFLD","KFLG","KFLL","KFLO","KFLP","KFLV","KFLX","KFLY","KFME","KFMH","KFMM","KFMN","KFMY","KFMZ","KFNB","KFNL","KFNT","KFOA","KFOD","KFOE","KFOK","KFOM","KFOT","KFOZ","KFPK","KFPR","KFQD","KFRG","KFRH","KFRI","KFRM","KFRR","KFSD","KFSE","KFSI","KFSK","KFSM","KFSO","KFST","KFSU","KFSW","KFTG","KFTK","KFTT","KFTW","KFTY","KFUL","KFVE","KFVX","KFWA","KFWC","KFWN","KFWQ","KFWS","KFXE","KFXY","KFYE","KFYJ","KFYM","KFYV","KFZG","KFZI","KFZY","KGAB","KGAD","KGAF","KGAG","KGAI","KGBD","KGBN","KGBR","KGCC","KGCD","KGCK","KGCM","KGCN","KGDJ","KGDM","KGDP","KGDV","KGDY","KGED","KGEG","KGEU","KGEV","KGEY","KGFA","KGFK","KGFL","KGGE","KGGF","KGGG","KGGI","KGGW","KGHG","KGHM","KGIC","KGIF","KGJT","KGKJ","KGKT","KGKY","KGLD","KGLH","KGLS","KGLW","KGMJ","KGMU","KGNB","KGNC","KGNF","KGNG","KGNI","KGNT","KGNV","KGOK","KGON","KGOO","KGOV","KGPI","KGPT","KGRB","KGRD","KGRF","KGRI","KGRK","KGRN","KGRR","KGSB","KGSO","KGSP","KGSW","KGTB","KGTE","KGTF","KGTG","KGTR","KGTU","KGUC","KGUP","KGUS","KGUY","KGVE","KGVQ","KGVT","KGWB","KGWO","KGWR","KGWS","KGWW","KGXA","KGXY","KGYB","KGYH","KGYI","KGYR","KGYY","KGZH","KGZL","KHAB","KHAE","KHAF","KHAI","KHAO","KHAR","KHBC","KHBG","KHBI","KHBR","KHBZ","KHCD","KHDE","KHDN","KHDO","KHEE","KHEF","KHEG","KHEI","KHEQ","KHEY","KHEZ","KHFD","KHFF","KHGR","KHHF","KHHR","KHHW","KHIE","KHIF","KHII","KHIO","KHJH","KHJO","KHKA","KHKS","KHKY","KHLC","KHLG","KHLN","KHLR","KHLX","KHMN","KHMS","KHMT","KHMZ","KHND","KHNZ","KHOB","KHOE","KHON","KHOP","KHOT","KHOU","KHPN","KHQG","KHQM","KHQU","KHQZ","KHRI","KHRJ","KHRL","KHRO","KHRU","KHRX","KHSA","KHSE","KHSI","KHSP","KHSR","KHST","KHSV","KHTH","KHTO","KHTS","KHUA","KHUF","KHUL","KHUM","KHUT","KHVC","KHVE","KHVN","KHVR","KHVS","KHWD","KHWO","KHWQ","KHWV","KHWY","KHXD","KHXF","KHYA","KHYI","KHYR","KHYS","KHYW","KHYX","KHZE","KHZL","KIAB","KIAD","KIAG","KIAH","KIBM","KICR","KICT","KIDA","KIDI","KIDL","KIDP","KIEN","KIFP","KIGM","KIGX","KIIB","KIIY","KIJD","KIJX","KIKV","KIKW","KILE","KILG","KILM","KILN","KIML","KIMM","KIMS","KIND","KINJ","KINK","KINS","KINT","KINW","KIOW","KIPJ","KIPL","KIPT","KISM","KISN","KISO","KISP","KISW","KITH","KITR","KIWA","KIWI","KIXD","KIYK","KIZA","KIZG","KJAC","KJAN","KJAX","KJBR","KJCT","KJDN","KJEF","KJFK","KJFX","KJER","KJGG","KJHN","KJHW","KJKA","KJMS","KJNX","KJQF","KJRA","KJRB","KJST","KJSV","KJVW","KJWG","KJWN","KJYO","KJYR","KJZI","KJZP","KKIC","KKLS","KKNB","KLAA","KLAF","KLAL","KLAM","KLAN","KLAR","KLAS","KLAW","KLAX","KLBB","KLBE","KLBF","KLBL","KLBR","KLBT","KLCG","KLCK","KLCH","KLCI","KLCQ","KLDJ","KLDM","KLEB","KLEE","KLEM","KLEW","KLEX","KLFI","KLFK","KLFT","KLGA","KLGB","KLGD","KLGF","KLGU","KLHB","KLHM","KLHQ","KLHV","KLHX","KLHZ","KLIC","KLIT","KLKP","KLKR","KLKU","KLKV","KLLJ","KLLQ","KLLU","KLMO","KLMS","KLMT","KLNA","KLNC","KLND","KLNK","KLNN","KLNP","KLNS","KLOL","KLOR","KLOT","KLOU","KLOZ","KLPC","KLPR","KLQK","KLQR","KLRD","KLRF","KLRG","KLRU","KLSB","KLSE","KLSF","KLSK","KLSN","KLSV","KLTS","KLTY","KLUF","KLUG","KLUL","KLVK","KLVL","KLVM","KLVN","KLVS","KLWB","KLWC","KLWL","KLWM","KLWS","KLWT","KLWV","KLXL","KLXN","KLXT","KLXV","KLYH","KLYO","KLZU","KLZZ","KMAC","KMAE","KMAF","KMAI","KMAL","KMAN","KMAO","KMAW","KMBG","KMBO","KMBS","KMBT","KMCB","KMCC","KMCE","KMCF","KMCI","KMCK","KMCN","KMCO","KMCW","KMCZ","KMDD","KMDQ","KMDS","KMDT","KMDW","KMDZ","KMEB","KMEI","KMEJ","KMEM","KMER","KMEV","KMFE","KMFI","KMFR","KMFV","KMGE","KMGG","KMGJ","KMGM","KMGW","KMGY","KMHE","KMHK","KMHL","KMHN","KMHR","KMHS","KMHT","KMHV","KMIA","KMIB","KMIC","KMIO","KMIT","KMIV","KMJX","KMKA","KMKE","KMKJ","KMKL","KMKO","KMKT","KMKY","KMLB","KMLC","KMLD","KMLE","KMLF","KMLI","KMLS","KMLT","KMLU","KMMH","KMMI","KMMK","KMMS","KMMT","KMMU","KMMV","KMNI","KMNZ","KMOB","KMOD","KMOR","KMOT","KMPE","KMPI","KMPJ","KMPO","KMPR","KMPV","KMQI","KMQJ","KMQS","KMQY","KMRB","KMRF","KMRH","KMRN","KMRY","KMSL","KMSN","KMSO","KMSP","KMSS","KMSV","KMSY","KMTC","KMTH","KMTJ","KMTN","KMTP","KMTV","KMTW","KMUO","KMUT","KMUU","KMVC","KMVI","KMVL","KMVM","KMVY","KMWH","KMWK","KMWL","KMXA","KMXF","KMXO","KMYF","KMYL","KMYR","KMYV","KMYZ","KMZJ","KN","KNAB","KNBC","KNBJ","KNCA","KNDY","KNEL","KNEN","KNEW","KNFD","KNFE","KNFG","KNFJ","KNFL","KNFW","KNGP","KNGS","KNGU","KNGZ","KNHK","KNHL","KNHZ","KNID","KNIP","KNJK","KNJM","KNJW","KNKL","KNKT","KNKX","KNLC","KNMM","KNOW","KNPA","KNPI","KNQA","KNQB","KNQX","KNRA","KNRB","KNRN","KNRQ","KNRS","KNSI","KNTD","KNTK","KNTU","KNUC","KNUI","KNUN","KNUQ","KNUW","KNVI","KNWL","KNYG","KNYL","KNXF","KNXP","KNXX","KNZJ","KNZY","KOAJ","KOAK","KOAR","KOBE","KOBI","KOCF","KOCH","KOCW","KODO","KODX","KOEL","KOFF","KOFK","KOFP","KOGA","KOGB","KOGD","KOGS","KOIC","KOIN","KOJA","KOJC","KOKB","KOKC","KOKK","KOKM","KOKS","KOKV","KOLD","KOLE","KOLF","KOLM","KOLS","KOLU","KOLV","KOLZ","KOMA","KOMH","KOMK","KOMN","KONA","KONL","KONO","KONP","KONT","KONX","KOPF","KOPL","KOQN","KOQU","KORB","KORD","KORE","KORF","KORG","KORH","KORL","KORS","KOSH","KOSU","KOSX","KOTH","KOTM","KOUN","KOVE","KOVS","KOWB","KOWD","KOWI","KOWK","KOXB","KOXC","KOXD","KOXR","KOYM","KOZA","KOZR","KOZS","KPAE","KPAM","KPAN","KPAO","KPBF","KPBG","KPBI","KPBX","KPCM","KPCU","KPCZ","KPDC","KPDK","KPDT","KPDX","KPEO","KPEQ","KPFC","KPFN","KPGA","KPGD","KPGR","KPGV","KPHF","KPHG","KPHH","KPHK","KPHL","KPHP","KPHT","KPHX","KPIA","KPIB","KPIE","KPIH","KPIR","KPIT","KPKB","KPKV","KPLB","KPLK","KPLR","KPLU","KPMB","KPMD","KPMV","KPMZ","KPNA","KPNC","KPNE","KPNM","KPNN","KPNS","KPOB","KPOC","KPOU","KPOY","KPPF","KPQI","KPQL","KPRB","KPRC","KPRN","KPRX","KPSB","KPSC","KPSF","KPSK","KPSM","KPSO","KPSP","KPTB","KPTD","KPTN","KPTS","KPTT","KPTV","KPTW","KPUB","KPUC","KPUJ","KPUW","KPVB","KPVC","KPVD","KPVE","KPVF","KPVG","KPVJ","KPVU","KPVW","KPWA","KPWD","KPWK","KPWM","KPWT","KPXE","KPYG","KPYM","KPYP","KPYX","KQA7","KQAD","KQAE","KQAJ","KQAQ","KQAX","KQAY","KQCO","KQCT","KQCU","KQD9","KQDM","KQEZ","KQGV","KQGX","KQIR","KQIU","KQL5","KQMA","KQMG","KQMH","KQNC","KQNN","KQNS","KQNT","KQNY","KQOS","KQPC","KQPD","KQRY","KQSA","KQSE","KQSL","KQSM","KQSR","KQTA","KQTI","KQTO","KQTU","KQTX","KQTZ","KQVO","KQWM","KQXJ","KQXN","KQYB","KRAC","KRAL","KRAP","KRAW","KRBD","KRBE","KRBG","KRBL","KRBM","KRBW","KRCA","KRCE","KRCM","KRCT","KRDD","KRDG","KRDM","KRDR","KRDU","KRED","KREI","KREO","KRGK","KRHP","KRHV","KRIC","KRID","KRIF","KRIL","KRIR","KRIU","KRIV","KRIW","KRJD","KRKR","KRKD","KRKS","KRLD","KRME","KRMN","KRND","KRNM","KRNO","KRNT","KRNV","KROA","KROC","KROG","KROW","KRPB","KRPD","KRPH","KRPX","KRQE","KRRT","KRSL","KRST","KRSW","KRTN","KRTS","KRUE","KRUG","KRUQ","KRUT","KRVL","KRVS","KRWI","KRWL","KRWV","KRXE","KRYN","KRYV","KRYW","KRYY","KRZL","KRZN","KRZT","KRZZ","KSAA","KSAC","KSAD","KSAF","KSAN","KSAS","KSAT","KSAV","KSAW","KSAZ","KSBA","KSBD","KSBM","KSBN","KSBP","KSBS","KSBX","KSBY","KSCB","KSCD","KSCH","KSCK","KSCR","KSDC","KSDF","KSDL","KSDM","KSDY","KSEA","KSEE","KSEF","KSEG","KSEM","KSEP","KSEZ","KSFB","KSFD","KSFF","KSFM","KSFO","KSFQ","KSFZ","KSGF","KSGJ","KSGT","KSGU","KSGU","KSHD","KSHN","KSHR","KSHV","KSIF","KSIK","KSIY","KSJC","KSJN","KSJT","KSKA","KSKF","KSKI","KSKX","KSLB","KSLC","KSLE","KSLG","KSLI","KSLK","KSLN","KSLR","KSMD","KSME","KSMF","KSMN","KSMO","KSMQ","KSMS","KSMX","KSNA","KSNC","KSNK","KSNL","KSNS","KSNT","KSNY","KSOA","KSOP","KSOW","KSPA","KSPB","KSPD","KSPF","KSPG","KSPS","KSPW","KSPX","KSQL","KSRC","KSRQ","KSRR","KSSC","KSSF","KSSN","KSSQ","KSTC","KSTF","KSTK","KSTL","KSTP","KSTS","KSUA","KSUN","KSUS","KSUT","KSUU","KSUW","KSUX","KSUZ","KSVC","KSVE","KSVH","KSWF","KSWI","KSWO","KSWT","KSWW","KSXL","KSXT","KSXU","KSYF","KSYI","KSYL","KSYN","KSYR","KSZL","KSZP","KSZT","KTAD","KTAN","KTBX","KTCC","KTCL","KTCM","KTCS","KTCY","KTDF","KTDO","KTEB","KTEL","KTEX","KTGI","KTHM","KTHP","KTHV","KTIK","KTIW","KTIX","KTKI","KTKO","KTLH","KTLR","KTMB","KTME","KTMK","KTNP","KTNT","KTNU","KTNX","KTOA","KTOI","KTOL","KTOP","KTOR","KTPA","KTPF","KTPH","KTPL","KTQE","KTQH","KTQK","KTRI","KTRK","KTRM","KTRX","KTSP","KTTA","KTTD","KTTF","KTTN","KTUL","KTUP","KTUS","KTVC","KTVL","KTVR","KTVY","KTWF","KTWT","KTXK","KTYL","KTYQ","KTYR","KTYS","KTZR","KTZT","KUAO","KUBE","KUBS","KUCA","KUCP","KUDD","KUDG","KUES","KUGN","KUIL","KUIN","KUKF","KUKI","KUKL","KUKT","KULS","KUMP","KUNI","KUNU","KUNV","KUOS","KUOX","KUTS","KUUU","KUVA","KUZA","KVAY","KVBG","KVBT","KVBW","KVCB","KVCT","KVCV","KVDF","KVEL","KVER","KVES","KVGT","KVIH","KVIS","KVJI","KVKS","KVKX","KVLD","KVLL","KVMR","KVNC","KVNY","KVPS","KVPZ","KVQQ","KVRB","KVSF","KVTA","KVTN","KVUJ","KVUO","KVVS","KVYS","KWAL","KWAY","KWBW","KWDG","KWHP","KWJF","KWLD","KWLW","KWMC","KWRB","KWRI","KWRL","KWST","KWVI","KWVL","KWWD","KWWR","KWYS","KXBP","KXFL","KXMR","KXNA","KXNO","KXTA","KXVG","KYIP","KYKM","KYKN","KYNG","KZEF","KZER","KZPH","KZUN","KZZV"]

AIRPORT_LIST = ["KATL","KLAX","KORD","KJFK","KDEN","KSFO","KLAS","KCLT","KSEA","KPHX","KMIA","KMCO","KMSP","KBOS","KDTW","KPHL","KBWI","KSLC","KIAD","KPDX","KDAL","KSTL","KBNA","KHOU","KAUS","KMSY","KRDU","KMCI","KSMF","KSAT","KIND","KCLE","KPIT","KMKE","KCVG","KJAX","KBUF","KOMA","KARB"]



MONTH_DAY_COUNT = [31,28,31,30,31,30,31,31,30,31,30,31]

CACHE_FNAME = 'scraping_cache_dict.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def scrape_wunderground(airport, year, month):
    for month in range(month, month + 1):
        url = "https://www.wunderground.com/history/airport/" + airport + "/" + str(year) + "/" + str(month) + "/1/MonthlyCalendar.html"

        if url in CACHE_DICTION:
            try:
                pass
            except:
                print("cache error")   
        else:
            try:
                #print("Scraping wunderground")
                page_text = requests.get(url).text
                page_soup = BeautifulSoup(page_text, 'html.parser')
                day_table = page_soup.find_all(class_='dayTable')
                monthly_list = []

                for day in day_table:
                    try:
                        low = day.find(class_='low').text    
                        low = low.replace("°","") 
                        high = day.find(class_='high').text
                        high = high.replace("°","") 
                        daily_dictionary = {}
                        daily_dictionary["low"] = low
                        daily_dictionary["high"] = high 
                        monthly_list.append(daily_dictionary)
                    except:
                        pass
                        #print("no data or error for this date")    
            except:
                print("failed to scrape wunderground month page")

            CACHE_DICTION[url] = monthly_list
            dumped_json_cache = json.dumps(CACHE_DICTION)
            fw = open(CACHE_FNAME,"w")
            fw.write(dumped_json_cache)
            fw.close() 
        #print(CACHE_DICTION[url])
    for i in CACHE_DICTION[url]:
        if i["high"] == " - ":
            print(CACHE_DICTION[url])

    print(AIRPORT_LIST.index(airport), airport, year, month)    


def averages_scrape_wunderground(airport, year, month):
    for month in range(month, month + 1):
        url = "https://www.wunderground.com/history/airport/" + airport + "/" + str(year) + "/" + str(month) + "/1/MonthlyCalendar.html"
        cache_url = "averages-" + url
        cached_data = CACHE_DICTION[cache_url]
        missing_data = True

        for item in cached_data:
            if item["high"] == ' - ':
                missing_data = False

        if len(cached_data) == MONTH_DAY_COUNT[month-1]:
            missing_data = False

        if cache_url in CACHE_DICTION and missing_data == False :
            try:
                print("using cached data")
            except:
                print("cache error")   
        else:
            try:
                #print("Scraping wunderground")
                page_text = requests.get(url).text
                page_soup = BeautifulSoup(page_text, 'html.parser')
                day_table = page_soup.find_all(class_='dayTable')
                monthly_list = []

                for day in day_table:
                    try:
                        low = day.find_all(class_='low')  
                        low = low[1].text
                        low = low.replace("°","") 
                        high = day.find_all(class_='high')
                        high = high[1].text
                        high = high.replace("°","") 
                        daily_dictionary = {}
                        daily_dictionary["low"] = low
                        daily_dictionary["high"] = high 
                        monthly_list.append(daily_dictionary)
                    except:
                        pass
                        #print("no data or error for this date")    
            except:
                print("failed to scrape wunderground month page")

            CACHE_DICTION[cache_url] = monthly_list
            dumped_json_cache = json.dumps(CACHE_DICTION)
            fw = open(CACHE_FNAME,"w")
            fw.write(dumped_json_cache)
            fw.close() 
        #print(CACHE_DICTION[url])
    print(AIRPORT_LIST.index(airport), airport, year, month)  
    print(CACHE_DICTION[cache_url])


def display_averages(airport, month_requested, day_requested, table_name):
    if table_name == "wunderground_historical_averages_large_cities":
        count = 0
        high_adder = 0
        low_adder = 0
        error_in_month = False
        for year in range(2000,2018):
            for month in range(month_requested, month_requested + 1):
                try:
                    count += 1
                    url = "https://www.wunderground.com/history/airport/" + airport + "/" + str(year) + "/" + str(month) + "/1/MonthlyCalendar.html"
                    monthly_list = CACHE_DICTION[url]
                    high = float(monthly_list[day_requested-1]["high"])
                    high_adder += high
                    
                    low = float(monthly_list[day_requested-1]["low"])
                    low_adder += low

                    date_formatted = str(month) + "/" + str(day_requested) + "/" + str(year)
                    # print(count, date_formatted, "High:", high, "Low:", low)
                except:
                    date_formatted = str(month) + "/" + str(day_requested) + "/" + str(year)
                    error_in_month = True

        date_formatted = str(month) + "/" + str(day_requested)
        return(date_formatted, round(high_adder/count,2), round(low_adder/count,2)) 
    elif table_name == "wunderground_historical_averages2":
        for month in range(month_requested, month_requested + 1):
            try:
                url = "averages-https://www.wunderground.com/history/airport/" + airport + "/2017/" + str(month) + "/1/MonthlyCalendar.html"
                monthly_list = CACHE_DICTION[url]
                try:
                    high = float(monthly_list[day_requested-1]["high"])
                except:
                    high = "-"    
                try:
                    low = float(monthly_list[day_requested-1]["low"])
                except:
                    low = "-"
                date_formatted = str(month) + "/" + str(day_requested) + "/2017"

                # print(count, date_formatted, "High:", high, "Low:", low)
            except:
                date_formatted = str(month) + "/" + str(day_requested) + "/2017"
                error_in_month = True
                #print("error on",date_formatted )  
        date_formatted = str(month) + "/" + str(day_requested)       
        return(date_formatted, high, low) 

    elif table_name == "wunderground_large_cities_2017":
        for year in range(2017,2018):
            for month in range(month_requested, month_requested + 1):

                try:
                    url = "https://www.wunderground.com/history/airport/" + airport + "/" + str(year) + "/" + str(month) + "/1/MonthlyCalendar.html"
                    monthly_list = CACHE_DICTION[url]
                    high = float(monthly_list[day_requested-1]["high"])                 
                    low = float(monthly_list[day_requested-1]["low"])

                    date_formatted = str(month) + "/" + str(day_requested) + "/" + str(year)
                    # print(count, date_formatted, "High:", high, "Low:", low)
                except:
                    date_formatted = str(month) + "/" + str(day_requested) + "/" + str(year)
                    high = "error"
                    low = "error"

        date_formatted = str(month) + "/" + str(day_requested)

        return(date_formatted, round(high), round(low))                                 
                
def init_database(db_name):

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    # code to insert Countries table
    # statement = "DROP TABLE IF EXISTS 'wunderground_historical_averages' ";
    # cur.execute(statement)
    # conn.commit()

    # statement = '''
    #     CREATE TABLE IF NOT EXISTS 'wunderground_historical_averages' (
    #         'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
    #         'Date' TEXT,
    #         'LocationCode' TEXT,
    #         'AverageHigh' REAL,
    #         'AverageLow' REAL
    #     );
    # '''
    # cur.execute(statement)

    # statement = "DROP TABLE IF EXISTS 'wunderground_historical_averages2' ";
    # cur.execute(statement)
    # conn.commit()

    # statement = '''
    #     CREATE TABLE IF NOT EXISTS 'wunderground_historical_averages2' (
    #         'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
    #         'Date' TEXT,
    #         'LocationCode' TEXT,
    #         'AverageHigh' REAL,
    #         'AverageLow' REAL
    #     );
    # '''
    # cur.execute(statement)

    # conn.commit()
    # conn.close()

    # statement = "DROP TABLE IF EXISTS 'wunderground_large_cities_2017' ";
    # cur.execute(statement)
    # conn.commit()

    # statement = '''
    #     CREATE TABLE IF NOT EXISTS 'wunderground_large_cities_all_data' (
    #         'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
    #         'Date' TEXT,
    #         'LocationCode' TEXT,
    #         'AverageHigh' REAL,
    #         'AverageLow' REAL
    #     );
    # '''
    # cur.execute(statement)

    conn.commit()
    conn.close()    


def insert_into_wunderground_table(db_name, month, day, airport, table_name, year):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    #average_data = display_averages(airport, month, day, table_name)

    try:
        url = "https://www.wunderground.com/history/airport/" + airport + "/" + str(year) + "/" + str(month) + "/1/MonthlyCalendar.html"
        monthly_list = CACHE_DICTION[url]

        high = float(monthly_list[day-1]["high"])                 
        low = float(monthly_list[day-1]["low"])

        date_formatted = str(month) + "/" + str(day) + "/" + str(year)
        print(date_formatted, airport, high, low)
        insertion = (None, date_formatted, airport, high, low)
        statement = 'INSERT INTO "' + table_name + '" '
        statement += 'VALUES (?, ?, ?, ?, ?)'

        cur.execute(statement, insertion)
        conn.commit()
        conn.close()
    except:
        pass    

def start_insert(airport_list_number1, airport_list_number2, table_name):
    for airport_number in range(airport_list_number1, airport_list_number2):
        airport = AIRPORT_LIST[airport_number]
        try:
            for year in range(2001,2018):
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 1, day, airport, table_name, year)
                for day in range(1,29): 
                    insert_into_wunderground_table(DBNAME, 2, day, airport, table_name, year)
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 3, day, airport, table_name, year)
                for day in range(1,31): 
                    insert_into_wunderground_table(DBNAME, 4, day, airport, table_name, year)
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 5, day, airport, table_name, year)
                for day in range(1,31): 
                    insert_into_wunderground_table(DBNAME, 6, day, airport, table_name, year)
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 7, day, airport, table_name, year)
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 8, day, airport, table_name, year)
                for day in range(1,31): 
                    insert_into_wunderground_table(DBNAME, 9, day, airport, table_name, year)
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 10, day, airport, table_name, year)
                for day in range(1,31): 
                    insert_into_wunderground_table(DBNAME, 11, day, airport, table_name, year)
                for day in range(1,32): 
                    insert_into_wunderground_table(DBNAME, 12, day, airport, table_name, year) 
        except:
            print("airport error")
            print(airport, airport_list_number1, airport_list_number2, table_name)


def start_scrape(airport_list_number1, airport_list_number2):
    for airport in range(airport_list_number1, airport_list_number2):
        airport_code = AIRPORT_LIST[airport]       
        for year in range(2000,2018):
            for i in range(1,13):
                scrape_wunderground(airport_code, year, i)



def averages_start_scrape(airport_list_number1, airport_list_number2):
    for airport in range(airport_list_number1, airport_list_number2):
        airport_code = AIRPORT_LIST[airport]       
        for year in range(2017,2018):
            for i in range(1,13):
                averages_scrape_wunderground(airport_code, year, i)




#init_database(DBNAME)


#use this to scrape and store data into cache
# start_scrape(0, 61) 
# averages_start_scrape(105, 106) 

#use this to insert into database from cached data


#start_insert(38,39, "wunderground_large_cities_all_data")




