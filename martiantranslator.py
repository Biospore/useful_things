﻿#!/usr/bin/python3
import re

class MartianTranslator:
    _to_martian = str('%m►▨(d◕◂q&◖◝2e◓▯>m▦◗30▽◍b9▾▬@&◌▰=/◙◍[9▤◙v>▧▥% ▵ m:▧◘5.▶◀&*◛▾k~◄▭v9◐▶)z◐■u[◉◊?u◃◊er▥◉de◍◚&0◓◇rc▣■wp◂▬=)▭◊:0○◔:#◄▫<b◗▢?q▩◒=:▾▽}3▯▣98▿▮@7▱▦ry►◎i>◀▵d{◝◍7e▰◍4_◓◐>8▮□z#◅●)s▣◆m?◕▤x%◜◆_i◔▵sj◘▤2>▹▿1f◎◚_u◗▩_9▢▷cn◐◂@0▬▸a3▼▼*=●◄?^◅◍@:▥▭c#◕▭~ ◊ g]◛◒kx▣◓&x▪▮o(◂◈(~▿▹?&◌◍g+▤▹6~▰■29◖▬$=◊▭p)◜▦8*►▸i1▤◒{:▥◎p-◓◛0[▻▢5&◓►x$▬▾aj▭▨t~◓◊9z▷◂f8◛◈u.▣▻z4◌▲g$◄◕l_▫▪[,◎▱m_▫◜.r△◖].▣▪)l◚▶*.◓▵ia◙▰e=◚◈1@◘▼v[◀▾r9◑▨m8◁▮b.○◝as◖●s7▰▹o_◌▣}?◍◗}1◁△nf▫◊nr◛▸$8◁◛ok►▩xs▰◌4?▪▬n{◝▪86◘▬+7▭►+i◝◂4d△►d1◜▪}_◑◍s*◈▽kj▼◍8?●▥d$◒◑>x◚◗!f◀▻@a◆◜>+◍○!p◜◓2#◆▧f>◁◝a+▤▤>o◃▯l3◇▣vn▷◍x=▨○a6▱▾d=◇◄w+◕▮qx►▧6e◒○o*◛▲<(◛▦!(◑○&_◒▹}:▩◍6z◉▴(h▶▱m,◘△,!◀▩z5▯▰$q▷◓05▿◇6$▭▯9 ◛ fe▯▤bm▧▭t=◙▧y+◒◊*h▫▦tt▤▫>=◔◚^u◈▬-e▱◂!a▼△:2▨▸3!▨▹wc◘◌?~▻▰n2◇◃o#▤◝))◖▧kg△▼:5◉►yr▷◇g~▨◉rj◃◓ l ◐z8▹○hu◐□g#▭◉<g▧◔=q◙□%b◒▬gj●◘5r◂▪d&▨▩2u◉◗b%◈◇tm◒◌?x◃◖s-◊▥*7◗◔(c▬▣.v▢▽@*◜◙@[◌◒l*◚●d~▴○]4▥▱1n◈◒n@■▽:x◐▹ ] ●==◜◅(k▸▫6r◚▴$0◂▭l(▸▴>~▨◀{w▯■7+◁▣>6▶□u:◘◀$^▼▱0-▩◛b_◘◉e:◔◒_c◂▢is◜◃/[▭▵e?▽◊m@▣▵%,▮◀v)◃■,i◉△f{□○4%▮▷[t◈◆/?◔▧7^◀▯js▶▰.9▾▥88▦▩(@◖◒<y▮▯j1◄◔=*◈▪]1◍▫0%▧▬ ! ◙2?◊■u4▧▼s/◑◁5x◁◃0t▴▱y[▦○cx▭□iw◜▻#l◂▧1)◜◗!{◕◅4p◙■,b►◊i$▯▨0v●▵ft▱▤o0▰◆)+◕◀bj◛◚&l◐◐f?◚▦-x▹▩z1▾◇3q▩◌_<◍◅!#▲◝2a■◛%&▦▿a-▪◘v^▱◚3)▣▿ol◃▲bn◂▥j?◂◚0l◔◂=]▽◎>h▲◔oc■▯~&◐▬$y◕▩*{▰◈0)▮●u5▰►17▵▯.b▧◉db□◜gf▨▦4z◁▦w=▤◆?p◘◜~w◄◉h#◈◎hr▹▫ai◁▧.0◒▰*?◍▮~u◃◎b#▴●dn▯◌[a◌▦.h◆▬/j◖◆02▮◈vu▨◗ g ◑12◌▤l#◖◓bo◗▦em▱◐^}◎▯l.▦□f#▩◖/s▬◌sw►◇ o ▶**◊▮7(▩▼e ◄ 6)◇▴i6▻▯95▥▪.:◇◕xa▤▽[5◗◚0?►▥1q○▱mt▥▮$r▼◆nq◝▤_%▾▯b{◖○j4◔▤3}▣●ap◙▢&@▷◛<}▲◓f:▷◌( ◗ 3{◑▷#%▤○@k◍◄qs◓▹+:◛▻)u▹▶-w◕◆b,▼◓a?●▲}v▢▾/7▾●xj◇▢p=▹▪.o◁◚ci◎▲)!▶◔yb◅▷ % ▵6%▭◅!0▤▿>(◈▣%w▰▢u~▹◝!]◊▧__◉◑c]◗◓{v◜◊i@▶▤%s▬◛(?▻◖%o◝▣k3▻◐*6►◅8)◖◑@>◃▪>s▶◇9>◈◝zl▣▹t[▢▦&h▼○lk◁►f&▾◈l2▻△a*◒◆{,◊▯[4◆●!-◐○?%▧▩+t○▨=#◄▽:w▣▰*@▾▶5n▫▽8b■▲k<▶◉}+◑◉x,►▭g(▹▲8g◛◜+(▸▷<j◜◍_:▪▷y*▷◅^!▼►t2△◅_m▵►dc▽▯)5□▪39◐▰6}◔◖ql◇► 7 ■-!◂◗[/▷◑5+▥◙62◜▶9x◈◗d^▭◃=o▫▾?0◎◀7,◎▾~/▵◐z,▶◘]?□◂a/◆◖,-◕◒*+▱▩qu◄◖48▾▰=3▻◀%[▯▱9~▿▿]x◛◇!&◐◗-o◆◙2.▣▱o,▴◙82▼▵lw▯▬n_▢◄rz▼▲]7▮▣7]◚▣v2▥◓fn◈▾{1◑◄>l◃▴%:▴◘j7▥▬&.▱▵ek◑◙0.▻▵xn▨◆&e◍▨u>▦▽.z●▮2b▿▦7u▹▼=j▻▲xt◊◒j{◚▪b]◇▲wq▵▫)3▦▰?o▨◅(&○◉pd△◎us◓▽nb▸▮ky◑◓y,►◝i!△▯<q▪◄^+◘◛_o▵◌&/▰○7q▹◎ms►◐yi◌▢m[▪▼kp◐◄k&►◍o&◃◈:]▰▦4#▦◈v#◝◀u6▶▢bs◊▶x6◒▽{b◁◘i,◖▹_h▬▤/@◛▴{3◇▶mc▽○_>◆◊%?◂◔{(▷▫3/□▬c6▱▻)d◗▫)7▸◒9^◈□ ) ▹z.◂◆y~○◊8p▸▵)[◄◍,a□◘&!◖▿c9▯◒x<▢▬r1▪◛*m►▯vw◍◁_ ▬ 20▯◄hv▭◛xe◖◁fu◗◒6u●◛>0▶▾.e▢▫z&▧◌kf▽◆*s►▱w(▶●nl◗▥@.▲◐* ▾ k2○◑(<▦▨_~▴▪3<◄□61◆◘3x◎▫$!◒◙p,▻▷8s▵◖oy◝▯:_◂△$j◃▦z@▯▵)w▧◑y@▴◅-6◆▥@m□▱qi▪◐$#◖■nw◎◉dj▽□o}◀◃#n▬◘:7▧●9d◀▲d3◗○az▣▮s>◀◊.+◁▹+f◇◈ly▲▬3.▣▽q[◌◁,&►◜%>▻●]v▱◁^1▦▸:<◌▬t:▰▤at◊◁6+▶▷v%▿▤ev◂▣r.◄▶]f▪▪<1◗▬^(▯◁y=▢◗k6◖▵zr▬◉pz▰△qc◁◀#i◕◄7{◛▽)j◌▾~~◃▱qg◑◈~9▽▽~h□▼)>◙◁)c▤▶4b◃◇s~◑△c(▩▹bx▮◃5g▿◜5(▴▢35▽▥ez◆◅7/◛◀r^▭◍g8▵◇,#◖◃+@►▲)g▥◔py▹◓o[◎◓3[△▮,8►◄&b▽►s]▣►79◉▽sx△▴)?►▦^r▷▦~(▪◅?j▰▯+4►▵zq▣▲)t◍◂e_◂◘_l◀▽c$◌◃#0▢□vm△▻m]▹△a&◂◁xk◚◁p4◊△7:▤▴99◔◜ws▪◊u,▷▧^q◎△r?▦◑42▲▫uj◄▦[=◍▢}d▮▦bf◉◛[]◙▱/^▮◛ 6 ◚1o◊▫f0▣◅v+▴▾f6▰▲@@▯◈u8▭▼r:▹◉dq▧▧=!◕◎o{◚◀7v▥□f4▽●!d▣◌?-◀◍64▰▿!_◀▿&6▸◑ns◕◗?g◀▭zb▭▩@e◁◙ri◁◉,?◗◄ht▯▯^$▷◙#5▥◆v7○◅-]◊◆mh▰▻>@▥▤-}◉◍[$▴▵h ► +z◒△%r◌◓mp▨▼ { ◔]p◕◍$]▽◐n)◑▮..▣◐>%◝▾:s▷▾s@▶◑{a▯▴?h◑▲_t◜▴#j►▾{e○◇2,▮►aq▲◊@2◖▱ 0 ◂!!▮▭!}▷▲vy◚►%%◝◙ w ▩([▬●$ ◅ al●□68▻▧#1▱▽[l▻▬3$▽▼*i►◃:v▥◚{>◝▼1_◔▰5#▾▾@5▮▾i:●▼i0◉▨}0▦▵1%▴▫h9▯▩43◄◓}z◓◀9{◔▻--▢▴?1▹▧f2◄▨.<◔◄+%▫▿=t▤◅ya◉▼g)▵▿k@◃▹wo▥▻g/▨◁!m▿◖m&◐▻wf◒▵^b◂◄pq▼◎%~◌▴5}▲◍f@▭▮}w►◚u)◚▰q%◙▿<8◍▧wx◜◄6p□▴]=○▣8#◃◔ / △vv◗□vb▫▵>r▻▼]r▭▰:6■▤#*▱■~o▻◍s}▶▴11▹◖9h▮▪]d▮▮sc▤▬jj◖▰:4△▨00◈◃ao▩▸.1◚◘~%▴◎b~▮◙^6▮△.k▬◜e-◕►:e▾▤xv◆▩7=▧◁m6◘►18▿▶f3▵▧3 ◖ @_◍◖e<●◜?e△◁0k◎▣zc▼◅_-◂◑ca▢◊2!◍▻$+◕◛-b◉▲#@▥◊15◅◚f<◇◅{q◅▴k,◚▭^p▽■]3▪●+/▫▯jt▥◇k=◛▧16▻○i%◈▰@f◊◀52▨◕<w◖▴pt◇▰9+◙▥87▶◁+6▮◒ie□◆a1▮▻yj◓◂0=◅◇u&○▴[c▽▾<6◂◎kq◓◝e@◒◕<t◇◌r/▣◄ c ▭i=▾◆l,▴◇x(◛▱ s ▦1m►◗$x◗▶a ◕ )1◄▬_7◊▴cp▬◒3z□◈>b◙◕[?◖◂=x◙◎z7■◗sp◛▩@=▢◘7y◍◒b(▮◝y2◔▽>w◃▻g3○▯tf◉◘.6◝◈1,►●o4▸◓1$▫► j ▲z/◗◝ih◐◓ $ ◅[*▪◙3*◓▼bb▥◑on◗◌]u◁▬1g▴▼nz◂◙*#▶◅%5▪◚#o◑◔l6▻◔o]▩◙]-▱▰9]◂▷a#▲◚!z▦▤![▨▫&k▦▱{/▨◔#>◆◆!@▿▣+^▢◂<)▢◖r&◄◛_j▮▩c@◃◍0}◑▱=u◙▨0]▫●z[◚▷k}▱►b?▰◉sl△■*/◀◓$n◀▢&p◉◇j ▲ =h◂▮8=◕▯hb◆▲s=◎▪[f◒◂+o▢◛/$◄▱tq▵▷(_◛△1.◒◒$_▫◇.4▫◆&$◜◁]g▤◘8y◍◉@8◑▸sn◝▽%]◙▽k*◑▤!4■▻}k▻◌c0◕▲%g◂▻pf◒▴-1▾◌5s○◚3r▵◆#.▷◘8r▢▪iu▵◁0@▣▩,]▵▾{{▼▪#!▱▼km▤▮ay▴▤.x▦◂8<▨◒_[◎▧j^►◕ak▾▻x ◝ qz◙◙q(◃▾j3◎▵mw▫◙=^◝▬9v▹▦b1◌△,w◃◂ps◀◕se◜▢6*▻◓u<▯▥e$◃◆40▽◌><▤▨]m▢▥g&◍◕ny▿◐a@▴◝0/▭◈-2◄◑+.▹▥h/◛◔*p◘◓x}▯◔g0■◄ha◐◅e5◗▵%#▶◗+=▻▦cd◉◐kt▪▰i~▲▦[@▱◅5-▹◑#_▵▭2t○○p □ +c◝◎i-◊▻~n◅◛#z►◈,}◉▥c)◘▥*5△▵+q▵◉4g◑□#g◗▲hq■◍v/▰▥q{▼▾y{▴◖_}▩▣~3▼◐d/▰◝7g◙▯i9▰▬yd▩▤&:▩▮({◑◜j9▰▰dp◜▣92▿◕6m◌○y#▰◅0,▭◌n*▯●8i▰▷1 ◘ 9.▱▧&^▥▥!b▢▼]b▢▶$u◎◗6n△◃1i◌◎dl◉▰?.▰◊ > ▪^j▢◔}=◘□e2▪◍] ● 8.◈◌i4▸▨-t□▻$4▿▷9f▫◄^=▬▻m2◝◉$c◒◝dw▬▦9:▲▿b}▯◚%!◕▢*g△◜t8□◁(:▯◀, ◉ 6.▮◚?i◒▱,p◄△$*◕▴?w◐◁*^◒◀)x◖▸81▩▫yl▹▱g.△▢s^◚▹ob◉◂cg▪▲y?◕▼b!□■]s▥▿[r◈▹pm▵■r2▤●-$◑◇$}▩◜h*▹▵!<◛▫f-▤◂q4◄◐.l▱▥#^◐△rt◓▷{<▫▥ 2 ▤}2◓◆c3▴▴x9▫◝<l◕◘j$▣◇-v▮▰<^□▦ma◊▱n1▫▮]#▱◆s:□◃5,□◀63▶▲l~◘▰%n▦▲p[◎▴k5◖◘,q□▲89◔◕2i▼◘ou▭◘1x◝△t(◉■~x◈◛^l▸◆h.◁▼!2▾◘h+◉▷aa◐▲~r◜▥w9◛◉)v◒◁jz▩◕ic▮◐[0◅▵f~◆▼%a◌◘c?◔▷^{▫▸7[◕▹.(◅◀/q◚◒0z▣◔0#◆▭=p◁○z^▷◉!.◘▲)8▤◎8d▪◗b=▽▦_k◉▫p{■▥+r▨◍&z▬◔4a▬◑*(▯▻xi△◐2]▼◁my○◈uf▿◀4-▼▩[p▲◁)^▬▿fs▩▦/)◚▩p^◒◄/0▲◂gy◇▼t3◀◒lb▵▥>g◆▶q2▣▷!x○△td◀▧5e▲▴s%◝▵t1▴▥<5▷◄o%◆▪7)◈▥0{▤▪pj◛◝:z◊●??◇◉5u▵▨(r▸▿k-▨□wa○▧,s▨▵3e◅◘}m◄●3@◇▯i?◒▻%i▰◖jq▽◗z?◊◅kb▿■,{◎◄%1▫◔2(▶▫$:◅◄4>●◐(7◙◃{g▿▫}&▶◕j%◌▻zn◅▯_*▬▢4f▫▫4n▫▣&]▿▸4v◐▽> ▪ te◗▹<%▽▭%h▤◁d7▩▩}b▶◈ y ◃zx▢▿%v▲▨+g◔◐3h◈▷[{▯◑c~◃▰+m▨◘w#◑▣,4►■.%▰◘yy▧○~}◘▫xz▻►qd▴◑t>▼◇>n▣▭,n◕▽3=◙◅ * ▾w2▤◀q>◚◉i/▢◇8@◀◆?t◍▼-c▿◉/!▦■^.▥◛4y▿◎.7□▿k0◁◈r-◀◖x-▲▸8/▿●d ▱ 85▪►{+▪△?,◇◒o6▥▯}~◀▥pi◆▷0b▽▩^?◀▰af◛▣i2△▭bt▵▼8~◎▩$d◄◅>$●▣g7◝▩r(◗◖.5▶▨4h◘◂f9◉▮/c◍◆p2◍▷:!▢▩z%◅▤]c▬▼(!▿◗yh■□i{▯△en◔□z}▲◆k?◔▭9p■◔ck▮▴ow▭▦0e▱◍v*▧◖5?◓▰vs▾◒>q◔◇%x▯▽y5◂▹,=▵▬2/●△3a◖▶-%◃◁h%◒●8l▱▯c1◑■gv◇◘5~▤◔]*▫◛-^◐◙!q◀▼vo◊▽-l▮▥r%▬▴+v□▷+n▻▩wv◊◓^8◛▥->▦●g2◍▹cq◝◔!3▿◆,v◀▪b+◅▬s?▤◗[8▬▮76►◆<d◉▾gm◅◆f.◊◙x/◛◍[h◉● 3 ◖}5◂▩x{▾▩*e▪◆q0▢▵zf□▶5j◖◔?:◅▧:(▷■z9◖▻8:◎◇=k▦▹ @ ◇ ~ ◊~+◄▥%z▿◝$a▸▪-i◓▤n#●▱@3▤▼[_■▶)b▦▾1}◜▿?*▤▢e%◖◛!e◐▪h:◛▿cs▷►n ◁ nu▹◘)f▭▢:t◙▭_=▥◗eq▩■r]◗▰~{▶◂+y▢▱c-▦◕1?▲▲.#◗▼5)◇○<s▨▬?8◈▶-s■◁xl△◘t<◕◇dz▽▧0o◇◙t7◇▭jl◖▩$t△◄x_◘▷0&◀▱//◗▿) ▹ $o▯▼_?◎▤5[■▵5v◐▵0n◇◛e7▼▭:1□▮dv▬○,~▻◚j0▮▼+>▨◛rg◖◐lc▲■no○◓ , ◉<r◗◀ti◅▹&}▢◌x2▱▭1*◐◈tw△◗{_◖◖lu◕▫qe◄▹we▵◃wt▯▭^*▩◚-7◅◕of▶▶@1▨◊*n▢◃_0▶▪,j■▾+2○▬=z■◅8[▿◒a7▶▮>!▻▭ye▮◆b6▵◎(-◉▧0 ◂ j:◝◘06◖◅$[▰◀69◛◘gq◅◝g<●▹~e◌■w6◂▿wn▱◔)2◀◅z:◖◙)r○◕p@▾◀/}▧◝0s▩△^z▱◕v8◙◀oa▹►y1◍□y3◊▷gr▱▸)_◓◖y4▧▴ym▥▵1:▪◕]a◚◚!c◈▩:u◈▻eh◗▭^m◊▤^x▸◜pp◃▤+0◉◝lm◎◅<m◗◛v1◛◊@-▽◜t6◐◌zk▭▪ch►◒[(▿◄13▢▣7}◍▤.~▧◇*w◘◐@#▮◘r5◝▲r$◜◖5^◗◕,y▻◇-y▪▻./◓▪#9▯▪pr◃◝6b▲□f+◜▨zz●◓#=►▢2d▧◊4c◖◇<u◎◎4{◎▶i3▴◗-/◑▵1y◌▱&1▣▬b ▢ 0x△◛<:◙◈c!▭◂1e◜▤&2●▧ze◖◊l}▼▷83▾□-0■◕9s▰◃1w◀▫ar○●m=■●65▩▱#]◁▭*b▰▾_n◐◚?f◛◅(b►▶q5▪◌1{▩◈}<△▰r[◗▪o3▩◉# ◀ qr▼▸~5◆▴b^◖◀uv▷▮i<◃▵=5◜▭<[◙▻bg▹◚s{◕◁*r◌▧1&▫□()◊▨?=■▹ua◌◅ku◐▿-#◖◄6_◚◑hd◁◐z=▣◝m ◓ c+▲▻#e▰◜.{▣◈&r■◐bv◓●qa▥◄<<◖▨+]◚◛7#◄◝<]▵▴@h◊◃v(◛■#a▻◝m9▾▪<z▣▦or◌◛t0◐◎:8▭▫e3◉◚:m▩◅ul◜▯(=◊◝p3▥●}$◃▫9%▼◃fa◑▦}(►◁-z○◗r*▪▸+}◀◁~2◑◚sv▨▤a,◃◀$)▨◄b/▽◙j.◐◀.)◙◖zo◘◊q-◕▦=8◃◙[:◚△c<▴▬]^◑◀_^◉◙s#▽▵},◀▣57▰◚{!◛□f%□▥[n▸◄$6▣▶)(▣◗h,○▦v6▦▭{*▹◆@$◓■= ▰ 7b▿▲w,◇◇[b◜▫8a◗▻71◚■qo◍◊/n◒▩ p □4.▽▴,d◌▿q ○ yf◒◜_6▧▤k1◒▧8{▬◎?3▢△&=◘▻,6△▪qk▥◂ge▪◀?z△▩un▽◝ty▷◀]/▧◃d?▴◈t]■◜>p◖◚fc◘●n>▲▭sb◕◉2&◎▬a0▸▬?/◚▿d,▱◖qm◐▥<.◖▭4(▪▹$,◄▻s(◜◑90▱◄5a▣◛=6◓▢z{▽◔sh▿▼sq◜◔w-◝◄]]◄▿_v▧▯45◒◅}8▵◕2h◂◝sy◅◒o=◆▢g>▶▹6:◗▮-=▽▰-,▻▣k ▷ 75▲◜b3▹◌lf▯◗p:▭◇-j▢◓(/▧▰su▻▤q}◁◕uo◌◆9&■▦(g▨►jc■△mn◔▨ui◄▰y7△▲[i■►=s▵◛pk▬◗w5▷▣{y◜◈=a◘◃@q◗◜)o■▩r3▯▾3^◇◔hm◅▽=&◎◆ww◌□p5▴◐8z◗◂46▶◌tv▣▣8t◆◀7i▤◕x!◝▸uz▾▮cv▩▯o8▵● _ ▬)$◎◝dh◇△og◍►0h▫◕fo▪▴f!▴►}6◛◁s!▲►fx▶◐d.◚◇ 5 ◆1k▪◖ 9 ◛a.○▪y!▱◗%}◈◁,9▯◊xp○□g_◆◍$z◌◌ib◐◉u3▥◃z$◑◃qw△▬.}▦▣jw◆◒%@▾▷p.▲◖)i◈◚w.●◌[j▼◑mv▧◂e(▧▨9j▬◙3w▬◈k%▩◃:n▼▮xx▰◓zg▬▱!s▫▤%-◘◄=e◍▶-@◂▸_)▻◘pn□▨nj▢▧6j▹▴3l◈◄@p▶◚a[▨◐@g◅▨yq▪■ah▻◜%.◒▯xo◌▨uq◙◊>z▨◃ut▤△/+◌◚j&◅▭{-◕○fp◁▲=i◑▪z*▴◊%_◒▼rn▭▴cy◕◙]j▸▱ : ▣m3▢▯}.▸◛8_◝◇ab●▦e^◎◈wl▲▶&[▲▧#u▯◃1d◉▸%j◓▮[#◁■rs◝◌$p△▷.m●▻n<▨▥v4◓◃_.▩▻k:◎▥).◜◝9/◃◘(t▮◖h6▴▩s)◉▭h(▴▧=}▫▶ew◊◍>1▸◉2g▣◉r0□◛8h▲▾:a▥◅4t◙►^#◇◊yp▥◌[ ▸ 4}◗▽4)▨△]k◐▱}r◗◗&&▮◉c8◕◚$7◆◗9k▪▢@t◐▤,u◙▶^]◌▵^-◎◌-:▹◃~6▶▽1<●►>e▴▰be▾▹:i◙▩+!▭◑r=▻◂c*◜□{i◑▴g5◂■~1◅◉34▭◖6<▱◊*t▴▭](►▬)/◓▦}7◃◑{^◇▽:c●▨@^◚◄n5◜▸/1◌►=@◛◑x8▢▭st▱○p<▨◓yt▪◈7&◍▰to◅◗ax◙▾ga◅◂9[■▢1b△▫a:◇▨im▻▨vr◔►ep▽◁:k▩◊*-▾◜>u◀△cf▮▶+3▴◀w?◙▬e{◀▨~[▪▦{#▨●#?▤◓8>▯▦l$▢◑}-▼■=r●▭!+►◛ss▪▿74▱▨3g▩◆#p▿◃~>▹▯o$◍▽r@◛▤=f◝◒,@◘◇b5◎▽t^▵◂~i◕▻fd◘○2%◇●>_▻◕n4◀▤h3◚▮e/◑◘8(◅▰5>◓△#w◄◄?>▴▦[^◝▶*1▣▾!*◍◜/_▲▽pb△▽q,◌◂<&◎◜)-◗◇k(▪▨e6◅▫#8▽▷ r ◒)p▮◄y>▧◛d0◀◌2x▭▬!7▢◙$s▰□eb▩◑jv◇▱fh▫▩8o▽◅}j▸▹=%▥◝y8◚▻1s◎■2z▾▣l]►◔32▧◕e#◙◄=<■◉_s▷▪v ▥ l ◐ j8◑▫he○▭5<▤◊1-◎◃9(▶▵*2◌◈n$◀◄q3◕■l?▱◝w~◉◌c5▨▿- ▫ @(▩▧a2◝◑%+◌▮(3▰▱_{●◎u}▸◀<n◃□hj◍◘~q◂▫/%▹▭x3▨▴{4▢▸/.◜◎b$○◐9t◃●(1●◁/v▤◖y%◚◊k7◚▤?#▩▬o?▸◇x)◙▴h<◒■2~▨▻q*◚◔.!▵▱84◔▩ig▩◂9,▼◂m<▧◗^v▫◘]&▸◍ h ►z]◒◔: ▣ r6▵◜hc▭▭_f◁▷*q◀▹a5◓▨ec○▻49▮◕r+□◑<h△▥u?◛○(f▽◃d]▥△4x◀◛fy■▭j/▯▶31◂►r#◉○t+◛▮hg◒▦{ ◔ kl◂□fg◗◁y_◇■m%▱◛ru▧■?l▾◑.u▽◛j~▯○&<◁▨pw▸◅nd◃◚fj▴◔/:◙▹[d▷▤9a▢◚&a▽△9=◚◌r>▬▵4~▯▮bh○◎p}◌▪(+▦▢~=▸▥]<◔▥)n▤▥ue◃▧25▬▷{c▫▷~d●◔}h◀▮4k○◆@u◑▰4l▻▫66△◒%3◇▷s8▫◈o2◛◌~v▨◚<?▥▷mq►▰?v◜◀eu▸◌]!◒►=l►▣/3◈■}>◅◐5i▯◍<f◗◎f*◂◂+ ▮ [%○■]z▮◂bc▷▵3n▹□4r◇▥51◜▲ag◘◝f)▣▸cb◐▯^0◓◁!n◂▰c7◚◐*,◔◔ls◚◎7-◉◖nc◙◛5y◃◉/y▤□c&◔▮x5▾◔c[▽▮^h▮◁-3◒▨hy◚▨h=▫▴7*◍◑}9▬▫*[◁▢@]◅▪]@△▹$g▣▤~p◇□+,▣◂~^▫▲iz▫◐nv▭◙^n◙▪ju▼▽vk◛◆w)▯▿v}△◂p&◂▾fq◗▷=~◉▩<7▭◜+9▹◂v_▥▰8n◖◍+e▴▷w_◘◅4+▢●1j▦◘(e▢▤bl◜◘]~▾▵_r◓◙#:◃◛09▸▣(.■◚-&◁▽{}▱◘,:◚◕b2■◝t5▩▢w:◗◍^%▫◚<*◊▾=-►▼]:▤◉/a◗◃-n◚▬#}▤►l&◒◉j}▲◘b[▤▱jp▩▭::◌◖7?▮◎j_◊►~_▵▰ov◑◂hf◆◔.f▨▢a^◕▰{)○◄d+▱△=v◛▼/6▴▨3,▼◚-4▹◍ph◑●io▴△m+▬◆wu□▩z_▼◈r!◃◐6[▴▯%y◔◈y<▽▱-q▾◗y-◎▮x+▴◌na▱◃.s▦◝gz▥▲.2▢◍hz◆▨g!○▾yv◒◃4m◝◖>)◉◅6t▫▻$w◁◊-*◆◃1^◑▧5=◌▸dm▮■s,▷▼>3◇◝5o▭▤rf◛►^e□▢)#◑◐d9►◑l=▬■ef▩▪y}●◉%^▨▽lr►▷>*▢▢e]◍◈hx▹◇wy◅◌+1▰◇$%▩▴7m▣◑p#◆◂? ◍ jn◚◆oq▾▿f}▭◓p(►△%e▹▻>c▭▶]e◘▪m$▪▫x.▽◇=+▪◃_5◔◙ix◊□n6◈▨9#◌◕w[◙▼3m►◙59◑▻+5◑▼@6△◇@4▲▢[3◍◛x?▾◝l9▱▶yw◎▰?$◚◃br◀◗}t◀◘+_▲▣:{▵▮jf▪○pc◄▼ k ▷g[▩◝. ▧ w$▻◈@)▤▻8}◊◔%8▸◔vc◚◍k.▿◙-_■■d:◔▴+[◝◝[<△◑v$►◂h>◆▣7k▼▻q^▥▨@ ◇ 5q◍◐]}◙◂vt□◒=g◘▣6!◊◉(p◂▯ee▴◛bp▬◂w1○◍p+◌◜1#▰▸k]▵▻&5◊▿:r▰◎w^▼□nn■◈3>◆■{x▯▸?}△▸ex◙◌(i◄◒8]◙◐8$▸◈b7◗◅/f◌▩wi◌◀{k◁◄4=▰●@c►▮ln▢▮.p◔○=[●▷ [ ▸m#◓▲a]▵◊!h▦◉{@◓◚ij◙◜q#◈▢[.◃▽(v▧▸5f■▸5/▬▽)*◆□1l◓▩++▹▨6y△◔x@▮◅4@▷▸:j◈◔)9▽▶&?○▤8q▿◁4&◑▭[!▾○w*▸▧^o▥▣)@▵▶s0◈◉i&▱◈?2▭◒27◅◓.*▫◎sr▲◄n&◂▨v=◝◐ys◁◎<{◚▾po▽▣^w◕▣vi◇▮9i▦▪u]◊▦ml◗◑b>▵▹qt◘▧2y▸◐g6◍◇3:▾◕#)◑▥)4▽◓e!▦▷0c▪◁ub▸◎ + ▮[z▦▻5_△◝5%▬▩r<◐▨[v◁◍~t▰◔*3▲▼:/◒▸,1▮▹ u ▨tg●▤&t◘◗q?◆▯v&◄▷&o▶▥*9▾►-(●◃d%■◂3?▤▣ . ▧d4●◚qh◛◄*$◝◜lj▻◆-.◓◑u*▨◎@j▲◑)<▸▢3f▩◐t,△▤k[▪◝vx◍▿+<◎▨hp▶◍(*▧◀6i◒◛_2▦◄!k◌▽rw◎◔h0◚▥(}◁▪rh◓◓0u◂○f[◉▵][▯◎d-◖▼+&▵◒<$◙◆!1▹◗jx◇▩,f◄◁8+▲◌!)■▿/<▾▧2$▼▢zy▸◁mu◀□~g◛◐w>◁◔fl▴◂3y▱▣yc▴▻6x▼▿eg▣◖!>◒▷jy▾▢f5▲▮jg▶◜%{◝◅^,▷◒e&▽▤/>▭●8m▦◀70◇▵tr◚◓2 ▤ 3]▶◆!o▦◛j6▢▲:p◖▽q)◄▩(q▫◒:^▪◜a>◔▣-m▵◓]8▣◚:y▻▽.q▵○a8▣◀t.◎◍uy◐▼7o▻◛[-□◗x7▫◂1t▧▪rd◆◈q9◘▦vg◔◑~<◅▼,<◆◇&u◎●=y▼▨[7▷□#c◝◛j=◒◈6=◇▹>i▭◝-5◂▵>[◔▦[~◙◒2n◉▢<+◛▢i)▭◆~c□◅ct◈▮6,▧◒@d◚◂c/▫◍lz●◝}@▹◁5*◁◗vq▿▪a{▾▲+l◘▴$e▶◖l!◊▸0~▫◀.@◙◝gc◕▸i]◑►(]◄◗zi▥▶)~▷◐-u▾◁iy◅▣3b◜△[m▷▱.w▶◊2[▰◗o5▵◈01◅◃zd▴□^c◗▧w@▯□l:▶◄=0▩▷qf◈◑j*◔◀e}◜►^ ◌  = ▰$i▢◕m~◔◝vh◌◝60▬▨)y◛◙?5▶○h8▽◕v,◖◌}e▴◚:l◙▵i.▶▸g1▿▥h{◆▮=.▭■vl◐◒/&◛◛m(◒◗7z◃◃6w◀▸ z ▿#m▣◘[y◓▭%6▻▹55▲▯d*◍▩~y▬▭%9◌◇v-○▼2m◛◎fr▨◂kn▬□+~▴◍*_◆►9e▼◄)q▲◀>d▼◖%4▸□ea▱▱k^◚▸q_◚▯+x◃▼zh▶▻{l◅◙[o●◅%0▴◜!^◀◂[>◗△qy▸▽.d◍◝hw◉◓ n ◁3~◛◃*d▿▯%k◓▫#{◊▬fi▼▰3#▹▹}q▽◉gs▧▢/9▿▾m)◎▹*v◄▾! ◙ )h▨▾le◊▣dt◅◖9-▨◙9m▬◐g=◍▸n-◔△/g■◆1(◜◒ox◐▭>5▯◉19◃▷(>◝◊&v◇◓/]▧▮2@▧▲e,▸◗(5◊▲~z▥▩_4▨◝v0▦◃-?▬◓n8◕▿5!▬◝pa▦◓,+▽▨tk◓○h$▧◈@}◅▲zt◜▼]9▤▩q]▻◁(6◃◄7s▲▥8j◜▵ei▽◖{%▽▪?4●◀4^▾▸&4◜▮9?●▢a9▼▥1r◐▮%/▿◑b4▿▻bd◉◈a~◂◕@i▣□ll▱◜._◁▤t ◈ _+▥■rq▰▽1/◔▸sg◅▩~!▦◙,e▦▧t}▯►lh◙◘_3◜▧=n□▧9)▲◇m7◀▶>}◜▩l%◁▩lg◀◔pl◜▽.t■▴1a◔◉oe▼◗6{◑▽>j◌▭37◊▹<@◒▭y ◃ %(◖◜h4◇▫]0◈▭,x▴▽f(●▰pu▻□54◀◉3u□▵y^◘◚fw◖▮-<◉□z>◎▷dy▱▷*f▼◙x0○▷14○▰vd◂◍4*◕▵22▱▹6v◌▼l4◜▾5z▼◝w]▷▴ip▤▦[}▪◎u(►◀c:▿▵el●▬u_▴◓>-◄◌j-◕◜q$◐◜(n◗●d[▸◊3t▭▧gn▩▲g@◖▷{d◜■y:◅▶?9▯◓v.◗▱3%◓▱-9△▦p$◗◙$(◈▧$-▰▪h^▲▷~#▮▲d5▵△om▫○f]◂●&n●○!w▧▫5 ◆ gt◖□?(▻▻j,□□9!◕▶k/▸▦lt◉◁if◁▱&)▰▶up▻◉@,▦◁w4◅◊p>◘▱&,◉◉bq◖◎q!◑▾i}▻■e.◂◒7p▭◄p~▱▪g-◆◓1!▲△zw◎◒vj□◙l-▣▯ x ◝a)◑◊~k►◘jb▢◉_#▮◓^>▨▨,^◘◈4e◐◝qq◉▤#6◅▮v@◖▫2w◓◍g:▷▹.g◂▽ot▭◐!=◆◐}g△●>#●▪9b◊◘u#◅▥f ▴ gu◇◗bw◓◔^/◛▹r8◓▴c ▭ m/□◄lx◆▵{&▷○u2◎◕& ◜ ~j◝▻9@▣◙_a▫▹xg▱◀7$▣◎si◑◒je▯▷,7▿□cz▨▷#-◊◊$1◜●8u◙◓^<■◎0^◘▾>t□◐f$◍△+?▯◇[g◕▧+s◝▴r_▢◅=d◒◐ii▶◒u=▢◆ks▾▦#,▵▦:9▢◐e>►▹go◓◌0y◝▭i7□▽gw▼◛xr◎◘{n◑◌gk◝■-g◓▸rv▢▨_b▪▤}c◎►e~◌●h7▬▪ i ▼8-▲●:g▨◌]l◝◗d<◖▾^@▦►6l▥◘}x◈◐*%◎▿e0◎◙0p▽◒47◙●-d■◇<i◉◄k_▲○36▻◗58▻▮h&◘▶am□◊!u◘▢2v▩►a%◄◃[[▿▱%7▧◆k+□◉sf◍▥9y▩▨!/◈○et△◍,,◁▾ < ◎41▰▧zu◓▾o7▷▨eo▩□/2◔◌*u■▱b:▴◕97◛●ld▢▹e1◔▶os▫◉by▶▦h2◇◆)k◂◛(9◙▤s[▼▯8c▼◌#k▾◊-~▹●),◔▬>9▦◜zj◈▦*y◈◂=7▲▹1h◒◚me▩○xc▹▣kd▸►$b◖▦j!▾◉7<►◌i5◄■3c◔▱n}◈▼3_◛▶av▻▸h)▭▥0m▹◅{9◑◛]{◊◚m!▥◖2q▥◁w/▱▴0a▷▷]_▤◚.a◘◆mm▴◆!?▸◝$~◃▬u{▲▵h-▿◊-h◘◕mi▷◗*j◔▢9g◉◕0f◂◃e4▬◚ae◅△*>▹◄yk▮▧l8▪◔,)○▫n.▸▼y&▲▩>a▹▽_e▧◅&m◁◇c%▽▻tu▿▭u$▷◃_/◝□wz▭△1]◖▢wj◇◁(l▸◃2f▲◛$@▹◛r ◒ <p◛◂5$◐▦21◇◜2j◑▬< ◎ 9o▾◓e)△▧,g●▽>y▮◑(#▥◍6d▨▣?]▹▾@!▹▷*]▲◅0g◅○}[▪▽:3◄◚.3◘▯x4▭▽wb▰▭[x◇▤jk◜▰z-◈►:,◊◛_x◇▻:+○◘4:◝▫_,◇▪pe▱▮iv▰▴7t◐►r)►○pg◐◊?c►▫ff◓◘1>◛▵<4▤■/*○◌.c▨◑u0▽◄+*◂◜&(◀◙f/□▰:%◎▼-f▱◙72▫◓{z►▪3k◄◘b0▮◜&s●◂g,▸▰%u◃▶@y◘◙,t▷▬(j◗▯3j▩◔/k◔◎c,▷◊ 4 ▽*8▧▿}!◁▰}f▹▢4[◎◖6>◀■w}▩◄!~▯▹-a▦▫i+◚▧38▰◂.j◊◕o^▧◚$/▾▼gx□▯}s▼◒7 ■ &y▥◀-p▪▶,/▦◊y.●◊@9●◍4s○◒f_◆▾uk▾◍hk▫▧yg▾▭@s◜▷}y▮◇zv▫◌=(◊▼u^▷▿}^►◖b<▪◓{u◔◅n[◁▫n(▶▧6g◛▪q8◎▻!i▯▲8&▱▬e9◜◉^4◘■ra▣▧.i◐▧x>●▫,o▷◁{8▷◆m>○▲%l◑◆.y▦◚fz◇▧&-▲◕x#◜◐zm◌◔4j▨◈wh◘▵5w▤▯q/▷▭7l▶■_w▱◒uu▦▯^t▣▨]t▴◁p%▭◎x1◑▢d}◐▩#h◊◇w8▦▥9w▵▸@~◊◜q:◌▹j5◍◎o1◑◑m5◜◇x[▲◈0*◁◌e*▮▿t#▣◕sa▥○(0◕▾*}▭▣gg○▩:d▬◃cm○▮7.▴▶03▱◓s<▫▼xq◜◂u ▨ rm▤◃l<◊▪?{◀▴:[▼▫>/◇◂#s◇◑6a▶▼@x◚▼f1▲▱sd◓◉6o▰▨94◆△6(▪◇24◛▭~0▰◛<=▸▲_8▮▬9c○▥ d ▱t-◛▬0d●▯=9▷◜{[▨◜s ▦ z0◘◒rk◒◎.$◝▿a(▣◁*&▾◂h[◁◂~l◀◐z6▼●$5▫▨,.△▱}%●▿co◔▲#$◎▢=?■◓3v▭▹5m◈▱$3◈◅}p▥▼u7◌▥%f▯◙>?◐▫d#▭○~@◁●_g◚◖#r◊◑q<▧▻s4●▶zs◇◐/m▿▽+d◊◐&g◇▿k#◍●2s○▢1c▩▽u-◖▣#4▹◈{6◖▥07▴▣0i▩◘%p▪▧7a◎□/8○▹p1◍◔6c▭▲q.◉◀7!◄▸m*▬◄?6▢◎%)◜▱t*◗■/i▨▭u@◀►^_◒▥!t▸■{0◖△9$◃◅#/▶◓7%▪▵]>▭◁n:◎▭*0◈◍{t◁▸}}◄◀s+▥▴@r●◒n9◅◅%c◈◊#7►▽3d◎○l1▿◌((▨◖~m▷◖/-◕◌ik◎◑_1▩▾m}◂◌,(◒▢jm●■^:◆○{]◆◁tl▵▪91◔▿+b▰◒fm▻▶7~▸▤!:◕◃w%◁▴xb▸●]2◈◘a<▶▩!%►▤(z◇◎tx◄►^g◉▬.]◉▣z+◐◃mb◀◚p!◆▫ja◆▸&d■▮_q▼▬)e▥◜^d▧◙z ▿ [e◔▼ce◈◖${●◇tn▿△.8▥◈~4▻◅}#◍▪p]▵◔8v▼◕{?▯▢6@▬▬)a◍◍y9◕▨2r◍◓rb▷▥rx◖◈z(◑◅6 ◚ it▸◖/e▧▣j+▤◜:h▷▻t$◘◘ro▣◜6#◓▻,%▪▾j(◑▹xy▣▢#t◔◘v3▶▯k$▩◀[+▱▲67▹▸26◉▻!v◆◄aw■▷+8▶►c}◒◖cj◀▦sz▽▲,m▱□&3◕△t/▹◙*<▸▶<~▵▣:~◓◕1[▼▣v!◗◉,5◐▢]n▣△%2▪◉d>◖▤b*◉▯s5◙○h}▣◒/h◑◎5t▣◃?y▿▴.>◂◓(w◍◃t&▰◙[u○◜l{◇◖&c▬►^&◗► e ◄$f▷▯b&◝◆md▸▾ka●▾]i▶◙op◌◗kk■◊#y▻◒xf◍◀dd▩▥)%►▴ v ▥5:◍▴k4▵◗/u▬▲p8▾▫[q■▬l/◛▰(y▽◀&#◕▷vp◅◎d_◈▴rr◒◍n~▭◀?7◕◊au▸◘2l□►bi▫◃a4◔▹?<◛▨y]◕▬?m▻◎u/▧►,h▮◔5c▰▫o~▽◈_!▽▢mj▾△#b▯◝b8▹◜u!◓□gb▭▱np▮▫]+◐▸?@◅▢.[▥►c2▰▣qb◈◈t!▬◁]o▵◝p?◙▮!r◑◕@z△△2^▧□m{◊▢m^◙◚kv◄◙uw▯◜<0▶▭t?◝▷~?■▪v5◀◈3p▨▧i_▢■9n■◖t4◔◁>&■◘}i▦◖=_▾◅#v◉◜04▽▹n^◀◀/=▾◐~)◁◆2)▷◎k>◅▦/ △ ne◝▹@o▪□f=◈◕50▬▶5l◆▹/{●▸(x◎◂&j▸▸@+▬▧cw◚▢}*▶▿k8◉◒gh▿○/#◓▿:>◒▶+w▭◔oo◊▵<#▿▬:f▻▥)6◁◅?_▿◅-8▬◀ ? ◍7x▣○ta▵◙{5○▸])◐◍l>▤◇/l○◀:)▵◀r}◗▸^)◄◎ji▮◍6?◕◖=w▼◔x:◑▶a_▷▶nh◓▣#q◒◓n+▵□wk▰◑1u▻▾p*▥▫6s◍▯<9◃▥j@▫△4]▤▾56▯◐_d▨▮f,◝◚7r▧▦gi△▣lp◖▯g9▢◝^9◍▲g*▭▿!,▼◊($□▣3&◅►9u▱●n3◝▮9r◂◐s3◑◝?a○◂ f ▴vz◛◕~b▮◗?s◊◈*!◅◔}o◃►>^◔▯m.◍▵il◁▻b@▸◂&7▭▾2k▤▵re◘◖#x◈◀g}▮◊78▦▶_(◘▿xd◔●s_◄◂:*◘▸+-▪▯o-◙▷6f◌▫l5▵▢va▼▶o@◀●j)▷◕jd△◓7n▸◕li◜▬~a▰◐7w◁◒~,◉◔b)▿◓_@◓◈ 1 ◘v~◜◛hh◂◉c=◑▯e[◆▽2p▵▩kz▯▧>f△◀yo◂▶mx◑◖i(▵▲b-◄▲x]▻◑5]◃◒^f▪▣{o▼▤:}■▰lo▵▽4/▮▢#&▮○mr▧▾ux◄▵p7◊◎y$▾■.&◄▯8k●▩q~◈◙id◜◌d@▤▭#d◂▦:=▵▵0$◘▽g{◆▤x*▤◄=c◐▴h@◕◓f^◔◍t9◍◙8w■▣]w◘◑q6▤◛ m ◓8,▼▦v{▱▫&q◛◖(o◅▾#2▥▢@{▿▧+$◘▩m-◝▥/z▸◚(4◑▿=2◍▱?b◒▲!5▻▱s&◍▾pv▱◉8 ▯ n%▪▭&f▾◎~$▯◘cl◜○*c◌◐0q◐◔p/▨■*k◀◎r~▥◕)0◓◄0w◙△53▦◔ni◈▸ ^ ◌um◆◚$2△◕@/◈◜5p◁◑h1▸▻+j▦◆so▻◃+k▽◂h?▤◐[k□▸.^▯◂u%◉▶l)◉◃xm◄◈x^▦▬xu▬△7d◃△w{▶◎<k▾▨}/△◊y/▫◅sk▻▪q7▩◇+u◕◑*z◈●4$◄◇1p◒▿*4△◚!9▾▴gl►▻g4◉◎,_◒□z!▽◚ki◅◑8x▾◛ej▧▵/b◓▬@n◃▩~f◀◜,$◂▴r{◉◆c^▥▧n/○◁/w◝◕~s◎◛}l▨▶ - ▫dk◝►>4◃◗!j◔◆wd▪◑0r◊◖>:◝◃r,◕▱s9▣◍+)▭▸}]▾◃n?◈▤wr▦◐j#▨▲@<◄▧:$◍▣{$▪▱ug◆▰>{◍▭jr◀◇?n▸▯od◓◜&+◚▲_]►◓gp▹◐*)▷◝~]□◍^s◈▵mg▰▵93◊◄#f◆▿u+▥▽/r◒▣^~◈▯?r◌▶4o◛◓80▩◗s1◚▫k!◒▾9}▻▿nt▢◈{2▤◈3s▷◔)=▤◍k9▰◕o ▶ th◌▷iq▭◚o)◈▲ a ◕1~◖◗>k◕◝dg◘◎4i◄○$>▿►w&◝▦}u◁◖3o△▿8^◀○l[◉▪d(◀▷}a◅◜ts◗▤h~▧◍33◙▣=$◔▾y0▢▻lq▹◊4<▫▭j[◘▭uh■◌s2▪▩,l▣▥df◎◊6&◓◗qv◗◆nm○▽<o○►*a◑▩^[○◃ir◔◗*x▱▿qj▯▫h5▬◍fb◒▮?)▼◀-)▩▿r4▫▱6h○◖=b◔◊/x▷▢rl△◉n]▱◑,c■▫y)▽◑:.▥▹#+◖▪l+□△4q▬◅-[▪◒kw◉▦}{▦◌tp◐◆ # ◀[6◐◑+h◖▲}n◜◚v<▵◍<a▫◁bk▹◕%q▤▧</▪▥i^▹▬ve▢◁y(▦◒,3◚▵g ◑ qp▴▿10▹◔{~▢○5{▥▾5d◗▴>.▾◄w!◇▸a=◄▣9_◃◌yz△◙?k◝▱(s▲◉xw◘◁cc▾▱$<◙◗,k◆◌<c○◛@w●◖]h◌▯j2▥▸a$◗◘!l▮▤j>◔▪yu▿◂ 8 ▯mk□▭3(▧△5b▮▨px◓▶_&◄▮ds◃○&>◄◜~*▹◒s$◔◛~-◄◆la▦◍73▩▵yn◃▢n=○◙l@▧◄kc▬▯0!●◈oj◎▸w7▨◇7@▶◛{7▹▤o>▨▱%$●▴^^▻▴{j▰◁c{◕◔yx◄▤o!▫■x~▯◛g^▯◕a}□▾2+▮▵ } ▻>2▿◛)]◙◉-+▤▸c.▷◚]6◔◓=,◉▿ko▬▹9<◂◖)&◕◕.,▨▰)}▢◒g%▷▽bu◈◓3-◗▾s.◉▹8e◇▦!8▢◀4 ▽ h]◊▰}4▲◃<e▫◗gd◗▣q=▦◎in◅◈*:◎▦#~▬◊d)▰▮o+◇◚$9▤◌{h◕◐2<◒◇o<▢◜2:◊▩=m◇▬):◆▻t)◓◎zp◆◉_$▭◗<_◅▱+#□◕o/▱◎kr▰◄vf◙▦%*◝▢cr◔◃&i▩▰(8▯◖#3■▼,*◐◕/5□◖]$◑◗g?◎◐@l◆◎wm◝▧ac▱▢!6△◆!g◌◑n,▣▴-k◚▱#(◕●#<□◚-{▯◆ q ○##▴◉(%●◆ur◂▼(u■▧<,▴◒o.◙◑9l▧▶i ▼ l0◚□hi◌◉[2▰▩:@◕□lv◙▲z2◝●[&▧▱0+◌◙9*▶◃l7▨▪7j►◉{=◙◔r7◁▵7>◁▥oi▿▩ba▼◉m0▲▤m1◁▿,0▻◙^y○▵ad▩◎jo◜◜h!▣◊@%◍■hl◀◑&~●◑?!▧◜p6▦▴:b▰▼p9▿◍0(◃▿ud▽▫?[□▫6]◗▨[)◗◐77△▾mo▲◒n7◃▮/d▷◈(^◌◄3i▽◘z~▸○j<▭▷w3◊◗*~▽▬dx◅□1z▲◗*l◈▫0_◊◌4,◐◛0:□▤>,◜▹})▥◐q1▩●1=▴▮7h▮▸f7▹◀nk◒▪0j◐◘{f▿▢)m▸◙]%▬▰d!◂▤1v▲▰mf▩◓es◓▥6-▦▦a!◎◁:?▤▲,z◂▲[w◍▦$&▫▰d6▸△/p◗◊<2▩▶0>◐▷[s▱◇e+◃▨%d◂◊,>▣▫23▾◚tz▷△c_◃▭/~◆◝uc▸▭v?◁◁o9◖◕1+◐●&w▦△t@●◙^2●◗[1○▿oz▢▰ b ▢ed□◇7c▫▬.=▹■{.■◙:&◚◜{r▹▮e8◚◅$$◅▻]y◖►>]◛▷&8◉▱?+◒▫@?▢►.?▵◅%<○▶{s△◈$l△▶2{►►} ▻ i#□◔(m▯◅<x▶◝kh▦◅fk■◑^5▿▰c>◒▤6k▮◌@v▨▯hs◀◝<!▹▰]5▾◙i8▷●?d◃▣@b▽▸nx▤▰d8◕◈tb▬▥^k▲◎5@□◎2-◅◁44▿◚di◝◁>7▤▷){◐▾n0◒◘q+▸▩<v◙▸6^◁▶96◂◀(2▮▱sm◅▸+{◝▨wg▼◜/o◅■t_◂▱$?◐◇o:◃◕c4▥◒xh▵◑6/▧◎2}▴▹w0▵◘i*▪◂cu□▹,[◆◑_p◓◅28◊○=>◅▿-r◐◖$.●● t ◈s6▣▼=1◄▴2*▲▪q@▶△dr◛◗^i◊◂u1◈△ & ◜3+▬◕p_▩◁,r▫▢%t▫◖>>◇◀:-▫◑z<△○t%▼▴4!◚◝$v◕▪08▥▦ke◈▿du◝◓/t■▨2=■○~7▿◈da▭◕:o◃▸tj◘◍ey▶▬qn◆◛.-◙◇4w▱◌5k□◌=4◚▽8f◄▢2o▿◘{m▤◑ ( ◗8!▦▮ho◘▮2c►▿>v▮▽z)◆▱7_▷▰^7▦◇fv▴■z3◓▧oh▴▸p0◆◕],◀▬za◘◔9q◌◊+p▧◐h_◇◍tc▻◊&%◚◙k)◂◇y6◁□m4◂◅5h▲◙4u◇▾rp▷▩{p▵◚j]◝▰,2◗◈:q▻◄<>◘▨mz◝○&{◁◓w ▩ an▼▹]q◍▬_z▵◄jh▭▻<-▶▣6q◜◕i[□◓bz■◀ng▿◔~:●◕x&■◃={▧◓~.◛▯*o◁◜$m□●w<▧▽~8◔▫<3◖◉hn▿▨0<◁▯&9□◝v:◕▥k{◐▣l^▬◖2_▽▿do△◌/4◆▦$h◓◒%=◚○v]◃◜7f◔■d2►□n!◍◌8%▧▹#[▦▼t{◘▹(a◄◊^a■◒+a▴▲!y△□_y▬◇u9▴◃.n◄▪/,▧▷(,◙▫$k▵▤!$▼▧^3▴◄/(▾◖')
    _to_english = str('►▨%m◕◂(d◖◝q&◓▯2e▦◗>m▽◍30▾▬b9◌▰@&◙◍=/▤◙[9▧▥v>▵ % ▧◘m:▶◀5.◛▾&*◄▭k~◐▶v9◐■)z◉◊u[◃◊?u▥◉er◍◚de◓◇&0▣■rc◂▬wp▭◊=)○◔:0◄▫:#◗▢<b▩◒?q▾▽=:▯▣}3▿▮98▱▦@7►◎ry◀▵i>◝◍d{▰◍7e◓◐4_▮□>8◅●z#▣◆)s◕▤m?◜◆x%◔▵_i◘▤sj▹▿2>◎◚1f◗▩_u▢▷_9◐◂cn▬▸@0▼▼a3●◄*=◅◍?^▥▭@:◕▭c#◊ ~ ◛◒g]▣◓kx▪▮&x◂◈o(▿▹(~◌◍?&▤▹g+▰■6~◖▬29◊▭$=◜▦p)►▸8*▤◒i1▥◎{:◓◛p-▻▢0[◓►5&▬▾x$▭▨aj◓◊t~▷◂9z◛◈f8▣▻u.◌▲z4◄◕g$▫▪l_◎▱[,▫◜m_△◖.r▣▪].◚▶)l◓▵*.◙▰ia◚◈e=◘▼1@◀▾v[◑▨r9◁▮m8○◝b.◖●as▰▹s7◌▣o_◍◗}?◁△}1▫◊nf◛▸nr◁◛$8►▩ok▰◌xs▪▬4?◝▪n{◘▬86▭►+7◝◂+i△►4d◜▪d1◑◍}_◈▽s*▼◍kj●▥8?◒◑d$◚◗>x◀▻!f◆◜@a◍○>+◜◓!p◆▧2#◁◝f>▤▤a+◃▯>o◇▣l3▷◍vn▨○x=▱▾a6◇◄d=◕▮w+►▧qx◒○6e◛▲o*◛▦<(◑○!(◒▹&_▩◍}:◉▴6z▶▱(h◘△m,◀▩,!▯▰z5▷◓$q▿◇05▭▯6$◛ 9 ▯▤fe▧▭bm◙▧t=◒◊y+▫▦*h▤▫tt◔◚>=◈▬^u▱◂-e▼△!a▨▸:2▨▹3!◘◌wc▻▰?~◇◃n2▤◝o#◖▧))△▼kg◉►:5▷◇yr▨◉g~◃◓rj ◐ l▹○z8◐□hu▭◉g#▧◔<g◙□=q◒▬%b●◘gj◂▪5r▨▩d&◉◗2u◈◇b%◒◌tm◃◖?x◊▥s-◗◔*7▬▣(c▢▽.v◜◙@*◌◒@[◚●l*▴○d~▥▱]4◈◒1n■▽n@◐▹:x ● ]◜◅==▸▫(k◚▴6r◂▭$0▸▴l(▨◀>~▯■{w◁▣7+▶□>6◘◀u:▼▱$^▩◛0-◘◉b_◔◒e:◂▢_c◜◃is▭▵/[▽◊e?▣▵m@▮◀%,◃■v)◉△,i□○f{▮▷4%◈◆[t◔▧/?◀▯7^▶▰js▾▥.9▦▩88◖◒(@▮▯<y◄◔j1◈▪=*◍▫]1▧▬0% ◙ !◊■2?▧▼u4◑◁s/◁◃5x▴▱0t▦○y[▭□cx◜▻iw◂▧#l◜◗1)◕◅!{◙■4p►◊,b▯▨i$●▵0v▱▤ft▰◆o0◕◀)+◛◚bj◐◐&l◚▦f?▹▩-x▾◇z1▩◌3q◍◅_<▲◝!#■◛2a▦▿%&▪◘a-▱◚v^▣▿3)◃▲ol◂▥bn◂◚j?◔◂0l▽◎=]▲◔>h■▯oc◐▬~&◕▩$y▰◈*{▮●0)▰►u5▵▯17▧◉.b□◜db▨▦gf◁▦4z▤◆w=◘◜?p◄◉~w◈◎h#▹▫hr◁▧ai◒▰.0◍▮*?◃◎~u▴●b#▯◌dn◌▦[a◆▬.h◖◆/j▮◈02▨◗vu ◑ g◌▤12◖◓l#◗▦bo▱◐em◎▯^}▦□l.▩◖f#▬◌/s►◇sw ▶ o◊▮**▩▼7(◄ e ◇▴6)▻▯i6▥▪95◇◕.:▤▽xa◗◚[5►▥0?○▱1q▥▮mt▼◆$r◝▤nq▾▯_%◖○b{◔▤j4▣●3}◙▢ap▷◛&@▲◓<}▷◌f:◗ ( ◑▷3{▤○#%◍◄@k◓▹qs◛▻+:▹▶)u◕◆-w▼◓b,●▲a?▢▾}v▾●/7◇▢xj▹▪p=◁◚.o◎▲ci▶◔)!◅▷yb ▵ %▭◅6%▤▿!0◈▣>(▰▢%w▹◝u~◊▧!]◉◑__◗◓c]◜◊{v▶▤i@▬◛%s▻◖(?◝▣%o▻◐k3►◅*6◖◑8)◃▪@>▶◇>s◈◝9>▣▹zl▢▦t[▼○&h◁►lk▾◈f&▻△l2◒◆a*◊▯{,◆●[4◐○!-▧▩?%○▨+t◄▽=#▣▰:w▾▶*@▫▽5n■▲8b▶◉k<◑◉}+►▭x,▹▲g(◛◜8g▸▷+(◜◍<j▪▷_:▷◅y*▼►^!△◅t2▵►_m▽▯dc□▪)5◐▰39◔◖6}◇►ql ■ 7◂◗-!▷◑[/▥◙5+◜▶62◈◗9x▭◃d^▫▾=o◎◀?0◎▾7,▵◐~/▶◘z,□◂]?◆◖a/◕◒,-▱▩*+◄◖qu▾▰48▻◀=3▯▱%[▿▿9~◛◇]x◐◗!&◆◙-o▣▱2.▴◙o,▼▵82▯▬lw▢◄n_▼▲rz▮▣]7◚▣7]▥◓v2◈▾fn◑◄{1◃▴>l▴◘%:▥▬j7▱▵&.◑◙ek▻▵0.▨◆xn◍▨&e▦▽u>●▮.z▿▦2b▹▼7u▻▲=j◊◒xt◚▪j{◇▲b]▵▫wq▦▰)3▨◅?o○◉(&△◎pd◓▽us▸▮nb◑◓ky►◝y,△▯i!▪◄<q◘◛^+▵◌_o▰○&/▹◎7q►◐ms◌▢yi▪▼m[◐◄kp►◍k&◃◈o&▰▦:]▦◈4#◝◀v#▶▢u6◊▶bs◒▽x6◁◘{b◖▹i,▬▤_h◛▴/@◇▶{3▽○mc◆◊_>◂◔%?▷▫{(□▬3/▱▻c6◗▫)d▸◒)7◈□9^ ▹ )◂◆z.○◊y~▸▵8p◄◍)[□◘,a◖▿&!▯◒c9▢▬x<▪◛r1►▯*m◍◁vw▬ _ ▯◄20▭◛hv◖◁xe◗◒fu●◛6u▶▾>0▢▫.e▧◌z&▽◆kf►▱*s▶●w(◗▥nl▲◐@.▾ * ○◑k2▦▨(<▴▪_~◄□3<◆◘61◎▫3x◒◙$!▻▷p,▵◖8s◝▯oy◂△:_◃▦$j▯▵z@▧◑)w▴◅y@◆▥-6□▱@m▪◐qi◖■$#◎◉nw▽□dj◀◃o}▬◘#n▧●:7◀▲9d◗○d3▣▮az◀◊s>◁▹.+◇◈+f▲▬ly▣▽3.◌◁q[►◜,&▻●%>▱◁]v▦▸^1◌▬:<▰▤t:◊◁at▶▷6+▿▤v%◂▣ev◄▶r.▪▪]f◗▬<1▯◁^(▢◗y=◖▵k6▬◉zr▰△pz◁◀qc◕◄#i◛▽7{◌▾)j◃▱~~◑◈qg▽▽~9□▼~h◙◁)>▤▶)c◃◇4b◑△s~▩▹c(▮◃bx▿◜5g▴▢5(▽▥35◆◅ez◛◀7/▭◍r^▵◇g8◖◃,#►▲+@▥◔)g▹◓py◎◓o[△▮3[►◄,8▽►&b▣►s]◉▽79△▴sx►▦)?▷▦^r▪◅~(▰▯?j►▵+4▣▲zq◍◂)t◂◘e_◀▽_l◌◃c$▢□#0△▻vm▹△m]◂◁a&◚◁xk◊△p4▤▴7:◔◜99▪◊ws▷▧u,◎△^q▦◑r?▲▫42◄▦uj◍▢[=▮▦}d◉◛bf◙▱[]▮◛/^ ◚ 6◊▫1o▣◅f0▴▾v+▰▲f6▯◈@@▭▼u8▹◉r:▧▧dq◕◎=!◚◀o{▥□7v▽●f4▣◌!d◀◍?-▰▿64◀▿!_▸◑&6◕◗ns◀▭?g▭▩zb◁◙@e◁◉ri◗◄,?▯▯ht▷◙^$▥◆#5○◅v7◊◆-]▰▻mh▥▤>@◉◍-}▴▵[$► h ◒△+z◌◓%r▨▼mp ◔ {◕◍]p▽◐$]◑▮n)▣◐..◝▾>%▷▾:s▶◑s@▯▴{a◑▲?h◜▴_t►▾#j○◇{e▮►2,▲◊aq◖▱@2 ◂ 0▮▭!!▷▲!}◚►vy◝◙%% ▩ w▬●([◅ $ ●□al▻▧68▱▽#1▻▬[l▽▼3$►◃*i▥◚:v◝▼{>◔▰1_▾▾5#▮▾@5●▼i:◉▨i0▦▵}0▴▫1%▯▩h9◄◓43◓◀}z◔▻9{▢▴--▹▧?1◄▨f2◔◄.<▫▿+%▤◅=t◉▼ya▵▿g)◃▹k@▥▻wo▨◁g/▿◖!m◐▻m&◒▵wf◂◄^b▼◎pq◌▴%~▲◍5}▭▮f@►◚}w◚▰u)◙▿q%◍▧<8◜◄wx□▴6p○▣]=◃◔8# △ /◗□vv▫▵vb▻▼>r▭▰]r■▤:6▱■#*▻◍~o▶▴s}▹◖11▮▪9h▮▮]d▤▬sc◖▰jj△▨:4◈◃00▩▸ao◚◘.1▴◎~%▮◙b~▮△^6▬◜.k◕►e-▾▤:e◆▩xv▧◁7=◘►m6▿▶18▵▧f3◖ 3 ◍◖@_●◜e<△◁?e◎▣0k▼◅zc◂◑_-▢◊ca◍▻2!◕◛$+◉▲-b▥◊#@◅◚15◇◅f<◅▴{q◚▭k,▽■^p▪●]3▫▯+/▥◇jt◛▧k=▻○16◈▰i%◊◀@f▨◕52◖▴<w◇▰pt◙▥9+▶◁87▮◒+6□◆ie▮▻a1◓◂yj◅◇0=○▴u&▽▾[c◂◎<6◓◝kq◒◕e@◇◌<t▣◄r/ ▭ c▾◆i=▴◇l,◛▱x( ▦ s►◗1m◗▶$x◕ a ◄▬)1◊▴_7▬◒cp□◈3z◙◕>b◖◂[?◙◎=x■◗z7◛▩sp▢◘@=◍◒7y▮◝b(◔▽y2◃▻>w○▯g3◉◘tf◝◈.6►●1,▸◓o4▫►1$ ▲ j◗◝z/◐◓ih ◅ $▪◙[*◓▼3*▥◑bb◗◌on◁▬]u▴▼1g◂◙nz▶◅*#▪◚%5◑◔#o▻◔l6▩◙o]▱▰]-◂▷9]▲◚a#▦▤!z▨▫![▦▱&k▨◔{/◆◆#>▿▣!@▢◂+^▢◖<)◄◛r&▮▩_j◃◍c@◑▱0}◙▨=u▫●0]◚▷z[▱►k}▰◉b?△■sl◀◓*/◀▢$n◉◇&p▲ j ◂▮=h◕▯8=◆▲hb◎▪s=◒◂[f▢◛+o◄▱/$▵▷tq◛△(_◒◒1.▫◇$_▫◆.4◜◁&$▤◘]g◍◉8y◑▸@8◝▽sn◙▽%]◑▤k*■▻!4▻◌}k◕▲c0◂▻%g◒▴pf▾◌-1○◚5s▵◆3r▷◘#.▢▪8r▵◁iu▣▩0@▵▾,]▼▪{{▱▼#!▤▮km▴▤ay▦◂.x▨◒8<◎▧_[►◕j^▾▻ak◝ x ◙◙qz◃▾q(◎▵j3▫◙mw◝▬=^▹▦9v◌△b1◃◂,w◀◕ps◜▢se▻◓6*▯▥u<◃◆e$▽◌40▤▨><▢▥]m◍◕g&▿◐ny▴◝a@▭◈0/◄◑-2▹▥+.◛◔h/◘◓*p▯◔x}■◄g0◐◅ha◗▵e5▶◗%#▻▦+=◉◐cd▪▰kt▲▦i~▱◅[@▹◑5-▵▭#_○○2t□ p ◝◎+c◊▻i-◅◛~n►◈#z◉▥,}◘▥c)△▵*5▵◉+q◑□4g◗▲#g■◍hq▰▥v/▼▾q{▴◖y{▩▣_}▼◐~3▰◝d/◙▯7g▰▬i9▩▤yd▩▮&:◑◜({▰▰j9◜▣dp▿◕92◌○6m▰◅y#▭◌0,▯●n*▰▷8i◘ 1 ▱▧9.▥▥&^▢▼!b▢▶]b◎◗$u△◃6n◌◎1i◉▰dl▰◊?. ▪ >▢◔^j◘□}=▪◍e2● ] ◈◌8.▸▨i4□▻-t▿▷$4▫◄9f▬▻^=◝◉m2◒◝$c▬▦dw▲▿9:▯◚b}◕▢%!△◜*g□◁t8▯◀(:◉ , ▮◚6.◒▱?i◄△,p◕▴$*◐◁?w◒◀*^◖▸)x▩▫81▹▱yl△▢g.◚▹s^◉◂ob▪▲cg◕▼y?□■b!▥▿]s◈▹[r▵■pm▤●r2◑◇-$▩◜$}▹▵h*◛▫!<▤◂f-◄◐q4▱▥.l◐△#^◓▷rt▫▥{< ▤ 2◓◆}2▴▴c3▫◝x9◕◘<l▣◇j$▮▰-v□▦<^◊▱ma▫▮n1▱◆]#□◃s:□◀5,▶▲63◘▰l~▦▲%n◎▴p[◖◘k5□▲,q◔◕89▼◘2i▭◘ou◝△1x◉■t(◈◛~x▸◆^l◁▼h.▾◘!2◉▷h+◐▲aa◜▥~r◛◉w9◒◁)v▩◕jz▮◐ic◅▵[0◆▼f~◌◘%a◔▷c?▫▸^{◕▹7[◅◀.(◚◒/q▣◔0z◆▭0#◁○=p▷◉z^◘▲!.▤◎)8▪◗8d▽▦b=◉▫_k■▥p{▨◍+r▬◔&z▬◑4a▯▻*(△◐xi▼◁2]○◈my▿◀uf▼▩4-▲◁[p▬▿)^▩▦fs◚▩/)◒◄p^▲◂/0◇▼gy◀◒t3▵▥lb◆▶>g▣▷q2○△!x◀▧td▲▴5e◝▵s%▴▥t1▷◄<5◆▪o%◈▥7)▤▪0{◛◝pj◊●:z◇◉??▵▨5u▸▿(r▨□k-○▧wa▨▵,s◅◘3e◄●}m◇▯3@◒▻i?▰◖%i▽◗jq◊◅z?▿■kb◎◄,{▫◔%1▶▫2(◅◄$:●◐4>◙◃(7▿▫{g▶◕}&◌▻j%◅▯zn▬▢_*▫▫4f▫▣4n▿▸&]◐▽4v▪ > ◗▹te▽▭<%▤◁%h▩▩d7▶◈}b ◃ y▢▿zx▲▨%v◔◐+g◈▷3h▯◑[{◃▰c~▨◘+m◑▣w#►■,4▰◘.%▧○yy◘▫~}▻►xz▴◑qd▼◇t>▣▭>n◕▽,n◙◅3= ▾ *▤◀w2◚◉q>▢◇i/◀◆8@◍▼?t▿◉-c▦■/!▥◛^.▿◎4y□▿.7◁◈k0◀◖r-▲▸x-▿●8/▱ d ▪►85▪△{+◇◒?,▥▯o6◀▥}~◆▷pi▽▩0b◀▰^?◛▣af△▭i2▵▼bt◎▩8~◄◅$d●▣>$◝▩g7◗◖r(▶▨.5◘◂4h◉▮f9◍◆/c◍▷p2▢▩:!◅▤z%▬▼]c▿◗(!■□yh▯△i{◔□en▲◆z}◔▭k?■◔9p▮▴ck▭▦ow▱◍0e▧◖v*◓▰5?▾◒vs◔◇>q▯▽%x◂▹y5▵▬,=●△2/◖▶3a◃◁-%◒●h%▱▯8l◑■c1◇◘gv▤◔5~▫◛]*◐◙-^◀▼!q◊▽vo▮▥-l▬▴r%□▷+v▻▩+n◊◓wv◛▥^8▦●->◍▹g2◝◔cq▿◆!3◀▪,v◅▬b+▤◗s?▬▮[8►◆76◉▾<d◅◆gm◊◙f.◛◍x/◉●[h ◖ 3◂▩}5▾▩x{▪◆*e▢▵q0□▶zf◖◔5j◅▧?:▷■:(◖▻z9◎◇8:▦▹=k ◇ @ ◊ ~◄▥~+▿◝%z▸▪$a◓▤-i●▱n#▤▼@3■▶[_▦▾)b◜▿1}▤▢?*◖◛e%◐▪!e◛▿h:▷►cs◁ n ▹◘nu▭▢)f◙▭:t▥◗_=▩■eq◗▰r]▶◂~{▢▱+y▦◕c-▲▲1?◗▼.#◇○5)▨▬<s◈▶?8■◁-s△◘xl◕◇t<▽▧dz◇◙0o◇▭t7◖▩jl△◄$t◘▷x_◀▱0&◗▿//▹ ) ▯▼$o◎▤_?■▵5[◐▵5v◇◛0n▼▭e7□▮:1▬○dv▻◚,~▮▼j0▨◛+>◖◐rg▲■lc○◓no ◉ ,◗◀<r◅▹ti▢◌&}▱▭x2◐◈1*△◗tw◖◖{_◕▫lu◄▹qe▵◃we▯▭wt▩◚^*◅◕-7▶▶of▨◊@1▢◃*n▶▪_0■▾,j○▬+2■◅=z▿◒8[▶▮a7▻▭>!▮◆ye▵◎b6◉▧(-◂ 0 ◝◘j:◖◅06▰◀$[◛◘69◅◝gq●▹g<◌■~e◂▿w6▱◔wn◀◅)2◖◙z:○◕)r▾◀p@▧◝/}▩△0s▱◕^z◙◀v8▹►oa◍□y1◊▷y3▱▸gr◓◖)_▧▴y4▥▵ym▪◕1:◚◚]a◈▩!c◈▻:u◗▭eh◊▤^m▸◜^x◃▤pp◉◝+0◎◅lm◗◛<m◛◊v1▽◜@-◐◌t6▭▪zk►◒ch▿◄[(▢▣13◍▤7}▧◇.~◘◐*w▮◘@#◝▲r5◜◖r$◗◕5^▻◇,y▪▻-y◓▪./▯▪#9◃◝pr▲□6b◜▨f+●◓zz►▢#=▧◊2d◖◇4c◎◎<u◎▶4{▴◗i3◑▵-/◌▱1y▣▬&1▢ b △◛0x◙◈<:▭◂c!◜▤1e●▧&2◖◊ze▼▷l}▾□83■◕-0▰◃9s◀▫1w○●ar■●m=▩▱65◁▭#]▰▾*b◐◚_n◛◅?f►▶(b▪◌q5▩◈1{△▰}<◗▪r[▩◉o3◀ # ▼▸qr◆▴~5◖◀b^▷▮uv◃▵i<◜▭=5◙▻<[▹◚bg◕◁s{◌▧*r▫□1&◊▨()■▹?=◌◅ua◐▿ku◖◄-#◚◑6_◁◐hd▣◝z=◓ m ▲▻c+▰◜#e▣◈.{■◐&r◓●bv▥◄qa◖▨<<◚◛+]◄◝7#▵▴<]◊◃@h◛■v(▻◝#a▾▪m9▣▦<z◌◛or◐◎t0▭▫:8◉◚e3▩◅:m◜▯ul◊◝(=▥●p3◃▫}$▼◃9%◑▦fa►◁}(○◗-z▪▸r*◀◁+}◑◚~2▨▤sv◃◀a,▨◄$)▽◙b/◐◀j.◙◖.)◘◊zo◕▦q-◃◙=8◚△[:▴▬c<◑◀]^◉◙_^▽▵s#◀▣},▰◚57◛□{!□▥f%▸◄[n▣▶$6▣◗)(○▦h,▦▭v6▹◆{*◓■@$▰ = ▿▲7b◇◇w,◜▫[b◗▻8a◚■71◍◊qo◒▩/n □ p▽▴4.◌▿,d○ q ◒◜yf▧▤_6◒▧k1▬◎8{▢△?3◘▻&=△▪,6▥◂qk▪◀ge△▩?z▽◝un▷◀ty▧◃]/▴◈d?■◜t]◖◚>p◘●fc▲▭n>◕◉sb◎▬2&▸▬a0◚▿?/▱◖d,◐▥qm◖▭<.▪▹4(◄▻$,◜◑s(▱◄90▣◛5a◓▢=6▽◔z{▿▼sh◜◔sq◝◄w-◄▿]]▧▯_v◒◅45▵◕}8◂◝2h◅◒sy◆▢o=▶▹g>◗▮6:▽▰-=▻▣-,▷ k ▲◜75▹◌b3▯◗lf▭◇p:▢◓-j▧▰(/▻▤su◁◕q}◌◆uo■▦9&▨►(g■△jc◔▨mn◄▰ui△▲y7■►[i▵◛=s▬◗pk▷▣w5◜◈{y◘◃=a◗◜@q■▩)o▯▾r3◇◔3^◅▽hm◎◆=&◌□ww▴◐p5◗◂8z▶◌46▣▣tv◆◀8t▤◕7i◝▸x!▾▮uz▩▯cv▵●o8 ▬ _◎◝)$◇△dh◍►og▫◕0h▪▴fo▴►f!◛◁}6▲►s!▶◐fx◚◇d. ◆ 5▪◖1k ◛ 9○▪a.▱◗y!◈◁%}▯◊,9○□xp◆◍g_◌◌$z◐◉ib▥◃u3◑◃z$△▬qw▦▣.}◆◒jw▾▷%@▲◖p.◈◚)i●◌w.▼◑[j▧◂mv▧▨e(▬◙9j▬◈3w▩◃k%▼▮:n▰◓xx▬▱zg▫▤!s◘◄%-◍▶=e◂▸-@▻◘_)□▨pn▢▧nj▹▴6j◈◄3l▶◚@p▨◐a[◅▨@g▪■yq▻◜ah◒▯%.◌▨xo◙◊uq▨◃>z▤△ut◌◚/+◅▭j&◕○{-◁▲fp◑▪=i▴◊z*◒▼%_▭▴rn◕◙cy▸▱]j ▣ :▢▯m3▸◛}.◝◇8_●▦ab◎◈e^▲▶wl▲▧&[▯◃#u◉▸1d◓▮%j◁■[#◝◌rs△▷$p●▻.m▨▥n<◓◃v4▩▻_.◎▥k:◜◝).◃◘9/▮◖(t▴▩h6◉▭s)▴▧h(▫▶=}◊◍ew▸◉>1▣◉2g□◛r0▲▾8h▥◅:a◙►4t◇◊^#▥◌yp▸ [ ◗▽4}▨△4)◐▱]k◗◗}r▮◉&&◕◚c8◆◗$7▪▢9k◐▤@t◙▶,u◌▵^]◎◌^-▹◃-:▶▽~6●►1<▴▰>e▾▹be◙▩:i▭◑+!▻◂r=◜□c*◑▴{i◂■g5◅◉~1▭◖34▱◊6<▴▭*t►▬](◓▦)/◃◑}7◇▽{^●▨:c◚◄@^◜▸n5◌►/1◛◑=@▢▭x8▱○st▨◓p<▪◈yt◍▰7&◅◗to◙▾ax◅◂ga■▢9[△▫1b◇▨a:▻▨im◔►vr▽◁ep▩◊:k▾◜*-◀△>u▮▶cf▴◀+3◙▬w?◀▨e{▪▦~[▨●{#▤◓#?▯▦8>▢◑l$▼■}-●▭=r►◛!+▪▿ss▱▨74▩◆3g▿◃#p▹▯~>◍▽o$◛▤r@◝◒=f◘◇,@◎▽b5▵◂t^◕▻~i◘○fd◇●2%▻◕>_◀▤n4◚▮h3◑◘e/◅▰8(◓△5>◄◄#w▴▦?>◝▶[^▣▾*1◍◜!*▲▽/_△▽pb◌◂q,◎◜<&◗◇)-▪▨k(◅▫e6▽▷#8 ◒ r▮◄)p▧◛y>◀◌d0▭▬2x▢◙!7▰□$s▩◑eb◇▱jv▫▩fh▽◅8o▸▹}j▥◝=%◚▻y8◎■1s▾▣2z►◔l]▧◕32◙◄e#■◉=<▷▪_s▥ v ◐ l ◑▫j8○▭he▤◊5<◎◃1-▶▵9(◌◈*2◀◄n$◕■q3▱◝l?◉◌w~▨▿c5▫ - ▩▧@(◝◑a2◌▮%+▰▱(3●◎_{▸◀u}◃□<n◍◘hj◂▫~q▹▭/%▨▴x3▢▸{4◜◎/.○◐b$◃●9t●◁(1▤◖/v◚◊y%◚▤k7▩▬?#▸◇o?◙▴x)◒■h<▨▻2~◚◔q*▵▱.!◔▩84▩◂ig▼◂9,▧◗m<▫◘^v▸◍]& ► h◒◔z]▣ : ▵◜r6▭▭hc◁▷_f◀▹*q◓▨a5○▻ec▮◕49□◑r+△▥<h◛○u?▽◃(f▥△d]◀◛4x■▭fy▯▶j/◂►31◉○r#◛▮t+◒▦hg◔ { ◂□kl◗◁fg◇■y_▱◛m%▧■ru▾◑?l▽◛.u▯○j~◁▨&<▸◅pw◃◚nd▴◔fj◙▹/:▷▤[d▢◚9a▽△&a◚◌9=▬▵r>▯▮4~○◎bh◌▪p}▦▢(+▸▥~=◔▥]<▤▥)n◃▧ue▬▷25▫▷{c●◔~d◀▮}h○◆4k◑▰@u▻▫4l△◒66◇▷%3▫◈s8◛◌o2▨◚~v▥▷<?►▰mq◜◀?v▸◌eu◒►]!►▣=l◈■/3◅◐}>▯◍5i◗◎<f◂◂f*▮ + ○■[%▮◂]z▷▵bc▹□3n◇▥4r◜▲51◘◝ag▣▸f)◐▯cb◓◁^0◂▰!n◚◐c7◔◔*,◚◎ls◉◖7-◙◛nc◃◉5y▤□/y◔▮c&▾◔x5▽▮c[▮◁^h◒▨-3◚▨hy▫▴h=◍◑7*▬▫}9◁▢*[◅▪@]△▹]@▣▤$g◇□~p▣◂+,▫▲~^▫◐iz▭◙nv◙▪^n▼▽ju◛◆vk▯▿w)△◂v}◂▾p&◗▷fq◉▩=~▭◜<7▹◂+9▥▰v_◖◍8n▴▷+e◘◅w_▢●4+▦◘1j▢▤(e◜◘bl▾▵]~◓◙_r◃◛#:▸▣09■◚(.◁▽-&▱◘{}◚◕,:■◝b2▩▢t5◗◍w:▫◚^%◊▾<*►▼=-▤◉]:◗◃/a◚▬-n▤►#}◒◉l&▲◘j}▤▱b[▩▭jp◌◖::▮◎7?◊►j_▵▰~_◑◂ov◆◔hf▨▢.f◕▰a^○◄{)▱△d+◛▼=v▴▨/6▼◚3,▹◍-4◑●ph▴△io▬◆m+□▩wu▼◈z_◃◐r!▴▯6[◔◈%y▽▱y<▾◗-q◎▮y-▴◌x+▱◃na▦◝.s▥▲gz▢◍.2◆▨hz○▾g!◒◃yv◝◖4m◉◅>)▫▻6t◁◊$w◆◃-*◑▧1^◌▸5=▮■dm▷▼s,◇◝>3▭▤5o◛►rf□▢^e◑◐)#►◑d9▬■l=▩▪ef●◉y}▨▽%^►▷lr▢▢>*◍◈e]▹◇hx◅◌wy▰◇+1▩▴$%▣◑7m◆◂p#◍ ? ◚◆jn▾▿oq▭◓f}►△p(▹▻%e▭▶>c◘▪]e▪▫m$▽◇x.▪◃=+◔◙_5◊□ix◈▨n6◌◕9#◙▼w[►◙3m◑▻59◑▼+5△◇@6▲▢@4◍◛[3▾◝x?▱▶l9◎▰yw◚◃?$◀◗br◀◘}t▲▣+_▵▮:{▪○jf◄▼pc ▷ k▩◝g[▧ . ▻◈w$▤▻@)◊◔8}▸◔%8◚◍vc▿◙k.■■-_◔▴d:◝◝+[△◑[<►◂v$◆▣h>▼▻7k▥▨q^◇ @ ◍◐5q◙◂]}□◒vt◘▣=g◊◉6!◂▯(p▴◛ee▬◂bp○◍w1◌◜p+▰▸1#▵▻k]◊▿&5▰◎:r▼□w^■◈nn◆■3>▯▸{x△▸?}◙◌ex◄◒(i◙◐8]▸◈8$◗◅b7◌▩/f◌◀wi◁◄{k▰●4=►▮@c▢▮ln◔○.p●▷=[ ▸ [◓▲m#▵◊a]▦◉!h◓◚{@◙◜ij◈▢q#◃▽[.▧▸(v■▸5f▬▽5/◆□)*◓▩1l▹▨++△◔6y▮◅x@▷▸4@◈◔:j▽▶)9○▤&?▿◁8q◑▭4&▾○[!▸▧w*▥▣^o▵▶)@◈◉s0▱◈i&▭◒?2◅◓27▫◎.*▲◄sr◂▨n&◝◐v=◁◎ys◚▾<{▽▣po◕▣^w◇▮vi▦▪9i◊▦u]◗◑ml▵▹b>◘▧qt▸◐2y◍◇g6▾◕3:◑▥#)▽◓)4▦▷e!▪◁0c▸◎ub ▮ +▦▻[z△◝5_▬▩5%◐▨r<◁◍[v▰◔~t▲▼*3◒▸:/▮▹,1 ▨ u●▤tg◘◗&t◆▯q?◄▷v&▶▥&o▾►*9●◃-(■◂d%▤▣3? ▧ .●◚d4◛◄qh◝◜*$▻◆lj◓◑-.▨◎u*▲◑@j▸▢)<▩◐3f△▤t,▪◝k[◍▿vx◎▨+<▶◍hp▧◀(*◒◛6i▦◄_2◌▽!k◎◔rw◚▥h0◁▪(}◓◓rh◂○0u◉▵f[▯◎][◖▼d-▵◒+&◙◆<$▹◗!1◇▩jx◄◁,f▲◌8+■▿!)▾▧/<▼▢2$▸◁zy◀□mu◛◐~g◁◔w>▴◂fl▱▣3y▴▻yc▼▿6x▣◖eg◒▷!>▾▢jy▲▮f5▶◜jg◝◅%{▷◒^,▽▤e&▭●/>▦◀8m◇▵70◚◓tr▤ 2 ▶◆3]▦◛!o▢▲j6◖▽:p◄▩q)▫◒(q▪◜:^◔▣a>▵◓-m▣◚]8▻▽:y▵○.q▣◀a8◎◍t.◐▼uy▻◛7o□◗[-▫◂x7▧▪1t◆◈rd◘▦q9◔◑vg◅▼~<◆◇,<◎●&u▼▨=y▷□[7◝◛#c◒◈j=◇▹6=▭◝>i◂▵-5◔▦>[◙◒[~◉▢2n◛▢<+▭◆i)□◅~c◈▮ct▧◒6,◚◂@d▫◍c/●◝lz▹◁}@◁◗5*▿▪vq▾▲a{◘▴+l▶◖$e◊▸l!▫◀0~◙◝.@◕▸gc◑►i]◄◗(]▥▶zi▷◐)~▾◁-u◅▣iy◜△3b▷▱[m▶◊.w▰◗2[▵◈o5◅◃01▴□zd◗▧^c▯□w@▶◄l:▩▷=0◈◑qf◔◀j*◜►e}◌ ^  ▰ =▢◕$i◔◝m~◌◝vh▬▨60◛◙)y▶○?5▽◕h8◖◌v,▴◚}e◙▵:l▶▸i.▿▥g1◆▮h{▭■=.◐◒vl◛◛/&◒◗m(◃◃7z◀▸6w ▿ z▣◘#m◓▭[y▻▹%6▲▯55◍▩d*▬▭~y◌◇%9○▼v-◛◎2m▨◂fr▬□kn▴◍+~◆►*_▼◄9e▲◀)q▼◖>d▸□%4▱▱ea◚▸k^◚▯q_◃▼+x▶▻zh◅◙{l●◅[o▴◜%0◀◂!^◗△[>▸▽qy◍◝.d◉◓hw ◁ n◛◃3~▿▯*d◓▫%k◊▬#{▼▰fi▹▹3#▽◉}q▧▢gs▿▾/9◎▹m)◄▾*v◙ ! ▨▾)h◊▣le◅◖dt▨◙9-▬◐9m◍▸g=◔△n-■◆/g◜◒1(◐▭ox▯◉>5◃▷19◝◊(>◇◓&v▧▮/]▧▲2@▸◗e,◊▲(5▥▩~z▨◝_4▦◃v0▬◓-?◕▿n8▬◝5!▦◓pa▽▨,+◓○tk▧◈h$◅▲@}◜▼zt▤▩]9▻◁q]◃◄(6▲▥7s◜▵8j▽◖ei▽▪{%●◀?4▾▸4^◜▮&4●▢9?▼▥a9◐▮1r▿◑%/▿▻b4◉◈bd◂◕a~▣□@i▱◜ll◁▤._◈ t ▥■_+▰▽rq◔▸1/◅▩sg▦◙~!▦▧,e▯►t}◙◘lh◜▧_3□▧=n▲◇9)◀▶m7◜▩>}◁▩l%◀◔lg◜▽pl■▴.t◔◉1a▼◗oe◑▽6{◌▭>j◊▹37◒▭<@◃ y ◖◜%(◇▫h4◈▭]0▴▽,x●▰f(▻□pu◀◉54□▵3u◘◚y^◖▮fw◉□-<◎▷z>▱▷dy▼◙*f○▷x0○▰14◂◍vd◕▵4*▱▹22◌▼6v◜▾l4▼◝5z▷▴w]▤▦ip▪◎[}►◀u(▿▵c:●▬el▴◓u_◄◌>-◕◜j-◐◜q$◗●(n▸◊d[▭▧3t▩▲gn◖▷g@◜■{d◅▶y:▯◓?9◗▱v.◓▱3%△▦-9◗◙p$◈▧$(▰▪$-▲▷h^▮▲~#▵△d5▫○om◂●f]●○&n▧▫!w◆ 5 ◖□gt▻▻?(□□j,◕▶9!▸▦k/◉◁lt◁▱if▰▶&)▻◉up▦◁@,◅◊w4◘▱p>◉◉&,◖◎bq◑▾q!▻■i}◂◒e.▭◄7p▱▪p~◆◓g-▲△1!◎◒zw□◙vj▣▯l- ◝ x◑◊a)►◘~k▢◉jb▮◓_#▨▨^>◘◈,^◐◝4e◉▤qq◅▮#6◖▫v@◓◍2w▷▹g:◂▽.g▭◐ot◆◐!=△●}g●▪>#◊◘9b◅▥u#▴ f ◇◗gu◓◔bw◛▹^/◓▴r8▭ c □◄m/◆▵lx▷○{&◎◕u2◜ & ◝▻~j▣◙9@▫▹_a▱◀xg▣◎7$◑◒si▯▷je▿□,7▨▷cz◊◊#-◜●$1◙◓8u■◎^<◘▾0^□◐>t◍△f$▯◇+?◕▧[g◝▴+s▢◅r_◒◐=d▶◒ii▢◆u=▾▦ks▵▦#,▢◐:9►▹e>◓◌go◝▭0y□▽i7▼◛gw◎◘xr◑◌{n◝■gk◓▸-g▢▨rv▪▤_b◎►}c◌●e~▬▪h7 ▼ i▲●8-▨◌:g◝◗]l◖▾d<▦►^@▥◘6l◈◐}x◎▿*%◎◙e0▽◒0p◙●47■◇-d◉◄<i▲○k_▻◗36▻▮58◘▶h&□◊am◘▢!u▩►2v◄◃a%▿▱[[▧◆%7□◉k+◍▥sf▩▨9y◈○!/△◍et◁▾,, ◎ <▰▧41◓▾zu▷▨o7▩□eo◔◌/2■▱*u▴◕b:◛●97▢▹ld◔▶e1▫◉os▶▦by◇◆h2◂◛)k◙▤(9▼▯s[▼◌8c▾◊#k▹●-~◔▬),▦◜>9◈▦zj◈◂*y▲▹=7◒◚1h▩○me▹▣xc▸►kd◖▦$b▾◉j!►◌7<◄■i5◔▱3c◈▼n}◛▶3_▻▸av▭▥h)▹◅0m◑◛{9◊◚]{▥◖m!▥◁2q▱▴w/▷▷0a▤◚]_◘◆.a▴◆mm▸◝!?◃▬$~▲▵u{▿◊h-◘◕-h▷◗mi◔▢*j◉◕9g◂◃0f▬◚e4◅△ae▹◄*>▮▧yk▪◔l8○▫,)▸▼n.▲▩y&▹▽>a▧◅_e◁◇&m▽▻c%▿▭tu▷◃u$◝□_/▭△wz◖▢1]◇◁wj▸◃(l▲◛2f▹◛$@◒ r ◛◂<p◐▦5$◇◜21◑▬2j◎ < ▾◓9o△▧e)●▽,g▮◑>y▥◍(#▨▣6d▹▾?]▹▷@!▲◅*]◅○0g▪▽}[◄◚:3◘▯.3▭▽x4▰▭wb◇▤[x◜▰jk◈►z-◊◛:,◇▻_x○◘:+◝▫4:◇▪_,▱▮pe▰▴iv◐►7t►○r)◐◊pg►▫?c◓◘ff◛▵1>▤■<4○◌/*▨◑.c▽◄u0◂◜+*◀◙&(□▰f/◎▼:%▱◙-f▫◓72►▪{z◄◘3k▮◜b0●◂&s▸▰g,◃▶%u◘◙@y▷▬,t◗▯(j▩◔3j◔◎/k▷◊c, ▽ 4▧▿*8◁▰}!▹▢}f◎◖4[◀■6>▩◄w}▯▹!~▦▫-a◚▧i+▰◂38◊◕.j▧◚o^▾▼$/□▯gx▼◒}s■ 7 ▥◀&y▪▶-p▦◊,/●◊y.●◍@9○◒4s◆▾f_▾◍uk▫▧hk▾▭yg◜▷@s▮◇}y▫◌zv◊▼=(▷▿u^►◖}^▪◓b<◔◅{u◁▫n[▶▧n(◛▪6g◎▻q8▯▲!i▱▬8&◜◉e9◘■^4▣▧ra◐▧.i●▫x>▷◁,o▷◆{8○▲m>◑◆%l▦◚.y◇▧fz▲◕&-◜◐x#◌◔zm▨◈4j◘▵wh▤▯5w▷▭q/▶■7l▱◒_w▦▯uu▣▨^t▴◁]t▭◎p%◑▢x1◐▩d}◊◇#h▦▥w8▵▸9w◊◜@~◌▹q:◍◎j5◑◑o1◜◇m5▲◈x[◁◌0*▮▿e*▣◕t#▥○sa◕▾(0▭▣*}○▩gg▬◃:d○▮cm▴▶7.▱◓03▫▼s<◜◂xq▨ u ▤◃rm◊▪l<◀▴?{▼▫:[◇◂>/◇◑#s▶▼6a◚▼@x▲▱f1◓◉sd▰▨6o◆△94▪◇6(◛▭24▰◛~0▸▲<=▮▬_8○▥9c ▱ d◛▬t-●▯0d▷◜=9▨◜{[▦ s ◘◒z0◒◎rk◝▿.$▣◁a(▾◂*&◁◂h[◀◐~l▼●z6▫▨$5△▱,.●▿}%◔▲co◎▢#$■◓=?▭▹3v◈▱5m◈◅$3▥▼}p◌▥u7▯◙%f◐▫>?▭○d#◁●~@◚◖_g◊◑#r▧▻q<●▶s4◇◐zs▿▽/m◊◐+d◇▿&g◍●k#○▢2s▩▽1c◖▣u-▹◈#4◖▥{6▴▣07▩◘0i▪▧%p◎□7a○▹/8◍◔p1▭▲6c◉◀q.◄▸7!▬◄m*▢◎?6◜▱%)◗■t*▨▭/i◀►u@◒▥^_▸■!t◖△{0◃◅9$▶◓#/▪▵7%▭◁]>◎▭n:◈◍*0◁▸{t◄◀}}▥▴s+●◒@r◅◅n9◈◊%c►▽#7◎○3d▿◌l1▨◖((▷◖~m◕◌/-◎◑ik▩▾_1◂◌m}◒▢,(●■jm◆○^:◆◁{]▵▪tl◔▿91▰◒+b▻▶fm▸▤7~◕◃!:◁▴w%▸●xb◈◘]2▶▩a<►▤!%◇◎(z◄►tx◉▬^g◉▣.]◐◃z+◀◚mb◆▫p!◆▸ja■▮&d▼▬_q▥◜)e▧◙^d▿ z ◔▼[e◈◖ce●◇${▿△tn▥◈.8▻◅~4◍▪}#▵◔p]▼◕8v▯▢{?▬▬6@◍◍)a◕▨y9◍◓2r▷▥rb◖◈rx◑◅z(◚ 6 ▸◖it▧▣/e▤◜j+▷▻:h◘◘t$▣◜ro◓▻6#▪▾,%◑▹j(▣▢xy◔◘#t▶▯v3▩◀k$▱▲[+▹▸67◉▻26◆◄!v■▷aw▶►+8◒◖c}◀▦cj▽▲sz▱□,m◕△&3▹◙t/▸▶*<▵▣<~◓◕:~▼▣1[◗◉v!◐▢,5▣△]n▪◉%2◖▤d>◉▯b*◙○s5▣◒h}◑◎/h▣◃5t▿▴?y◂◓.>◍◃(w▰◙t&○◜[u◇◖l{▬►&c◗►^& ◄ e▷▯$f◝◆b&▸▾md●▾ka▶◙]i◌◗op■◊kk▻◒#y◍◀xf▩▥dd►▴)% ▥ v◍▴5:▵◗k4▬▲/u▾▫p8■▬[q◛▰l/▽◀(y◕▷&#◅◎vp◈▴d_◒◍rr▭◀n~◕◊?7▸◘au□►2l▫◃bi◔▹a4◛▨?<◕▬y]▻◎?m▧►u/▮◔,h▰▫5c▽◈o~▽▢_!▾△mj▯◝#b▹◜b8◓□u!▭▱gb▮▫np◐▸]+◅▢?@▥►.[▰▣c2◈◈qb▬◁t!▵◝]o◙▮p?◑◕!r△△@z▧□2^◊▢m{◙◚m^◄◙kv▯◜uw▶▭<0◝▷t?■▪~?◀◈v5▨▧3p▢■i_■◖9n◔◁t4■◘>&▦◖}i▾◅=_◉◜#v▽▹04◀◀n^▾◐/=◁◆~)▷◎2)◅▦k>△ / ◝▹ne▪□@o◈◕f=▬▶50◆▹5l●▸/{◎◂(x▸▸&j▬▧@+◚▢cw▶▿}*◉◒k8▿○gh◓▿/#◒▶:>▭◔+w◊▵oo▿▬<#▻▥:f◁◅)6▿◅?_▬◀-8 ◍ ?▣○7x▵◙ta○▸{5◐◍])▤◇l>○◀/l▵◀:)◗▸r}◄◎^)▮◍ji◕◖6?▼◔=w◑▶x:▷▶a_◓▣nh◒◓#q▵□n+▰◑wk▻▾1u▥▫p*◍▯6s◃▥<9▫△j@▤▾4]▯◐56▨▮_d◝◚f,▧▦7r△▣gi◖▯lp▢◝g9◍▲^9▭▿g*▼◊!,□▣($◅►3&▱●9u◝▮n3◂◐9r◑◝s3○◂?a ▴ f◛◕vz▮◗~b◊◈?s◅◔*!◃►}o◔▯>^◍▵m.◁▻il▸◂b@▭▾&7▤▵2k◘◖re◈◀#x▮◊g}▦▶78◘▿_(◔●xd◄◂s_◘▸:*▪▯+-◙▷o-◌▫6f▵▢l5▼▶va◀●o@▷◕j)△◓jd▸◕7n◜▬li▰◐~a◁◒7w◉◔~,▿◓b)◓◈_@ ◘ 1◜◛v~◂◉hh◑▯c=◆▽e[▵▩2p▯▧kz△◀>f◂▶yo◑◖mx▵▲i(◄▲b-▻◑x]◃◒5]▪▣^f▼▤{o■▰:}▵▽lo▮▢4/▮○#&▧▾mr◄▵ux◊◎p7▾■y$◄▯.&●▩8k◈◙q~◜◌id▤▭d@◂▦#d▵▵:=◘▽0$◆▤g{▤◄x*◐▴=c◕◓h@◔◍f^◍◙t9■▣8w◘◑]w▤◛q6 ◓ m▼▦8,▱▫v{◛◖&q◅▾(o▥▢#2▿▧@{◘▩+$◝▥m-▸◚/z◑▿(4◍▱=2◒▲?b▻▱!5◍▾s&▱◉pv▯ 8 ▪▭n%▾◎&f▯◘~$◜○cl◌◐*c◐◔0q▨■p/◀◎*k▥◕r~◓◄)0◙△0w▦◔53◈▸ni ◌ ^◆◚um△◕$2◈◜@/◁◑5p▸▻h1▦◆+j▻◃so▽◂+k▤◐h?□▸[k▯◂.^◉▶u%◉◃l)◄◈xm▦▬x^▬△xu◃△7d▶◎w{▾▨<k△◊}/▫◅y/▻▪sk▩◇q7◕◑+u◈●*z◄◇4$◒▿1p△◚*4▾▴!9►▻gl◉◎g4◒□,_▽◚z!◅◑ki▾◛8x▧▵ej◓▬/b◃▩@n◀◜~f◂▴,$◉◆r{▥▧c^○◁n/◝◕/w◎◛~s▨▶}l ▫ -◝►dk◃◗>4◔◆!j▪◑wd◊◖0r◝◃>:◕▱r,▣◍s9▭▸+)▾◃}]◈▤n?▦◐wr▨▲j#◄▧@<◍▣:$▪▱{$◆▰ug◍▭>{◀◇jr▸▯?n◓◜od◚▲&+►◓_]▹◐gp▷◝*)□◍~]◈▵^s▰▵mg◊◄93◆▿#f▥▽u+◒▣/r◈▯^~◌▶?r◛◓4o▩◗80◚▫s1◒▾k!▻▿9}▢◈nt▤◈{2▷◔3s▤◍)=▰◕k9▶ o ◌▷th▭◚iq◈▲o) ◕ a◖◗1~◕◝>k◘◎dg◄○4i▿►$>◝▦w&◁◖}u△▿3o◀○8^◉▪l[◀▷d(◅◜}a◗▤ts▧◍h~◙▣33◔▾=$▢▻y0▹◊lq▫▭4<◘▭j[■◌uh▪▩s2▣▥,l◎◊df◓◗6&◗◆qv○▽nm○►<o◑▩*a○◃^[◔◗ir▱▿*x▯▫qj▬◍h5◒▮fb▼◀?)▩▿-)▫▱r4○◖6h◔◊=b▷▢/x△◉rl▱◑n]■▫,c▽◑y)▥▹:.◖▪#+□△l+▬◅4q▪◒-[◉▦kw▦◌}{◐◆tp ◀ #◐◑[6◖▲+h◜◚}n▵◍v<▫◁<a▹◕bk▤▧%q▪▥</▹▬i^▢◁ve▦◒y(◚▵,3◑ g ▴▿qp▹◔10▢○{~▥▾5{◗▴5d▾◄>.◇▸w!◄▣a=◃◌9_△◙yz◝▱?k▲◉(s◘◁xw▾▱cc◙◗$<◆◌,k○◛<c●◖@w◌▯]h▥▸j2◗◘a$▮▤!l◔▪j>▿◂yu ▯ 8□▭mk▧△3(▮▨5b◓▶px◄▮_&◃○ds◄◜&>▹◒~*◔◛s$◄◆~-▦◍la▩▵73◃▢yn○◙n=▧◄l@▬▯kc●◈0!◎▸oj▨◇w7▶◛7@▹▤{7▨▱o>●▴%$▻▴^^▰◁{j◕◔c{◄▤yx▫■o!▯◛x~▯◕g^□▾a}▮▵2+ ▻ }▿◛>2◙◉)]▤▸-+▷◚c.◔◓]6◉▿=,▬▹ko◂◖9<◕◕)&▨▰.,▢◒)}▷▽g%◈◓bu◗▾3-◉▹s.◇▦8e▢◀!8▽ 4 ◊▰h]▲◃}4▫◗<e◗▣gd▦◎q=◅◈in◎▦*:▬◊#~▰▮d)◇◚o+▤◌$9◕◐{h◒◇2<▢◜o<◊▩2:◇▬=m◆▻):◓◎t)◆◉zp▭◗_$◅▱<_□◕+#▱◎o/▰◄kr◙▦vf◝▢%*◔◃cr▩▰&i▯◖(8■▼#3◐◕,*□◖/5◑◗]$◎◐g?◆◎@l◝▧wm▱▢ac△◆!6◌◑!g▣▴n,◚▱-k◕●#(□◚#<▯◆-{ ○ q▴◉##●◆(%◂▼ur■▧(u▴◒<,◙◑o.▧▶9l▼ i ◚□l0◌◉hi▰▩[2◕□:@◙▲lv◝●z2▧▱[&◌◙0+▶◃9*▨▪l7►◉7j◙◔{=◁▵r7◁▥7>▿▩oi▼◉ba▲▤m0◁▿m1▻◙,0○▵^y▩◎ad◜◜jo▣◊h!◍■@%◀◑hl●◑&~▧◜?!▦▴p6▰▼:b▿◍p9◃▿0(▽▫ud□▫?[◗▨6]◗◐[)△▾77▲◒mo◃▮n7▷◈/d◌◄(^▽◘3i▸○z~▭▷j<◊◗w3▽▬*~◅□dx▲◗1z◈▫*l◊◌0_◐◛4,□▤0:◜▹>,▥◐})▩●q1▴▮1=▮▸7h▹◀f7◒▪nk◐◘0j▿▢{f▸◙)m▬▰]%◂▤d!▲▰1v▩◓mf◓▥es▦▦6-◎◁a!▤▲:?◂▲,z◍▦[w▫▰$&▸△d6◗◊/p▩▶<2◐▷0>▱◇[s◃▨e+◂◊%d▣▫,>▾◚23▷△tz◃▭c_◆◝/~▸▭uc◁◁v?◖◕o9◐●1+▦△&w●◙t@●◗^2○▿[1▢▰oz ▢ b□◇ed▫▬7c▹■.=■◙{.◚◜:&▹▮{r◚◅e8◅▻$$◖►]y◛▷>]◉▱&8◒▫?+▢►@?▵◅.?○▶%<△◈{s△▶$l►►2{▻ } □◔i#▯◅(m▶◝<x▦◅kh■◑fk▿▰^5◒▤c>▮◌6k▨▯@v◀◝hs▹▰<!▾◙]5▷●i8◃▣?d▽▸@b▤▰nx◕◈d8▬▥tb▲◎^k□◎5@◅◁2-▿◚44◝◁di▤▷>7◐▾){◒◘n0▸▩q+◙▸<v◁▶6^◂◀96▮▱(2◅▸sm◝▨+{▼◜wg◅■/o◂▱t_◐◇$?◃◕o:▥◒c4▵◑xh▧◎6/▴▹2}▵◘w0▪◂i*□▹cu◆◑,[◓◅_p◊○28◅▿=>◐◖-r●●$. ◈ t▣▼s6◄▴=1▲▪2*▶△q@◛◗dr◊◂^i◈△u1 ◜ &▬◕3+▩◁p_▫▢,r▫◖%t◇◀>>▫◑:-△○z<▼▴t%◚◝4!◕▪$v▥▦08◈▿ke◝◓du■▨/t■○2=▿◈~7▭◕da◃▸:o◘◍tj▶▬ey◆◛qn◙◇.-▱◌4w□◌5k◚▽=4◄▢8f▿◘2o▤◑{m ◗ (▦▮8!◘▮ho►▿2c▮▽>v◆▱z)▷▰7_▦◇^7▴■fv◓▧z3▴▸oh◆◕p0◀▬],◘◔za◌◊9q▧◐+p◇◍h_▻◊tc◚◙&%◂◇k)◁□y6◂◅m4▲◙5h◇▾4u▷▩rp▵◚{p◝▰j]◗◈,2▻◄:q◘▨<>◝○mz◁◓&{▩ w ▼▹an◍▬]q▵◄_z▭▻jh▶▣<-◜◕6q□◓i[■◀bz▿◔ng●◕~:■◃x&▧◓={◛▯~.◁◜*o□●$m▧▽w<◔▫~8◖◉<3▿▨hn◁▯0<□◝&9◕▥v:◐▣k{▬◖l^▽▿2_△◌do◆▦/4◓◒$h◚○%=◃◜v]◔■7f►□d2◍◌n!▧▹8%▦▼#[◘▹t{◄◊(a■◒^a▴▲+a△□!y▬◇_y▴◃u9◄▪.n▧▷/,◙▫(,▵▤$k▼▧!$▴◄^3▾◖/(')
    _martian_table = None
    _english_table = None

    def english_to_martian(self, message):
        message = str(message).lower()
        if not self._martian_table:
            self._martian_table = self.make_table(self._to_martian)
        return self.translate(message, self._martian_table)

    def martian_to_english(self, message):
        message = str(message).lower()
        if not self._english_table:
            self._english_table = self.make_table(self._to_english)
        return self.translate(message, self._english_table)

    def make_table(self, data):
        _start = 0
        _offset = 2
        _len = len(data)
        _table = dict()
        while(_len):
            _first = data[_start:_offset]
            _second = data[_start + 2:_offset + 2]
            _table.update({_first:_second})
            _start += 4
            _offset += 4
            _len -= 4
        return _table

    def translate(self, message, table):
        lines = re.split(r"[~\r\n]+", message)
        translated_lines = []
        for line in lines:
            translated_lines.append(self.translate_line(line, table))
        return "\r\n".join(translated_lines)

    def translate_line(self, line, table):
        if (len(line) % 2 == 1):
            line = line + ' '
        _start = 0
        _len = len(line)
        _translated = ''
        while (_len):
            _pair = line[_start:_start + 2]
            try:
                _translated += table[_pair]
            except:
                _translated += _pair
            _len -= 2
            _start += 2
        return _translated
