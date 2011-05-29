#!/usr/bin/perl -w
# -*- perl -*-

###########################################################################
# This is a tokenizer for English. It was written as a single perl script #
#      by Yaser Al-Onaizan based on several scripts by Dan Melamed.       #
#  WS'99 STatistical Machine Translation Team.                            #     
#  IN: Englsih text in STDIN                                              #
#  OUT: tokenized English text in STDOUT                                  #
#  
#  Rada: fixed bug in the Emerge_abbr function 
###########################################################################     

while(<STDIN>){
    &Estem_contractions();
    &Edelimit_tokens();
    &Estem_elision();
    &Emerge_abbr();
    tr/[ \t\r\n]//s; # supress multiple white spaces into single space
    s/^\s+//;
    print STDOUT ;
}



sub Estem_contractions(){

    s/\'t/ \'t/g;
    s/\'m/ \'m/g;
    s/\'re/ \'re/g;
    s/\'ll/ \'ll/g;
    s/\'ve/ \'ve/g;
# put space before ambiguous contractions
    s/([^ ])\'s/$1 \'s/g;
    s/([^ ])\'d/$1 \'d/g;    
}


sub Estem_elision(){
# stems English elisions, except for the ambiguous cases of 's and 'd

    s/Won \'t/Won* n\'t/g;
    s/Can \'t/Can* n\'t/g;
    s/Shan \'t/Shan* n\'t/g;
    s/won \'t/won* n\'t/g;
    s/can \'t/can* n\'t/g;
    s/shan \'t/shan* n\'t/g;
    s/n 't/ n't/g;
# s/ 'm/ am/g;
# s/n 't/ not/g;
# s/ 're/ are/g;
# s/ 'll/ will/g;
# s/ 've/ have/g;

}

