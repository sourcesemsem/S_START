import asyncio
from collections import deque
from random import choice

from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from sbb_b import sbb_b 
from ..core.managers import edit_delete, edit_or_reply

async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call

def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@sbb_b.on(admin_cmd(pattern="دعوه للمكالمه(?: |$)(.*)"))
async def _(e):
    ok = await edit_or_reply(e, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")
@sbb_b.on(admin_cmd(pattern="بدء مكالمه(?: |$)(.*)"))
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await edit_or_reply(e, "`جار بدء المكالمة ✅...`")
    except Exception as ex:
        await edit_or_reply(e, f"`{str(ex)}`")

# ================العاب جيبثون=========================

R = [
    "**𓆰**العـاب الاحترافيه** 🎮𓆪 \n"
    "  ❶ **⪼**  [حرب الفضاء 🛸](https://t.me/gamee?game=ATARIAsteroids)   \n"
    "  ❷ **⪼**  [لعبة فلابي بيرد 🐥](https://t.me/awesomebot?game=FlappyBird)   \n"
    "  ❸ **⪼**  [القط المشاكس 🐱](https://t.me/gamee?game=CrazyCat)   \n"
    "  ❹ **⪼**  [صيد الاسماك 🐟](https://t.me/gamee?game=SpikyFish3)   \n"
    "  ❺ **⪼**  [سباق الدراجات 🏍](https://t.me/gamee?game=MotoFX2)   \n"
    "  ❻ **⪼**  [سباق سيارات 🏎](https://t.me/gamee?game=F1Racer)   \n"
    "  ❼ **⪼**  [شطرنج ♟](https://t.me/T4TTTTBOT?game=chess)   \n"
    "  ❽ **⪼**  [كرة القدم ⚽](https://t.me/gamee?game=FootballStar)   \n"
    "  ❾ **⪼**  [كرة السلة 🏀](https://t.me/gamee?game=BasketBoyRush)   \n"
    "  ❿ **⪼**  [سلة 2 🎯](https://t.me/gamee?game=DoozieDunks)   \n"
    "  ⓫ **⪼**  [ضرب الاسهم 🏹](https://t.me/T4TTTTBOT?game=arrow)   \n"
    "  ⓬ **⪼**  [لعبة الالوان 🔵🔴](https://t.me/T4TTTTBOT?game=color)   \n"
    "  ⓭ **⪼**  [كونج فو 🎽](https://t.me/gamee?game=KungFuInc)   \n"
    "  ⓮ **⪼**  [🐍 لعبة الافعى 🐍](https://t.me/T4TTTTBOT?game=snake)   \n"
    "  ⓯ **⪼**  [🚀 لعبة الصواريخ 🚀](https://t.me/T4TTTTBOT?game=rocket)   \n"
    "  ⓰ **⪼**  [كيب اب 🧿](https://t.me/gamee?game=KeepitUP)   \n"
    "  ⓱ **⪼**  [جيت واي 🚨](https://t.me/gamee?game=Getaway)   \n"
    "  ⓲ **⪼**  [الالـوان 🔮](https://t.me/gamee?game=ColorHit)   \n"
    "  ⓳ **⪼**  [مدفع الكرات🏮](https://t.me/gamee?game=NeonBlaster)   \n"
    "**-** مطور السورس **⪼ [𐇮 𓂐 𓆩 سمير 𓆪 𖠛 ](t.me/DEV_SAMIR)   \n"
    "**-** قناة السورس **⪼ [𐇮 𓂐 𓆩سورس سيمو𓆪 𖠛🇷🇺  ](t.me/FTTUTY)   "
]

@sbb_b.on(admin_cmd(pattern="الالعاب$"))
async def ithker(knopis):
    await knopis.edit(choice(R))

# ================= Citation_morning =================
Citation_morning = [
    "أَعُوذُ بِاللهِ مِنْ الشَّيْطَانِ الرَّجِيمِ اللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلاَ يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ وَلاَ يَؤُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ.",
    "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ هُوَ ٱللَّهُ أَحَدٌ، ٱللَّهُ ٱلصَّمَدُ، لَمْ يَلِدْ وَلَمْ يُولَدْ، وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ. ",
    "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ، مِن شَرِّ مَا خَلَقَ، وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ، وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ، وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ.",
    "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",
    "أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُ بِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر.",
    "اللّهـمَّ أَنْتَ رَبِّـي لا إلهَ إلاّ أَنْتَ، خَلَقْتَنـي وَأَنا عَبْـدُك، وَأَنا عَلـى عَهْـدِكَ وَوَعْـدِكَ ما اسْتَـطَعْـت، أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ.",
    "رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً. ",
    "اللّهُـمَّ إِنِّـي أَصْبَـحْتُ أُشْـهِدُك، وَأُشْـهِدُ حَمَلَـةَ عَـرْشِـك، وَمَلَائِكَتَكَ، وَجَمـيعَ خَلْـقِك، أَنَّـكَ أَنْـتَ اللهُ لا إلهَ إلاّ أَنْـتَ وَحْـدَكَ لا شَريكَ لَـك، وَأَنَّ ُ مُحَمّـداً عَبْـدُكَ وَرَسـولُـك.",
    "اللّهُـمَّ ما أَصْبَـَحَ بي مِـنْ نِعْـمَةٍ أَو بِأَحَـدٍ مِـنْ خَلْـقِك ، فَمِـنْكَ وَحْـدَكَ لا شريكَ لَـك ، فَلَـكَ الْحَمْـدُ وَلَـكَ الشُّكْـر. ",
    "حَسْبِـيَ اللّهُ لا إلهَ إلاّ هُوَ عَلَـيهِ تَوَكَّـلتُ وَهُوَ رَبُّ العَرْشِ العَظـيم.",
    "من قالها كفاه الله ما أهمه من أمر الدنيا والأخرة.",
    "بِسـمِ اللهِ الذي لا يَضُـرُّ مَعَ اسمِـهِ شَيءٌ في الأرْضِ وَلا في السّمـاءِ وَهـوَ السّمـيعُ العَلـيم.",
    "اللّهُـمَّ بِكَ أَصْـبَحْنا وَبِكَ أَمْسَـينا، وَبِكَ نَحْـيا وَبِكَ نَمُـوتُ وَإِلَـيْكَ النُّـشُور.",
    "أَصْبَـحْـنا عَلَى فِطْرَةِ الإسْلاَمِ، وَعَلَى كَلِمَةِ الإِخْلاَصِ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ، وَعَلَى مِلَّةِ أَبِينَا إبْرَاهِيمَ حَنِيفاً مُسْلِماً وَمَا كَانَ مِنَ المُشْرِكِينَ.",
    "سُبْحـانَ اللهِ وَبِحَمْـدِهِ عَدَدَ خَلْـقِه، وَرِضـا نَفْسِـه، وَزِنَـةَ عَـرْشِـه، وَمِـدادَ كَلِمـاتِـه.",
    "اللّهُـمَّ عافِـني في بَدَنـي، اللّهُـمَّ عافِـني في سَمْـعي، اللّهُـمَّ عافِـني في بَصَـري، لا إلهَ إلاّ أَنْـتَ.",
    "اللّهُـمَّ إِنّـي أَعـوذُ بِكَ مِنَ الْكُـفر، وَالفَـقْر، وَأَعـوذُ بِكَ مِنْ عَذابِ القَـبْر، لا إلهَ إلاّ أَنْـتَ.",
    "اللّهُـمَّ إِنِّـي أسْـأَلُـكَ العَـفْوَ وَالعـافِـيةَ في الدُّنْـيا وَالآخِـرَة، اللّهُـمَّ إِنِّـي أسْـأَلُـكَ العَـفْوَ وَالعـافِـيةَ في ديني وَدُنْـيايَ وَأهْـلي وَمالـي، اللّهُـمَّ اسْتُـرْ عـوْراتي وَآمِـنْ رَوْعاتي، اللّهُـمَّ احْفَظْـني مِن بَـينِ يَدَيَّ وَمِن خَلْفـي وَعَن يَمـيني وَعَن شِمـالي، وَمِن فَوْقـي، وَأَعـوذُ بِعَظَمَـتِكَ أَن أُغْـتالَ مِن تَحْتـي.",
    "يَا حَيُّ يَا قيُّومُ بِرَحْمَتِكَ أسْتَغِيثُ أصْلِحْ لِي شَأنِي كُلَّهُ وَلاَ تَكِلْنِي إلَى نَفْسِي طَـرْفَةَ عَيْنٍ.",
    "أَصْبَـحْـنا وَأَصْبَـحْ المُـلكُ للهِ رَبِّ العـالَمـين، اللّهُـمَّ إِنِّـي أسْـأَلُـكَ خَـيْرَ هـذا الـيَوْم ، فَـتْحَهُ، وَنَصْـرَهُ، وَنـورَهُ وَبَـرَكَتَـهُ، وَهُـداهُ، وَأَعـوذُ بِـكَ مِـنْ شَـرِّ ما فـيهِ وَشَـرِّ ما بَعْـدَه.",
    "اللّهُـمَّ عالِـمَ الغَـيْبِ وَالشّـهادَةِ فاطِـرَ السّماواتِ وَالأرْضِ رَبَّ كـلِّ شَـيءٍ وَمَليـكَه، أَشْهَـدُ أَنْ لا إِلـهَ إِلاّ أَنْت، أَعـوذُ بِكَ مِن شَـرِّ نَفْسـي وَمِن شَـرِّ الشَّيْـطانِ وَشِرْكِهِ، وَأَنْ أَقْتَـرِفَ عَلـى نَفْسـي سوءاً أَوْ أَجُـرَّهُ إِلـى مُسْـلِم.",
    "أَعـوذُ بِكَلِمـاتِ اللّهِ التّـامّـاتِ مِنْ شَـرِّ ما خَلَـق.",
    "اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ على سيدنا مُحمَّد.",
    "اللَّهُمَّ إِنَّا نَعُوذُ بِكَ مِنْ أَنْ نُشْرِكَ بِكَ شَيْئًا نَعْلَمُهُ، وَنَسْتَغْفِرُكَ لِمَا لَا نَعْلَمُهُ.",
    "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ الْهَمِّ وَالْحَزَنِ، وَأَعُوذُ بِكَ مِنْ الْعَجْزِ وَالْكَسَلِ، وَأَعُوذُ بِكَ مِنْ الْجُبْنِ وَالْبُخْلِ، وَأَعُوذُ بِكَ مِنْ غَلَبَةِ الدَّيْنِ، وَقَهْرِ الرِّجَالِ.",
    "أسْتَغْفِرُ اللهَ العَظِيمَ الَّذِي لاَ إلَهَ إلاَّ هُوَ، الحَيُّ القَيُّومُ، وَأتُوبُ إلَيهِ.",
    "يَا رَبِّ، لَكَ الْحَمْدُ كَمَا يَنْبَغِي لِجَلَالِ وَجْهِكَ، وَلِعَظِيمِ سُلْطَانِكَ.",
    "اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا، وَرِزْقًا طَيِّبًا، وَعَمَلًا مُتَقَبَّلًا.",
    "اللَّهُمَّ أَنْتَ رَبِّي لا إِلَهَ إِلا أَنْتَ، عَلَيْكَ تَوَكَّلْتُ ، وَأَنْتَ رَبُّ الْعَرْشِ الْعَظِيمِ، مَا شَاءَ اللَّهُ كَانَ، وَمَا لَمْ يَشَأْ لَمْ يَكُنْ، وَلا حَوْلَ وَلا قُوَّةَ إِلا بِاللَّهِ الْعَلِيِّ الْعَظِيمِ، أَعْلَمُ أَنَّ اللَّهَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ، وَأَنَّ اللَّهَ قَدْ أَحَاطَ بِكُلِّ شَيْءٍ عِلْمًا، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَمِنْ شَرِّ كُلِّ دَابَّةٍ أَنْتَ آخِذٌ بِنَاصِيَتِهَا ، إِنَّ رَبِّي عَلَى صِرَاطٍ مُسْتَقِيمٍ.",
    "لَا إلَه إلّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءِ قَدِيرِ.",
    "كانت له عدل عشر رقاب، وكتبت له مئة حسنة، ومحيت عنه مئة سيئة، وكانت له حرزا من الشيطان.",
    "سُبْحـانَ اللهِ وَبِحَمْـدِهِ.",
    "حُطَّتْ خَطَايَاهُ وَإِنْ كَانَتْ مِثْلَ زَبَدِ الْبَحْرِ، لَمْ يَأْتِ أَحَدٌ يَوْمَ الْقِيَامَةِ بِأَفْضَلَ مِمَّا جَاءَ بِهِ إِلَّا أَحَدٌ قَالَ مِثْلَ مَا قَالَ أَوْ زَادَ عَلَيْهِ.",
    "أسْتَغْفِرُ اللهَ وَأتُوبُ إلَيْهِ.",
    "لا إلَهَ إلَّا اللَّهُ، وحْدَهُ لا شَرِيكَ له، له المُلْكُ وله الحَمْدُ، وهو علَى كُلِّ شيءٍ قَدِيرٌ.",
    "كانَتْ له عَدْلَ عَشْرِ رِقابٍ، وكُتِبَتْ له مِئَةُ حَسَنَةٍ، ومُحِيَتْ عنْه مِئَةُ سَيِّئَةٍ، وكانَتْ له حِرْزًا مِنَ الشَّيْطانِ يَومَهُ ذلكَ حتَّى يُمْسِيَ، ولَمْ يَأْتِ أحَدٌ بأَفْضَلَ ممَّا جاءَ به، إلَّا أحَدٌ عَمِلَ أكْثَرَ مِن ذلكَ.",
    " اللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلاَ يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ وَلاَ يَؤُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ ❤️💘",
" قُلْ هُوَ اللَّهُ أَحَدٌ، اللَّهُ الصَّمَدُ، لَمْ يَلِدْ وَلَمْ يُولَدْ، وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ ❤️💘",
" قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ، مِن شَرِّ مَا خَلَقَ، وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ، وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ، وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ ❤️💘",
" قُلْ أَعُوذُ بِرَبِّ النَّاسِ، مَلِكِ النَّاسِ، إِلَهِ النَّاسِ، مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ، الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ، مِنَ الْجِنَّةِ وَ النَّاسِ ❤️💘",
" أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله ، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير ، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه ، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُبِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر ، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر ❤️💘",
" اللّهـمَّ أَنْتَ رَبِّـي لا إلهَ إلاّ أَنْتَ ، خَلَقْتَنـي وَأَنا عَبْـدُك ، وَأَنا عَلـى عَهْـدِكَ وَوَعْـدِكَ ما اسْتَـطَعْـت ، أَعـوذُبِكَ مِنْ شَـرِّ ما صَنَـعْت ، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ ❤️💘",
" رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً ❤️💘",
" اللّهُـمَّ ما أَصْبَـَحَ بي مِـنْ نِعْـمَةٍ أَو بِأَحَـدٍ مِـنْ خَلْـقِك ، فَمِـنْكَ وَحْـدَكَ لا شريكَ لَـك ، فَلَـكَ الْحَمْـدُ وَلَـكَ الشُّكْـر ❤️💘",
" أَصْبَـحْـنا عَلَى فِطْرَةِ الإسْلاَمِ، وَعَلَى كَلِمَةِ الإِخْلاَصِ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ، وَعَلَى مِلَّةِ أَبِينَا إبْرَاهِيمَ حَنِيفاً مُسْلِماً وَمَا كَانَ مِنَ المُشْرِكِينَ ❤️💘",
" اللّهُـمَّ عافِـني في بَدَنـي ، اللّهُـمَّ عافِـني في سَمْـعي ، اللّهُـمَّ عافِـني في بَصَـري ، لا إلهَ إلاّ أَنْـتَ ❤️💘",
" اللّهُـمَّ إِنّـي أَعـوذُ بِكَ مِنَ الْكُـفر ، وَالفَـقْر ، وَأَعـوذُ بِكَ مِنْ عَذابِ القَـبْر ، لا إلهَ إلاّ أَنْـتَ ❤️💘",
" اللّهُـمَّ إِنِّـي أسْـأَلُـكَ العَـفْوَ وَالعـافِـيةَ في الدُّنْـيا وَالآخِـرَة ، اللّهُـمَّ إِنِّـي أسْـأَلُـكَ العَـفْوَ وَالعـافِـيةَ في ديني وَدُنْـيايَ وَأهْـلي وَمالـي ، اللّهُـمَّ اسْتُـرْ عـوْراتي وَآمِـنْ رَوْعاتـي ، اللّهُـمَّ احْفَظْـني مِن بَـينِ يَدَيَّ وَمِن خَلْفـي وَعَن يَمـيني وَعَن شِمـالي ، وَمِن فَوْقـي ، وَأَعـوذُ بِعَظَمَـتِكَ أَن أُغْـتالَ مِن تَحْتـي ❤️💘",
" يَا حَيُّ يَا قيُّومُ بِرَحْمَتِكَ أسْتَغِيثُ أصْلِحْ لِي شَأنِي كُلَّهُ وَلاَ تَكِلُنِي إلَى نَفْسِي طَـرْفَةَ عَيْنٍ ❤️💘",
" أَصْبَـحْـنا وَأَصْبَـحْ المُـلكُ للهِ رَبِّ العـالَمـين ، اللّهُـمَّ إِنِّـي أسْـأَلُـكَ خَـيْرَ هـذا الـيَوْم ، فَـتْحَهُ ، وَنَصْـرَهُ ، وَنـورَهُ وَبَـرَكَتَـهُ ، وَهُـداهُ ، وَأَعـوذُ بِـكَ مِـنْ شَـرِّ ما فـيهِ وَشَـرِّ ما بَعْـدَه ❤️💘",
" اللّهُـمَّ عالِـمَ الغَـيْبِ وَالشّـهادَةِ فاطِـرَ السّماواتِ وَالأرْضِ رَبَّ كـلِّ شَـيءٍ وَمَليـكَه ، أَشْهَـدُ أَنْ لا إِلـهَ إِلاّ أَنْت ، أَعـوذُ بِكَ مِن شَـرِّ نَفْسـي وَمِن شَـرِّ الشَّيْـطانِ وَشِـرْكِه ، وَأَنْ أَقْتَـرِفَ عَلـى نَفْسـي سوءاً أَوْ أَجُـرَّهُ إِلـى مُسْـلِم ❤️💘",
" أَعـوذُ بِكَلِمـاتِ اللّهِ التّـامّـاتِ مِنْ شَـرِّ ما خَلَـق ??💘",
" اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ على نَبِيِّنَا مُحمَّد ❤️💘",
" اللَّهُمَّ إِنَّا نَعُوذُ بِكَ مِنْ أَنْ نُشْرِكَ بِكَ شَيْئًا نَعْلَمُهُ ، وَنَسْتَغْفِرُكَ لِمَا لَا نَعْلَمُهُ ❤️💘",
" أسْتَغْفِرُ اللهَ العَظِيمَ الَّذِي لاَ إلَهَ إلاَّ هُوَ، الحَيُّ القَيُّومُ، وَأتُوبُ إلَيهِ ❤️💘",
" يَا رَبِّ , لَكَ الْحَمْدُ كَمَا يَنْبَغِي لِجَلَالِ وَجْهِكَ , وَلِعَظِيمِ سُلْطَانِكَ ❤️💘",
" لَا إلَه إلّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلُّ شَيْءِ قَدِيرِ ❤️💘",
" اللَّهُمَّ أَنْتَ رَبِّي لا إِلَهَ إِلا أَنْتَ ، عَلَيْكَ تَوَكَّلْتُ ، وَأَنْتَ رَبُّ الْعَرْشِ الْعَظِيمِ , مَا شَاءَ اللَّهُ كَانَ ، وَمَا لَمْ يَشَأْ لَمْ يَكُنْ ، وَلا حَوْلَ وَلا قُوَّةَ إِلا بِاللَّهِ الْعَلِيِّ الْعَظِيمِ , أَعْلَمُ أَنَّ اللَّهَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ، وَأَنَّ اللَّهَ قَدْ أَحَاطَ بِكُلِّ شَيْءٍ عِلْمًا , اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي ، وَمِنْ شَرِّ كُلِّ دَابَّةٍ أَنْتَ آخِذٌ بِنَاصِيَتِهَا ، إِنَّ رَبِّي عَلَى صِرَاطٍ مُسْتَقِيمٍ ❤️💘",
" سُبْحـانَ اللهِ وَبِحَمْـدِهِ ❤️💘",
"كُنْ لحوحاً فِي الدّعاءِ،فقدْ أوشكَ السّهمُ أنْ يُصيبَ. 💗",

]


@sbb_b.on(admin_cmd(pattern="اذكار$"))
async def ithker(knopis):
    await knopis.edit(choice(Citation_morning))

Citation_morning = [
"واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",

"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",

"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية 👻😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل 👻😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "," مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة..    راح عشان يحاسب بيقوله الولاعة ديه بكام؟   قاله دينار..  قاله منا عارف ان هي نار بس بكام 🤓😂", 
"بنت حبت تشتغل مع رئيس عصابة..   شغلها في غسيل الأموال 🤓😂 ", 
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه.. قاله سهلة.. استلف من الناس فلوس هيسألوا عليك كل يوم! 🤓😂",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟    ﻗﺎﻟﻬﺎ اﻫﻮه..   ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ..   ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه. 🤓😂",
"واحده ست سايقه على الجي بي اس..  قالها انحرفي قليلًا..   قلعت الطرحة. 🤓😂 ",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة.. صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح.. أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون؟ حد يبيع مرسيدس؟ 🤓😂",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه. 🤓😂",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه.. ومبسوطة أوي وبتضحك.. سألوها بتضحكي على إيه؟ قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا. 🤓😂",
"بنت حبت تشتغل مع رئيس عصابة..   شغلها في غسيل الأموال 🤓😂",
"مره واحد اشترى فراخ..   علشان يربيها فى قفص صدره.🤓😂",
"مرة واحد من الفيوم مات..   أهله صوصوا عليه.🤓😂",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟    ﻗﺎﻟﻬﺎ اﻫﻮه..   ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ..   ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه.🤓😂",
"مره واحد شاط كرة فى المقص..   اتخرمت. 🤓😂",
"مرة واحد رايح لواحد صاحبه.. فا البواب وقفه بيقول له انت طالع لمين.. قاله طالع أسمر شوية لبابايا.. قاله يا أستاذ طالع لمين في العماره 🤓😂",

]


@sbb_b.on(admin_cmd(pattern="نكته$"))
async def ithker(knopis):
    await knopis.edit(choice(Citation_morning))

Citation1_morning = [
    "** ‎كت تويت | أكثر شيء يُسكِت الطفل برأيك؟ **",
    "** ‎كت تويت ‏| تخيّل لو أنك سترسم شيء وحيد فيصبح حقيقة، ماذا سترسم؟ **",
    "** كت تويت | قناة الكرتون المفضلة في طفولتك ؟ **",
    "** كت تويت | الحرية لـ ... ؟ **",
    "** كت تويت ‏| كلمة للصُداع؟ **",
    "** كت تويت ‏| ما الشيء الذي يُفارقك؟ **",
    "** كت تويت ‏| ما الشيء الذي يُفارقك؟ **",
    "** كت تويت | موقف مميز فعلته مع شخص ولايزال يذكره لك؟ **",
    "** كت تويت ‏| أيهما ينتصر، الكبرياء أم الحب؟ **",
    "** كت تويت | بعد ١٠ سنين شنو تصير ؟ **",
    "** كت تويت ‏| مِن أغرب وأجمل الأسماء التي مرت عليك؟ **",
    "** كت تويت | عمرك شلت مصيبة عن شخص برغبتك ؟ **",
    "** كت تويت | أكثر سؤال وجِّه إليك مؤخرًا؟ **",
    "** كت تويت | ما هو الشيء الذي يجعلك تشعر بالخوف؟ **",
    "** كت تويت | شنو الي يفسد الصداقة؟ **",
    "** كت تويت | شخص لاترفض له طلبا ؟ **",
    "** كت تويت | كم مره خسرت شخص تحبه؟ **",
    "** كت تويت | كيف تتعامل مع الاشخاص السلبيين ؟ **",
    "** كت تويت | كلمة تشعر بالخجل اذا قيلت لك؟ **",
    "** كت تويت | جسمك اكبر من عٌمرك او العكسّ ؟! **",
    "** كت تويت |أقوى كذبة مشت عليك ؟ **",
    "** كت تويت | تتأثر بدموع شخص يبكي قدامك قبل تعرف السبب ؟ **",
    "** كت تويت | هل حدث وضحيت من أجل شخصٍ أحببت؟ **",
    "** كت تويت | أكثر تطبيق تستخدمه مؤخرًا؟ **",
    "** كت تويت | ‏اكثر شي يرضيك اذا زعلت بدون تفكير ؟ **",
    "** كت تويت | شنو محتاج حتى تكون مبسوط ؟ **",
    "** كت تويت | مطلبك الوحيد الحين ؟ **",
    "** كت تويت | هل حدث وشعرت بأنك ارتكبت أحد الذنوب أثناء الصيام؟ **",
    "** كت تويت | اكثر مطور تحبه بجيبثون منو ؟ **",

]


@sbb_b.on(admin_cmd(pattern="كت$"))
async def ithker(knopis):
    await knopis.edit(choice(Citation1_morning))

Jepthon_5erok = [
    "** ‎لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ **",
    "** لو خيروك |  أسئلة محرجة أسئلة صراحة ماذا ستختار؟ **",
    "** هل كذبت على والديك من قبل..؟ **",
    "** لو خيروك |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟ **",
    "** لو خيروك |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟ **",
    "** تحس انك محظوظ بالاشخاص الي حولك ؟ **",
    "** لو خيروك |  بين مشاهدة كرة القدم أو متابعة الأخبار؟ **",
    "** لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟ **",
    "** لو خيروك |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟ **",
    "** لو كنت شخص آخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟ **",
    "** لو خيروك |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟ **",
    "** لو خيروك |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟ **",
    "** لو خيروك |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟ **",
    "** لو خيروك |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟ **",
    "** لو خيروك |  بين البقاء بدون هاتف لمدة شهر أو بدون إنترنت لمدة أسبوع؟ **",
    "** لو خيروك |  بين رجل أعمال أو أمير؟ **",
    "** لو خيروك |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟ **",
    "** لو خيروك |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟ **",
    "** لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟ **",
    "** لو خيروك |  بين الإبحار لمدة أسبوع كامل أو السفر على متن طائرة لـ 3 أيام متواصلة؟! **",
    "** لو خيروك |  بين أن تصبحي عارضة أزياء وبين ميك آب أرتيست؟ **",
    "** لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟ **",
    "** لو خيروك |  بين زوجتك وابنك/ابنتك؟ **",
    "** لو خيروك |  بين إما الحصول على المال أو على المزيد من الوقت؟ **",
    "** لو خيروك |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟ **",
    "** لو خيروك |  بين أمك وأبيك؟ **",
    "** لو خيروك |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟ **",
    "** لو خيروك |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟ **",
    "** لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ **",

]


@sbb_b.on(admin_cmd(pattern="خيروك$"))
async def ithker(knopis):
    await knopis.edit(choice(Jepthon_5erok))

    
@sbb_b.on(admin_cmd(pattern="اذكار عشر$"))    
async def ithker(event):
    "h"
    event = await edit_or_reply(event, "أَصْبَـحْـنا عَلَى فِطْرَةِ الإسْلاَمِ")
    await event.edit("أَعُوذُ بِاللهِ مِنْ الشَّيْطَانِ الرَّجِيمِ اللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلاَ يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ وَلاَ يَؤُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ.")
    await asyncio.sleep(9)
    await event.edit("بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ هُوَ ٱللَّهُ أَحَدٌ، ٱللَّهُ ٱلصَّمَدُ، لَمْ يَلِدْ وَلَمْ يُولَدْ، وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ.")
    await asyncio.sleep(9)
    await event.edit("بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ، مِن شَرِّ مَا خَلَقَ، وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ، وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ، وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ.")
    await asyncio.sleep(9)
    await event.edit("بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ. ")
    await asyncio.sleep(9)
    await event.edit("أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُ بِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر. ")
    await asyncio.sleep(9)
    await event.edit("اللّهـمَّ أَنْتَ رَبِّـي لا إلهَ إلاّ أَنْتَ، خَلَقْتَنـي وَأَنا عَبْـدُك، وَأَنا عَلـى عَهْـدِكَ وَوَعْـدِكَ ما اسْتَـطَعْـت، أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ. ")
    await asyncio.sleep(9)
    await event.edit("رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً.")
    await asyncio.sleep(9)
    await event.edit("اللّهُـمَّ إِنِّـي أَصْبَـحْتُ أُشْـهِدُك، وَأُشْـهِدُ حَمَلَـةَ عَـرْشِـك، وَمَلَائِكَتَكَ، وَجَمـيعَ خَلْـقِك، أَنَّـكَ أَنْـتَ اللهُ لا إلهَ إلاّ أَنْـتَ وَحْـدَكَ لا شَريكَ لَـك، وَأَنَّ ُ مُحَمّـداً عَبْـدُكَ وَرَسـولُـك.")
    await asyncio.sleep(9)    
    await event.edit("اللّهُـمَّ ما أَصْبَـَحَ بي مِـنْ نِعْـمَةٍ أَو بِأَحَـدٍ مِـنْ خَلْـقِك ، فَمِـنْكَ وَحْـدَكَ لا شريكَ لَـك ، فَلَـكَ الْحَمْـدُ وَلَـكَ الشُّكْـر.")
    await asyncio.sleep(9)
    await event.edit("حَسْبِـيَ اللّهُ لا إلهَ إلاّ هُوَ عَلَـيهِ تَوَكَّـلتُ وَهُوَ رَبُّ العَرْشِ العَظـيم.")
    await asyncio.sleep(9)   

Jepthon_Shnow = [
    "** ‎هذا واحد طايح حظه ومسربت **",
    "** هذا واحد شراب عرك ويدور بنات وكرنج **",
    "** ولكعبة ولحمزه والانجيل والتوراة هذا ينيج 😹 **",
    "** هذا واحد فقير ومحبوب ويحب الخير للناس 😍 **",
    "** هذا اخوي وحبيبي ربي يحفظه ويخليه الية ❤️‍🔥 **",
    "** هذا واحد حلو موكف المنطقه تك رجل بحلاته 🤤 **",
]


@sbb_b.on(admin_cmd(pattern="شنو رأيك بهذا$"))
async def ithker(knopis):
    await knopis.edit(choice(Jepthon_Shnow))

Jepthon_Bosa = [
    "** ‎امممممممممح يبووو شنو من خد 😍 **",
    "** امممممح بوية مو شفه عسلل 😻 **",
    "** ويييع شبوس منه غير ريحة حلكة تكتل 🤮 **",
    "** ما ابوسة لعبت نفسي منه 😒 **",
    "** مححح افيششش البوسة ودتني لغير عالم 🤤 **",

]


@sbb_b.on(admin_cmd(pattern="بوسة$"))
async def ithker(knopis):
    await knopis.edit(choice(Jepthon_Bosa))
