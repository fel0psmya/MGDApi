from fastapi import FastAPI,  HTTPException
from collections import OrderedDict
from pydantic import BaseModel
from typing import List

app = FastAPI()

# main.py
# Modelo dos jogos
class Game(BaseModel):
    id: int
    name: str
    imageUrl: str
    trailerUrl: str
    description: str
    platforms: List[str]
    releaseDate: str
    screenshots: List[str]
    artworkUrl: str

# Lista de jogos (dados fixos)
game_list = [
    Game(
        id=1,
        name="Enigma do Medo",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/co93ft.webp",
        trailerUrl="https://www.youtube.com/watch?v=Hjl6usm5WCo",
        description="Become Mia, a paranormal detective searching for her missing father inside the Perimeter - a place that doesn't exist. Investigate clues like a real detective and unravel the mysteries behind the Enigma of Fear, defeating the terrible monsters who'll try to stop you.",
        platforms=["PC (Microsoft Windows)"],
        releaseDate="2024",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/schjpq.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/schjpo.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/schjpn.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/ar36b9.webp"
    ),
    Game(
        id=2,
        name="Stardew Valley",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/xrpmydnu9rpxvxfjkiu7.webp",
        trailerUrl="https://www.youtube.com/watch?v=8A7A1X1TVNc",
        description="Stardew Valley is an open-ended country-life RPG!",
        platforms=[
            "Android", "iOS", "Linux", "Mac", "Nintendo Switch",
            "PC (Microsoft Windows)", "PlayStation 4", "PlayStation Vita", "Wii U", "Xbox One"
        ],
        releaseDate="2016",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/rhxs1x9w5hf5kde2osf5.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/iwswpvxa9ytrpk8yjcyx.webp","https://images.igdb.com/igdb/image/upload/t_720p/sw7rtba7p1xs77klsime.webp","https://images.igdb.com/igdb/image/upload/t_720p/g1aakqbkp2quq0krqeky.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/ar5l8.webp"
    ),
    Game(
        id=3,
        name="Disco Elysium",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/co1sfj.webp",
        trailerUrl="https://www.youtube.com/watch?v=SEJOJ4AUBic",
        description="A CRPG in which, waking up in a hotel room a total amnesiac with highly opinionated voices in his head, a middle-aged detective on a murder case inadvertently ends up playing a part in the political dispute between a local labour union and a larger international body, all while struggling to piece together his past, diagnose the nature of the reality around him and come to terms with said reality.",
        platforms=["Mac", "PC (Microsoft Windows)"],
        releaseDate="2019",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/jgfwlctsfh8yljnjdeab.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/qfml0sjrmeiv5gf6tgg1.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/ar4m6.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/ar4m8.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/ar4m5.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/ar4m9.webp"
    ),
    Game(
        id=4,
        name="Deltarune",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/co3w7g.webp",
        trailerUrl="https://www.youtube.com/watch?v=9HjcVhf54YI",
        description="UNDERTALE's parallel story, DELTARUNE. Meet new and old characters in a tale that steps closer to its end, chapter by chapter. Dodge bullets in nonviolent RPG battles as you listen to funky, funky music.",
        platforms=["Mac", "Nintendo Switch", "PC (Microsoft Windows)", "PlayStation 4"],
        releaseDate="TBD",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/scdl5l.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scdl5m.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scdl5k.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/ar17go.webp"
    ),
    Game(
        id=5,
        name="The Last Of Us Part I",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/co5xex.webp",
        trailerUrl="https://www.youtube.com/watch?v=LW5NwaUXgIA",
        description="Experience the emotional storytelling and unforgettable characters of Joel and Ellie in The Last of Us, winner of over 200 Game of the Year awards and now rebuilt for PlayStation 5.\n" +
                    "Enjoy a total overhaul of the original experience, faithfully reproduced but incorporating modernized gameplay, improved controls and expanded accessibility options. Plus, feel immersed with improved effects and enhanced exploration and combat.\n" +
                    "It also includes the Left Behind story DLC.",
        platforms=["PC (Microsoft Windows)", "Playstation 5"],
        releaseDate="2022",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/schcg6.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/schcg7.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scq0k5.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/ar1oia.webp"
    ),
    Game(
        id=6,
        name="Omori",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/co1xlp.webp",
        trailerUrl="https://www.youtube.com/watch?v=nV0BST2nifk&t=8s&ab_channel=OMOCAT",
        description="A turn-based surreal horror RPG in which a child traverses various mundane, quirky, humourous, mysterious and horrific lands with his friends in search of a missing person while confronting his past and his fears. Explore a strange world full of colorful friends and foes. When the time comes, the path you’ve chosen will determine your fate... and perhaps the fate of others as well.",
        platforms=["Mac", "Nintendo 3DS", "Nintendo Switch", "PC (Microsoft Windows)", "Playstation 4", "Playstation Vita", "Xbox One", "Xbox Series X|S"],
        releaseDate="2020",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/sc752s.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc752r.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc752t.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc752v.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc752u.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/arive.webp"
    ),
    Game(
        id=7,
        name="Spiritfarer",
        imageUrl="https://images.igdb.com/igdb/image/upload/t_cover_big/co2fe7.webp",
        trailerUrl="https://www.youtube.com/watch?v=Xu4JHmcfrtw&t=14s&ab_channel=ThunderLotus",
        description="Spiritfarer is a cozy management game about dying. You play Stella, ferrymaster to the deceased, a Spiritfarer. Build a boat to explore the world, then befriend and care for spirits before finally releasing them into the afterlife. Farm, mine, fish, harvest, cook, and craft your way across mystical seas. Join the adventure as Daffodil the cat, in two-player cooperative play. Spend relaxing quality time with your spirit passengers, create lasting memories, and, ultimately, learn how to say goodbye to your cherished friends. What will you leave behind?",
        platforms=["Google Stadia", "Linux", "Mac", "Nintendo Switch", "PC (Microsoft Windows)", "Playstation 4", "Xbox One"],
        releaseDate="2020",
        screenshots=[
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lcc.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lca.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lcb.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lc8.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lc7.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lc9.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lcd.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6lce.webp"
        ],
        artworkUrl="https://images.igdb.com/igdb/image/upload/t_720p/ar8eu.webp"
    ),
     Game(
        id = 8,
        name = "Vampire Survivors",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co4bzv.webp",
        trailerUrl = "https://www.youtube.com/watch?v=6HXNxWbRgsg",
        description = "Mow thousands of night creatures and survive until dawn! Vampire Survivors is a gothic horror casual game with rogue-lite elements, where your choices can allow you to quickly snowball against the hundreds of monsters that get thrown at you.",
        platforms = ["Android", "iOS", "Mac", "Nintendo Switch", "PC (Microsoft Windows)", "Playstation 4", "Playstation 5", "Xbox One", "Xbox Series X|S"],
        releaseDate = "2022",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/scf8q1.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scf8q2.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scf8q3.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scf8q4.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scf8q0.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar1cnh.webp"
    ),
    Game(
        id = 9,
        name = "Hollow Knight",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co93cr.webp",
        trailerUrl = "https://www.youtube.com/watch?v=Y2amTl5lBYM",
        description = "A 2D metroidvania with an emphasis on close combat and exploration in which the player enters the once-prosperous now-bleak insect kingdom of Hallownest, travels through its various districts, meets friendly inhabitants, fights hostile ones and uncovers the kingdom's history while improving their combat abilities and movement arsenal by fighting bosses and accessing out-of-the-way areas.",
        platforms = ["Linux", "Mac", "Nintendo Switch", "PC (Microsoft Windows)", "Wii U"],
        releaseDate = "2017",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/p3svrq6ewzxnn7p1a3v9.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/ityinxmtkakwbokpcwws.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/bkgxmg2m4h8wf5g9tblh.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/a3f72xprqkfuqdmha5ks.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/q634ullxbvipm6q6mcq9.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ylrp6zuf9e7tcu1nvuir.webp"
    ),
    Game(
        id = 10,
        name = "The Witcher IV",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co95i0.webp",
        trailerUrl = "https://www.youtube.com/watch?v=54dabgZJ5YA&t=4s&ab_channel=TheWitcher",
        description = "The Witcher IV is a single-player, open-world RPG from CD PROJEKT RED. At the start of a new saga, players take on the role of Ciri, a professional monster slayer, and embark on a journey through a brutal dark-fantasy world.",
        platforms = ["PC (Microsoft Windows)", "PlayStation 5", "Xbox Series X|S"],
        releaseDate = "2024",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/qy2iw9fvcbb4lcpw4bzm.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/qy2iw9fvcbb4lcpw4bzb.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/7vcuubjrjc6szpqw5a8i.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar1l6l.webp"
    ),
    Game(
        id = 11,
        name = "Persona 3 Reload",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co6z12.webp",
        trailerUrl = "https://www.youtube.com/watch?v=4py4V5xwXWE",
        description = "Step into the shoes of a transfer student thrust into an unexpected fate when entering the hour \"hidden\" between one day and the next. Awaken an incredible power and chase the mysteries of the Dark Hour, fight for your friends, and leave a mark on their memories forever.\nPersona 3 Reload is a captivating reimagining of the genre-defining RPG, reborn for the modern era.",
        platforms = ["PC (Microsoft Windows)", "Playstation 4", "Playstation 5", "Xbox One", "Xbox Series X|S"],
        releaseDate = "2024",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/scmww8.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sco1d3.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sco1d4.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sco1d8.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sco1da.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar2gyi.webp"
    ),
    Game(
        id = 12,
        name = "Persona 4 Golden",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co1n1x.webp",
        trailerUrl = "https://www.youtube.com/watch?v=Bnt0JxytEpo",
        description = "Persona 4 Golden is a remastered version of the critically acclaimed Persona 4. Step into the shoes of a high school student and uncover the secrets behind the mysterious deaths in a small Japanese town. With a mix of dungeon crawling, social simulation, and life-simulation elements, it’s a deeply immersive experience.",
        platforms = ["PC (Microsoft Windows)", "PlayStation Vita"],
        releaseDate = "2012",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/fnpbq0wy3fczzzwr2k1m.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/zx3rfqbtbdnib0m8arcn.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/r89g5ktv0kljptpgones.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/gc5xs0cejelrvqxobrxq.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/yssc5jule0r5psjbzelz.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/arm0o.webp"
    ),
    Game(
        id = 13,
        name = "Persona 4 Arena Ultimax",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co5k1y.webp",
        trailerUrl = "https://www.youtube.com/watch?v=znZJLRW8v4w",
        description = "Persona 4 Arena Ultimax is a fast-paced 2D fighting game featuring characters from Persona 3 and Persona 4. Players can engage in one-on-one combat while uncovering the mysterious events taking place in the Midnight Channel, with a deep story mode and a unique blend of Persona and fighting game mechanics.",
        platforms = ["Arcade", "Nintendo Switch", "PC (Microsoft Windows)", "PlayStation 3", "Playstation 4", "Xbox 360"],
        releaseDate = "2013",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7df4.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7df5.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7df3.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc8s75.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc8s77.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc8s79.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar1h94.webp"
    ),
    Game(
        id = 14,
        name = "Persona 5 Royal",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co1nic.webp",
        trailerUrl = "https://www.youtube.com/watch?v=o9QjlLdYK5I",
        description = "Persona 5 Royal is an expanded version of the original Persona 5 game, featuring new characters, a new semester, and additional story content. It follows the story of the Phantom Thieves, a group of high school students with the ability to enter the hearts of corrupt individuals and steal their desires.",
        platforms = ["Nintendo Switch", "PC (Microsoft Windows)", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X|S"],
        releaseDate = "2019",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6vps.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6vpt.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6vq0.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc6vpx.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar616.webp"
    ),
    Game(
        id = 15,
        name = "Persona 5 Strikers",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co2zoq.webp",
        trailerUrl = "https://www.youtube.com/watch?v=E0gVre6APWo",
        description = "Persona 5 Strikers is a crossover between Koei Tecmo's hack and slash Dynasty Warriors series and Atlus's turn-based role-playing game Persona series. As a result, it features gameplay elements from both, such as the real-time action combat of the former with the turn-based Persona-battling aspect of the latter. The game is set six months after the events of Persona 5, and follows Joker and the rest of the Phantom Thieves of Hearts as they end up in a mysterious version of Tokyo filled with supernatural enemies.",
        platforms = ["PlayStation 4", "Nintendo Switch", "PC (Microsoft Windows)"],
        releaseDate = "2020",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7fgn.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7fgf.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7fgh.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sc7fgg.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar9t4.webp"
    ),
    Game(
        id = 16,
        name = "Metaphor: ReFantazio",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co8d9t.webp",
        trailerUrl = "https://www.youtube.com/watch?v=zItvCKVaUrI",
        description = "From the creative minds of the Persona series – Metaphor: ReFantazio marks ATLUS’ first ever, full-scale fantasy RPG, brought to you by director Katsura Hashino, character designer Shigenori Soejima, and composer Shoji Meguro. \n Write your destiny and rise above fear as you step into a fantasy world unlike anything you’ve seen before. Fraught with unsettling mystery, the kingdom stands on a precipice. Now, you must embark on a journey, overcoming obstacles and forging bonds with friends.",
        platforms = ["Playstation 4", "PlayStation 5", "Xbox Series X|S", "PC (Microsoft Windows)"],
        releaseDate = "2024",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/scmwmr.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scmwmu.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scmwmt.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scmwmq.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar2uqr.webpp"
    ),
    Game(
        id = 17,
        name = "Shin Megami Tensei V",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co39zk.webp",
        trailerUrl = "https://www.youtube.com/watch?v=1PgRBcRi5NY",
        description = "Shin Megami Tensei V, the fifth numbered game of the Shin Megami Tensei series, is a role-playing video game set in modern-day Tokyo. It will feature returning gameplay elements from previous games, such as the ability to fuse demons, along with new mechanics.",
        platforms = ["Nintendo Switch"],
        releaseDate = "2021",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/scdryj.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/ppzlvufypgbvtmpylz0h.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/nohayrbz5araygyvhjj1.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/arcoh.webp"
    ),
    Game(
        id = 18,
        name = "13 Sentinels: Aegis Rim",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co2uls.webp",
        trailerUrl = "https://www.youtube.com/watch?v=1bKaQuW_aQY",
        description = "Uncover the truth and delve into a 2D sidescrolling adventure featuring gorgeous art and environments. Then, battle the kaiju in fast-paced, top-down combat. Customize the Sentinels with an arsenal of mechsuit weaponry, and fight to defend humanity!",
        platforms = ["Nintendo Switch","PlayStation 4"],
        releaseDate = "2019",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/jpf7ujdcjyvazvnudop0.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scgxgt.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/scgxgw.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/ar664.webp"
    ),
    Game(
        id = 19,
        name = "The Legend of Zelda: Breath of the Wild",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co3p2d.webp",
        trailerUrl = "https://www.youtube.com/watch?v=zw47_q9wbBE",
        description = "The Legend of Zelda: Breath of the Wild is the first 3D open-world game in the Zelda series. Link can travel anywhere and be equipped with weapons and armor found throughout the world to grant him various bonuses. Unlike many games in the series, Breath of the Wild does not impose a specific order in which quests or dungeons must be completed. While the game still has environmental obstacles such as weather effects, inhospitable lands, or powerful enemies, many of them can be overcome using the right method. A lot of critics ranked Breath of the Wild as one of the best video games of all time.",
        platforms = ["Nintendo Switch", "Wii U"],
        releaseDate = "2017",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/sckj69.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sckj6a.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sckj6d.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/sckj6h.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/fgubhnuapjmdbxwqxhsq.webp"
    ),
    Game(
        id = 20,
        name = "Gris",
        imageUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/co1qv5.webp",
        trailerUrl = "https://www.youtube.com/watch?v=RdrvV25zoA8",
        description = "Gris is a 2D platformer developed by Nomada Studio and published by Devolver Digital. Released in December 2018, it is a visually striking game that follows the journey of a young woman named Gris as she navigates a world of grief and loss. The game features no dialogue, relying on its hand-painted art style, evocative music, and environmental storytelling to convey its themes. \n Gameplay involves exploration, light platforming, and puzzle-solving, with Gris gaining new abilities as the story progresses. It received critical acclaim for its artistic design and emotional depth.",
        platforms = ["Android", "iOS", "Linux", "Mac", "Nintendo Switch", "PC (Microsoft Windows)", "PlayStation 4", "Xbox One"],
        releaseDate = "2017",
        screenshots = [
            "https://images.igdb.com/igdb/image/upload/t_720p/r6zh3o4ot1ora3oaxzfk.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/ka9fgqhas5sio9tx2u00.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/feuprow76l4jfydxc3ku.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/dbfw8bia3n8vvpnax8fh.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/oazo3tuykdhwbndvisb5.webp",
            "https://images.igdb.com/igdb/image/upload/t_720p/oyxvfyzqcnyyhwcdjtjg.webp"
        ],
        artworkUrl = "https://images.igdb.com/igdb/image/upload/t_720p/arbue.webpp"
    )
]

# Função para obter todos os jogos
def get_all_games():
    # Converte todos os jogos da lista para dicionários
    return [OrderedDict(game.model_dump()) for game in game_list]

# Função para obter um jogo por ID
def get_game_by_id(game_id):
    for game in game_list:
        if game.id == game_id:
            # Converte o jogo encontrado em dicionário
            return OrderedDict(game.model_dump())
    return None  # Retorna None caso o jogo não exista

@app.get("/games", response_model=List[Game])
def read_games():
    games = get_all_games()
    return games

@app.get("/games/{game_id}", response_model=Game)
def read_game(game_id: int):
    game = get_game_by_id(game_id)
    if game:
        return game
    else:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")