sub Edelimit_tokens(){
# puts spaces around punctuation and special symbols

# stardardize quotes
    s/\'\' /\" /g;
    s/ \`\`/ \"/g;
    s/\'\'$/\"/g;
    s/^\`\`/\"/g;
    
# put space after any period that's followed by a non-number and non-period
    s/\.([^0-9\.])/\. $1/g;
    s/\.$/\. /g;
# put space before any period that's followed by a space or another period, 
# unless preceded by another period
# the following space is introduced in the previous command
    s/([^\.])\.([ \.])/$1 \.$2/g;
    
# put space around sequences of colons and comas, unless they're
# surrounded by numbers or other colons and comas
    s/([0-9:])\:([0-9:])/$1<CLTKN>$2/g;
    s/\:/ \: /g;
    s/([0-9]) ?<CLTKN> ?([0-9])/$1\:$2/g;
    s/([0-9,])\,([0-9,])/$1<CMTKN>$2/g;
    s/\,/ \, /g;
    s/([0-9]) ?<CMTKN> ?([0-9])/$1\,$2/g;
    
# put space before any other punctuation and special symbol sequences
    s/([^ \!])(\!+)/$1 $2/g;
    s/([^ \?])(\?+)/$1 $2/g;
    s/([^ \;])(\;+)/$1 $2/g;
    s/([^ \"])(\"+)/$1 $2/g;
    s/([^ \)])(\)+)/$1 $2/g;
    s/([^ \(])(\(+)/$1 $2/g;
    s/([^ \/])(\/+)/$1 $2/g;
    s/([^ \&])(\&+)/$1 $2/g;
    s/([^ \^])(\^+)/$1 $2/g;
    s/([^ \%])(\%+)/$1 $2/g;
    s/([^ \$])(\$+)/$1 $2/g;
    s/([^ \+])(\++)/$1 $2/g;
    s/([^ \-])(\-+)/$1 $2/g;
    s/([^ \#])(\#+)/$1 $2/g;
    s/([^ \*])(\*+)/$1 $2/g;
    s/([^ \[])(\[+)/$1 $2/g;
    s/([^ \]])(\]+)/$1 $2/g;
    s/([^ \{])(\{+)/$1 $2/g;
    s/([^ \}])(\}+)/$1 $2/g;
    s/([^ \>])(\>+)/$1 $2/g;
    s/([^ \<])(\<+)/$1 $2/g;
    s/([^ \_])(\_+)/$1 $2/g;
    s/([^ \\])(\\+)/$1 $2/g;
    s/([^ \|])(\|+)/$1 $2/g;
    s/([^ \=])(\=+)/$1 $2/g;
    s/([^ \'])(\'+)/$1 $2/g;
    s/([^ \`])(\`+)/$1 $2/g;
    
    s/([^ \²])(\²+)/$1 $2/g;
    s/([^ \³])(\³+)/$1 $2/g;
    s/([^ \«])(\«+)/$1 $2/g;
    s/([^ \»])(\»+)/$1 $2/g;
    s/([^ \¢])(\¢+)/$1 $2/g;
    s/([^ \°])(\°+)/$1 $2/g;
    
# put space after any other punctuation and special symbols sequences
    s/(\!+)([^ \!])/$1 $2/g;
    s/(\?+)([^ \?])/$1 $2/g;
    s/(\;+)([^ \;])/$1 $2/g;
    s/(\"+)([^ \"])/$1 $2/g;
    s/(\(+)([^ \(])/$1 $2/g;
    s/(\)+)([^ \)])/$1 $2/g;
    s/(\/+)([^ \/])/$1 $2/g;
    s/(\&+)([^ \&])/$1 $2/g;
    s/(\^+)([^ \^])/$1 $2/g;
    s/(\%+)([^ \%])/$1 $2/g;
    s/(\$+)([^ \$])/$1 $2/g;
    s/(\++)([^ \+])/$1 $2/g;
    s/(\-+)([^ \-])/$1 $2/g;
    s/(\#+)([^ \#])/$1 $2/g;
    s/(\*+)([^ \*])/$1 $2/g;
    s/(\[+)([^ \[])/$1 $2/g;
    s/(\]+)([^ \]])/$1 $2/g;
    s/(\}+)([^ \}])/$1 $2/g;
    s/(\{+)([^ \{])/$1 $2/g;
    s/(\\+)([^ \\])/$1 $2/g;
    s/(\|+)([^ \|])/$1 $2/g;
    s/(\_+)([^ \_])/$1 $2/g;
    s/(\<+)([^ \<])/$1 $2/g;
    s/(\>+)([^ \>])/$1 $2/g;
    s/(\=+)([^ \=])/$1 $2/g;
    s/(\`+)([^ \`])/$1 $2/g;
# s/(\'+)([^ \'])/$1 $2/g;      # do not insert space after forward tic

    s/(\²+)([^ \²])/$1 $2/g;
    s/(\³+)([^ \³])/$1 $2/g;
    s/(\«+)([^ \«])/$1 $2/g;
    s/(\»+)([^ \»])/$1 $2/g;
    s/(\¢+)([^ \¢])/$1 $2/g;
    s/(\°+)([^ \°])/$1 $2/g;

# separate alphabetical tokens

    s/([a-zA-Z]+)/ $1 /g;    
}


sub Emerge_abbr(){
    s/[\s\.]U\s+\.\s+S\s+\.\s+S\s+\.\s+R\s+\./U.S.S.R./g;
    s/[\s\.]U\s+\.\s+S\s+\.\s+A\s+\./U.S.A./g;
    s/[\s\.]P\s+\.\s+E\s+\.\s+I\s+\./P.E.I./g;
    s/[\s\.]p\s+\.\s+m\s+\./p.m./g;
    s/[\s\.]a\s+\.\s+m\s+\./a.m./g;
    s/[\s\.]U\s+\.\s+S\s+\./U.S./g;
    s/[\s\.]B\s+\.\s+C\s+\./B.C./g;
    s/[\s\.]vol\s+\./vol./g;
    s/[\s\.]viz\s+\./viz./g;
    s/[\s\.]v\s+\./v./g;
    s/[\s\.]terr\s+\./terr./g;
    s/[\s\.]tel\s+\./tel./g;
    s/[\s\.]subss\s+\./subss./g;
    s/[\s\.]subs\s+\./subs./g;
    s/[\s\.]sub\s+\./sub./g;
    s/[\s\.]sess\s+\./sess./g;
    s/[\s\.]seq\s+\./seq./g;
    s/[\s\.]sec\s+\./sec./g;
    s/[\s\.]rév\s+\./rév./g;
    s/[\s\.]rev\s+\./rev./g;
    s/[\s\.]repl\s+\./repl./g;
    s/[\s\.]rep\s+\./rep./g;
    s/[\s\.]rel\s+\./rel./g;
    s/[\s\.]paras\s+\./paras./g;
    s/[\s\.]para\s+\./para./g;
    s/[\s\.]op\s+\./op./g;
    s/[\s\.]nom\s+\./nom./g;
    s/[\s\.]nil\s+\./nil./g;
    s/[\s\.]mr\s+\./mr./g;
    s/[\s\.]lég\s+\./lég./g;
    s/[\s\.]loc\s+\./loc./g;
    s/[\s\.]jur\s+\./jur./g;
    s/[\s\.]int\s+\./int./g;
    s/[\s\.]incl\s+\./incl./g;
    s/[\s\.]inc\s+\./inc./g;
    s/[\s\.]id\s+\./id./g;
    s/[\s\.]ibid\s+\./ibid./g;
    s/[\s\.]hum\s+\./hum./g;
    s/[\s\.]hon\s+\./hon./g;
    s/[\s\.]gén\s+\./gén./g;
    s/[\s\.]etc\s+\./etc./g;
    s/[\s\.]esp\s+\./esp./g;
    s/[\s\.]eg\s+\./eg./g;
    s/[\s\.]eds\s+\./eds./g;
    s/[\s\.]ed\s+\./ed./g;
    s/[\s\.]crit\s+\./crit./g;
    s/[\s\.]corp\s+\./corp./g;
    s/[\s\.]conf\s+\./conf./g;
    s/[\s\.]comp\s+\./comp./g;
    s/[\s\.]comm\s+\./comm./g;
    s/[\s\.]com\s+\./com./g;
    s/[\s\.]co\s+\./co./g;
    s/[\s\.]civ\s+\./civ./g;
    s/[\s\.]cit\s+\./cit./g;
    s/[\s\.]chap\s+\./chap./g;
    s/[\s\.]cert\s+\./cert./g;
    s/[\s\.]ass\s+\./ass./g;
    s/[\s\.]arts\s+\./arts./g;
    s/[\s\.]art\s+\./art./g;
    s/[\s\.]alta\s+\./alta./g;
    s/[\s\.]al\s+\./al./g;
    s/[\s\.]Yes\s+\./Yes./g;
    s/[\s\.]XX\s+\./XX./g;
    s/[\s\.]XVIII\s+\./XVIII./g;
    s/[\s\.]XVII\s+\./XVII./g;
    s/[\s\.]XVI\s+\./XVI./g;
    s/[\s\.]XV\s+\./XV./g;
    s/[\s\.]XIX\s+\./XIX./g;
    s/[\s\.]XIV\s+\./XIV./g;
    s/[\s\.]XIII\s+\./XIII./g;
    s/[\s\.]XII\s+\./XII./g;
    s/[\s\.]XI\s+\./XI./g;
    s/[\s\.]X\s+\./X./g;
    s/[\s\.]Wash\s+\./Wash./g;
    s/[\s\.]Vol\s+\./Vol./g;
    s/[\s\.]Vict\s+\./Vict./g;
    s/[\s\.]Ves\s+\./Ves./g;
    s/[\s\.]Va\s+\./Va./g;
    s/[\s\.]VIII\s+\./VIII./g;
    s/[\s\.]VII\s+\./VII./g;
    s/[\s\.]VI\s+\./VI./g;
    s/[\s\.]V\s+\./V./g;
    s/[\s\.]Univ\s+\./Univ./g;
    s/[\s\.]Trib\s+\./Trib./g;
    s/[\s\.]Tr\s+\./Tr./g;
    s/[\s\.]Tex\s+\./Tex./g;
    s/[\s\.]Surr\s+\./Surr./g;
    s/[\s\.]Supp\s+\./Supp./g;
    s/[\s\.]Sup\s+\./Sup./g;
    s/[\s\.]Stud\s+\./Stud./g;
    s/[\s\.]Ste\s+\./Ste./g;
    s/[\s\.]Stat\s+\./Stat./g;
    s/[\s\.]Stan\s+\./Stan./g;
    s/[\s\.]St\s+\./St./g;
    s/[\s\.]Soc\s+\./Soc./g;
    s/[\s\.]Sgt\s+\./Sgt./g;
    s/[\s\.]Sess\s+\./Sess./g;
    s/[\s\.]Sept\s+\./Sept./g;
    s/[\s\.]Sch\s+\./Sch./g;
    s/[\s\.]Sask\s+\./Sask./g;
    s/[\s\.]ST\s+\./ST./g;
    s/[\s\.]Ry\s+\./Ry./g;
    s/[\s\.]Rev\s+\./Rev./g;
    s/[\s\.]Rep\s+\./Rep./g;
    s/[\s\.]Reg\s+\./Reg./g;
    s/[\s\.]Ref\s+\./Ref./g;
    s/[\s\.]Qué\s+\./Qué./g;
    s/[\s\.]Que\s+\./Que./g;
    s/[\s\.]Pub\s+\./Pub./g;
    s/[\s\.]Pty\s+\./Pty./g;
    s/[\s\.]Prov\s+\./Prov./g;
    s/[\s\.]Prop\s+\./Prop./g;
    s/[\s\.]Prof\s+\./Prof./g;
    s/[\s\.]Probs\s+\./Probs./g;
    s/[\s\.]Plc\s+\./Plc./g;
    s/[\s\.]Pas\s+\./Pas./g;
    s/[\s\.]Parl\s+\./Parl./g;
    s/[\s\.]Pa\s+\./Pa./g;
    s/[\s\.]Oxf\s+\./Oxf./g;
    s/[\s\.]Ont\s+\./Ont./g;
    s/[\s\.]Okla\s+\./Okla./g;
    s/[\s\.]Nw\s+\./Nw./g;
    s/[\s\.]Nos\s+\./Nos./g;
    s/[\s\.]No\s+\./No./g;
    s/[\s\.]Nfld\s+\./Nfld./g;
    s/[\s\.]NOC\s+\./NOC./g;
    s/[\s\.]Mut\s+\./Mut./g;
    s/[\s\.]Mtl\s+\./Mtl./g;
    s/[\s\.]Ms\s+\./Ms./g;
    s/[\s\.]Mrs\s+\./Mrs./g;
    s/[\s\.]Mr\s+\./Mr./g;
    s/[\s\.]Mod\s+\./Mod./g;
    s/[\s\.]Minn\s+\./Minn./g;
    s/[\s\.]Mich\s+\./Mich./g;
    s/[\s\.]Mgr\s+\./Mgr./g;
    s/[\s\.]Mfg\s+\./Mfg./g;
    s/[\s\.]Messrs\s+\./Messrs./g;
    s/[\s\.]Mass\s+\./Mass./g;
    s/[\s\.]Mar\s+\./Mar./g;
    s/[\s\.]Man\s+\./Man./g;
    s/[\s\.]Maj\s+\./Maj./g;
    s/[\s\.]MURRAY\s+\./MURRAY./g;
    s/[\s\.]MR\s+\./MR./g;
    s/[\s\.]M\s+\./M./g;
    s/[\s\.]Ltd\s+\./Ltd./g;
    s/[\s\.]Ll\s+\./Ll./g;
    s/[\s\.]Ld\s+\./Ld./g;
    s/[\s\.]LTD\s+\./LTD./g;
    s/[\s\.]Jun\s+\./Jun./g;
    s/[\s\.]Jr\s+\./Jr./g;
    s/[\s\.]JJ\s+\./JJ./g;
    s/[\s\.]JA\s+\./JA./g;
    s/[\s\.]Ir\s+\./Ir./g;
    s/[\s\.]Int\s+\./Int./g;
    s/[\s\.]Inst\s+\./Inst./g;
    s/[\s\.]Ins\s+\./Ins./g;
    s/[\s\.]Inc\s+\./Inc./g;
    s/[\s\.]Imm\s+\./Imm./g;
s/[\s\.]Ill\s+\./Ill./g;
s/[\s\.]IX\s+\./IX./g;
s/[\s\.]IV\s+\./IV./g;
s/[\s\.]INC\s+\./INC./g;
s/[\s\.]III\s+\./III./g;
s/[\s\.]II\s+\./II./g;
s/[\s\.]I\s+\./I./g;
s/[\s\.]Hum\s+\./Hum./g;
s/[\s\.]Hon\s+\./Hon./g;
s/[\s\.]Harv\s+\./Harv./g;
s/[\s\.]Hagg\s+\./Hagg./g;
s/[\s\.]HON\s+\./HON./g;
s/[\s\.]Geo\s+\./Geo./g;
s/[\s\.]Genl\s+\./Genl./g;
s/[\s\.]Gen\s+\./Gen./g;
s/[\s\.]Gaz\s+\./Gaz./g;
s/[\s\.]Fin\s+\./Fin./g;
s/[\s\.]Fed\s+\./Fed./g;
s/[\s\.]Feb\s+\./Feb./g;
s/[\s\.]Fam\s+\./Fam./g;
s/[\s\.]Fac\s+\./Fac./g;
s/[\s\.]Europ\s+\./Europ./g;
s/[\s\.]Eur\s+\./Eur./g;
s/[\s\.]Esq\s+\./Esq./g;
s/[\s\.]Enr\s+\./Enr./g;
s/[\s\.]Eng\s+\./Eng./g;
s/[\s\.]Eliz\s+\./Eliz./g;
s/[\s\.]Edw\s+\./Edw./g;
s/[\s\.]Educ\s+\./Educ./g;
s/[\s\.]Dr\s+\./Dr./g;
s/[\s\.]Doc\s+\./Doc./g;
s/[\s\.]Dist\s+\./Dist./g;
s/[\s\.]Dept\s+\./Dept./g;
s/[\s\.]Dears\s+\./Dears./g;
s/[\s\.]Dal\s+\./Dal./g;
s/[\s\.]Ct\s+\./Ct./g;
s/[\s\.]Cst\s+\./Cst./g;
s/[\s\.]Crim\s+\./Crim./g;
s/[\s\.]Cr\s+\./Cr./g;
s/[\s\.]Cowp\s+\./Cowp./g;
s/[\s\.]Corp\s+\./Corp./g;
s/[\s\.]Conv\s+\./Conv./g;
s/[\s\.]Cons\s+\./Cons./g;
s/[\s\.]Conn\s+\./Conn./g;
s/[\s\.]Comp\s+\./Comp./g;
s/[\s\.]Comm\s+\./Comm./g;
s/[\s\.]Com\s+\./Com./g;
s/[\s\.]Colum\s+\./Colum./g;
s/[\s\.]Co\s+\./Co./g;
s/[\s\.]Cl\s+\./Cl./g;
s/[\s\.]Civ\s+\./Civ./g;
s/[\s\.]Cir\s+\./Cir./g;
s/[\s\.]Chas\s+\./Chas./g;
s/[\s\.]Ch\s+\./Ch./g;
s/[\s\.]Cf\s+\./Cf./g;
s/[\s\.]Cdn\s+\./Cdn./g;
s/[\s\.]Cass\s+\./Cass./g;
s/[\s\.]Cas\s+\./Cas./g;
s/[\s\.]Car\s+\./Car./g;
s/[\s\.]Can\s+\./Can./g;
s/[\s\.]Calif\s+\./Calif./g;
s/[\s\.]Cal\s+\./Cal./g;
s/[\s\.]Bros\s+\./Bros./g;
s/[\s\.]Bl\s+\./Bl./g;
s/[\s\.]Bd\s+\./Bd./g;
s/[\s\.]Aust\s+\./Aust./g;
s/[\s\.]Aug\s+\./Aug./g;
s/[\s\.]Assur\s+\./Assur./g;
s/[\s\.]Assn\s+\./Assn./g;
s/[\s\.]App\s+\./App./g;
s/[\s\.]Am\s+\./Am./g;
s/[\s\.]Alta\s+\./Alta./g;
s/[\s\.]Admin\s+\./Admin./g;
s/[\s\.]Adjut\s+\./Adjut./g;
s/[\s\.]APPLIC\s+\./APPLIC./g;

}
