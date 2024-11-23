import os
from playwright.sync_api import sync_playwright
from tqdm import tqdm

# البيانات
s = [
    {
        "id": "dce4c9f5f5dcb6a28ee07b39",
        "tags": [
            "sage",
            "beige",
            "brown",
            "orange",
            "nature",
            "vintage",
            "warm",
            "food"
        ],
        "colors": [
            "dce4c9",
            "f5f5dc",
            "b6a28e",
            "e07b39"
        ]
    },
    {
        "id": "432e544b4376ae445ae8bcb9",
        "tags": [
            "black",
            "navy",
            "maroon",
            "peach",
            "night",
            "dark",
            "halloween"
        ],
        "colors": [
            "432e54",
            "4b4376",
            "ae445a",
            "e8bcb9"
        ]
    },
    {
        "id": "fff7d18b5dff6a42c2563a9c",
        "tags": [
            "yellow",
            "purple",
            "retro",
            "neon",
            "kids"
        ],
        "colors": [
            "fff7d1",
            "8b5dff",
            "6a42c2",
            "563a9c"
        ]
    },
    {
        "id": "c2ffc79edf9c62825d526e48",
        "tags": [
            "green",
            "summer",
            "nature"
        ],
        "colors": [
            "c2ffc7",
            "9edf9c",
            "62825d",
            "526e48"
        ]
    },
    {
        "id": "faf6e3d8dbbdb59f782a3663",
        "tags": [
            "beige",
            "sage",
            "brown",
            "navy",
            "vintage",
            "earth"
        ],
        "colors": [
            "faf6e3",
            "d8dbbd",
            "b59f78",
            "2a3663"
        ]
    },
    {
        "id": "ff80004c1f7a219b9deeeeee",
        "tags": [
            "orange",
            "purple",
            "teal",
            "grey",
            "retro",
            "kids"
        ],
        "colors": [
            "ff8000",
            "4c1f7a",
            "219b9d",
            "eeeeee"
        ]
    },
    {
        "id": "fef3e2fab12ffa812ffa4032",
        "tags": [
            "peach",
            "orange",
            "red",
            "gold",
            "happy",
            "warm"
        ],
        "colors": [
            "fef3e2",
            "fab12f",
            "fa812f",
            "fa4032"
        ]
    },
    {
        "id": "a6aebfc5d3e8d0e8c5fff8de",
        "tags": [
            "grey",
            "blue",
            "green",
            "yellow",
            "pastel",
            "light",
            "cream",
            "kids"
        ],
        "colors": [
            "a6aebf",
            "c5d3e8",
            "d0e8c5",
            "fff8de"
        ]
    },
    {
        "id": "3c552dca7373d7b26deee2b5",
        "tags": [
            "green",
            "peach",
            "beige",
            "yellow",
            "nature",
            "food",
            "vintage",
            "christmas"
        ],
        "colors": [
            "3c552d",
            "ca7373",
            "d7b26d",
            "eee2b5"
        ]
    },
    {
        "id": "1a1a1d3b1c326a1e55a64d79",
        "tags": [
            "black",
            "maroon",
            "purple",
            "pink",
            "dark",
            "night",
            "gradient",
            "halloween"
        ],
        "colors": [
            "1a1a1d",
            "3b1c32",
            "6a1e55",
            "a64d79"
        ]
    },
    {
        "id": "cb9df0f0c1e1fddbbbfff9bf",
        "tags": [
            "purple",
            "pink",
            "orange",
            "yellow",
            "pastel",
            "light",
            "spring",
            "sunset",
            "kids",
            "happy"
        ],
        "colors": [
            "cb9df0",
            "f0c1e1",
            "fddbbb",
            "fff9bf"
        ]
    },
    {
        "id": "3d5300abba7cffe31af09319",
        "tags": [
            "green",
            "sage",
            "yellow",
            "orange",
            "happy",
            "nature",
            "food"
        ],
        "colors": [
            "3d5300",
            "abba7c",
            "ffe31a",
            "f09319"
        ]
    },
    {
        "id": "000b58003161006a67fff4b7",
        "tags": [
            "navy",
            "teal",
            "yellow",
            "night",
            "winter",
            "dark",
            "cold",
            "wedding"
        ],
        "colors": [
            "000b58",
            "003161",
            "006a67",
            "fff4b7"
        ]
    },
    {
        "id": "fcf596fbd288ff9c73ff4545",
        "tags": [
            "yellow",
            "orange",
            "peach",
            "red",
            "gold",
            "warm",
            "gradient"
        ],
        "colors": [
            "fcf596",
            "fbd288",
            "ff9c73",
            "ff4545"
        ]
    },
    {
        "id": "c6e7ffd4f6fffbfbfbffddae",
        "tags": [
            "blue",
            "white",
            "beige",
            "sky",
            "light",
            "pastel",
            "kids",
            "wedding",
            "vintage"
        ],
        "colors": [
            "c6e7ff",
            "d4f6ff",
            "fbfbfb",
            "ffddae"
        ]
    },
    {
        "id": "7ed4add76c82b030523d0301",
        "tags": [
            "green",
            "pink",
            "red",
            "maroon",
            "retro"
        ],
        "colors": [
            "7ed4ad",
            "d76c82",
            "b03052",
            "3d0301"
        ]
    },
    {
        "id": "bfecffcdc1fffff6e3ffccea",
        "tags": [
            "blue",
            "purple",
            "yellow",
            "pink",
            "kids",
            "light",
            "pastel",
            "spring",
            "happy"
        ],
        "colors": [
            "bfecff",
            "cdc1ff",
            "fff6e3",
            "ffccea"
        ]
    },
    {
        "id": "740938af1740cc2b52de7c7d",
        "tags": [
            "maroon",
            "red",
            "peach",
            "gradient",
            "warm",
            "halloween"
        ],
        "colors": [
            "740938",
            "af1740",
            "cc2b52",
            "de7c7d"
        ]
    },
    {
        "id": "f3f3e0133e87608bc1cbdceb",
        "tags": [
            "beige",
            "navy",
            "blue",
            "sea",
            "winter",
            "cold"
        ],
        "colors": [
            "f3f3e0",
            "133e87",
            "608bc1",
            "cbdceb"
        ]
    },
    {
        "id": "1a1a1931511e859f3df6fcdf",
        "tags": [
            "brown",
            "green",
            "sage",
            "white",
            "food",
            "nature",
            "gradient",
            "vintage"
        ],
        "colors": [
            "1a1a19",
            "31511e",
            "859f3d",
            "f6fcdf"
        ]
    },
    {
        "id": "ffb38effcf9dffb26fde8f5f",
        "tags": [
            "peach",
            "orange",
            "brown",
            "skin",
            "warm",
            "pastel"
        ],
        "colors": [
            "ffb38e",
            "ffcf9d",
            "ffb26f",
            "de8f5f"
        ]
    },
    {
        "id": "dff2ebb9e5e87ab2d34a628a",
        "tags": [
            "blue",
            "navy",
            "sea",
            "gradient",
            "cold"
        ],
        "colors": [
            "dff2eb",
            "b9e5e8",
            "7ab2d3",
            "4a628a"
        ]
    },
    {
        "id": "3b1e549b7ebdd4bee4eeeeee",
        "tags": [
            "purple",
            "grey",
            "space",
            "gradient",
            "cold",
            "wedding"
        ],
        "colors": [
            "3b1e54",
            "9b7ebd",
            "d4bee4",
            "eeeeee"
        ]
    },
    {
        "id": "4c4b16898121e6c767f87a53",
        "tags": [
            "green",
            "sage",
            "yellow",
            "peach",
            "vintage",
            "fall",
            "nature",
            "food"
        ],
        "colors": [
            "4c4b16",
            "898121",
            "e6c767",
            "f87a53"
        ]
    },
    {
        "id": "37afe14cc9fef5f4b3fffecb",
        "tags": [
            "blue",
            "yellow",
            "sky",
            "light",
            "happy",
            "kids"
        ],
        "colors": [
            "37afe1",
            "4cc9fe",
            "f5f4b3",
            "fffecb"
        ]
    },
    {
        "id": "88c273fff1dbd4bdac536493",
        "tags": [
            "green",
            "beige",
            "navy",
            "vintage"
        ],
        "colors": [
            "88c273",
            "fff1db",
            "d4bdac",
            "536493"
        ]
    },
    {
        "id": "b1d690feec37ffa24cff77b7",
        "tags": [
            "sage",
            "yellow",
            "orange",
            "pink",
            "retro",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "b1d690",
            "feec37",
            "ffa24c",
            "ff77b7"
        ]
    },
    {
        "id": "c4e1f6feee91ffbd73ff9d3d",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "kids",
            "light",
            "summer"
        ],
        "colors": [
            "c4e1f6",
            "feee91",
            "ffbd73",
            "ff9d3d"
        ]
    },
    {
        "id": "e9eed9cbd2a49a7e6f54473f",
        "tags": [
            "sage",
            "green",
            "brown",
            "food",
            "earth",
            "nature",
            "gradient",
            "vintage",
            "winter"
        ],
        "colors": [
            "e9eed9",
            "cbd2a4",
            "9a7e6f",
            "54473f"
        ]
    },
    {
        "id": "a2d2dff6efbde4c087bc7c7c",
        "tags": [
            "blue",
            "red",
            "beige",
            "yellow",
            "peach",
            "summer",
            "pastel"
        ],
        "colors": [
            "a2d2df",
            "f6efbd",
            "e4c087",
            "bc7c7c"
        ]
    },
    {
        "id": "789dbcffe3e3fef9f2c9e9d2",
        "tags": [
            "blue",
            "peach",
            "white",
            "green",
            "pastel",
            "light",
            "kids",
            "wedding"
        ],
        "colors": [
            "789dbc",
            "ffe3e3",
            "fef9f2",
            "c9e9d2"
        ]
    },
    {
        "id": "6056788abfa3ffbf61ffe6a5",
        "tags": [
            "purple",
            "sage",
            "orange",
            "beige",
            "vintage"
        ],
        "colors": [
            "605678",
            "8abfa3",
            "ffbf61",
            "ffe6a5"
        ]
    },
    {
        "id": "e4e0e1d6c0b3ab886d493628",
        "tags": [
            "grey",
            "brown",
            "coffee",
            "skin",
            "gradient",
            "pastel",
            "earth",
            "fall",
            "food"
        ],
        "colors": [
            "e4e0e1",
            "d6c0b3",
            "ab886d",
            "493628"
        ]
    },
    {
        "id": "0d92f477cdfff95454c62e2e",
        "tags": [
            "blue",
            "red",
            "maroon",
            "retro",
            "happy"
        ],
        "colors": [
            "0d92f4",
            "77cdff",
            "f95454",
            "c62e2e"
        ]
    },
    {
        "id": "091057024caaec8305dbd3d3",
        "tags": [
            "navy",
            "blue",
            "orange",
            "grey",
            "retro",
            "space"
        ],
        "colors": [
            "091057",
            "024caa",
            "ec8305",
            "dbd3d3"
        ]
    },
    {
        "id": "00ff9cb6ffa1feffa7ffe700",
        "tags": [
            "mint",
            "green",
            "yellow",
            "light",
            "neon",
            "summer",
            "kids"
        ],
        "colors": [
            "00ff9c",
            "b6ffa1",
            "feffa7",
            "ffe700"
        ]
    },
    {
        "id": "f4f6fff3c623eb831710375c",
        "tags": [
            "white",
            "grey",
            "yellow",
            "orange",
            "navy",
            "retro",
            "gold",
            "wedding"
        ],
        "colors": [
            "f4f6ff",
            "f3c623",
            "eb8317",
            "10375c"
        ]
    },
    {
        "id": "fff100006bff08c2ffbcf2f6",
        "tags": [
            "yellow",
            "blue",
            "kids",
            "happy",
            "sky"
        ],
        "colors": [
            "fff100",
            "006bff",
            "08c2ff",
            "bcf2f6"
        ]
    },
    {
        "id": "243642387478629584e2f1e7",
        "tags": [
            "black",
            "teal",
            "sage",
            "gradient",
            "night"
        ],
        "colors": [
            "243642",
            "387478",
            "629584",
            "e2f1e7"
        ]
    },
    {
        "id": "257180f2e5bffd8b51cb6040",
        "tags": [
            "teal",
            "beige",
            "orange",
            "vintage",
            "wedding"
        ],
        "colors": [
            "257180",
            "f2e5bf",
            "fd8b51",
            "cb6040"
        ]
    },
    {
        "id": "a5b68decdfccfcfaeeda8359",
        "tags": [
            "sage",
            "peach",
            "beige",
            "orange",
            "pastel",
            "vintage",
            "earth",
            "food",
            "fall"
        ],
        "colors": [
            "a5b68d",
            "ecdfcc",
            "fcfaee",
            "da8359"
        ]
    },
    {
        "id": "798645fefae0f2eed7626f47",
        "tags": [
            "sage",
            "white",
            "beige",
            "green",
            "earth",
            "nature"
        ],
        "colors": [
            "798645",
            "fefae0",
            "f2eed7",
            "626f47"
        ]
    },
    {
        "id": "72bf78a0d683d3ee98feff9f",
        "tags": [
            "green",
            "yellow",
            "light",
            "gradient",
            "happy",
            "summer"
        ],
        "colors": [
            "72bf78",
            "a0d683",
            "d3ee98",
            "feff9f"
        ]
    },
    {
        "id": "fff7d1ffecc8ffd09bffb0b0",
        "tags": [
            "yellow",
            "beige",
            "orange",
            "peach",
            "pastel",
            "warm",
            "food",
            "sunset",
            "gradient",
            "light"
        ],
        "colors": [
            "fff7d1",
            "ffecc8",
            "ffd09b",
            "ffb0b0"
        ]
    },
    {
        "id": "a66e38ffad60ffeead96ceb4",
        "tags": [
            "brown",
            "orange",
            "yellow",
            "teal",
            "kids",
            "summer",
            "nature"
        ],
        "colors": [
            "a66e38",
            "ffad60",
            "ffeead",
            "96ceb4"
        ]
    },
    {
        "id": "ff65001e3e620b192c000000",
        "tags": [
            "orange",
            "blue",
            "navy",
            "black",
            "dark",
            "space",
            "halloween"
        ],
        "colors": [
            "ff6500",
            "1e3e62",
            "0b192c",
            "000000"
        ]
    },
    {
        "id": "4338787e60bfe4b1f0ffe1ff",
        "tags": [
            "purple",
            "pink",
            "space",
            "cold",
            "wedding"
        ],
        "colors": [
            "433878",
            "7e60bf",
            "e4b1f0",
            "ffe1ff"
        ]
    },
    {
        "id": "b7e0fffff5cdffcfb3e78f81",
        "tags": [
            "blue",
            "yellow",
            "peach",
            "red",
            "kids",
            "light",
            "rainbow",
            "happy",
            "summer"
        ],
        "colors": [
            "b7e0ff",
            "fff5cd",
            "ffcfb3",
            "e78f81"
        ]
    },
    {
        "id": "d2ff7273ec8b54c39215b392",
        "tags": [
            "green",
            "teal",
            "neon",
            "summer",
            "gradient",
            "kids",
            "happy"
        ],
        "colors": [
            "d2ff72",
            "73ec8b",
            "54c392",
            "15b392"
        ]
    },
    {
        "id": "87a2ffc4d7ffffd7c4fff4b5",
        "tags": [
            "blue",
            "peach",
            "yellow",
            "kids",
            "light",
            "summer"
        ],
        "colors": [
            "87a2ff",
            "c4d7ff",
            "ffd7c4",
            "fff4b5"
        ]
    },
    {
        "id": "eddfe0f5f5f7b7b7b7705c53",
        "tags": [
            "peach",
            "grey",
            "brown",
            "vintage",
            "pastel"
        ],
        "colors": [
            "eddfe0",
            "f5f5f7",
            "b7b7b7",
            "705c53"
        ]
    },
    {
        "id": "faf7f0d8d2c2b174574a4947",
        "tags": [
            "white",
            "beige",
            "brown",
            "black",
            "earth",
            "vintage",
            "warm",
            "fall",
            "skin",
            "wedding",
            "coffee"
        ],
        "colors": [
            "faf7f0",
            "d8d2c2",
            "b17457",
            "4a4947"
        ]
    },
    {
        "id": "347928c0eba6fffbe6fccd2a",
        "tags": [
            "green",
            "mint",
            "white",
            "yellow",
            "summer",
            "nature",
            "food",
            "happy"
        ],
        "colors": [
            "347928",
            "c0eba6",
            "fffbe6",
            "fccd2a"
        ]
    },
    {
        "id": "001f3f3a6d8c6a9ab0ead8b1",
        "tags": [
            "navy",
            "blue",
            "beige",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "001f3f",
            "3a6d8c",
            "6a9ab0",
            "ead8b1"
        ]
    },
    {
        "id": "e7ccccede8dca5b68dc1cfa1",
        "tags": [
            "pink",
            "peach",
            "grey",
            "sage",
            "green",
            "beige",
            "pastel",
            "vintage",
            "light",
            "spring",
            "food"
        ],
        "colors": [
            "e7cccc",
            "ede8dc",
            "a5b68d",
            "c1cfa1"
        ]
    },
    {
        "id": "640d5fd91656ee66a6ffeb55",
        "tags": [
            "maroon",
            "purple",
            "red",
            "pink",
            "yellow",
            "neon",
            "retro",
            "kids"
        ],
        "colors": [
            "640d5f",
            "d91656",
            "ee66a6",
            "ffeb55"
        ]
    },
    {
        "id": "e5d9f2f5efffcdc1ffa594f9",
        "tags": [
            "purple",
            "cold",
            "light",
            "pastel",
            "sky"
        ],
        "colors": [
            "e5d9f2",
            "f5efff",
            "cdc1ff",
            "a594f9"
        ]
    },
    {
        "id": "fff0d17957576643433b3030",
        "tags": [
            "beige",
            "brown",
            "cream",
            "coffee",
            "skin",
            "vintage"
        ],
        "colors": [
            "fff0d1",
            "795757",
            "664343",
            "3b3030"
        ]
    },
    {
        "id": "6256ca86d293c1e2a4fdfad9",
        "tags": [
            "blue",
            "green",
            "yellow",
            "kids",
            "happy",
            "retro"
        ],
        "colors": [
            "6256ca",
            "86d293",
            "c1e2a4",
            "fdfad9"
        ]
    },
    {
        "id": "384b70507687fcfaeeb8001f",
        "tags": [
            "navy",
            "white",
            "red",
            "retro",
            "christmas",
            "winter"
        ],
        "colors": [
            "384b70",
            "507687",
            "fcfaee",
            "b8001f"
        ]
    },
    {
        "id": "ff6600f5f5f58fd14f604cc3",
        "tags": [
            "orange",
            "white",
            "grey",
            "green",
            "blue",
            "retro",
            "kids",
            "happy"
        ],
        "colors": [
            "ff6600",
            "f5f5f5",
            "8fd14f",
            "604cc3"
        ]
    },
    {
        "id": "4379f2ffeb006ec207117554",
        "tags": [
            "blue",
            "yellow",
            "green",
            "kids",
            "happy"
        ],
        "colors": [
            "4379f2",
            "ffeb00",
            "6ec207",
            "117554"
        ]
    },
    {
        "id": "181c143c3d37697565ecdfcc",
        "tags": [
            "black",
            "grey",
            "teal",
            "beige",
            "night",
            "dark",
            "winter"
        ],
        "colors": [
            "181c14",
            "3c3d37",
            "697565",
            "ecdfcc"
        ]
    },
    {
        "id": "6439ff4f75ff00ccdd7cf5ff",
        "tags": [
            "blue",
            "mint",
            "sea",
            "cold",
            "gradient"
        ],
        "colors": [
            "6439ff",
            "4f75ff",
            "00ccdd",
            "7cf5ff"
        ]
    },
    {
        "id": "624e888967b3cb80abe6d9a2",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "warm",
            "sunset",
            "pastel",
            "gradient",
            "wedding"
        ],
        "colors": [
            "624e88",
            "8967b3",
            "cb80ab",
            "e6d9a2"
        ]
    },
    {
        "id": "c96868fadfa1fff4ea7eacb5",
        "tags": [
            "red",
            "yellow",
            "peach",
            "teal",
            "vintage",
            "pastel",
            "rainbow",
            "kids"
        ],
        "colors": [
            "c96868",
            "fadfa1",
            "fff4ea",
            "7eacb5"
        ]
    },
    {
        "id": "d2e0fbfef9d9dee5d48eaccd",
        "tags": [
            "blue",
            "yellow",
            "pastel",
            "light",
            "sky",
            "wedding",
            "summer"
        ],
        "colors": [
            "d2e0fb",
            "fef9d9",
            "dee5d4",
            "8eaccd"
        ]
    },
    {
        "id": "ff885bffe5cf557c5633372c",
        "tags": [
            "orange",
            "green",
            "black",
            "nature",
            "food"
        ],
        "colors": [
            "ff885b",
            "ffe5cf",
            "557c56",
            "33372c"
        ]
    },
    {
        "id": "654520825b326cbec781dae3",
        "tags": [
            "brown",
            "blue",
            "vintage",
            "wedding"
        ],
        "colors": [
            "654520",
            "825b32",
            "6cbec7",
            "81dae3"
        ]
    },
    {
        "id": "1230ae6c48c5c68fe6fff7f7",
        "tags": [
            "blue",
            "purple",
            "white",
            "peach",
            "space",
            "gradient",
            "cold"
        ],
        "colors": [
            "1230ae",
            "6c48c5",
            "c68fe6",
            "fff7f7"
        ]
    },
    {
        "id": "f5f7f8fcde70e8b86d185519",
        "tags": [
            "white",
            "grey",
            "yellow",
            "beige",
            "green",
            "vintage",
            "food"
        ],
        "colors": [
            "f5f7f8",
            "fcde70",
            "e8b86d",
            "185519"
        ]
    },
    {
        "id": "16423c6a9c89c4dad2e9efec",
        "tags": [
            "teal",
            "green",
            "grey",
            "gradient",
            "cold"
        ],
        "colors": [
            "16423c",
            "6a9c89",
            "c4dad2",
            "e9efec"
        ]
    },
    {
        "id": "343131a04747d8a25eeedf7a",
        "tags": [
            "black",
            "red",
            "maroon",
            "orange",
            "yellow",
            "gold",
            "gradient",
            "warm",
            "halloween"
        ],
        "colors": [
            "343131",
            "a04747",
            "d8a25e",
            "eedf7a"
        ]
    },
    {
        "id": "161d6f0b2f9f98ded9c7ffd8",
        "tags": [
            "navy",
            "blue",
            "teal",
            "mint",
            "cold",
            "winter",
            "sea",
            "gradient"
        ],
        "colors": [
            "161d6f",
            "0b2f9f",
            "98ded9",
            "c7ffd8"
        ]
    },
    {
        "id": "16325b227b9478b7d0ffdc7f",
        "tags": [
            "navy",
            "teal",
            "blue",
            "yellow",
            "sea",
            "winter"
        ],
        "colors": [
            "16325b",
            "227b94",
            "78b7d0",
            "ffdc7f"
        ]
    },
    {
        "id": "f5f5f548cfcb229799424242",
        "tags": [
            "grey",
            "teal",
            "black",
            "cold",
            "retro"
        ],
        "colors": [
            "f5f5f5",
            "48cfcb",
            "229799",
            "424242"
        ]
    },
    {
        "id": "bf2ef0ed3ef7feecb3fff6ea",
        "tags": [
            "purple",
            "yellow",
            "beige",
            "kids"
        ],
        "colors": [
            "bf2ef0",
            "ed3ef7",
            "feecb3",
            "fff6ea"
        ]
    },
    {
        "id": "295f98cdc2a5e1d7c6eae4dd",
        "tags": [
            "blue",
            "beige",
            "grey",
            "wedding",
            "vintage",
            "pastel"
        ],
        "colors": [
            "295f98",
            "cdc2a5",
            "e1d7c6",
            "eae4dd"
        ]
    },
    {
        "id": "a1d6b2cedf9ff1f3c2e8b86d",
        "tags": [
            "mint",
            "sage",
            "beige",
            "orange",
            "pastel",
            "light",
            "nature",
            "summer",
            "food"
        ],
        "colors": [
            "a1d6b2",
            "cedf9f",
            "f1f3c2",
            "e8b86d"
        ]
    },
    {
        "id": "fff8e8f7eed3aab396674636",
        "tags": [
            "beige",
            "sage",
            "brown",
            "vintage",
            "nature",
            "fall",
            "food",
            "warm",
            "earth"
        ],
        "colors": [
            "fff8e8",
            "f7eed3",
            "aab396",
            "674636"
        ]
    },
    {
        "id": "7695ff9dbdffffd7c4ff9874",
        "tags": [
            "blue",
            "peach",
            "orange",
            "kids",
            "retro",
            "wedding"
        ],
        "colors": [
            "7695ff",
            "9dbdff",
            "ffd7c4",
            "ff9874"
        ]
    },
    {
        "id": "ffeac5ffdbb56c4e31603f26",
        "tags": [
            "beige",
            "brown",
            "fall",
            "skin",
            "coffee",
            "warm",
            "vintage"
        ],
        "colors": [
            "ffeac5",
            "ffdbb5",
            "6c4e31",
            "603f26"
        ]
    },
    {
        "id": "ffbe98f05a7e125b9a0b8494",
        "tags": [
            "orange",
            "peach",
            "pink",
            "blue",
            "teal",
            "kids",
            "retro"
        ],
        "colors": [
            "ffbe98",
            "f05a7e",
            "125b9a",
            "0b8494"
        ]
    },
    {
        "id": "fabc3fe85c0dc7253e821131",
        "tags": [
            "yellow",
            "orange",
            "red",
            "maroon",
            "gold",
            "warm",
            "gradient"
        ],
        "colors": [
            "fabc3f",
            "e85c0d",
            "c7253e",
            "821131"
        ]
    },
    {
        "id": "7c93c355679c1e2a5ee1d7b7",
        "tags": [
            "blue",
            "navy",
            "beige",
            "winter",
            "sea",
            "wedding"
        ],
        "colors": [
            "7c93c3",
            "55679c",
            "1e2a5e",
            "e1d7b7"
        ]
    },
    {
        "id": "cd5c08fff5e4c1d8c36a9c89",
        "tags": [
            "orange",
            "white",
            "sage",
            "teal",
            "nature",
            "vintage",
            "wedding",
            "christmas",
            "food"
        ],
        "colors": [
            "cd5c08",
            "fff5e4",
            "c1d8c3",
            "6a9c89"
        ]
    },
    {
        "id": "0d7c6641b3a2bde8cad7c3f1",
        "tags": [
            "teal",
            "green",
            "purple",
            "retro",
            "kids"
        ],
        "colors": [
            "0d7c66",
            "41b3a2",
            "bde8ca",
            "d7c3f1"
        ]
    },
    {
        "id": "c0c78ca6b37dfefae0b99470",
        "tags": [
            "sage",
            "yellow",
            "white",
            "brown",
            "earth",
            "nature",
            "kids",
            "food",
            "summer",
            "vintage",
            "pastel"
        ],
        "colors": [
            "c0c78c",
            "a6b37d",
            "fefae0",
            "b99470"
        ]
    },
    {
        "id": "2e073f7a1cacad49e1ebd3f8",
        "tags": [
            "black",
            "purple",
            "night",
            "space",
            "dark",
            "gradient",
            "halloween"
        ],
        "colors": [
            "2e073f",
            "7a1cac",
            "ad49e1",
            "ebd3f8"
        ]
    },
    {
        "id": "ff8a8af4deb3f0eaaccce0ac",
        "tags": [
            "peach",
            "red",
            "beige",
            "yellow",
            "sage",
            "kids",
            "pastel",
            "light",
            "happy",
            "spring"
        ],
        "colors": [
            "ff8a8a",
            "f4deb3",
            "f0eaac",
            "cce0ac"
        ]
    },
    {
        "id": "00712dd5ed9ffffbe6ff9100",
        "tags": [
            "green",
            "white",
            "orange",
            "summer",
            "happy",
            "nature"
        ],
        "colors": [
            "00712d",
            "d5ed9f",
            "fffbe6",
            "ff9100"
        ]
    },
    {
        "id": "1e201e3c3d37697565ecdfcc",
        "tags": [
            "black",
            "sage",
            "grey",
            "beige",
            "night",
            "dark",
            "gradient",
            "halloween"
        ],
        "colors": [
            "1e201e",
            "3c3d37",
            "697565",
            "ecdfcc"
        ]
    },
    {
        "id": "3a10784e31aa3795bdf7f7f8",
        "tags": [
            "purple",
            "blue",
            "white",
            "gradient",
            "cold"
        ],
        "colors": [
            "3a1078",
            "4e31aa",
            "3795bd",
            "f7f7f8"
        ]
    },
    {
        "id": "800000982b1cdad4b5f2e8c6",
        "tags": [
            "maroon",
            "red",
            "beige",
            "warm",
            "wedding",
            "vintage"
        ],
        "colors": [
            "800000",
            "982b1c",
            "dad4b5",
            "f2e8c6"
        ]
    },
    {
        "id": "f7efe5e2bfd9c8a1e0674188",
        "tags": [
            "beige",
            "purple",
            "gradient",
            "kids",
            "wedding"
        ],
        "colors": [
            "f7efe5",
            "e2bfd9",
            "c8a1e0",
            "674188"
        ]
    },
    {
        "id": "a28b5586ab89cbe2b5e7fbe6",
        "tags": [
            "brown",
            "teal",
            "sage",
            "mint",
            "earth",
            "nature",
            "pastel",
            "light",
            "kids",
            "food"
        ],
        "colors": [
            "a28b55",
            "86ab89",
            "cbe2b5",
            "e7fbe6"
        ]
    },
    {
        "id": "d1e9f6f6eacbf1d3ceeecad5",
        "tags": [
            "blue",
            "yellow",
            "beige",
            "peach",
            "pastel",
            "kids",
            "light",
            "rainbow",
            "happy",
            "spring"
        ],
        "colors": [
            "d1e9f6",
            "f6eacb",
            "f1d3ce",
            "eecad5"
        ]
    },
    {
        "id": "f9dbba5b99c21a48701f316f",
        "tags": [
            "beige",
            "blue",
            "navy",
            "sea",
            "wedding",
            "retro"
        ],
        "colors": [
            "f9dbba",
            "5b99c2",
            "1a4870",
            "1f316f"
        ]
    },
    {
        "id": "f8ede3dfd3c3d0b8a8c5705d",
        "tags": [
            "beige",
            "peach",
            "red",
            "warm",
            "gradient",
            "skin",
            "vintage",
            "pastel",
            "food",
            "cream"
        ],
        "colors": [
            "f8ede3",
            "dfd3c3",
            "d0b8a8",
            "c5705d"
        ]
    },
    {
        "id": "a02334ffad60ffeead96ceb4",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "teal",
            "mint",
            "kids",
            "christmas",
            "retro",
            "rainbow"
        ],
        "colors": [
            "a02334",
            "ffad60",
            "ffeead",
            "96ceb4"
        ]
    },
    {
        "id": "ff8343f1dec6179bae4158a6",
        "tags": [
            "orange",
            "beige",
            "blue",
            "retro",
            "kids"
        ],
        "colors": [
            "ff8343",
            "f1dec6",
            "179bae",
            "4158a6"
        ]
    },
    {
        "id": "f6e96bbedc74a2ca71387f39",
        "tags": [
            "yellow",
            "green",
            "gradient",
            "nature",
            "summer",
            "kids"
        ],
        "colors": [
            "f6e96b",
            "bedc74",
            "a2ca71",
            "387f39"
        ]
    },
    {
        "id": "ccd5aee0e5b6faedcefefae0",
        "tags": [
            "sage",
            "peach",
            "beige",
            "pastel",
            "light",
            "happy",
            "nature",
            "cream",
            "spring",
            "food"
        ],
        "colors": [
            "ccd5ae",
            "e0e5b6",
            "faedce",
            "fefae0"
        ]
    },
    {
        "id": "b4d6cdffda76ff8c9eff4e88",
        "tags": [
            "teal",
            "yellow",
            "pink",
            "kids",
            "retro"
        ],
        "colors": [
            "b4d6cd",
            "ffda76",
            "ff8c9e",
            "ff4e88"
        ]
    },
    {
        "id": "921a40c75b7ad9ababf4d9d0",
        "tags": [
            "maroon",
            "pink",
            "peach",
            "food",
            "warm",
            "gradient"
        ],
        "colors": [
            "921a40",
            "c75b7a",
            "d9abab",
            "f4d9d0"
        ]
    },
    {
        "id": "f0a8d0f7b5caffc6c6ffebd4",
        "tags": [
            "pink",
            "peach",
            "beige",
            "light",
            "gradient",
            "sunset",
            "pastel",
            "skin",
            "kids"
        ],
        "colors": [
            "f0a8d0",
            "f7b5ca",
            "ffc6c6",
            "ffebd4"
        ]
    },
    {
        "id": "6482ad7fa1c3e2dad6f5eded",
        "tags": [
            "blue",
            "grey",
            "light",
            "cold",
            "wedding"
        ],
        "colors": [
            "6482ad",
            "7fa1c3",
            "e2dad6",
            "f5eded"
        ]
    },
    {
        "id": "bc9f8bb5cfb7cadabfe7e8d8",
        "tags": [
            "brown",
            "sage",
            "beige",
            "earth",
            "pastel",
            "vintage",
            "fall",
            "food",
            "light"
        ],
        "colors": [
            "bc9f8b",
            "b5cfb7",
            "cadabf",
            "e7e8d8"
        ]
    },
    {
        "id": "7c00fef9e400ffaf00f5004f",
        "tags": [
            "purple",
            "yellow",
            "red",
            "neon",
            "happy"
        ],
        "colors": [
            "7c00fe",
            "f9e400",
            "ffaf00",
            "f5004f"
        ]
    },
    {
        "id": "5222588c3061c63c51d95f59",
        "tags": [
            "purple",
            "maroon",
            "red",
            "orange",
            "warm",
            "dark",
            "night"
        ],
        "colors": [
            "522258",
            "8c3061",
            "c63c51",
            "d95f59"
        ]
    },
    {
        "id": "c9dabf9ca986808d7c5f6f65",
        "tags": [
            "sage",
            "pastel",
            "nature",
            "gradient",
            "vintage",
            "food"
        ],
        "colors": [
            "c9dabf",
            "9ca986",
            "808d7c",
            "5f6f65"
        ]
    },
    {
        "id": "1801614f1787eb3678fb773c",
        "tags": [
            "navy",
            "purple",
            "red",
            "pink",
            "orange",
            "retro",
            "dark",
            "night",
            "space"
        ],
        "colors": [
            "180161",
            "4f1787",
            "eb3678",
            "fb773c"
        ]
    },
    {
        "id": "02152603346e6eacdae2e2b6",
        "tags": [
            "black",
            "navy",
            "blue",
            "beige",
            "retro",
            "dark",
            "gradient"
        ],
        "colors": [
            "021526",
            "03346e",
            "6eacda",
            "e2e2b6"
        ]
    },
    {
        "id": "ffdfd6e3a5c7b692c2694f8e",
        "tags": [
            "peach",
            "pink",
            "purple",
            "gradient",
            "wedding"
        ],
        "colors": [
            "ffdfd6",
            "e3a5c7",
            "b692c2",
            "694f8e"
        ]
    },
    {
        "id": "f8ededff8225b43f3f173b45",
        "tags": [
            "white",
            "grey",
            "orange",
            "red",
            "black",
            "gold"
        ],
        "colors": [
            "f8eded",
            "ff8225",
            "b43f3f",
            "173b45"
        ]
    },
    {
        "id": "914f1edeac80f7dcb9b5c18e",
        "tags": [
            "brown",
            "beige",
            "sage",
            "green",
            "nature",
            "earth",
            "fall",
            "food"
        ],
        "colors": [
            "914f1e",
            "deac80",
            "f7dcb9",
            "b5c18e"
        ]
    },
    {
        "id": "fef3e2bec6a0708871606676",
        "tags": [
            "beige",
            "sage",
            "blue",
            "pastel",
            "vintage",
            "wedding"
        ],
        "colors": [
            "fef3e2",
            "bec6a0",
            "708871",
            "606676"
        ]
    },
    {
        "id": "201e43134b70508c9beeeeee",
        "tags": [
            "navy",
            "blue",
            "teal",
            "grey",
            "sea",
            "cold",
            "winter",
            "gradient"
        ],
        "colors": [
            "201e43",
            "134b70",
            "508c9b",
            "eeeeee"
        ]
    },
    {
        "id": "ef5a6ffff1dbd4bdac536493",
        "tags": [
            "red",
            "beige",
            "blue",
            "kids",
            "vintage"
        ],
        "colors": [
            "ef5a6f",
            "fff1db",
            "d4bdac",
            "536493"
        ]
    },
    {
        "id": "f6fb7ab4e38088d66c73bba3",
        "tags": [
            "yellow",
            "green",
            "teal",
            "nature",
            "light",
            "summer",
            "happy"
        ],
        "colors": [
            "f6fb7a",
            "b4e380",
            "88d66c",
            "73bba3"
        ]
    },
    {
        "id": "1a363640534c677d6ad6bd98",
        "tags": [
            "black",
            "sage",
            "beige",
            "dark",
            "gradient",
            "nature",
            "winter",
            "food"
        ],
        "colors": [
            "1a3636",
            "40534c",
            "677d6a",
            "d6bd98"
        ]
    },
    {
        "id": "f8ede3dfd3c3d0b8a88d493a",
        "tags": [
            "beige",
            "brown",
            "coffee",
            "skin",
            "warm",
            "pastel",
            "gradient"
        ],
        "colors": [
            "f8ede3",
            "dfd3c3",
            "d0b8a8",
            "8d493a"
        ]
    },
    {
        "id": "399918ecffe6ffaaaaff7777",
        "tags": [
            "green",
            "white",
            "peach",
            "red",
            "happy",
            "nature",
            "food",
            "kids",
            "vintage"
        ],
        "colors": [
            "399918",
            "ecffe6",
            "ffaaaa",
            "ff7777"
        ]
    },
    {
        "id": "17153b2e236c433d8bc8acd6",
        "tags": [
            "black",
            "navy",
            "purple",
            "space",
            "night",
            "dark",
            "gradient"
        ],
        "colors": [
            "17153b",
            "2e236c",
            "433d8b",
            "c8acd6"
        ]
    },
    {
        "id": "f3feb8ffde4dffb22cff4c4c",
        "tags": [
            "yellow",
            "orange",
            "red",
            "gold",
            "warm",
            "happy"
        ],
        "colors": [
            "f3feb8",
            "ffde4d",
            "ffb22c",
            "ff4c4c"
        ]
    },
    {
        "id": "987d9abb9ab1eeceb9fefbd8",
        "tags": [
            "purple",
            "peach",
            "yellow",
            "pastel",
            "light",
            "wedding",
            "gradient"
        ],
        "colors": [
            "987d9a",
            "bb9ab1",
            "eeceb9",
            "fefbd8"
        ]
    },
    {
        "id": "6c946fffd35affa823dc0083",
        "tags": [
            "sage",
            "yellow",
            "orange",
            "purple",
            "retro"
        ],
        "colors": [
            "6c946f",
            "ffd35a",
            "ffa823",
            "dc0083"
        ]
    },
    {
        "id": "ffb200eb5b00e4003ab60071",
        "tags": [
            "yellow",
            "orange",
            "red",
            "purple",
            "sunset",
            "gold",
            "warm"
        ],
        "colors": [
            "ffb200",
            "eb5b00",
            "e4003a",
            "b60071"
        ]
    },
    {
        "id": "77e4c836c2ce478ccf4535c1",
        "tags": [
            "mint",
            "blue",
            "sea",
            "gradient",
            "cold",
            "winter"
        ],
        "colors": [
            "77e4c8",
            "36c2ce",
            "478ccf",
            "4535c1"
        ]
    },
    {
        "id": "e9ff97ffd18effa38fff7ee2",
        "tags": [
            "yellow",
            "orange",
            "peach",
            "pink",
            "neon",
            "light",
            "spring",
            "happy"
        ],
        "colors": [
            "e9ff97",
            "ffd18e",
            "ffa38f",
            "ff7ee2"
        ]
    },
    {
        "id": "def9c49cdba650b498468585",
        "tags": [
            "green",
            "teal",
            "nature",
            "gradient"
        ],
        "colors": [
            "def9c4",
            "9cdba6",
            "50b498",
            "468585"
        ]
    },
    {
        "id": "405d72758694f7e7dcfff8f3",
        "tags": [
            "navy",
            "grey",
            "beige",
            "wedding",
            "vintage"
        ],
        "colors": [
            "405d72",
            "758694",
            "f7e7dc",
            "fff8f3"
        ]
    },
    {
        "id": "131842e68369ecceaefbf6e2",
        "tags": [
            "black",
            "orange",
            "beige",
            "retro"
        ],
        "colors": [
            "131842",
            "e68369",
            "ecceae",
            "fbf6e2"
        ]
    },
    {
        "id": "d6efd880af81508d4e1a5319",
        "tags": [
            "sage",
            "green",
            "nature",
            "gradient",
            "winter",
            "food"
        ],
        "colors": [
            "d6efd8",
            "80af81",
            "508d4e",
            "1a5319"
        ]
    },
    {
        "id": "dca47cffd3b6fcf8f3698474",
        "tags": [
            "peach",
            "white",
            "sage",
            "nature",
            "earth",
            "vintage",
            "wedding",
            "fall",
            "food"
        ],
        "colors": [
            "dca47c",
            "ffd3b6",
            "fcf8f3",
            "698474"
        ]
    },
    {
        "id": "4a249d009fbdf9e2aff6f5f5",
        "tags": [
            "purple",
            "blue",
            "teal",
            "yellow",
            "white",
            "grey",
            "retro"
        ],
        "colors": [
            "4a249d",
            "009fbd",
            "f9e2af",
            "f6f5f5"
        ]
    },
    {
        "id": "faffaf96c9f43fa2f60f67b1",
        "tags": [
            "yellow",
            "blue",
            "navy",
            "sky",
            "kids"
        ],
        "colors": [
            "faffaf",
            "96c9f4",
            "3fa2f6",
            "0f67b1"
        ]
    },
    {
        "id": "fff8dbffc7ed7d8abc304463",
        "tags": [
            "yellow",
            "beige",
            "pink",
            "blue",
            "navy",
            "kids",
            "wedding",
            "gradient"
        ],
        "colors": [
            "fff8db",
            "ffc7ed",
            "7d8abc",
            "304463"
        ]
    },
    {
        "id": "000000ff4191e90074fff078",
        "tags": [
            "black",
            "pink",
            "maroon",
            "yellow",
            "space"
        ],
        "colors": [
            "000000",
            "ff4191",
            "e90074",
            "fff078"
        ]
    },
    {
        "id": "eeedebe6b9a69391852f3645",
        "tags": [
            "grey",
            "peach",
            "sage",
            "black",
            "earth",
            "nature",
            "vintage",
            "fall",
            "food"
        ],
        "colors": [
            "eeedeb",
            "e6b9a6",
            "939185",
            "2f3645"
        ]
    },
    {
        "id": "36ba98e9c46af4a261e76f51",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "summer",
            "retro",
            "warm",
            "happy"
        ],
        "colors": [
            "36ba98",
            "e9c46a",
            "f4a261",
            "e76f51"
        ]
    },
    {
        "id": "667bc6fdffd2ffb4c2da7297",
        "tags": [
            "blue",
            "yellow",
            "pink",
            "kids",
            "vintage",
            "spring"
        ],
        "colors": [
            "667bc6",
            "fdffd2",
            "ffb4c2",
            "da7297"
        ]
    },
    {
        "id": "f5f7f8f4ce1437977745474b",
        "tags": [
            "white",
            "grey",
            "yellow",
            "green",
            "black",
            "retro"
        ],
        "colors": [
            "f5f7f8",
            "f4ce14",
            "379777",
            "45474b"
        ]
    },
    {
        "id": "07195208839537b7c3ebf4f6",
        "tags": [
            "navy",
            "blue",
            "teal",
            "white",
            "grey",
            "cold",
            "winter",
            "gradient",
            "sea"
        ],
        "colors": [
            "071952",
            "088395",
            "37b7c3",
            "ebf4f6"
        ]
    },
    {
        "id": "e7f0dc597445658147729762",
        "tags": [
            "grey",
            "sage",
            "green",
            "nature",
            "vintage",
            "pastel",
            "food"
        ],
        "colors": [
            "e7f0dc",
            "597445",
            "658147",
            "729762"
        ]
    },
    {
        "id": "ffe9d0fffed3bbe9ffb1afff",
        "tags": [
            "peach",
            "yellow",
            "blue",
            "purple",
            "pastel",
            "light",
            "kids",
            "happy",
            "rainbow",
            "spring"
        ],
        "colors": [
            "ffe9d0",
            "fffed3",
            "bbe9ff",
            "b1afff"
        ]
    },
    {
        "id": "a0937de7d4b5f6e6cbb6c7aa",
        "tags": [
            "brown",
            "beige",
            "sage",
            "nature",
            "food",
            "earth",
            "pastel",
            "vintage",
            "light",
            "fall"
        ],
        "colors": [
            "a0937d",
            "e7d4b5",
            "f6e6cb",
            "b6c7aa"
        ]
    },
    {
        "id": "973131e0a75ef9d689f5e7b2",
        "tags": [
            "maroon",
            "orange",
            "yellow",
            "beige",
            "warm",
            "gold",
            "food",
            "gradient"
        ],
        "colors": [
            "973131",
            "e0a75e",
            "f9d689",
            "f5e7b2"
        ]
    },
    {
        "id": "402e7a4c3bcf4b70f53dc2ec",
        "tags": [
            "navy",
            "blue",
            "sea",
            "dark",
            "gradient",
            "cold"
        ],
        "colors": [
            "402e7a",
            "4c3bcf",
            "4b70f5",
            "3dc2ec"
        ]
    },
    {
        "id": "91ddcff7f9f2e8c5e5f19ed2",
        "tags": [
            "teal",
            "mint",
            "white",
            "pink",
            "kids",
            "pastel",
            "happy",
            "light"
        ],
        "colors": [
            "91ddcf",
            "f7f9f2",
            "e8c5e5",
            "f19ed2"
        ]
    },
    {
        "id": "5a639c7776b39b86bde2bbe9",
        "tags": [
            "navy",
            "purple",
            "retro",
            "gradient",
            "cold"
        ],
        "colors": [
            "5a639c",
            "7776b3",
            "9b86bd",
            "e2bbe9"
        ]
    },
    {
        "id": "ff7f3efff6e980c4e9604cc3",
        "tags": [
            "orange",
            "beige",
            "white",
            "blue",
            "purple",
            "retro",
            "kids"
        ],
        "colors": [
            "ff7f3e",
            "fff6e9",
            "80c4e9",
            "604cc3"
        ]
    },
    {
        "id": "219c90fff455ffc700ee4e4e",
        "tags": [
            "teal",
            "yellow",
            "red",
            "happy",
            "retro"
        ],
        "colors": [
            "219c90",
            "fff455",
            "ffc700",
            "ee4e4e"
        ]
    },
    {
        "id": "fff5e1ff6969c800360c1844",
        "tags": [
            "beige",
            "red",
            "maroon",
            "black",
            "warm",
            "christmas"
        ],
        "colors": [
            "fff5e1",
            "ff6969",
            "c80036",
            "0c1844"
        ]
    },
    {
        "id": "102c571679abffb1b1ffcbcb",
        "tags": [
            "navy",
            "blue",
            "peach",
            "pink",
            "vintage",
            "wedding"
        ],
        "colors": [
            "102c57",
            "1679ab",
            "ffb1b1",
            "ffcbcb"
        ]
    },
    {
        "id": "05921206d0019bec00f3ff90",
        "tags": [
            "green",
            "yellow",
            "nature",
            "gradient",
            "neon",
            "happy"
        ],
        "colors": [
            "059212",
            "06d001",
            "9bec00",
            "f3ff90"
        ]
    },
    {
        "id": "d8efd395d2b355ad9bf1f8e8",
        "tags": [
            "green",
            "sage",
            "pastel",
            "food",
            "kids",
            "light"
        ],
        "colors": [
            "d8efd3",
            "95d2b3",
            "55ad9b",
            "f1f8e8"
        ]
    },
    {
        "id": "365e3281a263e7d37ffd9b63",
        "tags": [
            "green",
            "sage",
            "yellow",
            "orange",
            "nature",
            "summer",
            "food",
            "christmas"
        ],
        "colors": [
            "365e32",
            "81a263",
            "e7d37f",
            "fd9b63"
        ]
    },
    {
        "id": "ef9c66fcdc94c8cfa078aba8",
        "tags": [
            "orange",
            "yellow",
            "sage",
            "blue",
            "pastel",
            "kids",
            "spring"
        ],
        "colors": [
            "ef9c66",
            "fcdc94",
            "c8cfa0",
            "78aba8"
        ]
    },
    {
        "id": "ffde95add899bc5a94f075aa",
        "tags": [
            "beige",
            "yellow",
            "green",
            "purple",
            "pink",
            "retro",
            "spring",
            "nature"
        ],
        "colors": [
            "ffde95",
            "add899",
            "bc5a94",
            "f075aa"
        ]
    },
    {
        "id": "fdffe283b4ff5a72a01a2130",
        "tags": [
            "yellow",
            "blue",
            "navy",
            "black",
            "sea"
        ],
        "colors": [
            "fdffe2",
            "83b4ff",
            "5a72a0",
            "1a2130"
        ]
    },
    {
        "id": "5383926295a280b9adb3e2a7",
        "tags": [
            "teal",
            "green",
            "gradient",
            "sea",
            "cold",
            "winter"
        ],
        "colors": [
            "538392",
            "6295a2",
            "80b9ad",
            "b3e2a7"
        ]
    },
    {
        "id": "e88d67f3f7ec006989005c78",
        "tags": [
            "orange",
            "white",
            "blue",
            "navy",
            "vintage",
            "retro"
        ],
        "colors": [
            "e88d67",
            "f3f7ec",
            "006989",
            "005c78"
        ]
    },
    {
        "id": "050c9c3572ef3abef9a7e6ff",
        "tags": [
            "navy",
            "blue",
            "gradient",
            "sea",
            "cold",
            "space"
        ],
        "colors": [
            "050c9c",
            "3572ef",
            "3abef9",
            "a7e6ff"
        ]
    },
    {
        "id": "26355daf47d2ff8f00ffdb00",
        "tags": [
            "navy",
            "black",
            "purple",
            "orange",
            "yellow",
            "neon",
            "space",
            "kids"
        ],
        "colors": [
            "26355d",
            "af47d2",
            "ff8f00",
            "ffdb00"
        ]
    },
    {
        "id": "3aa6b9ffd0d0ff9eaaf9f9e0",
        "tags": [
            "teal",
            "pink",
            "yellow",
            "kids",
            "vintage",
            "happy"
        ],
        "colors": [
            "3aa6b9",
            "ffd0d0",
            "ff9eaa",
            "f9f9e0"
        ]
    },
    {
        "id": "2543366b8a7ab7b597dad3be",
        "tags": [
            "teal",
            "brown",
            "beige",
            "earth",
            "nature",
            "winter",
            "vintage",
            "wedding",
            "gradient"
        ],
        "colors": [
            "254336",
            "6b8a7a",
            "b7b597",
            "dad3be"
        ]
    },
    {
        "id": "feffd2ffeea9ffbf78ff7d29",
        "tags": [
            "yellow",
            "orange",
            "summer",
            "gradient",
            "light",
            "gold",
            "warm"
        ],
        "colors": [
            "feffd2",
            "ffeea9",
            "ffbf78",
            "ff7d29"
        ]
    },
    {
        "id": "fffdb56fdce35c88c45c2fc2",
        "tags": [
            "yellow",
            "blue",
            "purple",
            "summer",
            "sky",
            "sea",
            "happy"
        ],
        "colors": [
            "fffdb5",
            "6fdce3",
            "5c88c4",
            "5c2fc2"
        ]
    },
    {
        "id": "eeeeee686d76373a40dc5f00",
        "tags": [
            "grey",
            "black",
            "orange",
            "retro"
        ],
        "colors": [
            "eeeeee",
            "686d76",
            "373a40",
            "dc5f00"
        ]
    },
    {
        "id": "615efc7e8ef1d1d8c5eeeeee",
        "tags": [
            "blue",
            "sage",
            "grey",
            "wedding",
            "cold"
        ],
        "colors": [
            "615efc",
            "7e8ef1",
            "d1d8c5",
            "eeeeee"
        ]
    },
    {
        "id": "808836ffbf00ff9a00d10363",
        "tags": [
            "sage",
            "green",
            "yellow",
            "orange",
            "maroon",
            "nature",
            "warm",
            "retro"
        ],
        "colors": [
            "808836",
            "ffbf00",
            "ff9a00",
            "d10363"
        ]
    },
    {
        "id": "f1e5d1dbb5b5c39898987070",
        "tags": [
            "beige",
            "peach",
            "brown",
            "vintage",
            "warm",
            "fall",
            "cream",
            "coffee",
            "pastel"
        ],
        "colors": [
            "f1e5d1",
            "dbb5b5",
            "c39898",
            "987070"
        ]
    },
    {
        "id": "01204e028391f6dcacfeae6f",
        "tags": [
            "navy",
            "teal",
            "beige",
            "orange",
            "sea",
            "vintage"
        ],
        "colors": [
            "01204e",
            "028391",
            "f6dcac",
            "feae6f"
        ]
    },
    {
        "id": "ff0000ffa27fffe8c597be5a",
        "tags": [
            "red",
            "peach",
            "beige",
            "green",
            "nature",
            "summer",
            "spring",
            "food",
            "kids",
            "christmas"
        ],
        "colors": [
            "ff0000",
            "ffa27f",
            "ffe8c5",
            "97be5a"
        ]
    },
    {
        "id": "850f8dc738bde49bfff8f9d7",
        "tags": [
            "purple",
            "yellow",
            "wedding",
            "space"
        ],
        "colors": [
            "850f8d",
            "c738bd",
            "e49bff",
            "f8f9d7"
        ]
    },
    {
        "id": "ffa62fffc96fffe8c8acd793",
        "tags": [
            "orange",
            "peach",
            "summer",
            "light",
            "kids",
            "food"
        ],
        "colors": [
            "ffa62f",
            "ffc96f",
            "ffe8c8",
            "acd793"
        ]
    },
    {
        "id": "0032852a629aff7f3effda78",
        "tags": [
            "navy",
            "orange",
            "yellow",
            "sunset",
            "sky"
        ],
        "colors": [
            "003285",
            "2a629a",
            "ff7f3e",
            "ffda78"
        ]
    },
    {
        "id": "6f4e37a67b5becb176fed8b1",
        "tags": [
            "brown",
            "orange",
            "beige",
            "skin",
            "coffee",
            "earth",
            "warm",
            "fall"
        ],
        "colors": [
            "6f4e37",
            "a67b5b",
            "ecb176",
            "fed8b1"
        ]
    },
    {
        "id": "799351a1dd70f6eec9ee4e4e",
        "tags": [
            "green",
            "beige",
            "red",
            "christmas",
            "nature",
            "vintage"
        ],
        "colors": [
            "799351",
            "a1dd70",
            "f6eec9",
            "ee4e4e"
        ]
    },
    {
        "id": "f8f4e1af8f6f74512d543310",
        "tags": [
            "beige",
            "brown",
            "warm",
            "coffee",
            "gradient",
            "vintage"
        ],
        "colors": [
            "f8f4e1",
            "af8f6f",
            "74512d",
            "543310"
        ]
    },
    {
        "id": "8e3e63d2649af6fab9cae6b2",
        "tags": [
            "maroon",
            "pink",
            "yellow",
            "green",
            "wedding",
            "happy",
            "retro"
        ],
        "colors": [
            "8e3e63",
            "d2649a",
            "f6fab9",
            "cae6b2"
        ]
    },
    {
        "id": "240750344c64577b8d57a6a1",
        "tags": [
            "navy",
            "teal",
            "dark",
            "sea",
            "gradient",
            "cold",
            "winter"
        ],
        "colors": [
            "240750",
            "344c64",
            "577b8d",
            "57a6a1"
        ]
    },
    {
        "id": "00676940a5789dde8be6ff94",
        "tags": [
            "teal",
            "green",
            "nature",
            "gradient",
            "cold",
            "summer",
            "food"
        ],
        "colors": [
            "006769",
            "40a578",
            "9dde8b",
            "e6ff94"
        ]
    },
    {
        "id": "fffae6ff9f66ff5f00002379",
        "tags": [
            "beige",
            "yellow",
            "orange",
            "navy",
            "retro",
            "kids"
        ],
        "colors": [
            "fffae6",
            "ff9f66",
            "ff5f00",
            "002379"
        ]
    },
    {
        "id": "ace1afb0ebb4bff6c3e0fbe2",
        "tags": [
            "sage",
            "green",
            "light",
            "pastel",
            "gradient",
            "nature",
            "cream"
        ],
        "colors": [
            "ace1af",
            "b0ebb4",
            "bff6c3",
            "e0fbe2"
        ]
    },
    {
        "id": "b5c18eeadbc8c7b7a3f1f1f1",
        "tags": [
            "sage",
            "beige",
            "grey",
            "pastel",
            "light",
            "earth",
            "nature",
            "wedding",
            "food"
        ],
        "colors": [
            "b5c18e",
            "eadbc8",
            "c7b7a3",
            "f1f1f1"
        ]
    },
    {
        "id": "6dc5d1fde49efeb941dd761c",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "brown",
            "kids"
        ],
        "colors": [
            "6dc5d1",
            "fde49e",
            "feb941",
            "dd761c"
        ]
    },
    {
        "id": "ffff80ffaa80ff5580ff0080",
        "tags": [
            "yellow",
            "peach",
            "pink",
            "red",
            "neon",
            "warm",
            "happy"
        ],
        "colors": [
            "ffff80",
            "ffaa80",
            "ff5580",
            "ff0080"
        ]
    },
    {
        "id": "151515a91d3ac73659eeeeee",
        "tags": [
            "black",
            "maroon",
            "red",
            "grey",
            "space",
            "retro"
        ],
        "colors": [
            "151515",
            "a91d3a",
            "c73659",
            "eeeeee"
        ]
    },
    {
        "id": "c3ff93ffdb5cffaf61ff70ab",
        "tags": [
            "green",
            "yellow",
            "orange",
            "pink",
            "spring",
            "happy",
            "nature",
            "kids",
            "retro",
            "summer",
            "neon"
        ],
        "colors": [
            "c3ff93",
            "ffdb5c",
            "ffaf61",
            "ff70ab"
        ]
    },
    {
        "id": "fff9d0caf4ffa0deff5ab2ff",
        "tags": [
            "yellow",
            "blue",
            "summer",
            "sky",
            "light",
            "happy"
        ],
        "colors": [
            "fff9d0",
            "caf4ff",
            "a0deff",
            "5ab2ff"
        ]
    },
    {
        "id": "7469b6ad88c6e1afd1ffe6e6",
        "tags": [
            "purple",
            "pink",
            "gradient",
            "wedding",
            "kids"
        ],
        "colors": [
            "7469b6",
            "ad88c6",
            "e1afd1",
            "ffe6e6"
        ]
    },
    {
        "id": "cde8e5eef7ff7ab2b24d869c",
        "tags": [
            "teal",
            "white",
            "blue",
            "cold",
            "sea"
        ],
        "colors": [
            "cde8e5",
            "eef7ff",
            "7ab2b2",
            "4d869c"
        ]
    },
    {
        "id": "03aed268d2e8fdde55feefad",
        "tags": [
            "blue",
            "yellow",
            "summer",
            "light",
            "happy"
        ],
        "colors": [
            "03aed2",
            "68d2e8",
            "fdde55",
            "feefad"
        ]
    },
    {
        "id": "f3ca52f6e9b20a68477aba78",
        "tags": [
            "yellow",
            "beige",
            "green",
            "nature",
            "retro",
            "warm",
            "summer",
            "food"
        ],
        "colors": [
            "f3ca52",
            "f6e9b2",
            "0a6847",
            "7aba78"
        ]
    },
    {
        "id": "fff2d7ffe0b5f8c794d8ae7e",
        "tags": [
            "beige",
            "orange",
            "brown",
            "light",
            "skin",
            "cream",
            "warm",
            "coffee"
        ],
        "colors": [
            "fff2d7",
            "ffe0b5",
            "f8c794",
            "d8ae7e"
        ]
    },
    {
        "id": "32012f524c42e2dfd0f97300",
        "tags": [
            "purple",
            "grey",
            "orange",
            "vintage",
            "dark",
            "halloween"
        ],
        "colors": [
            "32012f",
            "524c42",
            "e2dfd0",
            "f97300"
        ]
    },
    {
        "id": "640d6bb51b75e65c19f8d082",
        "tags": [
            "purple",
            "orange",
            "yellow",
            "gradient",
            "sunset",
            "warm",
            "retro"
        ],
        "colors": [
            "640d6b",
            "b51b75",
            "e65c19",
            "f8d082"
        ]
    },
    {
        "id": "a87676ca8787e1acacffd0d0",
        "tags": [
            "peach",
            "pink",
            "pastel",
            "warm",
            "skin",
            "food",
            "kids"
        ],
        "colors": [
            "a87676",
            "ca8787",
            "e1acac",
            "ffd0d0"
        ]
    },
    {
        "id": "fc4100ffc55a00215e2c4e80",
        "tags": [
            "red",
            "orange",
            "yellow",
            "navy",
            "blue",
            "kids",
            "rainbow",
            "retro"
        ],
        "colors": [
            "fc4100",
            "ffc55a",
            "00215e",
            "2c4e80"
        ]
    },
    {
        "id": "c40c0cff6500ff8a08ffc100",
        "tags": [
            "red",
            "orange",
            "yellow",
            "gold",
            "warm",
            "happy"
        ],
        "colors": [
            "c40c0c",
            "ff6500",
            "ff8a08",
            "ffc100"
        ]
    },
    {
        "id": "ff76cefdffc294ffd8a3d8ff",
        "tags": [
            "pink",
            "yellow",
            "mint",
            "blue",
            "light",
            "rainbow",
            "happy",
            "kids",
            "spring",
            "neon"
        ],
        "colors": [
            "ff76ce",
            "fdffc2",
            "94ffd8",
            "a3d8ff"
        ]
    },
    {
        "id": "f5dad2fcffe0bacd9275a47f",
        "tags": [
            "peach",
            "yellow",
            "sage",
            "green",
            "nature",
            "pastel",
            "light",
            "summer",
            "food"
        ],
        "colors": [
            "f5dad2",
            "fcffe0",
            "bacd92",
            "75a47f"
        ]
    },
    {
        "id": "1a4d2e4f6f52e8dfcaf5efe6",
        "tags": [
            "green",
            "beige",
            "food",
            "wedding",
            "vintage",
            "nature"
        ],
        "colors": [
            "1a4d2e",
            "4f6f52",
            "e8dfca",
            "f5efe6"
        ]
    },
    {
        "id": "121481ffeae3ffcbcbffb1b1",
        "tags": [
            "blue",
            "navy",
            "peach",
            "pink",
            "wedding"
        ],
        "colors": [
            "121481",
            "ffeae3",
            "ffcbcb",
            "ffb1b1"
        ]
    },
    {
        "id": "1534483c5b6f948979dfd0b8",
        "tags": [
            "navy",
            "blue",
            "brown",
            "beige",
            "sea",
            "winter",
            "vintage"
        ],
        "colors": [
            "153448",
            "3c5b6f",
            "948979",
            "dfd0b8"
        ]
    },
    {
        "id": "fffbdaffec9effbb70ed9455",
        "tags": [
            "yellow",
            "orange",
            "summer",
            "light",
            "warm",
            "happy",
            "gold"
        ],
        "colors": [
            "fffbda",
            "ffec9e",
            "ffbb70",
            "ed9455"
        ]
    },
    {
        "id": "10439f874cccc65bcff27bbd",
        "tags": [
            "blue",
            "purple",
            "pink",
            "space",
            "cold",
            "retro",
            "gradient"
        ],
        "colors": [
            "10439f",
            "874ccc",
            "c65bcf",
            "f27bbd"
        ]
    },
    {
        "id": "e4c59eaf8260803d3b322c2b",
        "tags": [
            "beige",
            "brown",
            "maroon",
            "black",
            "coffee",
            "skin",
            "warm",
            "vintage",
            "gradient",
            "food"
        ],
        "colors": [
            "e4c59e",
            "af8260",
            "803d3b",
            "322c2b"
        ]
    },
    {
        "id": "b5c18ef7dcb9deac80b99470",
        "tags": [
            "green",
            "sage",
            "beige",
            "brown",
            "nature",
            "earth",
            "pastel",
            "kids"
        ],
        "colors": [
            "b5c18e",
            "f7dcb9",
            "deac80",
            "b99470"
        ]
    },
    {
        "id": "1e03420e46a39ac8cde1f7f5",
        "tags": [
            "black",
            "navy",
            "blue",
            "teal",
            "sea",
            "cold"
        ],
        "colors": [
            "1e0342",
            "0e46a3",
            "9ac8cd",
            "e1f7f5"
        ]
    },
    {
        "id": "fff5e08decb441b06e141e46",
        "tags": [
            "beige",
            "green",
            "navy",
            "black",
            "retro",
            "nature"
        ],
        "colors": [
            "fff5e0",
            "8decb4",
            "41b06e",
            "141e46"
        ]
    },
    {
        "id": "fefaf6eadbc8dac0a3102c57",
        "tags": [
            "white",
            "beige",
            "navy",
            "wedding",
            "vintage",
            "coffee"
        ],
        "colors": [
            "fefaf6",
            "eadbc8",
            "dac0a3",
            "102c57"
        ]
    },
    {
        "id": "f6f5f2f0ebe3f3d0d7ffefef",
        "tags": [
            "white",
            "grey",
            "beige",
            "peach",
            "pink",
            "skin",
            "pastel",
            "kids",
            "light",
            "cream"
        ],
        "colors": [
            "f6f5f2",
            "f0ebe3",
            "f3d0d7",
            "ffefef"
        ]
    },
    {
        "id": "4793afffc470dd57468b322c",
        "tags": [
            "blue",
            "orange",
            "red",
            "maroon",
            "rainbow",
            "kids",
            "vintage"
        ],
        "colors": [
            "4793af",
            "ffc470",
            "dd5746",
            "8b322c"
        ]
    },
    {
        "id": "0741731679ab5debd7c5ff95",
        "tags": [
            "navy",
            "blue",
            "mint",
            "green",
            "sea",
            "cold",
            "gradient",
            "winter"
        ],
        "colors": [
            "074173",
            "1679ab",
            "5debd7",
            "c5ff95"
        ]
    },
    {
        "id": "5bbcfffffab7ffd1e37ea1ff",
        "tags": [
            "blue",
            "yellow",
            "pink",
            "kids",
            "happy",
            "light"
        ],
        "colors": [
            "5bbcff",
            "fffab7",
            "ffd1e3",
            "7ea1ff"
        ]
    },
    {
        "id": "1c16788576ff7bc9ffa3ffd6",
        "tags": [
            "navy",
            "purple",
            "blue",
            "mint",
            "gradient",
            "space",
            "cold"
        ],
        "colors": [
            "1c1678",
            "8576ff",
            "7bc9ff",
            "a3ffd6"
        ]
    },
    {
        "id": "dba979ecca9ce8efcfafd198",
        "tags": [
            "brown",
            "orange",
            "beige",
            "sage",
            "green",
            "pastel",
            "vintage",
            "food",
            "nature",
            "earth",
            "summer"
        ],
        "colors": [
            "dba979",
            "ecca9c",
            "e8efcf",
            "afd198"
        ]
    },
    {
        "id": "6c0345dc6b19f7c566fff8dc",
        "tags": [
            "maroon",
            "orange",
            "yellow",
            "sunset",
            "warm",
            "gold",
            "fall"
        ],
        "colors": [
            "6c0345",
            "dc6b19",
            "f7c566",
            "fff8dc"
        ]
    },
    {
        "id": "003c43135d6677b0aae3fef7",
        "tags": [
            "teal",
            "mint",
            "night",
            "cold",
            "gradient",
            "sea"
        ],
        "colors": [
            "003c43",
            "135d66",
            "77b0aa",
            "e3fef7"
        ]
    },
    {
        "id": "a79277d1bb9eead8c0fff2e1",
        "tags": [
            "brown",
            "beige",
            "pastel",
            "vintage",
            "cream",
            "coffee",
            "skin",
            "food",
            "gradient",
            "warm"
        ],
        "colors": [
            "a79277",
            "d1bb9e",
            "ead8c0",
            "fff2e1"
        ]
    },
    {
        "id": "ffebb2e59be9d862bc8644a2",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "retro",
            "happy"
        ],
        "colors": [
            "ffebb2",
            "e59be9",
            "d862bc",
            "8644a2"
        ]
    },
    {
        "id": "86469cbc7fcdfb9ad1ffcdea",
        "tags": [
            "purple",
            "pink",
            "gradient",
            "kids"
        ],
        "colors": [
            "86469c",
            "bc7fcd",
            "fb9ad1",
            "ffcdea"
        ]
    },
    {
        "id": "a34343e9c874fbf8ddc0d6e8",
        "tags": [
            "red",
            "maroon",
            "yellow",
            "blue",
            "rainbow",
            "warm"
        ],
        "colors": [
            "a34343",
            "e9c874",
            "fbf8dd",
            "c0d6e8"
        ]
    },
    {
        "id": "b3c8cfbed7dcf1eedce5ddc5",
        "tags": [
            "blue",
            "beige",
            "summer",
            "sea",
            "wedding",
            "pastel",
            "light",
            "cream"
        ],
        "colors": [
            "b3c8cf",
            "bed7dc",
            "f1eedc",
            "e5ddc5"
        ]
    },
    {
        "id": "49243e704264bb8493dbafa0",
        "tags": [
            "purple",
            "maroon",
            "peach",
            "dark",
            "warm",
            "night",
            "halloween"
        ],
        "colors": [
            "49243e",
            "704264",
            "bb8493",
            "dbafa0"
        ]
    },
    {
        "id": "0c0c0c481e149b3922f2613f",
        "tags": [
            "black",
            "brown",
            "maroon",
            "orange",
            "dark",
            "fall",
            "halloween",
            "night"
        ],
        "colors": [
            "0c0c0c",
            "481e14",
            "9b3922",
            "f2613f"
        ]
    },
    {
        "id": "ffc94ac08b5c795458453f78",
        "tags": [
            "yellow",
            "brown",
            "navy",
            "gold",
            "warm"
        ],
        "colors": [
            "ffc94a",
            "c08b5c",
            "795458",
            "453f78"
        ]
    },
    {
        "id": "ffebb2e9a89bd875c7912bbc",
        "tags": [
            "yellow",
            "peach",
            "pink",
            "purple",
            "gradient",
            "kids"
        ],
        "colors": [
            "ffebb2",
            "e9a89b",
            "d875c7",
            "912bbc"
        ]
    },
    {
        "id": "d20062d6589fd895dac4e4ff",
        "tags": [
            "red",
            "purple",
            "blue",
            "gradient",
            "kids",
            "wedding",
            "retro"
        ],
        "colors": [
            "d20062",
            "d6589f",
            "d895da",
            "c4e4ff"
        ]
    },
    {
        "id": "f8f6e397e7e16ad4dd7aa2e3",
        "tags": [
            "beige",
            "teal",
            "blue",
            "summer",
            "sky",
            "sea",
            "light"
        ],
        "colors": [
            "f8f6e3",
            "97e7e1",
            "6ad4dd",
            "7aa2e3"
        ]
    },
    {
        "id": "fa7070fefdedc6ebc5a1c398",
        "tags": [
            "red",
            "white",
            "beige",
            "sage",
            "green",
            "vintage",
            "light",
            "food",
            "spring",
            "nature",
            "kids"
        ],
        "colors": [
            "fa7070",
            "fefded",
            "c6ebc5",
            "a1c398"
        ]
    },
    {
        "id": "d9edbfff98002c786590d26d",
        "tags": [
            "sage",
            "orange",
            "teal",
            "green",
            "nature",
            "retro",
            "summer",
            "food"
        ],
        "colors": [
            "d9edbf",
            "ff9800",
            "2c7865",
            "90d26d"
        ]
    },
    {
        "id": "fff7fc8b93ff5755feff71cd",
        "tags": [
            "white",
            "blue",
            "pink",
            "cold",
            "space",
            "retro",
            "wedding"
        ],
        "colors": [
            "fff7fc",
            "8b93ff",
            "5755fe",
            "ff71cd"
        ]
    },
    {
        "id": "ffaf45fb6d48d74b76673f69",
        "tags": [
            "orange",
            "red",
            "maroon",
            "purple",
            "gold",
            "warm",
            "sunset",
            "gradient"
        ],
        "colors": [
            "ffaf45",
            "fb6d48",
            "d74b76",
            "673f69"
        ]
    },
    {
        "id": "e72929ff5baeffe4cffffdd7",
        "tags": [
            "red",
            "pink",
            "peach",
            "yellow",
            "kids",
            "warm",
            "happy"
        ],
        "colors": [
            "e72929",
            "ff5bae",
            "ffe4cf",
            "fffdd7"
        ]
    },
    {
        "id": "efbc9bfbf3d5d6dac89cafaa",
        "tags": [
            "peach",
            "orange",
            "yellow",
            "beige",
            "sage",
            "pastel",
            "light",
            "earth",
            "food",
            "vintage"
        ],
        "colors": [
            "efbc9b",
            "fbf3d5",
            "d6dac8",
            "9cafaa"
        ]
    },
    {
        "id": "62725476885bddddddeeeeee",
        "tags": [
            "green",
            "sage",
            "grey",
            "vintage",
            "winter"
        ],
        "colors": [
            "627254",
            "76885b",
            "dddddd",
            "eeeeee"
        ]
    },
    {
        "id": "401f71824d74be7b72fdaf7b",
        "tags": [
            "purple",
            "brown",
            "orange",
            "night",
            "space",
            "gradient",
            "halloween"
        ],
        "colors": [
            "401f71",
            "824d74",
            "be7b72",
            "fdaf7b"
        ]
    },
    {
        "id": "49698958a399a8cd9fe2f4c5",
        "tags": [
            "navy",
            "teal",
            "green",
            "gradient",
            "sea",
            "cold"
        ],
        "colors": [
            "496989",
            "58a399",
            "a8cd9f",
            "e2f4c5"
        ]
    },
    {
        "id": "008dda41c9e2ace2e1f7eedd",
        "tags": [
            "blue",
            "teal",
            "beige",
            "summer",
            "happy",
            "gradient",
            "sky",
            "sea",
            "kids"
        ],
        "colors": [
            "008dda",
            "41c9e2",
            "ace2e1",
            "f7eedd"
        ]
    },
    {
        "id": "ff204ea0153e5d0e4100224d",
        "tags": [
            "red",
            "maroon",
            "navy",
            "dark",
            "neon",
            "gradient",
            "warm",
            "space"
        ],
        "colors": [
            "ff204e",
            "a0153e",
            "5d0e41",
            "00224d"
        ]
    },
    {
        "id": "430a5d5f374b8c6a5deee4b1",
        "tags": [
            "purple",
            "brown",
            "yellow",
            "retro",
            "gradient",
            "dark",
            "night",
            "vintage",
            "coffee",
            "halloween"
        ],
        "colors": [
            "430a5d",
            "5f374b",
            "8c6a5d",
            "eee4b1"
        ]
    },
    {
        "id": "007f734ccd99ffc700fff455",
        "tags": [
            "teal",
            "orange",
            "yellow",
            "kids",
            "neon",
            "happy"
        ],
        "colors": [
            "007f73",
            "4ccd99",
            "ffc700",
            "fff455"
        ]
    },
    {
        "id": "5356ff378ce767c6e3dff5ff",
        "tags": [
            "blue",
            "cold",
            "gradient",
            "winter"
        ],
        "colors": [
            "5356ff",
            "378ce7",
            "67c6e3",
            "dff5ff"
        ]
    },
    {
        "id": "fda403e8751a898121e5c287",
        "tags": [
            "orange",
            "green",
            "beige",
            "warm",
            "nature",
            "kids",
            "food"
        ],
        "colors": [
            "fda403",
            "e8751a",
            "898121",
            "e5c287"
        ]
    },
    {
        "id": "22283131363f76abaeeeeeee",
        "tags": [
            "black",
            "teal",
            "grey",
            "vintage",
            "dark",
            "wedding",
            "winter"
        ],
        "colors": [
            "222831",
            "31363f",
            "76abae",
            "eeeeee"
        ]
    },
    {
        "id": "240a34891652eabe6cffedd8",
        "tags": [
            "black",
            "maroon",
            "yellow",
            "beige",
            "retro",
            "wedding"
        ],
        "colors": [
            "240a34",
            "891652",
            "eabe6c",
            "ffedd8"
        ]
    },
    {
        "id": "e178c5ff8e8fffb38efffdcb",
        "tags": [
            "purple",
            "pink",
            "peach",
            "orange",
            "yellow",
            "light",
            "warm",
            "gold",
            "gradient",
            "happy"
        ],
        "colors": [
            "e178c5",
            "ff8e8f",
            "ffb38e",
            "fffdcb"
        ]
    },
    {
        "id": "fff3c7fec7b4fc819ef7418f",
        "tags": [
            "yellow",
            "peach",
            "pink",
            "gradient",
            "warm",
            "skin",
            "light",
            "spring"
        ],
        "colors": [
            "fff3c7",
            "fec7b4",
            "fc819e",
            "f7418f"
        ]
    },
    {
        "id": "b0c5a4d37676ebc49ff1ef99",
        "tags": [
            "sage",
            "red",
            "beige",
            "yellow",
            "nature",
            "earth",
            "spring",
            "kids",
            "vintage",
            "pastel"
        ],
        "colors": [
            "b0c5a4",
            "d37676",
            "ebc49f",
            "f1ef99"
        ]
    },
    {
        "id": "5f5d9c6196a6a4ce95f4edcc",
        "tags": [
            "navy",
            "teal",
            "green",
            "beige",
            "kids",
            "winter",
            "gradient"
        ],
        "colors": [
            "5f5d9c",
            "6196a6",
            "a4ce95",
            "f4edcc"
        ]
    },
    {
        "id": "1240767f9f80f9e897ffc374",
        "tags": [
            "navy",
            "sage",
            "green",
            "yellow",
            "orange",
            "earth",
            "vintage"
        ],
        "colors": [
            "124076",
            "7f9f80",
            "f9e897",
            "ffc374"
        ]
    },
    {
        "id": "b2b377d2d180e5e483f1f5a8",
        "tags": [
            "sage",
            "yellow",
            "light",
            "cream",
            "gradient",
            "nature",
            "food"
        ],
        "colors": [
            "b2b377",
            "d2d180",
            "e5e483",
            "f1f5a8"
        ]
    },
    {
        "id": "eadfb49bb0c151829bf6995c",
        "tags": [
            "beige",
            "blue",
            "orange",
            "pastel",
            "vintage",
            "wedding",
            "kids"
        ],
        "colors": [
            "eadfb4",
            "9bb0c1",
            "51829b",
            "f6995c"
        ]
    },
    {
        "id": "11423287a922fcdc2af7f6bb",
        "tags": [
            "green",
            "yellow",
            "summer",
            "nature",
            "food"
        ],
        "colors": [
            "114232",
            "87a922",
            "fcdc2a",
            "f7f6bb"
        ]
    },
    {
        "id": "ffe6e6e1afd1ad88c67469b6",
        "tags": [
            "peach",
            "pink",
            "purple",
            "pastel",
            "cream",
            "wedding",
            "gradient"
        ],
        "colors": [
            "ffe6e6",
            "e1afd1",
            "ad88c6",
            "7469b6"
        ]
    },
    {
        "id": "6420aaff3ea5ff7ed4ffb5da",
        "tags": [
            "purple",
            "pink",
            "retro",
            "neon",
            "space",
            "gradient",
            "kids"
        ],
        "colors": [
            "6420aa",
            "ff3ea5",
            "ff7ed4",
            "ffb5da"
        ]
    },
    {
        "id": "59d5e0f5dd61faa300f4538a",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "pink",
            "happy",
            "kids",
            "rainbow",
            "retro",
            "spring"
        ],
        "colors": [
            "59d5e0",
            "f5dd61",
            "faa300",
            "f4538a"
        ]
    },
    {
        "id": "a5dd9bc5ebaaf6f193f2c18d",
        "tags": [
            "green",
            "sage",
            "yellow",
            "peach",
            "pastel",
            "nature",
            "light",
            "summer",
            "food",
            "kids"
        ],
        "colors": [
            "a5dd9b",
            "c5ebaa",
            "f6f193",
            "f2c18d"
        ]
    },
    {
        "id": "5e1675ee4266ffd23f337357",
        "tags": [
            "purple",
            "red",
            "yellow",
            "green",
            "retro",
            "rainbow",
            "space",
            "kids",
            "christmas"
        ],
        "colors": [
            "5e1675",
            "ee4266",
            "ffd23f",
            "337357"
        ]
    },
    {
        "id": "35374b34495550727b78a083",
        "tags": [
            "black",
            "navy",
            "sage",
            "dark",
            "cold",
            "winter",
            "night",
            "halloween"
        ],
        "colors": [
            "35374b",
            "344955",
            "50727b",
            "78a083"
        ]
    },
    {
        "id": "fba834333a73387adf50c4ed",
        "tags": [
            "orange",
            "navy",
            "blue",
            "retro",
            "kids",
            "winter"
        ],
        "colors": [
            "fba834",
            "333a73",
            "387adf",
            "50c4ed"
        ]
    },
    {
        "id": "ff407dffcad440679e1b3c73",
        "tags": [
            "red",
            "pink",
            "blue",
            "navy",
            "wedding"
        ],
        "colors": [
            "ff407d",
            "ffcad4",
            "40679e",
            "1b3c73"
        ]
    },
    {
        "id": "0c359eee99c2ffe3caf6f5f5",
        "tags": [
            "navy",
            "blue",
            "pink",
            "beige",
            "grey",
            "white",
            "wedding",
            "kids",
            "gradient",
            "vintage"
        ],
        "colors": [
            "0c359e",
            "ee99c2",
            "ffe3ca",
            "f6f5f5"
        ]
    },
    {
        "id": "ffbe98feece2f7ded0e2bfb3",
        "tags": [
            "orange",
            "peach",
            "light",
            "warm",
            "pastel",
            "skin",
            "coffee"
        ],
        "colors": [
            "ffbe98",
            "feece2",
            "f7ded0",
            "e2bfb3"
        ]
    },
    {
        "id": "9195f6b7c9f2f9f07afb88b4",
        "tags": [
            "blue",
            "yellow",
            "pink",
            "kids",
            "happy",
            "rainbow"
        ],
        "colors": [
            "9195f6",
            "b7c9f2",
            "f9f07a",
            "fb88b4"
        ]
    },
    {
        "id": "b5c0d0ccd3caf5e8ddeed3d9",
        "tags": [
            "grey",
            "sage",
            "beige",
            "peach",
            "vintage",
            "pastel",
            "cream",
            "light",
            "earth"
        ],
        "colors": [
            "b5c0d0",
            "ccd3ca",
            "f5e8dd",
            "eed3d9"
        ]
    },
    {
        "id": "fff67ebfea7c9bcf53416d19",
        "tags": [
            "yellow",
            "green",
            "happy",
            "summer",
            "kids",
            "food"
        ],
        "colors": [
            "fff67e",
            "bfea7c",
            "9bcf53",
            "416d19"
        ]
    },
    {
        "id": "2016581d24ca98abeef9e8c9",
        "tags": [
            "black",
            "navy",
            "blue",
            "beige",
            "sea",
            "night",
            "cold",
            "winter"
        ],
        "colors": [
            "201658",
            "1d24ca",
            "98abee",
            "f9e8c9"
        ]
    },
    {
        "id": "2650732d95969ad0c2f1fada",
        "tags": [
            "navy",
            "teal",
            "sage",
            "cold",
            "winter",
            "sea",
            "gradient"
        ],
        "colors": [
            "265073",
            "2d9596",
            "9ad0c2",
            "f1fada"
        ]
    },
    {
        "id": "8e7ab5b784b7e493b3eea5a6",
        "tags": [
            "purple",
            "pink",
            "peach",
            "warm",
            "pastel",
            "vintage",
            "gradient",
            "sunset"
        ],
        "colors": [
            "8e7ab5",
            "b784b7",
            "e493b3",
            "eea5a6"
        ]
    },
    {
        "id": "070f2b1b1a55535c919290c3",
        "tags": [
            "navy",
            "blue",
            "dark",
            "cold",
            "night",
            "space",
            "gradient",
            "halloween"
        ],
        "colors": [
            "070f2b",
            "1b1a55",
            "535c91",
            "9290c3"
        ]
    },
    {
        "id": "211951836fff15f5baf0f3ff",
        "tags": [
            "navy",
            "purple",
            "mint",
            "grey",
            "retro",
            "neon",
            "kids"
        ],
        "colors": [
            "211951",
            "836fff",
            "15f5ba",
            "f0f3ff"
        ]
    },
    {
        "id": "000000f72798f57d1febf400",
        "tags": [
            "black",
            "pink",
            "orange",
            "yellow",
            "retro",
            "neon"
        ],
        "colors": [
            "000000",
            "f72798",
            "f57d1f",
            "ebf400"
        ]
    },
    {
        "id": "d7e4c0c6dcbabbc3a4b3a398",
        "tags": [
            "sage",
            "green",
            "brown",
            "nature",
            "earth",
            "pastel",
            "light",
            "food",
            "gradient"
        ],
        "colors": [
            "d7e4c0",
            "c6dcba",
            "bbc3a4",
            "b3a398"
        ]
    },
    {
        "id": "8cb9bdfefbf6ecb159b67352",
        "tags": [
            "teal",
            "white",
            "orange",
            "brown",
            "fall",
            "vintage",
            "earth"
        ],
        "colors": [
            "8cb9bd",
            "fefbf6",
            "ecb159",
            "b67352"
        ]
    },
    {
        "id": "9b4444c68484a3c9aaeeeeee",
        "tags": [
            "maroon",
            "peach",
            "sage",
            "grey",
            "earth",
            "vintage",
            "christmas",
            "food"
        ],
        "colors": [
            "9b4444",
            "c68484",
            "a3c9aa",
            "eeeeee"
        ]
    },
    {
        "id": "7f27ff9f70fdfdbf60ff8911",
        "tags": [
            "purple",
            "orange",
            "retro",
            "kids",
            "happy"
        ],
        "colors": [
            "7f27ff",
            "9f70fd",
            "fdbf60",
            "ff8911"
        ]
    },
    {
        "id": "211c6a59b4c374e291eff396",
        "tags": [
            "navy",
            "blue",
            "green",
            "yellow",
            "gradient",
            "cold",
            "kids"
        ],
        "colors": [
            "211c6a",
            "59b4c3",
            "74e291",
            "eff396"
        ]
    },
    {
        "id": "fff7f1ffe4c9e78895bed1cf",
        "tags": [
            "white",
            "beige",
            "peach",
            "red",
            "grey",
            "vintage",
            "light",
            "kids"
        ],
        "colors": [
            "fff7f1",
            "ffe4c9",
            "e78895",
            "bed1cf"
        ]
    },
    {
        "id": "cdfadbf6fdc3ffcf96ff8080",
        "tags": [
            "mint",
            "yellow",
            "orange",
            "red",
            "light",
            "spring",
            "kids",
            "rainbow",
            "gradient",
            "happy"
        ],
        "colors": [
            "cdfadb",
            "f6fdc3",
            "ffcf96",
            "ff8080"
        ]
    },
    {
        "id": "944e63b47b84caa6a6ffe7e7",
        "tags": [
            "maroon",
            "brown",
            "peach",
            "skin",
            "coffee",
            "food",
            "warm",
            "gradient"
        ],
        "colors": [
            "944e63",
            "b47b84",
            "caa6a6",
            "ffe7e7"
        ]
    },
    {
        "id": "40a2e3fff6e9bbe2ec0d9276",
        "tags": [
            "blue",
            "beige",
            "green",
            "cold",
            "kids",
            "sky"
        ],
        "colors": [
            "40a2e3",
            "fff6e9",
            "bbe2ec",
            "0d9276"
        ]
    },
    {
        "id": "b4b4b8c7c8cce3e1d9f2efe5",
        "tags": [
            "grey",
            "beige",
            "pastel",
            "vintage",
            "cream",
            "wedding"
        ],
        "colors": [
            "b4b4b8",
            "c7c8cc",
            "e3e1d9",
            "f2efe5"
        ]
    },
    {
        "id": "12372a436850adbc9ffbfada",
        "tags": [
            "green",
            "sage",
            "yellow",
            "winter",
            "nature",
            "gradient",
            "food"
        ],
        "colors": [
            "12372a",
            "436850",
            "adbc9f",
            "fbfada"
        ]
    },
    {
        "id": "e8c872fff3cfc9d7dd637a9f",
        "tags": [
            "yellow",
            "beige",
            "blue",
            "sea",
            "summer",
            "kids"
        ],
        "colors": [
            "e8c872",
            "fff3cf",
            "c9d7dd",
            "637a9f"
        ]
    },
    {
        "id": "1f2544474f7a81689dffd0ec",
        "tags": [
            "black",
            "navy",
            "purple",
            "pink",
            "gradient",
            "space",
            "night",
            "cold"
        ],
        "colors": [
            "1f2544",
            "474f7a",
            "81689d",
            "ffd0ec"
        ]
    },
    {
        "id": "0c2d57fc6736ffb0b0efecec",
        "tags": [
            "navy",
            "orange",
            "peach",
            "grey",
            "retro",
            "space"
        ],
        "colors": [
            "0c2d57",
            "fc6736",
            "ffb0b0",
            "efecec"
        ]
    },
    {
        "id": "eeedebe0ccbe7472643c3633",
        "tags": [
            "grey",
            "peach",
            "sage",
            "vintage",
            "winter"
        ],
        "colors": [
            "eeedeb",
            "e0ccbe",
            "747264",
            "3c3633"
        ]
    },
    {
        "id": "f28585ffa447fffc9bb7e5b4",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "rainbow",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "f28585",
            "ffa447",
            "fffc9b",
            "b7e5b4"
        ]
    },
    {
        "id": "fdf0d1ac7d8885586f643843",
        "tags": [
            "beige",
            "yellow",
            "peach",
            "maroon",
            "wedding",
            "gradient",
            "warm",
            "skin",
            "coffee"
        ],
        "colors": [
            "fdf0d1",
            "ac7d88",
            "85586f",
            "643843"
        ]
    },
    {
        "id": "6c22a66962ad83c0c196e9c6",
        "tags": [
            "purple",
            "blue",
            "teal",
            "mint",
            "sea",
            "cold",
            "gradient",
            "retro"
        ],
        "colors": [
            "6c22a6",
            "6962ad",
            "83c0c1",
            "96e9c6"
        ]
    },
    {
        "id": "561c246d2932c7b7a3e8d8c4",
        "tags": [
            "maroon",
            "brown",
            "beige",
            "coffee",
            "skin",
            "warm",
            "food"
        ],
        "colors": [
            "561c24",
            "6d2932",
            "c7b7a3",
            "e8d8c4"
        ]
    },
    {
        "id": "d04848f3b95ffde7676895d2",
        "tags": [
            "red",
            "orange",
            "yellow",
            "blue",
            "rainbow",
            "kids",
            "retro"
        ],
        "colors": [
            "d04848",
            "f3b95f",
            "fde767",
            "6895d2"
        ]
    },
    {
        "id": "0a1d56492e8737b5b6f2f597",
        "tags": [
            "navy",
            "purple",
            "teal",
            "yellow",
            "retro",
            "wedding",
            "kids"
        ],
        "colors": [
            "0a1d56",
            "492e87",
            "37b5b6",
            "f2f597"
        ]
    },
    {
        "id": "e1f0dad4e7c5bfd8af99bc85",
        "tags": [
            "sage",
            "green",
            "summer",
            "pastel",
            "cream",
            "light",
            "gradient",
            "nature"
        ],
        "colors": [
            "e1f0da",
            "d4e7c5",
            "bfd8af",
            "99bc85"
        ]
    },
    {
        "id": "0000000b60b040a2d8f0edcf",
        "tags": [
            "black",
            "blue",
            "beige",
            "sea",
            "winter",
            "cold"
        ],
        "colors": [
            "000000",
            "0b60b0",
            "40a2d8",
            "f0edcf"
        ]
    },
    {
        "id": "294b2950623a789461dbe7c9",
        "tags": [
            "green",
            "sage",
            "nature",
            "gradient"
        ],
        "colors": [
            "294b29",
            "50623a",
            "789461",
            "dbe7c9"
        ]
    },
    {
        "id": "fe7a363652ad280274e9f6ff",
        "tags": [
            "orange",
            "blue",
            "navy",
            "retro",
            "kids",
            "wedding"
        ],
        "colors": [
            "fe7a36",
            "3652ad",
            "280274",
            "e9f6ff"
        ]
    },
    {
        "id": "dcffb7ff6868ffbb64ffeaa7",
        "tags": [
            "green",
            "red",
            "orange",
            "yellow",
            "neon",
            "light",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "dcffb7",
            "ff6868",
            "ffbb64",
            "ffeaa7"
        ]
    },
    {
        "id": "f5eee6fff8e3f3d7cae6a4b4",
        "tags": [
            "grey",
            "beige",
            "peach",
            "pink",
            "pastel",
            "spring",
            "wedding",
            "light",
            "cream",
            "skin"
        ],
        "colors": [
            "f5eee6",
            "fff8e3",
            "f3d7ca",
            "e6a4b4"
        ]
    },
    {
        "id": "0306373c0753720455910a67",
        "tags": [
            "black",
            "purple",
            "maroon",
            "dark",
            "night",
            "space",
            "halloween"
        ],
        "colors": [
            "030637",
            "3c0753",
            "720455",
            "910a67"
        ]
    },
    {
        "id": "f9efdbebd9b49dbc98638889",
        "tags": [
            "beige",
            "green",
            "teal",
            "vintage",
            "pastel",
            "earth",
            "food"
        ],
        "colors": [
            "f9efdb",
            "ebd9b4",
            "9dbc98",
            "638889"
        ]
    },
    {
        "id": "a94438d24545e6baa3e4debe",
        "tags": [
            "brown",
            "red",
            "peach",
            "sage",
            "christmas",
            "gradient",
            "warm",
            "food"
        ],
        "colors": [
            "a94438",
            "d24545",
            "e6baa3",
            "e4debe"
        ]
    },
    {
        "id": "3e3232503c3c7e6363a87c7c",
        "tags": [
            "black",
            "brown",
            "peach",
            "vintage",
            "dark",
            "night",
            "gradient",
            "warm",
            "skin",
            "coffee"
        ],
        "colors": [
            "3e3232",
            "503c3c",
            "7e6363",
            "a87c7c"
        ]
    },
    {
        "id": "f8f4ecff9bd2d63484402b3a",
        "tags": [
            "beige",
            "pink",
            "black",
            "retro",
            "kids"
        ],
        "colors": [
            "f8f4ec",
            "ff9bd2",
            "d63484",
            "402b3a"
        ]
    },
    {
        "id": "ff9843ffdd9586a7fc3468c0",
        "tags": [
            "orange",
            "yellow",
            "blue",
            "happy",
            "sunset",
            "kids",
            "summer",
            "wedding",
            "retro"
        ],
        "colors": [
            "ff9843",
            "ffdd95",
            "86a7fc",
            "3468c0"
        ]
    },
    {
        "id": "d9edbfffb996ffcf81fdffab",
        "tags": [
            "green",
            "sage",
            "peach",
            "orange",
            "yellow",
            "pastel",
            "vintage",
            "light",
            "summer",
            "spring",
            "happy",
            "nature"
        ],
        "colors": [
            "d9edbf",
            "ffb996",
            "ffcf81",
            "fdffab"
        ]
    },
    {
        "id": "3329413b3486864af9f8e559",
        "tags": [
            "black",
            "navy",
            "purple",
            "yellow",
            "cold",
            "retro",
            "space"
        ],
        "colors": [
            "332941",
            "3b3486",
            "864af9",
            "f8e559"
        ]
    },
    {
        "id": "faef9bf6d7766da4aa647d87",
        "tags": [
            "yellow",
            "teal",
            "retro"
        ],
        "colors": [
            "faef9b",
            "f6d776",
            "6da4aa",
            "647d87"
        ]
    },
    {
        "id": "1d2b537e2553ff004dfaef5d",
        "tags": [
            "navy",
            "maroon",
            "red",
            "yellow",
            "neon",
            "space",
            "halloween"
        ],
        "colors": [
            "1d2b53",
            "7e2553",
            "ff004d",
            "faef5d"
        ]
    },
    {
        "id": "80bcbdaad9bbd5f0c1f9f7c9",
        "tags": [
            "teal",
            "green",
            "yellow",
            "nature",
            "pastel",
            "gradient",
            "light",
            "wedding",
            "kids"
        ],
        "colors": [
            "80bcbd",
            "aad9bb",
            "d5f0c1",
            "f9f7c9"
        ]
    },
    {
        "id": "dcf2f17fc7d93654860f1035",
        "tags": [
            "blue",
            "navy",
            "gradient",
            "cold",
            "sea",
            "winter"
        ],
        "colors": [
            "dcf2f1",
            "7fc7d9",
            "365486",
            "0f1035"
        ]
    },
    {
        "id": "2d32504247697077a1f6b17a",
        "tags": [
            "black",
            "navy",
            "orange",
            "dark",
            "gradient",
            "night",
            "winter",
            "cold",
            "halloween",
            "vintage"
        ],
        "colors": [
            "2d3250",
            "424769",
            "7077a1",
            "f6b17a"
        ]
    },
    {
        "id": "43766cf8fae5b1947076453b",
        "tags": [
            "teal",
            "yellow",
            "white",
            "beige",
            "brown",
            "vintage",
            "wedding",
            "earth",
            "nature",
            "fall",
            "christmas",
            "food"
        ],
        "colors": [
            "43766c",
            "f8fae5",
            "b19470",
            "76453b"
        ]
    },
    {
        "id": "92c7cfaad7d9fbf9f1e5e1da",
        "tags": [
            "blue",
            "white",
            "beige",
            "grey",
            "sky",
            "light",
            "pastel"
        ],
        "colors": [
            "92c7cf",
            "aad7d9",
            "fbf9f1",
            "e5e1da"
        ]
    },
    {
        "id": "3d3b40525cebbfcfe7f8edff",
        "tags": [
            "black",
            "blue",
            "grey",
            "pink",
            "space",
            "retro",
            "winter"
        ],
        "colors": [
            "3d3b40",
            "525ceb",
            "bfcfe7",
            "f8edff"
        ]
    },
    {
        "id": "ffe7c1f3ccf3e9a8f2dc84f3",
        "tags": [
            "beige",
            "purple",
            "kids",
            "warm",
            "spring"
        ],
        "colors": [
            "ffe7c1",
            "f3ccf3",
            "e9a8f2",
            "dc84f3"
        ]
    },
    {
        "id": "ffffecf1e4c3c6a969597e52",
        "tags": [
            "white",
            "yellow",
            "beige",
            "brown",
            "green",
            "nature",
            "fall",
            "food",
            "summer"
        ],
        "colors": [
            "ffffec",
            "f1e4c3",
            "c6a969",
            "597e52"
        ]
    },
    {
        "id": "eef5ffb4d4ff86b6f6176b87",
        "tags": [
            "blue",
            "teal",
            "gradient",
            "sky",
            "sea",
            "winter",
            "cold"
        ],
        "colors": [
            "eef5ff",
            "b4d4ff",
            "86b6f6",
            "176b87"
        ]
    },
    {
        "id": "11009e4942e4e6b9defae7f3",
        "tags": [
            "navy",
            "blue",
            "pink",
            "peach",
            "space",
            "wedding",
            "cold"
        ],
        "colors": [
            "11009e",
            "4942e4",
            "e6b9de",
            "fae7f3"
        ]
    },
    {
        "id": "4f6f5273907286a789d2e3c8",
        "tags": [
            "green",
            "sage",
            "nature",
            "summer",
            "food",
            "gradient",
            "vintage"
        ],
        "colors": [
            "4f6f52",
            "739072",
            "86a789",
            "d2e3c8"
        ]
    },
    {
        "id": "f2afefc499f37360df33186b",
        "tags": [
            "pink",
            "purple",
            "navy",
            "gradient"
        ],
        "colors": [
            "f2afef",
            "c499f3",
            "7360df",
            "33186b"
        ]
    },
    {
        "id": "11235a596fb7c6cf9bf6eca9",
        "tags": [
            "navy",
            "blue",
            "sage",
            "yellow",
            "wedding",
            "gradient",
            "cold",
            "winter"
        ],
        "colors": [
            "11235a",
            "596fb7",
            "c6cf9b",
            "f6eca9"
        ]
    },
    {
        "id": "756ab6ac87c5e0aed0ffe5e5",
        "tags": [
            "purple",
            "peach",
            "sunset",
            "gradient",
            "pastel",
            "warm",
            "sky",
            "kids"
        ],
        "colors": [
            "756ab6",
            "ac87c5",
            "e0aed0",
            "ffe5e5"
        ]
    },
    {
        "id": "7bd3eaa1eebdf6f7c4f6d6d6",
        "tags": [
            "blue",
            "green",
            "yellow",
            "peach",
            "pastel",
            "kids",
            "light",
            "rainbow",
            "happy",
            "spring"
        ],
        "colors": [
            "7bd3ea",
            "a1eebd",
            "f6f7c4",
            "f6d6d6"
        ]
    },
    {
        "id": "7d0a0abf3131ead196f3edc8",
        "tags": [
            "maroon",
            "red",
            "beige",
            "yellow",
            "warm",
            "christmas",
            "retro"
        ],
        "colors": [
            "7d0a0a",
            "bf3131",
            "ead196",
            "f3edc8"
        ]
    },
    {
        "id": "52d3d83887be38419d200e3a",
        "tags": [
            "teal",
            "blue",
            "navy",
            "cold",
            "winter",
            "sea",
            "gradient",
            "night"
        ],
        "colors": [
            "52d3d8",
            "3887be",
            "38419d",
            "200e3a"
        ]
    },
    {
        "id": "5f8670ff9800b80000820300",
        "tags": [
            "teal",
            "orange",
            "red",
            "maroon",
            "vintage",
            "wedding",
            "christmas",
            "food"
        ],
        "colors": [
            "5f8670",
            "ff9800",
            "b80000",
            "820300"
        ]
    },
    {
        "id": "3924675d3587a367b1ffd1e3",
        "tags": [
            "purple",
            "pink",
            "night",
            "space",
            "gradient",
            "halloween"
        ],
        "colors": [
            "392467",
            "5d3587",
            "a367b1",
            "ffd1e3"
        ]
    },
    {
        "id": "c3e2c2eaecccdbcc95cd8d7a",
        "tags": [
            "green",
            "sage",
            "yellow",
            "beige",
            "peach",
            "pastel",
            "vintage",
            "nature",
            "cream",
            "kids",
            "light",
            "wedding",
            "earth",
            "food"
        ],
        "colors": [
            "c3e2c2",
            "eaeccc",
            "dbcc95",
            "cd8d7a"
        ]
    },
    {
        "id": "ffecd64cb9e73559e00f2167",
        "tags": [
            "beige",
            "blue",
            "navy",
            "sea",
            "kids",
            "winter"
        ],
        "colors": [
            "ffecd6",
            "4cb9e7",
            "3559e0",
            "0f2167"
        ]
    },
    {
        "id": "607274faeed1ded0b6b2a59b",
        "tags": [
            "grey",
            "yellow",
            "beige",
            "brown",
            "vintage",
            "coffee",
            "earth",
            "cream"
        ],
        "colors": [
            "607274",
            "faeed1",
            "ded0b6",
            "b2a59b"
        ]
    },
    {
        "id": "5f0f40fb8b24e364149a031e",
        "tags": [
            "maroon",
            "orange",
            "red",
            "gold",
            "warm",
            "food"
        ],
        "colors": [
            "5f0f40",
            "fb8b24",
            "e36414",
            "9a031e"
        ]
    },
    {
        "id": "163020304d30b6c4b6eef0e5",
        "tags": [
            "green",
            "sage",
            "grey",
            "nature",
            "gradient",
            "winter"
        ],
        "colors": [
            "163020",
            "304d30",
            "b6c4b6",
            "eef0e5"
        ]
    },
    {
        "id": "f3f8ffe26ee57e30e149108b",
        "tags": [
            "white",
            "pink",
            "purple",
            "wedding",
            "gradient",
            "happy",
            "neon",
            "retro"
        ],
        "colors": [
            "f3f8ff",
            "e26ee5",
            "7e30e1",
            "49108b"
        ]
    },
    {
        "id": "88ab8eafc8adeee7daf2f1eb",
        "tags": [
            "green",
            "sage",
            "beige",
            "grey",
            "summer",
            "pastel",
            "kids",
            "light",
            "cream",
            "nature",
            "earth",
            "food"
        ],
        "colors": [
            "88ab8e",
            "afc8ad",
            "eee7da",
            "f2f1eb"
        ]
    },
    {
        "id": "ffb534fbf6eec1f2b065b741",
        "tags": [
            "orange",
            "white",
            "green",
            "food",
            "happy",
            "nature",
            "summer"
        ],
        "colors": [
            "ffb534",
            "fbf6ee",
            "c1f2b0",
            "65b741"
        ]
    },
    {
        "id": "711db0c21292ef4040ffa732",
        "tags": [
            "purple",
            "red",
            "orange",
            "sunset",
            "gradient",
            "retro",
            "warm",
            "space"
        ],
        "colors": [
            "711db0",
            "c21292",
            "ef4040",
            "ffa732"
        ]
    },
    {
        "id": "9bb8cdfff7d4eec759b1c381",
        "tags": [
            "blue",
            "beige",
            "yellow",
            "sage",
            "nature",
            "summer",
            "pastel",
            "kids"
        ],
        "colors": [
            "9bb8cd",
            "fff7d4",
            "eec759",
            "b1c381"
        ]
    },
    {
        "id": "0926351b42425c83749ec8b9",
        "tags": [
            "black",
            "teal",
            "sage",
            "night",
            "dark",
            "sea",
            "winter"
        ],
        "colors": [
            "092635",
            "1b4242",
            "5c8374",
            "9ec8b9"
        ]
    },
    {
        "id": "fff78affe382ffc47effad84",
        "tags": [
            "yellow",
            "orange",
            "peach",
            "sunset",
            "warm",
            "summer",
            "happy"
        ],
        "colors": [
            "fff78a",
            "ffe382",
            "ffc47e",
            "ffad84"
        ]
    },
    {
        "id": "ff90bcffc0d9f9f9e08acdd7",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "kids",
            "pastel"
        ],
        "colors": [
            "ff90bc",
            "ffc0d9",
            "f9f9e0",
            "8acdd7"
        ]
    },
    {
        "id": "527853f9e8d9f7b787ee7214",
        "tags": [
            "green",
            "beige",
            "peach",
            "orange",
            "vintage",
            "retro",
            "food",
            "nature",
            "christmas"
        ],
        "colors": [
            "527853",
            "f9e8d9",
            "f7b787",
            "ee7214"
        ]
    },
    {
        "id": "191919750e21e3651dbed754",
        "tags": [
            "black",
            "maroon",
            "orange",
            "green",
            "dark",
            "winter",
            "christmas",
            "halloween"
        ],
        "colors": [
            "191919",
            "750e21",
            "e3651d",
            "bed754"
        ]
    },
    {
        "id": "637e76c69774f8dfd4ffefe8",
        "tags": [
            "teal",
            "brown",
            "peach",
            "earth",
            "vintage"
        ],
        "colors": [
            "637e76",
            "c69774",
            "f8dfd4",
            "ffefe8"
        ]
    },
    {
        "id": "df826cf8ffd2d0f2888adab2",
        "tags": [
            "red",
            "green",
            "teal",
            "kids",
            "happy",
            "nature",
            "spring"
        ],
        "colors": [
            "df826c",
            "f8ffd2",
            "d0f288",
            "8adab2"
        ]
    },
    {
        "id": "161a3031304db6bbc4f0ece5",
        "tags": [
            "navy",
            "grey",
            "winter",
            "cold",
            "wedding"
        ],
        "colors": [
            "161a30",
            "31304d",
            "b6bbc4",
            "f0ece5"
        ]
    },
    {
        "id": "fff5c2f4f27e6db9ef3081d0",
        "tags": [
            "yellow",
            "blue",
            "sea",
            "kids"
        ],
        "colors": [
            "fff5c2",
            "f4f27e",
            "6db9ef",
            "3081d0"
        ]
    },
    {
        "id": "fed9ede7bcdebb9cc067729d",
        "tags": [
            "pink",
            "purple",
            "navy",
            "gradient",
            "wedding"
        ],
        "colors": [
            "fed9ed",
            "e7bcde",
            "bb9cc0",
            "67729d"
        ]
    },
    {
        "id": "c5fff896efff5fbdff7b66ff",
        "tags": [
            "mint",
            "blue",
            "purple",
            "cold",
            "sky",
            "sea",
            "winter",
            "gradient"
        ],
        "colors": [
            "c5fff8",
            "96efff",
            "5fbdff",
            "7b66ff"
        ]
    },
    {
        "id": "fdf7e4faeed1ded0b6bbab8c",
        "tags": [
            "beige",
            "brown",
            "cream",
            "coffee",
            "skin",
            "warm",
            "light"
        ],
        "colors": [
            "fdf7e4",
            "faeed1",
            "ded0b6",
            "bbab8c"
        ]
    },
    {
        "id": "6b240c994d1ce48f45f5cca0",
        "tags": [
            "maroon",
            "brown",
            "orange",
            "gold",
            "skin",
            "warm",
            "gradient"
        ],
        "colors": [
            "6b240c",
            "994d1c",
            "e48f45",
            "f5cca0"
        ]
    },
    {
        "id": "5f6f52a9b388fefae0b99470",
        "tags": [
            "green",
            "sage",
            "beige",
            "brown",
            "earth",
            "fall",
            "vintage",
            "food",
            "christmas"
        ],
        "colors": [
            "5f6f52",
            "a9b388",
            "fefae0",
            "b99470"
        ]
    },
    {
        "id": "2b2a4cb31312ea906ceee2de",
        "tags": [
            "navy",
            "red",
            "orange",
            "peach",
            "grey",
            "retro",
            "space",
            "halloween"
        ],
        "colors": [
            "2b2a4c",
            "b31312",
            "ea906c",
            "eee2de"
        ]
    },
    {
        "id": "7ed7c1f0dbafdc8686b06161",
        "tags": [
            "teal",
            "beige",
            "peach",
            "red",
            "maroon",
            "retro",
            "pastel",
            "rainbow",
            "kids"
        ],
        "colors": [
            "7ed7c1",
            "f0dbaf",
            "dc8686",
            "b06161"
        ]
    },
    {
        "id": "ecf4d69ad0c22d9596265073",
        "tags": [
            "sage",
            "teal",
            "navy",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "ecf4d6",
            "9ad0c2",
            "2d9596",
            "265073"
        ]
    },
    {
        "id": "ff8f8feef2969ade7b508d69",
        "tags": [
            "red",
            "peach",
            "yellow",
            "green",
            "spring",
            "nature",
            "kids"
        ],
        "colors": [
            "ff8f8f",
            "eef296",
            "9ade7b",
            "508d69"
        ]
    },
    {
        "id": "7071e8c683d7ed9ed6ffc7c7",
        "tags": [
            "blue",
            "purple",
            "pink",
            "peach",
            "retro",
            "wedding"
        ],
        "colors": [
            "7071e8",
            "c683d7",
            "ed9ed6",
            "ffc7c7"
        ]
    },
    {
        "id": "eef5ff9eb8d97c93c3a25772",
        "tags": [
            "blue",
            "maroon",
            "winter",
            "wedding",
            "cold"
        ],
        "colors": [
            "eef5ff",
            "9eb8d9",
            "7c93c3",
            "a25772"
        ]
    },
    {
        "id": "0766ad29adb2c5e898f3f3f3",
        "tags": [
            "blue",
            "teal",
            "green",
            "grey",
            "sea",
            "winter",
            "cold",
            "gradient"
        ],
        "colors": [
            "0766ad",
            "29adb2",
            "c5e898",
            "f3f3f3"
        ]
    },
    {
        "id": "ffc5c5ffebd8c7dca789b9ad",
        "tags": [
            "peach",
            "green",
            "teal",
            "pastel",
            "spring",
            "kids",
            "nature",
            "vintage",
            "light",
            "happy"
        ],
        "colors": [
            "ffc5c5",
            "ffebd8",
            "c7dca7",
            "89b9ad"
        ]
    },
    {
        "id": "000000f4dfc8f4eae0faf6f0",
        "tags": [
            "black",
            "beige",
            "vintage",
            "coffee",
            "warm"
        ],
        "colors": [
            "000000",
            "f4dfc8",
            "f4eae0",
            "faf6f0"
        ]
    },
    {
        "id": "860a35af2655a3b763f3f3f3",
        "tags": [
            "maroon",
            "green",
            "grey",
            "wedding",
            "christmas",
            "vintage"
        ],
        "colors": [
            "860a35",
            "af2655",
            "a3b763",
            "f3f3f3"
        ]
    },
    {
        "id": "83a2ffb4bdffffe3bbffd28f",
        "tags": [
            "blue",
            "beige",
            "orange",
            "sea",
            "summer",
            "kids"
        ],
        "colors": [
            "83a2ff",
            "b4bdff",
            "ffe3bb",
            "ffd28f"
        ]
    },
    {
        "id": "22092c872341be3144f05941",
        "tags": [
            "black",
            "maroon",
            "red",
            "orange",
            "dark",
            "warm",
            "gradient",
            "night",
            "halloween"
        ],
        "colors": [
            "22092c",
            "872341",
            "be3144",
            "f05941"
        ]
    },
    {
        "id": "001b791640d6ed5ab3ff90c2",
        "tags": [
            "navy",
            "blue",
            "pink",
            "space",
            "wedding",
            "retro"
        ],
        "colors": [
            "001b79",
            "1640d6",
            "ed5ab3",
            "ff90c2"
        ]
    },
    {
        "id": "ec8f5ef3b664f1eb909fbb73",
        "tags": [
            "orange",
            "yellow",
            "green",
            "warm",
            "vintage",
            "food",
            "nature",
            "kids"
        ],
        "colors": [
            "ec8f5e",
            "f3b664",
            "f1eb90",
            "9fbb73"
        ]
    },
    {
        "id": "f3eeeaebe3d5b0a695776b5d",
        "tags": [
            "grey",
            "beige",
            "brown",
            "cream",
            "coffee",
            "vintage",
            "pastel",
            "fall",
            "gradient"
        ],
        "colors": [
            "f3eeea",
            "ebe3d5",
            "b0a695",
            "776b5d"
        ]
    },
    {
        "id": "f2ffe9a6cf98557c55fa7070",
        "tags": [
            "green",
            "red",
            "nature",
            "spring",
            "food"
        ],
        "colors": [
            "f2ffe9",
            "a6cf98",
            "557c55",
            "fa7070"
        ]
    },
    {
        "id": "f1eaffe5d4ffdcbfffd0a2f7",
        "tags": [
            "purple",
            "light",
            "gradient",
            "cream"
        ],
        "colors": [
            "f1eaff",
            "e5d4ff",
            "dcbfff",
            "d0a2f7"
        ]
    },
    {
        "id": "363062435585818fb4f5e8c7",
        "tags": [
            "navy",
            "blue",
            "beige",
            "dark",
            "winter",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "363062",
            "435585",
            "818fb4",
            "f5e8c7"
        ]
    },
    {
        "id": "e0f4ff87c4ff39a7ffffeed9",
        "tags": [
            "blue",
            "beige",
            "sea",
            "summer",
            "kids",
            "happy"
        ],
        "colors": [
            "e0f4ff",
            "87c4ff",
            "39a7ff",
            "ffeed9"
        ]
    },
    {
        "id": "2b3499ff6c22ff9209ffd099",
        "tags": [
            "navy",
            "orange",
            "beige",
            "retro",
            "kids"
        ],
        "colors": [
            "2b3499",
            "ff6c22",
            "ff9209",
            "ffd099"
        ]
    },
    {
        "id": "164863427d9d9bbec8ddf2fd",
        "tags": [
            "navy",
            "blue",
            "cold",
            "gradient",
            "winter",
            "wedding"
        ],
        "colors": [
            "164863",
            "427d9d",
            "9bbec8",
            "ddf2fd"
        ]
    },
    {
        "id": "61a3baffffddd2de32a2c579",
        "tags": [
            "blue",
            "beige",
            "green",
            "sage",
            "spring",
            "summer",
            "nature",
            "happy"
        ],
        "colors": [
            "61a3ba",
            "ffffdd",
            "d2de32",
            "a2c579"
        ]
    },
    {
        "id": "fffbf5f7efe5c3acd07743db",
        "tags": [
            "white",
            "beige",
            "purple",
            "light",
            "wedding",
            "gradient"
        ],
        "colors": [
            "fffbf5",
            "f7efe5",
            "c3acd0",
            "7743db"
        ]
    },
    {
        "id": "a9a9a9fecda6ff9130ff5b22",
        "tags": [
            "grey",
            "peach",
            "orange",
            "vintage",
            "food"
        ],
        "colors": [
            "a9a9a9",
            "fecda6",
            "ff9130",
            "ff5b22"
        ]
    },
    {
        "id": "ece3ce7390724f6f523a4d39",
        "tags": [
            "beige",
            "sage",
            "earth",
            "nature",
            "vintage",
            "pastel",
            "winter",
            "food"
        ],
        "colors": [
            "ece3ce",
            "739072",
            "4f6f52",
            "3a4d39"
        ]
    },
    {
        "id": "706233b0926ae1c78ffae7c9",
        "tags": [
            "brown",
            "beige",
            "warm",
            "fall",
            "cream",
            "coffee",
            "skin"
        ],
        "colors": [
            "706233",
            "b0926a",
            "e1c78f",
            "fae7c9"
        ]
    },
    {
        "id": "0c356a0174beffc436fff0ce",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "wedding"
        ],
        "colors": [
            "0c356a",
            "0174be",
            "ffc436",
            "fff0ce"
        ]
    },
    {
        "id": "86a789b2c8bad2e3c8ebf3e8",
        "tags": [
            "sage",
            "cream",
            "light",
            "nature",
            "earth"
        ],
        "colors": [
            "86a789",
            "b2c8ba",
            "d2e3c8",
            "ebf3e8"
        ]
    },
    {
        "id": "3d30a2b15effffa33cfffb73",
        "tags": [
            "navy",
            "purple",
            "orange",
            "yellow",
            "sunset",
            "kids"
        ],
        "colors": [
            "3d30a2",
            "b15eff",
            "ffa33c",
            "fffb73"
        ]
    },
    {
        "id": "fcf5edf4bf96ce5a671f1717",
        "tags": [
            "beige",
            "peach",
            "red",
            "black",
            "warm",
            "gold",
            "christmas",
            "retro"
        ],
        "colors": [
            "fcf5ed",
            "f4bf96",
            "ce5a67",
            "1f1717"
        ]
    },
    {
        "id": "00a9ff89cff3a0e9ffcdf5fd",
        "tags": [
            "blue",
            "sky",
            "sea",
            "cold",
            "kids",
            "light"
        ],
        "colors": [
            "00a9ff",
            "89cff3",
            "a0e9ff",
            "cdf5fd"
        ]
    },
    {
        "id": "f875aaffdfdffff6f6aedefc",
        "tags": [
            "pink",
            "peach",
            "white",
            "blue",
            "light",
            "kids"
        ],
        "colors": [
            "f875aa",
            "ffdfdf",
            "fff6f6",
            "aedefc"
        ]
    },
    {
        "id": "1904827752fe8e8ffac2d9ff",
        "tags": [
            "navy",
            "purple",
            "blue",
            "cold",
            "night",
            "space",
            "gradient"
        ],
        "colors": [
            "190482",
            "7752fe",
            "8e8ffa",
            "c2d9ff"
        ]
    },
    {
        "id": "ed7d316c5f5b4f4a45f6f1ee",
        "tags": [
            "orange",
            "brown",
            "white",
            "vintage",
            "warm",
            "halloween",
            "food"
        ],
        "colors": [
            "ed7d31",
            "6c5f5b",
            "4f4a45",
            "f6f1ee"
        ]
    },
    {
        "id": "f5f7f8f4ce14495e5745474b",
        "tags": [
            "white",
            "grey",
            "yellow",
            "sage",
            "black",
            "retro"
        ],
        "colors": [
            "f5f7f8",
            "f4ce14",
            "495e57",
            "45474b"
        ]
    },
    {
        "id": "f9b57299b080748e63faf8ed",
        "tags": [
            "orange",
            "sage",
            "green",
            "white",
            "beige",
            "pastel",
            "nature",
            "food",
            "light"
        ],
        "colors": [
            "f9b572",
            "99b080",
            "748e63",
            "faf8ed"
        ]
    },
    {
        "id": "daddb1b3a492bfb29ed6c7ae",
        "tags": [
            "sage",
            "brown",
            "pastel",
            "vintage",
            "cream",
            "light",
            "fall",
            "earth"
        ],
        "colors": [
            "daddb1",
            "b3a492",
            "bfb29e",
            "d6c7ae"
        ]
    },
    {
        "id": "1926553876bfe1aa74f3f0ca",
        "tags": [
            "navy",
            "blue",
            "orange",
            "beige",
            "sea",
            "wedding",
            "vintage"
        ],
        "colors": [
            "192655",
            "3876bf",
            "e1aa74",
            "f3f0ca"
        ]
    },
    {
        "id": "a7d397f5eec8d0d4ca555843",
        "tags": [
            "green",
            "yellow",
            "grey",
            "sage",
            "vintage",
            "nature"
        ],
        "colors": [
            "a7d397",
            "f5eec8",
            "d0d4ca",
            "555843"
        ]
    },
    {
        "id": "fbecb2f8bdeb5272f2072541",
        "tags": [
            "yellow",
            "pink",
            "blue",
            "black",
            "navy",
            "kids",
            "rainbow",
            "retro"
        ],
        "colors": [
            "fbecb2",
            "f8bdeb",
            "5272f2",
            "072541"
        ]
    },
    {
        "id": "d6d46df4dfb6de8f5f9a4444",
        "tags": [
            "sage",
            "beige",
            "orange",
            "maroon",
            "food",
            "warm",
            "gold",
            "fall",
            "christmas"
        ],
        "colors": [
            "d6d46d",
            "f4dfb6",
            "de8f5f",
            "9a4444"
        ]
    },
    {
        "id": "b6fffa98e4ff80b3ff687eff",
        "tags": [
            "mint",
            "blue",
            "neon",
            "gradient",
            "sky",
            "summer",
            "cold"
        ],
        "colors": [
            "b6fffa",
            "98e4ff",
            "80b3ff",
            "687eff"
        ]
    },
    {
        "id": "610c9f940b92da0c81e95793",
        "tags": [
            "purple",
            "maroon",
            "red",
            "pink",
            "dark",
            "space",
            "warm"
        ],
        "colors": [
            "610c9f",
            "940b92",
            "da0c81",
            "e95793"
        ]
    },
    {
        "id": "3630624d4c7df99417f5f5f5",
        "tags": [
            "navy",
            "orange",
            "grey",
            "white",
            "retro",
            "wedding",
            "night"
        ],
        "colors": [
            "363062",
            "4d4c7d",
            "f99417",
            "f5f5f5"
        ]
    },
    {
        "id": "beadfad0bfffdfccfbfff8c9",
        "tags": [
            "purple",
            "yellow",
            "pastel",
            "light",
            "kids",
            "wedding",
            "spring"
        ],
        "colors": [
            "beadfa",
            "d0bfff",
            "dfccfb",
            "fff8c9"
        ]
    },
    {
        "id": "0f0f0f232d3f005b41008170",
        "tags": [
            "black",
            "teal",
            "night",
            "space",
            "dark",
            "halloween",
            "cold"
        ],
        "colors": [
            "0f0f0f",
            "232d3f",
            "005b41",
            "008170"
        ]
    },
    {
        "id": "0802a3ff4b91ff7676ffcd4b",
        "tags": [
            "navy",
            "blue",
            "red",
            "pink",
            "peach",
            "orange",
            "yellow",
            "rainbow",
            "kids",
            "happy",
            "retro"
        ],
        "colors": [
            "0802a3",
            "ff4b91",
            "ff7676",
            "ffcd4b"
        ]
    },
    {
        "id": "ff8080ffcf96f6fdc3cdfad5",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "rainbow",
            "summer",
            "pastel",
            "kids",
            "spring",
            "happy"
        ],
        "colors": [
            "ff8080",
            "ffcf96",
            "f6fdc3",
            "cdfad5"
        ]
    },
    {
        "id": "cd5c08f5e8b7c1d8c36a9c89",
        "tags": [
            "orange",
            "beige",
            "sage",
            "teal",
            "vintage",
            "wedding",
            "fall",
            "christmas"
        ],
        "colors": [
            "cd5c08",
            "f5e8b7",
            "c1d8c3",
            "6a9c89"
        ]
    },
    {
        "id": "04364a176b8764ccc5dafffb",
        "tags": [
            "navy",
            "teal",
            "mint",
            "sea",
            "cold",
            "winter"
        ],
        "colors": [
            "04364a",
            "176b87",
            "64ccc5",
            "dafffb"
        ]
    },
    {
        "id": "1320431f4172f1b4bbfdf0f0",
        "tags": [
            "navy",
            "pink",
            "peach",
            "wedding",
            "kids",
            "vintage"
        ],
        "colors": [
            "132043",
            "1f4172",
            "f1b4bb",
            "fdf0f0"
        ]
    },
    {
        "id": "362fd91aacac2e97a7eeeeee",
        "tags": [
            "blue",
            "teal",
            "grey",
            "cold",
            "wedding",
            "winter",
            "kids"
        ],
        "colors": [
            "362fd9",
            "1aacac",
            "2e97a7",
            "eeeeee"
        ]
    },
    {
        "id": "5d12d2b931fcff6ac2ffe5e5",
        "tags": [
            "purple",
            "pink",
            "peach",
            "retro",
            "space"
        ],
        "colors": [
            "5d12d2",
            "b931fc",
            "ff6ac2",
            "ffe5e5"
        ]
    },
    {
        "id": "fff2d8ead7bbbca37f113946",
        "tags": [
            "beige",
            "brown",
            "navy",
            "vintage",
            "skin",
            "coffee",
            "warm",
            "wedding"
        ],
        "colors": [
            "fff2d8",
            "ead7bb",
            "bca37f",
            "113946"
        ]
    },
    {
        "id": "001524445d48d6cc99fde5d4",
        "tags": [
            "black",
            "green",
            "sage",
            "peach",
            "vintage",
            "wedding",
            "winter",
            "earth"
        ],
        "colors": [
            "001524",
            "445d48",
            "d6cc99",
            "fde5d4"
        ]
    },
    {
        "id": "186f65b5cb99fce09bb2533e",
        "tags": [
            "teal",
            "green",
            "yellow",
            "maroon",
            "fall",
            "food",
            "vintage"
        ],
        "colors": [
            "186f65",
            "b5cb99",
            "fce09b",
            "b2533e"
        ]
    },
    {
        "id": "ffe4d6facbead988b9b0578d",
        "tags": [
            "peach",
            "pink",
            "purple",
            "kids",
            "gradient"
        ],
        "colors": [
            "ffe4d6",
            "facbea",
            "d988b9",
            "b0578d"
        ]
    },
    {
        "id": "d2e0fbf9f3ccd7e5ca8eaccd",
        "tags": [
            "blue",
            "yellow",
            "green",
            "sage",
            "kids",
            "pastel",
            "light",
            "happy"
        ],
        "colors": [
            "d2e0fb",
            "f9f3cc",
            "d7e5ca",
            "8eaccd"
        ]
    },
    {
        "id": "6499e99eddffa6f6ffbefff7",
        "tags": [
            "blue",
            "mint",
            "cold",
            "sky",
            "gradient",
            "neon"
        ],
        "colors": [
            "6499e9",
            "9eddff",
            "a6f6ff",
            "befff7"
        ]
    },
    {
        "id": "2e43744b527e7c81ade5c3a6",
        "tags": [
            "navy",
            "blue",
            "beige",
            "cold",
            "winter",
            "sea",
            "night"
        ],
        "colors": [
            "2e4374",
            "4b527e",
            "7c81ad",
            "e5c3a6"
        ]
    },
    {
        "id": "fff5e0ff6969c70039141e46",
        "tags": [
            "beige",
            "peach",
            "red",
            "maroon",
            "navy",
            "kids",
            "wedding"
        ],
        "colors": [
            "fff5e0",
            "ff6969",
            "c70039",
            "141e46"
        ]
    },
    {
        "id": "12486b41919778d6c6f5fccd",
        "tags": [
            "navy",
            "teal",
            "yellow",
            "sea",
            "gradient",
            "cold"
        ],
        "colors": [
            "12486b",
            "419197",
            "78d6c6",
            "f5fccd"
        ]
    },
    {
        "id": "219c90e9b824ee9322d83f31",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "red",
            "kids",
            "vintage",
            "retro"
        ],
        "colors": [
            "219c90",
            "e9b824",
            "ee9322",
            "d83f31"
        ]
    },
    {
        "id": "61826479ac78b0d9b1d0e7d2",
        "tags": [
            "sage",
            "green",
            "pastel",
            "earth",
            "food",
            "nature"
        ],
        "colors": [
            "618264",
            "79ac78",
            "b0d9b1",
            "d0e7d2"
        ]
    },
    {
        "id": "faf2d3f4e8693085c35cd2e6",
        "tags": [
            "beige",
            "yellow",
            "blue",
            "summer",
            "sea",
            "retro"
        ],
        "colors": [
            "faf2d3",
            "f4e869",
            "3085c3",
            "5cd2e6"
        ]
    },
    {
        "id": "5b0888713abe9d76c1e5cff7",
        "tags": [
            "purple",
            "space",
            "gradient"
        ],
        "colors": [
            "5b0888",
            "713abe",
            "9d76c1",
            "e5cff7"
        ]
    },
    {
        "id": "3d0c11d80032f78ca2f9dec9",
        "tags": [
            "maroon",
            "red",
            "pink",
            "peach",
            "beige",
            "gradient",
            "warm"
        ],
        "colors": [
            "3d0c11",
            "d80032",
            "f78ca2",
            "f9dec9"
        ]
    },
    {
        "id": "f1efefccc8aa7d7c7c191717",
        "tags": [
            "grey",
            "cold",
            "vintage"
        ],
        "colors": [
            "f1efef",
            "ccc8aa",
            "7d7c7c",
            "191717"
        ]
    },
    {
        "id": "ebe4d1b4b4b326577ce55604",
        "tags": [
            "beige",
            "grey",
            "navy",
            "orange",
            "vintage"
        ],
        "colors": [
            "ebe4d1",
            "b4b4b3",
            "26577c",
            "e55604"
        ]
    },
    {
        "id": "004225f5f5dcffb000ffcf9d",
        "tags": [
            "green",
            "orange",
            "peach",
            "vintage",
            "gold",
            "wedding",
            "warm",
            "food"
        ],
        "colors": [
            "004225",
            "f5f5dc",
            "ffb000",
            "ffcf9d"
        ]
    },
    {
        "id": "07195208839535a29ff2f7a1",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "cold",
            "winter",
            "sky",
            "sea",
            "gradient"
        ],
        "colors": [
            "071952",
            "088395",
            "35a29f",
            "f2f7a1"
        ]
    },
    {
        "id": "ecee818ddfcb82a0d8edb7ed",
        "tags": [
            "yellow",
            "mint",
            "blue",
            "pink",
            "rainbow",
            "kids",
            "happy",
            "pastel",
            "spring"
        ],
        "colors": [
            "ecee81",
            "8ddfcb",
            "82a0d8",
            "edb7ed"
        ]
    },
    {
        "id": "ffcc70fffadd8ecddd22668d",
        "tags": [
            "orange",
            "yellow",
            "blue",
            "navy",
            "summer",
            "kids"
        ],
        "colors": [
            "ffcc70",
            "fffadd",
            "8ecddd",
            "22668d"
        ]
    },
    {
        "id": "451952662549ae445af39f5a",
        "tags": [
            "purple",
            "maroon",
            "orange",
            "night",
            "space",
            "dark",
            "gradient",
            "warm",
            "skin",
            "gold",
            "halloween"
        ],
        "colors": [
            "451952",
            "662549",
            "ae445a",
            "f39f5a"
        ]
    },
    {
        "id": "f8f0e5eadbc8dac0a30f2c59",
        "tags": [
            "beige",
            "navy",
            "skin",
            "vintage",
            "wedding",
            "cream"
        ],
        "colors": [
            "f8f0e5",
            "eadbc8",
            "dac0a3",
            "0f2c59"
        ]
    },
    {
        "id": "f0f0f02135554f709ce5d283",
        "tags": [
            "grey",
            "navy",
            "blue",
            "yellow",
            "vintage",
            "wedding",
            "cold",
            "winter"
        ],
        "colors": [
            "f0f0f0",
            "213555",
            "4f709c",
            "e5d283"
        ]
    },
    {
        "id": "57375dff3fa4ff9b82ffc8c8",
        "tags": [
            "purple",
            "pink",
            "orange",
            "peach",
            "warm",
            "gradient",
            "kids"
        ],
        "colors": [
            "57375d",
            "ff3fa4",
            "ff9b82",
            "ffc8c8"
        ]
    },
    {
        "id": "27005d9400ffaed2ffe4f1ff",
        "tags": [
            "navy",
            "purple",
            "blue",
            "neon",
            "cold"
        ],
        "colors": [
            "27005d",
            "9400ff",
            "aed2ff",
            "e4f1ff"
        ]
    },
    {
        "id": "ffa1f5bc7af9f8ff95a6ff96",
        "tags": [
            "pink",
            "purple",
            "yellow",
            "green",
            "neon",
            "kids",
            "spring",
            "happy"
        ],
        "colors": [
            "ffa1f5",
            "bc7af9",
            "f8ff95",
            "a6ff96"
        ]
    },
    {
        "id": "ef9595efb495efd595ebef95",
        "tags": [
            "peach",
            "orange",
            "yellow",
            "sunset",
            "pastel",
            "warm",
            "gold",
            "summer",
            "food"
        ],
        "colors": [
            "ef9595",
            "efb495",
            "efd595",
            "ebef95"
        ]
    },
    {
        "id": "053b50176b8764ccc5eeeeee",
        "tags": [
            "navy",
            "blue",
            "teal",
            "grey",
            "cold",
            "winter",
            "gradient"
        ],
        "colors": [
            "053b50",
            "176b87",
            "64ccc5",
            "eeeeee"
        ]
    },
    {
        "id": "016a70ffffddd2de32a2c579",
        "tags": [
            "teal",
            "yellow",
            "green",
            "sage",
            "vintage",
            "summer",
            "nature",
            "cold"
        ],
        "colors": [
            "016a70",
            "ffffdd",
            "d2de32",
            "a2c579"
        ]
    },
    {
        "id": "952323a73121dad4b5f2e8c6",
        "tags": [
            "maroon",
            "red",
            "beige",
            "warm",
            "food",
            "wedding"
        ],
        "colors": [
            "952323",
            "a73121",
            "dad4b5",
            "f2e8c6"
        ]
    },
    {
        "id": "ffbb5cff9b50e25e3ec63d2f",
        "tags": [
            "orange",
            "red",
            "warm",
            "gradient",
            "fall",
            "gold"
        ],
        "colors": [
            "ffbb5c",
            "ff9b50",
            "e25e3e",
            "c63d2f"
        ]
    },
    {
        "id": "0e21a04d2db79d44c0ec53b0",
        "tags": [
            "navy",
            "blue",
            "purple",
            "space",
            "retro",
            "gradient",
            "halloween"
        ],
        "colors": [
            "0e21a0",
            "4d2db7",
            "9d44c0",
            "ec53b0"
        ]
    },
    {
        "id": "94a684aec3aee4e4d0ffeef4",
        "tags": [
            "sage",
            "green",
            "pink",
            "pastel",
            "vintage",
            "light",
            "nature",
            "earth",
            "food",
            "cream"
        ],
        "colors": [
            "94a684",
            "aec3ae",
            "e4e4d0",
            "ffeef4"
        ]
    },
    {
        "id": "45ffcafeffacffb6d9d67bff",
        "tags": [
            "yellow",
            "mint",
            "pink",
            "purple",
            "kids",
            "neon",
            "light",
            "happy"
        ],
        "colors": [
            "45ffca",
            "feffac",
            "ffb6d9",
            "d67bff"
        ]
    },
    {
        "id": "9a3b3bc08261e2c799f2ecbe",
        "tags": [
            "maroon",
            "brown",
            "beige",
            "yellow",
            "vintage",
            "gold",
            "warm",
            "skin",
            "sunset",
            "gradient",
            "coffee"
        ],
        "colors": [
            "9a3b3b",
            "c08261",
            "e2c799",
            "f2ecbe"
        ]
    },
    {
        "id": "fbf0b2ffc7ead8b4f8caedff",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "blue",
            "light",
            "sunset",
            "summer",
            "happy",
            "rainbow"
        ],
        "colors": [
            "fbf0b2",
            "ffc7ea",
            "d8b4f8",
            "caedff"
        ]
    },
    {
        "id": "96c291ffdbaaffb7b7f4eeee",
        "tags": [
            "green",
            "beige",
            "peach",
            "grey",
            "vintage",
            "nature",
            "spring"
        ],
        "colors": [
            "96c291",
            "ffdbaa",
            "ffb7b7",
            "f4eeee"
        ]
    },
    {
        "id": "793fdf7091f597fff4fffd8c",
        "tags": [
            "purple",
            "blue",
            "mint",
            "yellow",
            "neon",
            "gradient",
            "cold"
        ],
        "colors": [
            "793fdf",
            "7091f5",
            "97fff4",
            "fffd8c"
        ]
    },
    {
        "id": "040d12183d3d5c837493b1a6",
        "tags": [
            "black",
            "teal",
            "night",
            "winter",
            "dark",
            "cold",
            "sea"
        ],
        "colors": [
            "040d12",
            "183d3d",
            "5c8374",
            "93b1a6"
        ]
    },
    {
        "id": "faf1e4cedebd9eb384435334",
        "tags": [
            "beige",
            "green",
            "vintage",
            "food",
            "gradient",
            "wedding"
        ],
        "colors": [
            "faf1e4",
            "cedebd",
            "9eb384",
            "435334"
        ]
    },
    {
        "id": "191d881450a3337ccfffc436",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "sea",
            "kids"
        ],
        "colors": [
            "191d88",
            "1450a3",
            "337ccf",
            "ffc436"
        ]
    },
    {
        "id": "fff5e0ff6969bb2525141e46",
        "tags": [
            "beige",
            "red",
            "navy",
            "retro",
            "christmas"
        ],
        "colors": [
            "fff5e0",
            "ff6969",
            "bb2525",
            "141e46"
        ]
    },
    {
        "id": "352f445c5470b9b4c7faf0e6",
        "tags": [
            "grey",
            "beige",
            "gradient",
            "dark",
            "halloween",
            "night"
        ],
        "colors": [
            "352f44",
            "5c5470",
            "b9b4c7",
            "faf0e6"
        ]
    },
    {
        "id": "a8df8ef3fde8ffe5e5ffbfbf",
        "tags": [
            "green",
            "peach",
            "light",
            "summer",
            "spring",
            "food",
            "happy",
            "kids",
            "nature"
        ],
        "colors": [
            "a8df8e",
            "f3fde8",
            "ffe5e5",
            "ffbfbf"
        ]
    },
    {
        "id": "79155bc23373f6635cffba86",
        "tags": [
            "maroon",
            "purple",
            "orange",
            "beige",
            "sunset",
            "gradient",
            "warm",
            "gold"
        ],
        "colors": [
            "79155b",
            "c23373",
            "f6635c",
            "ffba86"
        ]
    },
    {
        "id": "0c356a279eff40f8ffd5ffd0",
        "tags": [
            "navy",
            "blue",
            "mint",
            "green",
            "sea",
            "cold",
            "winter",
            "gradient"
        ],
        "colors": [
            "0c356a",
            "279eff",
            "40f8ff",
            "d5ffd0"
        ]
    },
    {
        "id": "ebe76cf0b86eed7b7b836096",
        "tags": [
            "yellow",
            "orange",
            "peach",
            "purple",
            "retro",
            "kids",
            "gradient",
            "rainbow"
        ],
        "colors": [
            "ebe76c",
            "f0b86e",
            "ed7b7b",
            "836096"
        ]
    },
    {
        "id": "e19898a2678a4d3c773f1d38",
        "tags": [
            "peach",
            "purple",
            "navy",
            "black",
            "dark",
            "gradient",
            "night",
            "vintage",
            "skin"
        ],
        "colors": [
            "e19898",
            "a2678a",
            "4d3c77",
            "3f1d38"
        ]
    },
    {
        "id": "313866504099974ec3fe7be5",
        "tags": [
            "navy",
            "purple",
            "pink",
            "halloween",
            "gradient",
            "space"
        ],
        "colors": [
            "313866",
            "504099",
            "974ec3",
            "fe7be5"
        ]
    },
    {
        "id": "614bc333bbc585e6c5c8ffe0",
        "tags": [
            "purple",
            "teal",
            "mint",
            "winter",
            "cold",
            "kids"
        ],
        "colors": [
            "614bc3",
            "33bbc5",
            "85e6c5",
            "c8ffe0"
        ]
    },
    {
        "id": "fff3dadfccfbd0bfffbeadfa",
        "tags": [
            "beige",
            "purple",
            "pastel",
            "light",
            "kids",
            "cream"
        ],
        "colors": [
            "fff3da",
            "dfccfb",
            "d0bfff",
            "beadfa"
        ]
    },
    {
        "id": "96b6c5adc4ceeee0c9f1f0e8",
        "tags": [
            "blue",
            "grey",
            "beige",
            "pastel",
            "vintage",
            "light",
            "sea",
            "cream",
            "earth"
        ],
        "colors": [
            "96b6c5",
            "adc4ce",
            "eee0c9",
            "f1f0e8"
        ]
    },
    {
        "id": "900c3fc70039f94c10f8de22",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "gold",
            "neon",
            "gradient"
        ],
        "colors": [
            "900c3f",
            "c70039",
            "f94c10",
            "f8de22"
        ]
    },
    {
        "id": "f8f0e5eadbc8dac0a3102c57",
        "tags": [
            "beige",
            "navy",
            "warm",
            "gold",
            "skin",
            "vintage",
            "wedding"
        ],
        "colors": [
            "f8f0e5",
            "eadbc8",
            "dac0a3",
            "102c57"
        ]
    },
    {
        "id": "252b484450695b9a8bf7e987",
        "tags": [
            "black",
            "navy",
            "teal",
            "yellow",
            "night",
            "vintage",
            "winter"
        ],
        "colors": [
            "252b48",
            "445069",
            "5b9a8b",
            "f7e987"
        ]
    },
    {
        "id": "ffdbc39f91cc5c4b993d246c",
        "tags": [
            "peach",
            "purple",
            "navy",
            "retro",
            "wedding"
        ],
        "colors": [
            "ffdbc3",
            "9f91cc",
            "5c4b99",
            "3d246c"
        ]
    },
    {
        "id": "35155d512b814477ce8cabff",
        "tags": [
            "navy",
            "purple",
            "blue",
            "dark",
            "night",
            "sea",
            "winter"
        ],
        "colors": [
            "35155d",
            "512b81",
            "4477ce",
            "8cabff"
        ]
    },
    {
        "id": "c8e4b29ed2be7eaa92ffd9b7",
        "tags": [
            "sage",
            "green",
            "teal",
            "peach",
            "pastel",
            "nature",
            "summer",
            "kids",
            "light",
            "food"
        ],
        "colors": [
            "c8e4b2",
            "9ed2be",
            "7eaa92",
            "ffd9b7"
        ]
    },
    {
        "id": "ffc6acfff6dcc4c1a49e9fa5",
        "tags": [
            "peach",
            "yellow",
            "sage",
            "grey",
            "vintage",
            "pastel",
            "kids",
            "food"
        ],
        "colors": [
            "ffc6ac",
            "fff6dc",
            "c4c1a4",
            "9e9fa5"
        ]
    },
    {
        "id": "2414689f0d7fea1179f79bd3",
        "tags": [
            "navy",
            "maroon",
            "red",
            "pink",
            "halloween"
        ],
        "colors": [
            "241468",
            "9f0d7f",
            "ea1179",
            "f79bd3"
        ]
    },
    {
        "id": "6f61c0a084e88be8e5d5ffe4",
        "tags": [
            "purple",
            "mint",
            "retro",
            "neon",
            "cold",
            "happy"
        ],
        "colors": [
            "6f61c0",
            "a084e8",
            "8be8e5",
            "d5ffe4"
        ]
    },
    {
        "id": "eac696c8ae7d76582765451f",
        "tags": [
            "beige",
            "brown",
            "vintage",
            "earth",
            "nature",
            "gradient",
            "fall",
            "skin",
            "warm",
            "coffee"
        ],
        "colors": [
            "eac696",
            "c8ae7d",
            "765827",
            "65451f"
        ]
    },
    {
        "id": "27282961677ad8d9dafff6e0",
        "tags": [
            "black",
            "grey",
            "yellow",
            "night",
            "gradient"
        ],
        "colors": [
            "272829",
            "61677a",
            "d8d9da",
            "fff6e0"
        ]
    },
    {
        "id": "fde5ecfcbaade48586916db3",
        "tags": [
            "pink",
            "peach",
            "purple",
            "wedding",
            "happy",
            "gradient",
            "kids",
            "vintage",
            "sunset"
        ],
        "colors": [
            "fde5ec",
            "fcbaad",
            "e48586",
            "916db3"
        ]
    },
    {
        "id": "ffeeccffddccffccccfebbcc",
        "tags": [
            "yellow",
            "beige",
            "peach",
            "pink",
            "summer",
            "sunset",
            "light",
            "kids",
            "spring",
            "cream",
            "skin"
        ],
        "colors": [
            "ffeecc",
            "ffddcc",
            "ffcccc",
            "febbcc"
        ]
    },
    {
        "id": "3226538062d69288f8ffd2d7",
        "tags": [
            "navy",
            "purple",
            "peach",
            "night"
        ],
        "colors": [
            "322653",
            "8062d6",
            "9288f8",
            "ffd2d7"
        ]
    },
    {
        "id": "cece5affe17bfd8d14c51605",
        "tags": [
            "sage",
            "yellow",
            "orange",
            "maroon",
            "red",
            "nature",
            "food",
            "summer"
        ],
        "colors": [
            "cece5a",
            "ffe17b",
            "fd8d14",
            "c51605"
        ]
    },
    {
        "id": "f6f4eb91c8e4749bc24682a9",
        "tags": [
            "white",
            "grey",
            "blue",
            "sky",
            "sea",
            "cold"
        ],
        "colors": [
            "f6f4eb",
            "91c8e4",
            "749bc2",
            "4682a9"
        ]
    },
    {
        "id": "fba1b7ffd1dafff0f5ffdbaa",
        "tags": [
            "pink",
            "white",
            "yellow",
            "kids",
            "light"
        ],
        "colors": [
            "fba1b7",
            "ffd1da",
            "fff0f5",
            "ffdbaa"
        ]
    },
    {
        "id": "e8ffceacfadf94add77c73c0",
        "tags": [
            "green",
            "mint",
            "blue",
            "gradient",
            "neon",
            "cold"
        ],
        "colors": [
            "e8ffce",
            "acfadf",
            "94add7",
            "7c73c0"
        ]
    },
    {
        "id": "f11a7b9821763e001fffe5ad",
        "tags": [
            "pink",
            "red",
            "purple",
            "maroon",
            "yellow",
            "retro",
            "neon",
            "wedding"
        ],
        "colors": [
            "f11a7b",
            "982176",
            "3e001f",
            "ffe5ad"
        ]
    },
    {
        "id": "4619597a316fcd6688aed8cc",
        "tags": [
            "purple",
            "pink",
            "teal",
            "retro",
            "gradient",
            "space",
            "halloween",
            "winter"
        ],
        "colors": [
            "461959",
            "7a316f",
            "cd6688",
            "aed8cc"
        ]
    },
    {
        "id": "6c3428ba704fdfa878cee6f3",
        "tags": [
            "brown",
            "beige",
            "blue",
            "vintage",
            "nature",
            "earth",
            "warm",
            "fall",
            "coffee",
            "skin"
        ],
        "colors": [
            "6c3428",
            "ba704f",
            "dfa878",
            "cee6f3"
        ]
    },
    {
        "id": "0d1282eeededf0de36d71313",
        "tags": [
            "navy",
            "blue",
            "grey",
            "white",
            "yellow",
            "red",
            "rainbow",
            "retro",
            "kids"
        ],
        "colors": [
            "0d1282",
            "eeeded",
            "f0de36",
            "d71313"
        ]
    },
    {
        "id": "f2ee9d7a9d54557a468c3333",
        "tags": [
            "yellow",
            "green",
            "maroon",
            "vintage",
            "nature",
            "christmas",
            "food"
        ],
        "colors": [
            "f2ee9d",
            "7a9d54",
            "557a46",
            "8c3333"
        ]
    },
    {
        "id": "faf3f0d4e2d4ffcaccdbc4f0",
        "tags": [
            "white",
            "peach",
            "sage",
            "pink",
            "purple",
            "pastel",
            "light",
            "cream",
            "kids"
        ],
        "colors": [
            "faf3f0",
            "d4e2d4",
            "ffcacc",
            "dbc4f0"
        ]
    },
    {
        "id": "a1ccd1f4f2dee9b3847c9d96",
        "tags": [
            "blue",
            "beige",
            "orange",
            "teal",
            "pastel",
            "kids",
            "summer",
            "vintage"
        ],
        "colors": [
            "a1ccd1",
            "f4f2de",
            "e9b384",
            "7c9d96"
        ]
    },
    {
        "id": "1d5d9b75c2f6f4d160fbeeac",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "sky",
            "happy",
            "summer"
        ],
        "colors": [
            "1d5d9b",
            "75c2f6",
            "f4d160",
            "fbeeac"
        ]
    },
    {
        "id": "6528f7a076f9d7bbf5ede4ff",
        "tags": [
            "purple",
            "gradient",
            "space",
            "neon"
        ],
        "colors": [
            "6528f7",
            "a076f9",
            "d7bbf5",
            "ede4ff"
        ]
    },
    {
        "id": "f31559ff52a2ffb07fffecaf",
        "tags": [
            "red",
            "pink",
            "orange",
            "yellow",
            "spring",
            "gradient",
            "happy"
        ],
        "colors": [
            "f31559",
            "ff52a2",
            "ffb07f",
            "ffecaf"
        ]
    },
    {
        "id": "f4e0b9a8a1967d7463fe0000",
        "tags": [
            "beige",
            "grey",
            "red",
            "retro",
            "warm"
        ],
        "colors": [
            "f4e0b9",
            "a8a196",
            "7d7463",
            "fe0000"
        ]
    },
    {
        "id": "0719520b666a35a29f97feed",
        "tags": [
            "navy",
            "teal",
            "mint",
            "sea",
            "neon",
            "gradient",
            "cold",
            "space"
        ],
        "colors": [
            "071952",
            "0b666a",
            "35a29f",
            "97feed"
        ]
    },
    {
        "id": "331d2c3f2e3ea78295efe1d1",
        "tags": [
            "black",
            "peach",
            "beige",
            "vintage",
            "dark",
            "warm",
            "night",
            "halloween"
        ],
        "colors": [
            "331d2c",
            "3f2e3e",
            "a78295",
            "efe1d1"
        ]
    },
    {
        "id": "faf0d7ffd9c08cc0decceebc",
        "tags": [
            "beige",
            "peach",
            "blue",
            "green",
            "nature",
            "kids",
            "spring",
            "light",
            "summer"
        ],
        "colors": [
            "faf0d7",
            "ffd9c0",
            "8cc0de",
            "cceebc"
        ]
    },
    {
        "id": "1d5b79468b97ef6262f3aa60",
        "tags": [
            "navy",
            "teal",
            "red",
            "orange",
            "retro"
        ],
        "colors": [
            "1d5b79",
            "468b97",
            "ef6262",
            "f3aa60"
        ]
    },
    {
        "id": "78c1f39be8d8e2f6caf8fdcf",
        "tags": [
            "blue",
            "mint",
            "sage",
            "green",
            "yellow",
            "gradient",
            "light",
            "happy",
            "summer",
            "sky"
        ],
        "colors": [
            "78c1f3",
            "9be8d8",
            "e2f6ca",
            "f8fdcf"
        ]
    },
    {
        "id": "1a5d1af1c93bfbd85dfae392",
        "tags": [
            "green",
            "yellow",
            "food",
            "retro",
            "summer"
        ],
        "colors": [
            "1a5d1a",
            "f1c93b",
            "fbd85d",
            "fae392"
        ]
    },
    {
        "id": "0000004e4feb068fffeeeeee",
        "tags": [
            "black",
            "blue",
            "grey",
            "sea",
            "gradient",
            "cold"
        ],
        "colors": [
            "000000",
            "4e4feb",
            "068fff",
            "eeeeee"
        ]
    },
    {
        "id": "aac8a7c3edc0e9ffc2fdffae",
        "tags": [
            "sage",
            "green",
            "yellow",
            "pastel",
            "neon",
            "light",
            "summer",
            "happy",
            "gradient",
            "cream"
        ],
        "colors": [
            "aac8a7",
            "c3edc0",
            "e9ffc2",
            "fdffae"
        ]
    },
    {
        "id": "b5c99a862b0dfff9c9ffc95f",
        "tags": [
            "sage",
            "maroon",
            "brown",
            "yellow",
            "retro",
            "nature",
            "vintage",
            "earth",
            "fall",
            "food"
        ],
        "colors": [
            "b5c99a",
            "862b0d",
            "fff9c9",
            "ffc95f"
        ]
    },
    {
        "id": "4a55a27895cba0bfe0c5dff8",
        "tags": [
            "navy",
            "blue",
            "sea",
            "cold",
            "gradient"
        ],
        "colors": [
            "4a55a2",
            "7895cb",
            "a0bfe0",
            "c5dff8"
        ]
    },
    {
        "id": "ff9b9bffd6a5fffec4cbffa9",
        "tags": [
            "red",
            "peach",
            "orange",
            "yellow",
            "green",
            "pastel",
            "nature",
            "kids",
            "spring",
            "happy",
            "light"
        ],
        "colors": [
            "ff9b9b",
            "ffd6a5",
            "fffec4",
            "cbffa9"
        ]
    },
    {
        "id": "6527be9681eb45cfdda7ede7",
        "tags": [
            "purple",
            "teal",
            "mint",
            "cold",
            "retro"
        ],
        "colors": [
            "6527be",
            "9681eb",
            "45cfdd",
            "a7ede7"
        ]
    },
    {
        "id": "f5f5f5f2ead3dfd7bf3f2305",
        "tags": [
            "white",
            "grey",
            "beige",
            "brown",
            "vintage",
            "gold",
            "wedding",
            "coffee"
        ],
        "colors": [
            "f5f5f5",
            "f2ead3",
            "dfd7bf",
            "3f2305"
        ]
    },
    {
        "id": "ffeaddfcaeaeff8989ff6666",
        "tags": [
            "peach",
            "red",
            "warm",
            "kids",
            "food",
            "gradient"
        ],
        "colors": [
            "ffeadd",
            "fcaeae",
            "ff8989",
            "ff6666"
        ]
    },
    {
        "id": "4c4b16898121e7b10af7f1e5",
        "tags": [
            "green",
            "sage",
            "yellow",
            "beige",
            "nature",
            "vintage",
            "fall"
        ],
        "colors": [
            "4c4b16",
            "898121",
            "e7b10a",
            "f7f1e5"
        ]
    },
    {
        "id": "98eeccd0f5befbffdca4907c",
        "tags": [
            "mint",
            "green",
            "beige",
            "brown",
            "light",
            "happy"
        ],
        "colors": [
            "98eecc",
            "d0f5be",
            "fbffdc",
            "a4907c"
        ]
    },
    {
        "id": "164b601b6b934fc0d0a2ff86",
        "tags": [
            "navy",
            "blue",
            "green",
            "sea",
            "cold"
        ],
        "colors": [
            "164b60",
            "1b6b93",
            "4fc0d0",
            "a2ff86"
        ]
    },
    {
        "id": "2d4356435b66a76f6feab2a0",
        "tags": [
            "navy",
            "peach",
            "halloween",
            "dark",
            "vintage",
            "night"
        ],
        "colors": [
            "2d4356",
            "435b66",
            "a76f6f",
            "eab2a0"
        ]
    },
    {
        "id": "fffad7ffe4a7ff90bbff2171",
        "tags": [
            "yellow",
            "beige",
            "pink",
            "spring"
        ],
        "colors": [
            "fffad7",
            "ffe4a7",
            "ff90bb",
            "ff2171"
        ]
    },
    {
        "id": "001c30176b8764ccc5dafffb",
        "tags": [
            "black",
            "navy",
            "teal",
            "mint",
            "sea",
            "space",
            "cold"
        ],
        "colors": [
            "001c30",
            "176b87",
            "64ccc5",
            "dafffb"
        ]
    },
    {
        "id": "3aa6b9ffd0d0ff9eaac1ece4",
        "tags": [
            "blue",
            "teal",
            "pink",
            "mint",
            "retro",
            "kids",
            "happy"
        ],
        "colors": [
            "3aa6b9",
            "ffd0d0",
            "ff9eaa",
            "c1ece4"
        ]
    },
    {
        "id": "e7cea60a6ebd5a96e3a1c2f1",
        "tags": [
            "beige",
            "blue",
            "summer",
            "sea"
        ],
        "colors": [
            "e7cea6",
            "0a6ebd",
            "5a96e3",
            "a1c2f1"
        ]
    },
    {
        "id": "525fe1f86f03ffa41bfff6f4",
        "tags": [
            "blue",
            "orange",
            "yellow",
            "white",
            "retro",
            "happy"
        ],
        "colors": [
            "525fe1",
            "f86f03",
            "ffa41b",
            "fff6f4"
        ]
    },
    {
        "id": "f1c27bffd89ca2cdb085a389",
        "tags": [
            "orange",
            "sage",
            "pastel",
            "earth",
            "vintage",
            "fall",
            "food"
        ],
        "colors": [
            "f1c27b",
            "ffd89c",
            "a2cdb0",
            "85a389"
        ]
    },
    {
        "id": "a0c49dc4d7b2e1ecc8f7ffe5",
        "tags": [
            "green",
            "sage",
            "pastel",
            "light",
            "nature",
            "earth",
            "gradient",
            "cream"
        ],
        "colors": [
            "a0c49d",
            "c4d7b2",
            "e1ecc8",
            "f7ffe5"
        ]
    },
    {
        "id": "21336317594a8eac50d3d04f",
        "tags": [
            "navy",
            "green",
            "black",
            "nature",
            "space"
        ],
        "colors": [
            "213363",
            "17594a",
            "8eac50",
            "d3d04f"
        ]
    },
    {
        "id": "e966a02b27306554af9575de",
        "tags": [
            "pink",
            "black",
            "purple",
            "space",
            "retro",
            "wedding"
        ],
        "colors": [
            "e966a0",
            "2b2730",
            "6554af",
            "9575de"
        ]
    },
    {
        "id": "faf0e49bcdd2ff8551ffdede",
        "tags": [
            "beige",
            "teal",
            "orange",
            "peach",
            "kids",
            "vintage"
        ],
        "colors": [
            "faf0e4",
            "9bcdd2",
            "ff8551",
            "ffdede"
        ]
    },
    {
        "id": "0e29541f6e8c2e8a9984a7a1",
        "tags": [
            "navy",
            "blue",
            "teal",
            "dark",
            "night",
            "space"
        ],
        "colors": [
            "0e2954",
            "1f6e8c",
            "2e8a99",
            "84a7a1"
        ]
    },
    {
        "id": "22a699f2be22f29727f24c3d",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "red",
            "kids",
            "retro"
        ],
        "colors": [
            "22a699",
            "f2be22",
            "f29727",
            "f24c3d"
        ]
    },
    {
        "id": "ff78c4e1aeffffbdf7ffecec",
        "tags": [
            "pink",
            "purple",
            "peach",
            "beige",
            "sunset",
            "gradient",
            "happy",
            "spring"
        ],
        "colors": [
            "ff78c4",
            "e1aeff",
            "ffbdf7",
            "ffecec"
        ]
    },
    {
        "id": "09058046458ce8a9a9f4d3d3",
        "tags": [
            "navy",
            "peach",
            "gradient",
            "night"
        ],
        "colors": [
            "090580",
            "46458c",
            "e8a9a9",
            "f4d3d3"
        ]
    },
    {
        "id": "9ac5f499dbf5a7eceeffeebb",
        "tags": [
            "blue",
            "mint",
            "yellow",
            "summer",
            "sea",
            "sky",
            "light",
            "kids"
        ],
        "colors": [
            "9ac5f4",
            "99dbf5",
            "a7ecee",
            "ffeebb"
        ]
    },
    {
        "id": "606c5dfff4f4f7e6c4f1c376",
        "tags": [
            "sage",
            "white",
            "beige",
            "vintage",
            "gold",
            "fall",
            "wedding",
            "food"
        ],
        "colors": [
            "606c5d",
            "fff4f4",
            "f7e6c4",
            "f1c376"
        ]
    },
    {
        "id": "eee2deea906cb313122b2a4c",
        "tags": [
            "grey",
            "peach",
            "orange",
            "red",
            "maroon",
            "navy",
            "retro",
            "christmas",
            "space"
        ],
        "colors": [
            "eee2de",
            "ea906c",
            "b31312",
            "2b2a4c"
        ]
    },
    {
        "id": "c2dedcece5c7cdc2ae116a7b",
        "tags": [
            "blue",
            "beige",
            "earth",
            "navy",
            "sea",
            "pastel",
            "wedding",
            "winter"
        ],
        "colors": [
            "c2dedc",
            "ece5c7",
            "cdc2ae",
            "116a7b"
        ]
    },
    {
        "id": "e4a5ffffaac9ffcda8ffe7ce",
        "tags": [
            "purple",
            "pink",
            "beige",
            "kids",
            "happy",
            "sunset"
        ],
        "colors": [
            "e4a5ff",
            "ffaac9",
            "ffcda8",
            "ffe7ce"
        ]
    },
    {
        "id": "f5efe7d8c4b64f709c213555",
        "tags": [
            "beige",
            "blue",
            "navy",
            "vintage",
            "winter"
        ],
        "colors": [
            "f5efe7",
            "d8c4b6",
            "4f709c",
            "213555"
        ]
    },
    {
        "id": "40128b9336b4dd58d6ffe79b",
        "tags": [
            "purple",
            "yellow",
            "space",
            "neon",
            "happy"
        ],
        "colors": [
            "40128b",
            "9336b4",
            "dd58d6",
            "ffe79b"
        ]
    },
    {
        "id": "fce9f1f1d4e573bbc9080202",
        "tags": [
            "pink",
            "teal",
            "black",
            "retro",
            "wedding"
        ],
        "colors": [
            "fce9f1",
            "f1d4e5",
            "73bbc9",
            "080202"
        ]
    },
    {
        "id": "0079ff00dfa2f6fa70ff0060",
        "tags": [
            "blue",
            "teal",
            "yellow",
            "red",
            "neon",
            "summer",
            "happy",
            "rainbow",
            "kids",
            "spring"
        ],
        "colors": [
            "0079ff",
            "00dfa2",
            "f6fa70",
            "ff0060"
        ]
    },
    {
        "id": "884a39c38154ffc26ff9e0bb",
        "tags": [
            "brown",
            "beige",
            "vintage",
            "gold",
            "warm",
            "fall",
            "earth",
            "sunset",
            "skin",
            "coffee"
        ],
        "colors": [
            "884a39",
            "c38154",
            "ffc26f",
            "f9e0bb"
        ]
    },
    {
        "id": "9babb8eee3cbd7c0ae967e76",
        "tags": [
            "blue",
            "pastel",
            "vintage",
            "light",
            "earth",
            "skin",
            "winter",
            "wedding"
        ],
        "colors": [
            "9babb8",
            "eee3cb",
            "d7c0ae",
            "967e76"
        ]
    },
    {
        "id": "9376e0e893cff3bcc8f6ffa6",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "kids",
            "rainbow",
            "sunset",
            "gradient",
            "light"
        ],
        "colors": [
            "9376e0",
            "e893cf",
            "f3bcc8",
            "f6ffa6"
        ]
    },
    {
        "id": "30a2ff00c4ffffe7a0fff5b8",
        "tags": [
            "blue",
            "yellow",
            "sea",
            "kids"
        ],
        "colors": [
            "30a2ff",
            "00c4ff",
            "ffe7a0",
            "fff5b8"
        ]
    },
    {
        "id": "11009e4942e48696fec4b0ff",
        "tags": [
            "navy",
            "blue",
            "purple",
            "cold",
            "sea",
            "space"
        ],
        "colors": [
            "11009e",
            "4942e4",
            "8696fe",
            "c4b0ff"
        ]
    },
    {
        "id": "116d6e321e1e4e3636cd1818",
        "tags": [
            "teal",
            "black",
            "brown",
            "red",
            "vintage",
            "dark",
            "wedding",
            "halloween",
            "night"
        ],
        "colors": [
            "116d6e",
            "321e1e",
            "4e3636",
            "cd1818"
        ]
    },
    {
        "id": "f2d8d85c8984545b77374259",
        "tags": [
            "peach",
            "teal",
            "navy",
            "retro",
            "vintage",
            "pastel",
            "wedding"
        ],
        "colors": [
            "f2d8d8",
            "5c8984",
            "545b77",
            "374259"
        ]
    },
    {
        "id": "ecf8f9068da97e1717e55807",
        "tags": [
            "blue",
            "maroon",
            "orange",
            "retro",
            "kids",
            "wedding"
        ],
        "colors": [
            "ecf8f9",
            "068da9",
            "7e1717",
            "e55807"
        ]
    },
    {
        "id": "f9f5f6f8e8eefdcedff2bed1",
        "tags": [
            "white",
            "pink",
            "cream",
            "happy",
            "pastel",
            "skin",
            "light",
            "spring",
            "gradient"
        ],
        "colors": [
            "f9f5f6",
            "f8e8ee",
            "fdcedf",
            "f2bed1"
        ]
    },
    {
        "id": "27374d526d829db2bfdde6ed",
        "tags": [
            "navy",
            "blue",
            "grey",
            "dark",
            "night",
            "sea",
            "winter",
            "cold"
        ],
        "colors": [
            "27374d",
            "526d82",
            "9db2bf",
            "dde6ed"
        ]
    },
    {
        "id": "b70404db005bf79327ffe569",
        "tags": [
            "red",
            "pink",
            "orange",
            "yellow",
            "sunset",
            "warm",
            "gold",
            "kids"
        ],
        "colors": [
            "b70404",
            "db005b",
            "f79327",
            "ffe569"
        ]
    },
    {
        "id": "47a9924821217a3e3eeeeeee",
        "tags": [
            "teal",
            "brown",
            "grey",
            "white",
            "vintage",
            "winter",
            "nature"
        ],
        "colors": [
            "47a992",
            "482121",
            "7a3e3e",
            "eeeeee"
        ]
    },
    {
        "id": "79e0ee98eeccd0f5befbffdc",
        "tags": [
            "blue",
            "mint",
            "sage",
            "yellow",
            "neon",
            "light",
            "summer",
            "kids",
            "nature",
            "happy"
        ],
        "colors": [
            "79e0ee",
            "98eecc",
            "d0f5be",
            "fbffdc"
        ]
    },
    {
        "id": "025464e57c23e8aa42f8f1f1",
        "tags": [
            "navy",
            "orange",
            "white",
            "vintage",
            "wedding"
        ],
        "colors": [
            "025464",
            "e57c23",
            "e8aa42",
            "f8f1f1"
        ]
    },
    {
        "id": "c4dfdfd2e9e9e3f4f4f8f6f4",
        "tags": [
            "teal",
            "grey",
            "white",
            "pastel",
            "light",
            "cream",
            "cold"
        ],
        "colors": [
            "c4dfdf",
            "d2e9e9",
            "e3f4f4",
            "f8f6f4"
        ]
    },
    {
        "id": "b799ffacbcffaee2ffe6fffd",
        "tags": [
            "purple",
            "blue",
            "light",
            "sky",
            "happy",
            "winter"
        ],
        "colors": [
            "b799ff",
            "acbcff",
            "aee2ff",
            "e6fffd"
        ]
    },
    {
        "id": "ffb84cf266aba459d12cd3e1",
        "tags": [
            "orange",
            "pink",
            "purple",
            "blue",
            "neon",
            "kids",
            "retro",
            "summer"
        ],
        "colors": [
            "ffb84c",
            "f266ab",
            "a459d1",
            "2cd3e1"
        ]
    },
    {
        "id": "f5f0bbdbdfaab3c89073a9ad",
        "tags": [
            "yellow",
            "beige",
            "sage",
            "teal",
            "pastel",
            "earth",
            "nature",
            "cream",
            "summer"
        ],
        "colors": [
            "f5f0bb",
            "dbdfaa",
            "b3c890",
            "73a9ad"
        ]
    },
    {
        "id": "64384399627ac88ea7e7cbcb",
        "tags": [
            "brown",
            "maroon",
            "pink",
            "peach",
            "vintage",
            "night",
            "warm",
            "halloween",
            "food",
            "skin",
            "gradient"
        ],
        "colors": [
            "643843",
            "99627a",
            "c88ea7",
            "e7cbcb"
        ]
    },
    {
        "id": "4c4c6d1b9c85e8f6efffe194",
        "tags": [
            "navy",
            "teal",
            "white",
            "yellow",
            "retro",
            "winter",
            "kids"
        ],
        "colors": [
            "4c4c6d",
            "1b9c85",
            "e8f6ef",
            "ffe194"
        ]
    },
    {
        "id": "f9fbe7f0edd4eccdb4fea1a1",
        "tags": [
            "white",
            "yellow",
            "beige",
            "peach",
            "red",
            "cream",
            "light",
            "kids",
            "warm",
            "gold",
            "food"
        ],
        "colors": [
            "f9fbe7",
            "f0edd4",
            "eccdb4",
            "fea1a1"
        ]
    },
    {
        "id": "537188cbb279e1d4bbeeeeee",
        "tags": [
            "navy",
            "beige",
            "grey",
            "vintage",
            "pastel",
            "earth"
        ],
        "colors": [
            "537188",
            "cbb279",
            "e1d4bb",
            "eeeeee"
        ]
    },
    {
        "id": "fffaf4d25380e08e6df6c391",
        "tags": [
            "white",
            "maroon",
            "orange",
            "beige",
            "wedding",
            "kids",
            "spring"
        ],
        "colors": [
            "fffaf4",
            "d25380",
            "e08e6d",
            "f6c391"
        ]
    },
    {
        "id": "0c134f1d267d5c469cd4adfc",
        "tags": [
            "navy",
            "blue",
            "purple",
            "space",
            "dark",
            "gradient",
            "halloween"
        ],
        "colors": [
            "0c134f",
            "1d267d",
            "5c469c",
            "d4adfc"
        ]
    },
    {
        "id": "99a98fc1d0b5d6e8dbfff8de",
        "tags": [
            "sage",
            "yellow",
            "vintage",
            "light",
            "nature",
            "gradient",
            "fall",
            "cream"
        ],
        "colors": [
            "99a98f",
            "c1d0b5",
            "d6e8db",
            "fff8de"
        ]
    },
    {
        "id": "ff55bbffd3a3fcffb2b6eafa",
        "tags": [
            "pink",
            "beige",
            "yellow",
            "blue",
            "rainbow",
            "kids",
            "neon",
            "happy"
        ],
        "colors": [
            "ff55bb",
            "ffd3a3",
            "fcffb2",
            "b6eafa"
        ]
    },
    {
        "id": "e5f9dba0d8b3a2a37883764f",
        "tags": [
            "green",
            "sage",
            "brown",
            "nature",
            "winter",
            "earth"
        ],
        "colors": [
            "e5f9db",
            "a0d8b3",
            "a2a378",
            "83764f"
        ]
    },
    {
        "id": "fff7d4ffd95ac07f004c3d3d",
        "tags": [
            "yellow",
            "brown",
            "black",
            "gold",
            "gradient"
        ],
        "colors": [
            "fff7d4",
            "ffd95a",
            "c07f00",
            "4c3d3d"
        ]
    },
    {
        "id": "f99b7de76161b047598bacaa",
        "tags": [
            "orange",
            "red",
            "maroon",
            "teal",
            "vintage"
        ],
        "colors": [
            "f99b7d",
            "e76161",
            "b04759",
            "8bacaa"
        ]
    },
    {
        "id": "feff86b0daff19a7ce146c94",
        "tags": [
            "yellow",
            "blue",
            "navy",
            "sky",
            "kids"
        ],
        "colors": [
            "feff86",
            "b0daff",
            "19a7ce",
            "146c94"
        ]
    },
    {
        "id": "8294c4acb1d6dbdfeaffead2",
        "tags": [
            "blue",
            "grey",
            "beige",
            "sea",
            "pastel",
            "sky",
            "winter",
            "cold"
        ],
        "colors": [
            "8294c4",
            "acb1d6",
            "dbdfea",
            "ffead2"
        ]
    },
    {
        "id": "f6f1f1afd3e219a7ce146c94",
        "tags": [
            "beige",
            "white",
            "blue",
            "navy",
            "sky",
            "sea",
            "cold"
        ],
        "colors": [
            "f6f1f1",
            "afd3e2",
            "19a7ce",
            "146c94"
        ]
    },
    {
        "id": "be5a83e06469f2b6a0dedea7",
        "tags": [
            "maroon",
            "red",
            "peach",
            "sage",
            "sunset",
            "kids",
            "vintage",
            "christmas",
            "gradient"
        ],
        "colors": [
            "be5a83",
            "e06469",
            "f2b6a0",
            "dedea7"
        ]
    },
    {
        "id": "fff8d6f7e1aea4d0a4617a55",
        "tags": [],
        "colors": [
            "fff8d6",
            "f7e1ae",
            "a4d0a4",
            "617a55"
        ]
    },
    {
        "id": "f6ffdee3f2c1c9dbb2aac8a7",
        "tags": [],
        "colors": [
            "f6ffde",
            "e3f2c1",
            "c9dbb2",
            "aac8a7"
        ]
    },
    {
        "id": "8b1874b71375fc4f00f79540",
        "tags": [],
        "colors": [
            "8b1874",
            "b71375",
            "fc4f00",
            "f79540"
        ]
    },
    {
        "id": "9e6f21ffeeb3b8e7e1d4fafc",
        "tags": [
            "brown",
            "yellow",
            "teal",
            "blue",
            "sea",
            "summer",
            "kids",
            "earth",
            "vintage"
        ],
        "colors": [
            "9e6f21",
            "ffeeb3",
            "b8e7e1",
            "d4fafc"
        ]
    },
    {
        "id": "f1f6f9394867212a3e9ba4b5",
        "tags": [
            "blue",
            "navy",
            "grey",
            "night",
            "cold"
        ],
        "colors": [
            "f1f6f9",
            "394867",
            "212a3e",
            "9ba4b5"
        ]
    },
    {
        "id": "654e926c9bcfa5c0ddebd8b2",
        "tags": [
            "purple",
            "blue",
            "beige",
            "sea",
            "winter"
        ],
        "colors": [
            "654e92",
            "6c9bcf",
            "a5c0dd",
            "ebd8b2"
        ]
    },
    {
        "id": "f97b22fee8b09ca7777c9070",
        "tags": [
            "orange",
            "yellow",
            "sage",
            "nature",
            "fall",
            "vintage",
            "food"
        ],
        "colors": [
            "f97b22",
            "fee8b0",
            "9ca777",
            "7c9070"
        ]
    },
    {
        "id": "5f264a643a6b957777b0a4a4",
        "tags": [
            "maroon",
            "purple",
            "brown",
            "grey",
            "night",
            "dark",
            "halloween",
            "skin"
        ],
        "colors": [
            "5f264a",
            "643a6b",
            "957777",
            "b0a4a4"
        ]
    },
    {
        "id": "a6d0ddff6969ffd3b0fff9de",
        "tags": [
            "blue",
            "red",
            "peach",
            "yellow",
            "kids",
            "rainbow",
            "happy",
            "light",
            "spring"
        ],
        "colors": [
            "a6d0dd",
            "ff6969",
            "ffd3b0",
            "fff9de"
        ]
    },
    {
        "id": "ffdcb6ecc9eec9a7eb9384d1",
        "tags": [
            "beige",
            "purple",
            "sunset",
            "kids"
        ],
        "colors": [
            "ffdcb6",
            "ecc9ee",
            "c9a7eb",
            "9384d1"
        ]
    },
    {
        "id": "0a4d6808839505bfdb00ffca",
        "tags": [
            "navy",
            "teal",
            "blue",
            "mint",
            "sea",
            "cold",
            "gradient",
            "space"
        ],
        "colors": [
            "0a4d68",
            "088395",
            "05bfdb",
            "00ffca"
        ]
    },
    {
        "id": "ffebebade4db6da9e4f6ba6f",
        "tags": [
            "peach",
            "teal",
            "blue",
            "orange",
            "kids",
            "vintage",
            "spring",
            "happy"
        ],
        "colors": [
            "ffebeb",
            "ade4db",
            "6da9e4",
            "f6ba6f"
        ]
    },
    {
        "id": "2a2f4f917fb3e5beecfde2f3",
        "tags": [
            "navy",
            "purple",
            "pink",
            "space",
            "gradient",
            "wedding"
        ],
        "colors": [
            "2a2f4f",
            "917fb3",
            "e5beec",
            "fde2f3"
        ]
    },
    {
        "id": "ff6d60f7d060f3e99f98d8aa",
        "tags": [
            "red",
            "yellow",
            "green",
            "retro",
            "rainbow",
            "kids",
            "spring",
            "happy"
        ],
        "colors": [
            "ff6d60",
            "f7d060",
            "f3e99f",
            "98d8aa"
        ]
    },
    {
        "id": "bfccb57c96abb7b7b7edc6b1",
        "tags": [
            "sage",
            "blue",
            "grey",
            "peach",
            "earth",
            "nature",
            "vintage",
            "pastel",
            "winter",
            "food"
        ],
        "colors": [
            "bfccb5",
            "7c96ab",
            "b7b7b7",
            "edc6b1"
        ]
    },
    {
        "id": "3c486bf0f0f0f9d949f45050",
        "tags": [
            "navy",
            "white",
            "grey",
            "yellow",
            "red",
            "rainbow",
            "space",
            "retro",
            "kids"
        ],
        "colors": [
            "3c486b",
            "f0f0f0",
            "f9d949",
            "f45050"
        ]
    },
    {
        "id": "b9eddd87cbb9569daa577d86",
        "tags": [
            "mint",
            "teal",
            "blue",
            "navy",
            "sea",
            "winter",
            "cold",
            "gradient"
        ],
        "colors": [
            "b9eddd",
            "87cbb9",
            "569daa",
            "577d86"
        ]
    },
    {
        "id": "f2e3db41644a263a29e86a33",
        "tags": [
            "peach",
            "green",
            "orange",
            "nature",
            "vintage",
            "wedding",
            "food"
        ],
        "colors": [
            "f2e3db",
            "41644a",
            "263a29",
            "e86a33"
        ]
    },
    {
        "id": "d14d72ffababfcc8d1fef2f4",
        "tags": [
            "red",
            "peach",
            "pink",
            "white",
            "cream",
            "skin",
            "warm",
            "food",
            "gradient"
        ],
        "colors": [
            "d14d72",
            "ffabab",
            "fcc8d1",
            "fef2f4"
        ]
    },
    {
        "id": "070a52d21312ed2b2af15a59",
        "tags": [
            "navy",
            "red",
            "dark",
            "space"
        ],
        "colors": [
            "070a52",
            "d21312",
            "ed2b2a",
            "f15a59"
        ]
    },
    {
        "id": "3936464f45576d5d6ef4eee0",
        "tags": [
            "black",
            "grey",
            "beige",
            "night",
            "dark"
        ],
        "colors": [
            "393646",
            "4f4557",
            "6d5d6e",
            "f4eee0"
        ]
    },
    {
        "id": "fff3e2ffe5cafa9884e74646",
        "tags": [
            "beige",
            "peach",
            "red",
            "skin",
            "gradient",
            "happy",
            "warm",
            "gold"
        ],
        "colors": [
            "fff3e2",
            "ffe5ca",
            "fa9884",
            "e74646"
        ]
    },
    {
        "id": "f9e2af009fbd21006277037b",
        "tags": [
            "beige",
            "blue",
            "navy",
            "purple",
            "retro",
            "happy",
            "wedding"
        ],
        "colors": [
            "f9e2af",
            "009fbd",
            "210062",
            "77037b"
        ]
    },
    {
        "id": "fdf4f5e8a0bfba90c6c0dbea",
        "tags": [
            "white",
            "pink",
            "purple",
            "blue",
            "pastel",
            "light",
            "kids",
            "cream"
        ],
        "colors": [
            "fdf4f5",
            "e8a0bf",
            "ba90c6",
            "c0dbea"
        ]
    },
    {
        "id": "454545ff6000ffa559ffe6c7",
        "tags": [
            "black",
            "grey",
            "orange",
            "beige",
            "halloween",
            "space",
            "gold",
            "warm"
        ],
        "colors": [
            "454545",
            "ff6000",
            "ffa559",
            "ffe6c7"
        ]
    },
    {
        "id": "ddffbbc7e9b0b3c99ca4bc92",
        "tags": [
            "green",
            "sage",
            "nature",
            "cream",
            "light",
            "gradient",
            "pastel"
        ],
        "colors": [
            "ddffbb",
            "c7e9b0",
            "b3c99c",
            "a4bc92"
        ]
    },
    {
        "id": "f6f1e9ffd93dff84004f200d",
        "tags": [
            "beige",
            "grey",
            "white",
            "yellow",
            "orange",
            "brown",
            "gold",
            "neon",
            "warm",
            "gradient"
        ],
        "colors": [
            "f6f1e9",
            "ffd93d",
            "ff8400",
            "4f200d"
        ]
    },
    {
        "id": "89375fce5959bacddbf3e8ff",
        "tags": [
            "maroon",
            "red",
            "grey",
            "pink",
            "warm",
            "wedding",
            "vintage"
        ],
        "colors": [
            "89375f",
            "ce5959",
            "bacddb",
            "f3e8ff"
        ]
    },
    {
        "id": "f5f3c127e1c10ea2932f0f5d",
        "tags": [
            "yellow",
            "beige",
            "mint",
            "teal",
            "navy",
            "sea"
        ],
        "colors": [
            "f5f3c1",
            "27e1c1",
            "0ea293",
            "2f0f5d"
        ]
    },
    {
        "id": "0b244719376d576cbca5d7e8",
        "tags": [
            "navy",
            "blue",
            "sea",
            "night",
            "dark",
            "winter"
        ],
        "colors": [
            "0b2447",
            "19376d",
            "576cbc",
            "a5d7e8"
        ]
    },
    {
        "id": "feff86b0daffb9e9fcdaf5ff",
        "tags": [
            "yellow",
            "blue",
            "light",
            "happy",
            "sky",
            "kids",
            "summer"
        ],
        "colors": [
            "feff86",
            "b0daff",
            "b9e9fc",
            "daf5ff"
        ]
    },
    {
        "id": "b2a4ffffb4b4ffdeb4fdf7c3",
        "tags": [
            "purple",
            "peach",
            "beige",
            "yellow",
            "pastel",
            "light",
            "kids",
            "rainbow",
            "spring",
            "happy",
            "gradient",
            "sunset"
        ],
        "colors": [
            "b2a4ff",
            "ffb4b4",
            "ffdeb4",
            "fdf7c3"
        ]
    },
    {
        "id": "a9907ef3debaabc4aa675d50",
        "tags": [
            "brown",
            "beige",
            "sage",
            "vintage",
            "nature",
            "cream",
            "fall",
            "coffee",
            "warm",
            "earth",
            "food"
        ],
        "colors": [
            "a9907e",
            "f3deba",
            "abc4aa",
            "675d50"
        ]
    },
    {
        "id": "57c5b61598951a5f7a002b5b",
        "tags": [
            "teal",
            "navy",
            "sea",
            "gradient",
            "winter",
            "cold"
        ],
        "colors": [
            "57c5b6",
            "159895",
            "1a5f7a",
            "002b5b"
        ]
    },
    {
        "id": "000000262a56b8621be3ccae",
        "tags": [
            "black",
            "navy",
            "orange",
            "beige",
            "night",
            "coffee",
            "halloween",
            "vintage"
        ],
        "colors": [
            "000000",
            "262a56",
            "b8621b",
            "e3ccae"
        ]
    },
    {
        "id": "7aa874f7db6aebb02dd864a9",
        "tags": [
            "sage",
            "green",
            "yellow",
            "orange",
            "pink",
            "nature",
            "kids",
            "spring"
        ],
        "colors": [
            "7aa874",
            "f7db6a",
            "ebb02d",
            "d864a9"
        ]
    },
    {
        "id": "9a208ce11299ffeaeaf5c6ec",
        "tags": [
            "purple",
            "pink",
            "peach",
            "kids",
            "retro",
            "wedding"
        ],
        "colors": [
            "9a208c",
            "e11299",
            "ffeaea",
            "f5c6ec"
        ]
    },
    {
        "id": "7149c6fc2947fe6244ffdeb9",
        "tags": [
            "purple",
            "red",
            "orange",
            "beige",
            "sunset",
            "neon"
        ],
        "colors": [
            "7149c6",
            "fc2947",
            "fe6244",
            "ffdeb9"
        ]
    },
    {
        "id": "fff2ccffd966f4b183dfa67b",
        "tags": [
            "beige",
            "yellow",
            "orange",
            "peach",
            "pastel",
            "light",
            "warm",
            "summer",
            "fall",
            "gradient",
            "gold",
            "food"
        ],
        "colors": [
            "fff2cc",
            "ffd966",
            "f4b183",
            "dfa67b"
        ]
    },
    {
        "id": "245953408e91e49393d8d8d8",
        "tags": [
            "teal",
            "peach",
            "grey",
            "cold",
            "retro"
        ],
        "colors": [
            "245953",
            "408e91",
            "e49393",
            "d8d8d8"
        ]
    },
    {
        "id": "867070d5b4b4e4d0d0f5ebeb",
        "tags": [
            "brown",
            "peach",
            "cream",
            "skin",
            "fall",
            "pastel",
            "earth",
            "warm"
        ],
        "colors": [
            "867070",
            "d5b4b4",
            "e4d0d0",
            "f5ebeb"
        ]
    },
    {
        "id": "fff4e0ffbf9bb460604d4d4d",
        "tags": [
            "beige",
            "orange",
            "red",
            "black",
            "gold",
            "warm",
            "gradient"
        ],
        "colors": [
            "fff4e0",
            "ffbf9b",
            "b46060",
            "4d4d4d"
        ]
    },
    {
        "id": "f9f5ebe4dccfea5455002b5b",
        "tags": [
            "beige",
            "grey",
            "red",
            "navy",
            "wedding",
            "vintage",
            "retro"
        ],
        "colors": [
            "f9f5eb",
            "e4dccf",
            "ea5455",
            "002b5b"
        ]
    },
    {
        "id": "f6f1f119a7ce146c94000000",
        "tags": [
            "grey",
            "blue",
            "black",
            "sea",
            "cold"
        ],
        "colors": [
            "f6f1f1",
            "19a7ce",
            "146c94",
            "000000"
        ]
    },
    {
        "id": "bbd6b8aec2b694af9fdbe4c6",
        "tags": [
            "sage",
            "earth",
            "nature",
            "pastel",
            "kids"
        ],
        "colors": [
            "bbd6b8",
            "aec2b6",
            "94af9f",
            "dbe4c6"
        ]
    },
    {
        "id": "2d27274135438f43eef0eb8d",
        "tags": [
            "black",
            "grey",
            "purple",
            "yellow",
            "space",
            "retro"
        ],
        "colors": [
            "2d2727",
            "413543",
            "8f43ee",
            "f0eb8d"
        ]
    },
    {
        "id": "00235be21818ffdd8398dfd6",
        "tags": [
            "navy",
            "red",
            "yellow",
            "teal",
            "rainbow",
            "kids",
            "happy"
        ],
        "colors": [
            "00235b",
            "e21818",
            "ffdd83",
            "98dfd6"
        ]
    },
    {
        "id": "ccd5aee9edc9fefae0faedcd",
        "tags": [
            "sage",
            "yellow",
            "beige",
            "pastel",
            "cream",
            "nature",
            "light",
            "summer"
        ],
        "colors": [
            "ccd5ae",
            "e9edc9",
            "fefae0",
            "faedcd"
        ]
    },
    {
        "id": "aa77ffc9eeff97deff62cdff",
        "tags": [
            "purple",
            "blue",
            "cold",
            "kids",
            "sea"
        ],
        "colors": [
            "aa77ff",
            "c9eeff",
            "97deff",
            "62cdff"
        ]
    },
    {
        "id": "37306b66347f9e4784d27685",
        "tags": [
            "navy",
            "purple",
            "maroon",
            "peach",
            "space",
            "night",
            "dark",
            "gradient",
            "halloween"
        ],
        "colors": [
            "37306b",
            "66347f",
            "9e4784",
            "d27685"
        ]
    },
    {
        "id": "8d7b68a4907cc8b6a6f1dec9",
        "tags": [
            "brown",
            "beige",
            "coffee",
            "earth",
            "gradient",
            "warm",
            "vintage"
        ],
        "colors": [
            "8d7b68",
            "a4907c",
            "c8b6a6",
            "f1dec9"
        ]
    },
    {
        "id": "ffacacffbfa9ffebb4fbffb1",
        "tags": [
            "pink",
            "red",
            "yellow",
            "peach",
            "orange",
            "light",
            "sunset",
            "summer",
            "warm",
            "neon",
            "kids"
        ],
        "colors": [
            "ffacac",
            "ffbfa9",
            "ffebb4",
            "fbffb1"
        ]
    },
    {
        "id": "ede9d5e7ab9adf7857617143",
        "tags": [
            "beige",
            "peach",
            "green",
            "vintage",
            "christmas"
        ],
        "colors": [
            "ede9d5",
            "e7ab9a",
            "df7857",
            "617143"
        ]
    },
    {
        "id": "2c33332e4f4f0e8388cbe4de",
        "tags": [
            "black",
            "teal",
            "mint",
            "sea",
            "night",
            "dark",
            "gradient"
        ],
        "colors": [
            "2c3333",
            "2e4f4f",
            "0e8388",
            "cbe4de"
        ]
    },
    {
        "id": "5391653f497ff7c04af8f5e4",
        "tags": [
            "green",
            "navy",
            "yellow",
            "beige",
            "kids",
            "wedding"
        ],
        "colors": [
            "539165",
            "3f497f",
            "f7c04a",
            "f8f5e4"
        ]
    },
    {
        "id": "df2e38ddf7e3c7e8ca5d9c59",
        "tags": [
            "red",
            "green",
            "food",
            "summer",
            "christmas",
            "kids"
        ],
        "colors": [
            "df2e38",
            "ddf7e3",
            "c7e8ca",
            "5d9c59"
        ]
    },
    {
        "id": "f6e1c3e9a178a844487a3e65",
        "tags": [
            "beige",
            "orange",
            "maroon",
            "purple",
            "vintage",
            "warm",
            "gold",
            "gradient"
        ],
        "colors": [
            "f6e1c3",
            "e9a178",
            "a84448",
            "7a3e65"
        ]
    },
    {
        "id": "ecf2ff3e54ac655dbbbface2",
        "tags": [
            "grey",
            "blue",
            "purple",
            "winter",
            "cold"
        ],
        "colors": [
            "ecf2ff",
            "3e54ac",
            "655dbb",
            "bface2"
        ]
    },
    {
        "id": "f7f1e5e7b10a8981214c4b16",
        "tags": [
            "beige",
            "yellow",
            "orange",
            "sage",
            "green",
            "vintage",
            "warm",
            "summer",
            "fall",
            "nature",
            "gradient",
            "food"
        ],
        "colors": [
            "f7f1e5",
            "e7b10a",
            "898121",
            "4c4b16"
        ]
    },
    {
        "id": "804674a86464b3e5bef5ffc9",
        "tags": [
            "purple",
            "brown",
            "mint",
            "pastel",
            "vintage",
            "retro",
            "kids"
        ],
        "colors": [
            "804674",
            "a86464",
            "b3e5be",
            "f5ffc9"
        ]
    },
    {
        "id": "4e6e81f9dbbbff03032e3840",
        "tags": [
            "navy",
            "beige",
            "red",
            "black",
            "retro",
            "space"
        ],
        "colors": [
            "4e6e81",
            "f9dbbb",
            "ff0303",
            "2e3840"
        ]
    },
    {
        "id": "be6db7fdd36adc8449c04a82",
        "tags": [
            "purple",
            "yellow",
            "orange",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "be6db7",
            "fdd36a",
            "dc8449",
            "c04a82"
        ]
    },
    {
        "id": "edf1d69dc08b60996640513b",
        "tags": [
            "sage",
            "green",
            "nature",
            "earth"
        ],
        "colors": [
            "edf1d6",
            "9dc08b",
            "609966",
            "40513b"
        ]
    },
    {
        "id": "191825865dffe384ffffa3fd",
        "tags": [
            "black",
            "purple",
            "pink",
            "neon",
            "night",
            "space"
        ],
        "colors": [
            "191825",
            "865dff",
            "e384ff",
            "ffa3fd"
        ]
    },
    {
        "id": "3a10784e31aa2f58cd3795bd",
        "tags": [
            "navy",
            "purple",
            "blue",
            "teal",
            "night",
            "dark",
            "gradient",
            "cold",
            "sea"
        ],
        "colors": [
            "3a1078",
            "4e31aa",
            "2f58cd",
            "3795bd"
        ]
    },
    {
        "id": "3a98b9fff1dce8d5c4eeeeee",
        "tags": [
            "blue",
            "beige",
            "grey",
            "sea",
            "summer",
            "light"
        ],
        "colors": [
            "3a98b9",
            "fff1dc",
            "e8d5c4",
            "eeeeee"
        ]
    },
    {
        "id": "f7c8e0dfffd8b4e4ff95bdff",
        "tags": [
            "pink",
            "green",
            "blue",
            "pastel",
            "light",
            "kids",
            "spring",
            "happy"
        ],
        "colors": [
            "f7c8e0",
            "dfffd8",
            "b4e4ff",
            "95bdff"
        ]
    },
    {
        "id": "2b3467bad7e9fcffe7eb455f",
        "tags": [
            "navy",
            "blue",
            "red",
            "retro",
            "wedding",
            "space"
        ],
        "colors": [
            "2b3467",
            "bad7e9",
            "fcffe7",
            "eb455f"
        ]
    },
    {
        "id": "f5eaeaffb84cf16767a459d1",
        "tags": [
            "peach",
            "orange",
            "red",
            "purple",
            "kids"
        ],
        "colors": [
            "f5eaea",
            "ffb84c",
            "f16767",
            "a459d1"
        ]
    },
    {
        "id": "4d455de96479f5e9cf7db9b6",
        "tags": [
            "black",
            "red",
            "beige",
            "teal",
            "retro",
            "vintage"
        ],
        "colors": [
            "4d455d",
            "e96479",
            "f5e9cf",
            "7db9b6"
        ]
    },
    {
        "id": "ad7be93e54acbfdce5eeeeee",
        "tags": [
            "purple",
            "navy",
            "blue",
            "grey",
            "cold"
        ],
        "colors": [
            "ad7be9",
            "3e54ac",
            "bfdce5",
            "eeeeee"
        ]
    },
    {
        "id": "fefbe9e1eeddf0a04b183a1d",
        "tags": [
            "beige",
            "yellow",
            "sage",
            "orange",
            "vintage",
            "wedding"
        ],
        "colors": [
            "fefbe9",
            "e1eedd",
            "f0a04b",
            "183a1d"
        ]
    },
    {
        "id": "ecf2ffe3dffde5d1fafff4d2",
        "tags": [
            "blue",
            "purple",
            "yellow",
            "light",
            "kids",
            "sky",
            "cream"
        ],
        "colors": [
            "ecf2ff",
            "e3dffd",
            "e5d1fa",
            "fff4d2"
        ]
    },
    {
        "id": "635985443c6839305318122b",
        "tags": [
            "navy",
            "black",
            "dark",
            "cold",
            "night",
            "space",
            "winter"
        ],
        "colors": [
            "635985",
            "443c68",
            "393053",
            "18122b"
        ]
    },
    {
        "id": "060047b3005ee90064ff5f9e",
        "tags": [
            "navy",
            "red",
            "pink",
            "neon",
            "retro",
            "space",
            "warm"
        ],
        "colors": [
            "060047",
            "b3005e",
            "e90064",
            "ff5f9e"
        ]
    },
    {
        "id": "181823537fe7c0eef2e9f8f9",
        "tags": [
            "black",
            "blue",
            "mint",
            "sea",
            "winter",
            "cold"
        ],
        "colors": [
            "181823",
            "537fe7",
            "c0eef2",
            "e9f8f9"
        ]
    },
    {
        "id": "b9f3e4ea8feaffaacff6e6c2",
        "tags": [
            "mint",
            "purple",
            "pink",
            "peach",
            "beige",
            "pastel",
            "spring",
            "happy",
            "light",
            "rainbow"
        ],
        "colors": [
            "b9f3e4",
            "ea8fea",
            "ffaacf",
            "f6e6c2"
        ]
    },
    {
        "id": "f6f7c1bef0cbd1fff3c1aefc",
        "tags": [
            "yellow",
            "green",
            "purple",
            "spring",
            "kids"
        ],
        "colors": [
            "f6f7c1",
            "bef0cb",
            "d1fff3",
            "c1aefc"
        ]
    },
    {
        "id": "f0eeed609ea2c92c6d332c39",
        "tags": [
            "grey",
            "teal",
            "maroon",
            "black",
            "retro"
        ],
        "colors": [
            "f0eeed",
            "609ea2",
            "c92c6d",
            "332c39"
        ]
    },
    {
        "id": "0000000f629216ff00ffed00",
        "tags": [
            "black",
            "navy",
            "green",
            "yellow",
            "neon"
        ],
        "colors": [
            "000000",
            "0f6292",
            "16ff00",
            "ffed00"
        ]
    },
    {
        "id": "f9f54b8bf5fa3f979b205e61",
        "tags": [
            "yellow",
            "blue",
            "teal",
            "sky",
            "cold"
        ],
        "colors": [
            "f9f54b",
            "8bf5fa",
            "3f979b",
            "205e61"
        ]
    },
    {
        "id": "362fd93c84ab85cdfddefcf9",
        "tags": [
            "blue",
            "teal",
            "mint",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "362fd9",
            "3c84ab",
            "85cdfd",
            "defcf9"
        ]
    },
    {
        "id": "b5f1cce5fdd1c9f4aafcc2fc",
        "tags": [
            "green",
            "sage",
            "pink",
            "pastel",
            "nature",
            "spring",
            "food"
        ],
        "colors": [
            "b5f1cc",
            "e5fdd1",
            "c9f4aa",
            "fcc2fc"
        ]
    },
    {
        "id": "6096b493bfcfbdcdd6eee9da",
        "tags": [
            "blue",
            "grey",
            "beige",
            "sea",
            "pastel",
            "vintage",
            "cold",
            "earth",
            "gradient"
        ],
        "colors": [
            "6096b4",
            "93bfcf",
            "bdcdd6",
            "eee9da"
        ]
    },
    {
        "id": "a7727deddbc7f8ead8f9f5e7",
        "tags": [
            "brown",
            "peach",
            "beige",
            "light",
            "pastel",
            "cream",
            "coffee",
            "skin",
            "food",
            "wedding"
        ],
        "colors": [
            "a7727d",
            "eddbc7",
            "f8ead8",
            "f9f5e7"
        ]
    },
    {
        "id": "698269b99b6bf1dbbfaa5656",
        "tags": [
            "sage",
            "brown",
            "beige",
            "maroon",
            "vintage",
            "earth"
        ],
        "colors": [
            "698269",
            "b99b6b",
            "f1dbbf",
            "aa5656"
        ]
    },
    {
        "id": "20262e913175cd5888e9e8e8",
        "tags": [
            "black",
            "purple",
            "retro",
            "vintage",
            "grey",
            "space"
        ],
        "colors": [
            "20262e",
            "913175",
            "cd5888",
            "e9e8e8"
        ]
    },
    {
        "id": "ecf9fffffbebffe7ccf8cba6",
        "tags": [
            "blue",
            "yellow",
            "white",
            "beige",
            "light",
            "summer",
            "sea",
            "cream"
        ],
        "colors": [
            "ecf9ff",
            "fffbeb",
            "ffe7cc",
            "f8cba6"
        ]
    },
    {
        "id": "d61355f94a29fce22a30e3df",
        "tags": [
            "maroon",
            "red",
            "yellow",
            "mint",
            "teal",
            "rainbow",
            "kids",
            "spring",
            "happy"
        ],
        "colors": [
            "d61355",
            "f94a29",
            "fce22a",
            "30e3df"
        ]
    },
    {
        "id": "5d3891f99417e8e2e2f5f5f5",
        "tags": [
            "purple",
            "orange",
            "grey",
            "white",
            "retro",
            "wedding"
        ],
        "colors": [
            "5d3891",
            "f99417",
            "e8e2e2",
            "f5f5f5"
        ]
    },
    {
        "id": "f2cd5cf2921da61f69400e32",
        "tags": [
            "yellow",
            "orange",
            "purple",
            "maroon",
            "gold",
            "warm",
            "gradient"
        ],
        "colors": [
            "f2cd5c",
            "f2921d",
            "a61f69",
            "400e32"
        ]
    },
    {
        "id": "aae3e2d9acf5ffcefefdebed",
        "tags": [
            "teal",
            "purple",
            "pink",
            "beige",
            "pastel",
            "kids",
            "light",
            "wedding"
        ],
        "colors": [
            "aae3e2",
            "d9acf5",
            "ffcefe",
            "fdebed"
        ]
    },
    {
        "id": "645cbba084dcbface2ebc7e6",
        "tags": [
            "blue",
            "purple",
            "cold",
            "gradient"
        ],
        "colors": [
            "645cbb",
            "a084dc",
            "bface2",
            "ebc7e6"
        ]
    },
    {
        "id": "fffbf5f7efe5c3acd0674188",
        "tags": [
            "white",
            "beige",
            "purple",
            "vintage"
        ],
        "colors": [
            "fffbf5",
            "f7efe5",
            "c3acd0",
            "674188"
        ]
    },
    {
        "id": "00425a1f8a70bfdb38fc7300",
        "tags": [
            "navy",
            "teal",
            "green",
            "orange",
            "nature",
            "kids",
            "winter",
            "vintage"
        ],
        "colors": [
            "00425a",
            "1f8a70",
            "bfdb38",
            "fc7300"
        ]
    },
    {
        "id": "b9f3fcaee2ff93c6e7fedeff",
        "tags": [
            "blue",
            "pink",
            "sky",
            "pastel",
            "light",
            "kids"
        ],
        "colors": [
            "b9f3fc",
            "aee2ff",
            "93c6e7",
            "fedeff"
        ]
    },
    {
        "id": "03001c301e675b8fb9b6eada",
        "tags": [
            "black",
            "purple",
            "blue",
            "mint",
            "winter",
            "sea",
            "space",
            "dark",
            "gradient"
        ],
        "colors": [
            "03001c",
            "301e67",
            "5b8fb9",
            "b6eada"
        ]
    },
    {
        "id": "86a3b8e8d2a6f48484f55050",
        "tags": [
            "grey",
            "beige",
            "peach",
            "red",
            "vintage",
            "warm"
        ],
        "colors": [
            "86a3b8",
            "e8d2a6",
            "f48484",
            "f55050"
        ]
    },
    {
        "id": "7286d38ea7e9e5e0fffff2f2",
        "tags": [
            "blue",
            "peach",
            "white",
            "pastel",
            "cold",
            "light",
            "sky"
        ],
        "colors": [
            "7286d3",
            "8ea7e9",
            "e5e0ff",
            "fff2f2"
        ]
    },
    {
        "id": "ffd4d4ffffe8cde990aacb73",
        "tags": [
            "peach",
            "pink",
            "yellow",
            "white",
            "green",
            "light",
            "spring",
            "happy",
            "food"
        ],
        "colors": [
            "ffd4d4",
            "ffffe8",
            "cde990",
            "aacb73"
        ]
    },
    {
        "id": "84d2c5e4c988c27664b05a7a",
        "tags": [
            "teal",
            "yellow",
            "brown",
            "maroon",
            "retro",
            "vintage"
        ],
        "colors": [
            "84d2c5",
            "e4c988",
            "c27664",
            "b05a7a"
        ]
    },
    {
        "id": "5671897b8fa1cfb997fad6a5",
        "tags": [
            "navy",
            "grey",
            "brown",
            "beige",
            "sea",
            "winter",
            "earth"
        ],
        "colors": [
            "567189",
            "7b8fa1",
            "cfb997",
            "fad6a5"
        ]
    },
    {
        "id": "658864b7b78addddddeeeeee",
        "tags": [],
        "colors": [
            "658864",
            "b7b78a",
            "dddddd",
            "eeeeee"
        ]
    },
    {
        "id": "ffea208dcbe69df1dfe3f6ff",
        "tags": [
            "yellow",
            "blue",
            "mint",
            "summer",
            "kids",
            "neon",
            "light",
            "happy"
        ],
        "colors": [
            "ffea20",
            "8dcbe6",
            "9df1df",
            "e3f6ff"
        ]
    },
    {
        "id": "13005a00337c1c82ad03c988",
        "tags": [
            "navy",
            "blue",
            "green",
            "sea",
            "dark",
            "night",
            "cold"
        ],
        "colors": [
            "13005a",
            "00337c",
            "1c82ad",
            "03c988"
        ]
    },
    {
        "id": "ff8b13ecececf273e6cf4dce",
        "tags": [
            "orange",
            "grey",
            "pink",
            "purple",
            "kids",
            "retro"
        ],
        "colors": [
            "ff8b13",
            "ececec",
            "f273e6",
            "cf4dce"
        ]
    },
    {
        "id": "abc270fec868fda769473c33",
        "tags": [
            "sage",
            "orange",
            "black",
            "fall",
            "nature"
        ],
        "colors": [
            "abc270",
            "fec868",
            "fda769",
            "473c33"
        ]
    },
    {
        "id": "8200004e6c50f2debafaecd6",
        "tags": [
            "maroon",
            "sage",
            "beige",
            "wedding",
            "vintage",
            "food"
        ],
        "colors": [
            "820000",
            "4e6c50",
            "f2deba",
            "faecd6"
        ]
    },
    {
        "id": "0081b4fad3e7efa3c8f4d9e7",
        "tags": [
            "blue",
            "pink",
            "kids"
        ],
        "colors": [
            "0081b4",
            "fad3e7",
            "efa3c8",
            "f4d9e7"
        ]
    },
    {
        "id": "a75d5dd3756bf0997dffc3a1",
        "tags": [
            "brown",
            "peach",
            "orange",
            "skin",
            "nature",
            "coffee",
            "food",
            "gold",
            "warm",
            "gradient",
            "sunset"
        ],
        "colors": [
            "a75d5d",
            "d3756b",
            "f0997d",
            "ffc3a1"
        ]
    },
    {
        "id": "3d17666f1ab6ff0032cd0404",
        "tags": [
            "purple",
            "red",
            "space"
        ],
        "colors": [
            "3d1766",
            "6f1ab6",
            "ff0032",
            "cd0404"
        ]
    },
    {
        "id": "c780fae3acf9fada9dfbf1d3",
        "tags": [
            "purple",
            "yellow",
            "light",
            "kids",
            "spring"
        ],
        "colors": [
            "c780fa",
            "e3acf9",
            "fada9d",
            "fbf1d3"
        ]
    },
    {
        "id": "39b5e0a31acbff78f0f5ea5a",
        "tags": [
            "blue",
            "purple",
            "pink",
            "yellow",
            "retro",
            "neon",
            "kids"
        ],
        "colors": [
            "39b5e0",
            "a31acb",
            "ff78f0",
            "f5ea5a"
        ]
    },
    {
        "id": "eac7c7a0c3d2f7f5ebeae0da",
        "tags": [
            "peach",
            "blue",
            "grey",
            "beige",
            "pastel",
            "light",
            "earth",
            "cream"
        ],
        "colors": [
            "eac7c7",
            "a0c3d2",
            "f7f5eb",
            "eae0da"
        ]
    },
    {
        "id": "0081c95bc0f886e5ffffc93c",
        "tags": [
            "blue",
            "yellow",
            "summer",
            "sea",
            "happy"
        ],
        "colors": [
            "0081c9",
            "5bc0f8",
            "86e5ff",
            "ffc93c"
        ]
    },
    {
        "id": "ff7b54ffb26bffd56f939b62",
        "tags": [
            "orange",
            "sage",
            "yellow",
            "vintage",
            "gold",
            "nature"
        ],
        "colors": [
            "ff7b54",
            "ffb26b",
            "ffd56f",
            "939b62"
        ]
    },
    {
        "id": "d7e9b9fffbacffd495faab78",
        "tags": [
            "green",
            "sage",
            "yellow",
            "orange",
            "light",
            "gold",
            "happy",
            "spring"
        ],
        "colors": [
            "d7e9b9",
            "fffbac",
            "ffd495",
            "faab78"
        ]
    },
    {
        "id": "6c00ff3c79f52dcddff2deba",
        "tags": [
            "purple",
            "blue",
            "teal",
            "beige",
            "winter"
        ],
        "colors": [
            "6c00ff",
            "3c79f5",
            "2dcddf",
            "f2deba"
        ]
    },
    {
        "id": "b5d5c5b08bbbeca869f5f5dc",
        "tags": [
            "sage",
            "purple",
            "orange",
            "beige",
            "warm",
            "pastel",
            "vintage",
            "kids",
            "earth",
            "wedding"
        ],
        "colors": [
            "b5d5c5",
            "b08bbb",
            "eca869",
            "f5f5dc"
        ]
    },
    {
        "id": "7b28699d3c72c85c8effbaba",
        "tags": [
            "maroon",
            "purple",
            "peach",
            "gradient",
            "warm",
            "wedding",
            "sunset"
        ],
        "colors": [
            "7b2869",
            "9d3c72",
            "c85c8e",
            "ffbaba"
        ]
    },
    {
        "id": "f5edce89c4e158287f1a0000",
        "tags": [
            "beige",
            "blue",
            "purple",
            "black",
            "retro",
            "space"
        ],
        "colors": [
            "f5edce",
            "89c4e1",
            "58287f",
            "1a0000"
        ]
    },
    {
        "id": "579bb1e1d7c6ece8ddf8f4ea",
        "tags": [
            "blue",
            "beige",
            "white",
            "light",
            "cream",
            "vintage",
            "wedding"
        ],
        "colors": [
            "579bb1",
            "e1d7c6",
            "ece8dd",
            "f8f4ea"
        ]
    },
    {
        "id": "ffb100fbc252f0eccfa3bb98",
        "tags": [
            "orange",
            "beige",
            "sage",
            "summer",
            "happy",
            "food"
        ],
        "colors": [
            "ffb100",
            "fbc252",
            "f0eccf",
            "a3bb98"
        ]
    },
    {
        "id": "3c625561876ea6bb8deae7b1",
        "tags": [
            "green",
            "sage",
            "nature"
        ],
        "colors": [
            "3c6255",
            "61876e",
            "a6bb8d",
            "eae7b1"
        ]
    },
    {
        "id": "243763ff6e31ffebb7ad8e70",
        "tags": [
            "navy",
            "orange",
            "yellow",
            "brown",
            "retro",
            "kids"
        ],
        "colors": [
            "243763",
            "ff6e31",
            "ffebb7",
            "ad8e70"
        ]
    },
    {
        "id": "0a26471442722052952c74b3",
        "tags": [
            "navy",
            "blue",
            "dark",
            "sea",
            "cold"
        ],
        "colors": [
            "0a2647",
            "144272",
            "205295",
            "2c74b3"
        ]
    },
    {
        "id": "fd8a8af1f7b5a8d1d19ea1d4",
        "tags": [
            "red",
            "yellow",
            "teal",
            "blue",
            "pastel",
            "rainbow",
            "kids",
            "light"
        ],
        "colors": [
            "fd8a8a",
            "f1f7b5",
            "a8d1d1",
            "9ea1d4"
        ]
    },
    {
        "id": "3a4f7affc6d3fea1bfe98ead",
        "tags": [
            "navy",
            "pink",
            "skin"
        ],
        "colors": [
            "3a4f7a",
            "ffc6d3",
            "fea1bf",
            "e98ead"
        ]
    },
    {
        "id": "82aae391d8e4bfeaf5eafdfc",
        "tags": [
            "blue",
            "teal",
            "sky",
            "cold",
            "gradient"
        ],
        "colors": [
            "82aae3",
            "91d8e4",
            "bfeaf5",
            "eafdfc"
        ]
    },
    {
        "id": "ffd4b2fff6bdceedc786c8bc",
        "tags": [
            "peach",
            "yellow",
            "green",
            "teal",
            "light",
            "pastel",
            "summer",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "ffd4b2",
            "fff6bd",
            "ceedc7",
            "86c8bc"
        ]
    },
    {
        "id": "1a120b3c2a21d5cea3e5e5cb",
        "tags": [
            "black",
            "brown",
            "beige",
            "dark",
            "night",
            "coffee",
            "halloween",
            "warm"
        ],
        "colors": [
            "1a120b",
            "3c2a21",
            "d5cea3",
            "e5e5cb"
        ]
    },
    {
        "id": "dc0000850000ffdb89fff6c3",
        "tags": [
            "red",
            "maroon",
            "yellow",
            "kids"
        ],
        "colors": [
            "dc0000",
            "850000",
            "ffdb89",
            "fff6c3"
        ]
    },
    {
        "id": "f8ede3dfd3c3d0b8a885586f",
        "tags": [
            "beige",
            "maroon",
            "vintage",
            "pastel",
            "skin",
            "coffee",
            "cream",
            "fall",
            "warm",
            "gradient"
        ],
        "colors": [
            "f8ede3",
            "dfd3c3",
            "d0b8a8",
            "85586f"
        ]
    },
    {
        "id": "ada2ffc0deffffe5f1fff8e1",
        "tags": [
            "purple",
            "blue",
            "peach",
            "yellow",
            "rainbow",
            "kids",
            "light",
            "summer"
        ],
        "colors": [
            "ada2ff",
            "c0deff",
            "ffe5f1",
            "fff8e1"
        ]
    },
    {
        "id": "eb455ffcffe7bad7e92b3467",
        "tags": [
            "red",
            "white",
            "blue",
            "navy",
            "retro",
            "kids",
            "christmas"
        ],
        "colors": [
            "eb455f",
            "fcffe7",
            "bad7e9",
            "2b3467"
        ]
    },
    {
        "id": "ff597bff8e9ef9b5d0eeeeee",
        "tags": [
            "red",
            "pink",
            "grey",
            "kids",
            "food",
            "christmas"
        ],
        "colors": [
            "ff597b",
            "ff8e9e",
            "f9b5d0",
            "eeeeee"
        ]
    },
    {
        "id": "1c315e227c7088a47ce6e2c3",
        "tags": [
            "navy",
            "teal",
            "sage",
            "beige",
            "winter",
            "gradient",
            "cold",
            "sea",
            "nature"
        ],
        "colors": [
            "1c315e",
            "227c70",
            "88a47c",
            "e6e2c3"
        ]
    },
    {
        "id": "4721834b56d282c3ecf1f6f5",
        "tags": [
            "purple",
            "navy",
            "blue",
            "grey",
            "sea",
            "winter",
            "gradient",
            "cold"
        ],
        "colors": [
            "472183",
            "4b56d2",
            "82c3ec",
            "f1f6f5"
        ]
    },
    {
        "id": "ffffd0f3ccffd09cfaa555ec",
        "tags": [
            "yellow",
            "purple",
            "kids",
            "retro",
            "neon",
            "light",
            "happy"
        ],
        "colors": [
            "ffffd0",
            "f3ccff",
            "d09cfa",
            "a555ec"
        ]
    },
    {
        "id": "f56eb3cb1c8d7f167f460c68",
        "tags": [
            "pink",
            "purple",
            "gradient",
            "space"
        ],
        "colors": [
            "f56eb3",
            "cb1c8d",
            "7f167f",
            "460c68"
        ]
    },
    {
        "id": "faf8f1faeab1e5ba73c58940",
        "tags": [
            "beige",
            "yellow",
            "brown",
            "gold",
            "light",
            "gradient",
            "warm",
            "summer"
        ],
        "colors": [
            "faf8f1",
            "faeab1",
            "e5ba73",
            "c58940"
        ]
    },
    {
        "id": "439a9762b6b797dececbedd5",
        "tags": [
            "teal",
            "mint",
            "sea",
            "gradient",
            "winter"
        ],
        "colors": [
            "439a97",
            "62b6b7",
            "97dece",
            "cbedd5"
        ]
    },
    {
        "id": "181d31678983e6ddc4f0e9d2",
        "tags": [
            "black",
            "teal",
            "beige",
            "night",
            "vintage"
        ],
        "colors": [
            "181d31",
            "678983",
            "e6ddc4",
            "f0e9d2"
        ]
    },
    {
        "id": "fffbeb495579263159251749",
        "tags": [
            "yellow",
            "navy",
            "winter",
            "vintage"
        ],
        "colors": [
            "fffbeb",
            "495579",
            "263159",
            "251749"
        ]
    },
    {
        "id": "ccd6a6dae2b6f4ead5fffbe9",
        "tags": [
            "sage",
            "green",
            "beige",
            "nature",
            "earth",
            "light",
            "summer",
            "food"
        ],
        "colors": [
            "ccd6a6",
            "dae2b6",
            "f4ead5",
            "fffbe9"
        ]
    },
    {
        "id": "c0eee4f8f988ffcac8ff9e9e",
        "tags": [
            "mint",
            "yellow",
            "peach",
            "kids",
            "rainbow",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "c0eee4",
            "f8f988",
            "ffcac8",
            "ff9e9e"
        ]
    },
    {
        "id": "453c676d67e446c2cbf2f7a1",
        "tags": [
            "blue",
            "navy",
            "yellow",
            "purple",
            "dark",
            "warm",
            "winter",
            "night",
            "space",
            "sky"
        ],
        "colors": [
            "453c67",
            "6d67e4",
            "46c2cb",
            "f2f7a1"
        ]
    },
    {
        "id": "e8f3d6fcf9beffdca9faab78",
        "tags": [
            "sage",
            "yellow",
            "beige",
            "orange",
            "pastel",
            "light",
            "warm",
            "summer",
            "food",
            "gradient",
            "cream"
        ],
        "colors": [
            "e8f3d6",
            "fcf9be",
            "ffdca9",
            "faab78"
        ]
    },
    {
        "id": "2d033b810ca8c147e9e5b8f4",
        "tags": [
            "black",
            "purple",
            "gradient",
            "night",
            "dark",
            "space"
        ],
        "colors": [
            "2d033b",
            "810ca8",
            "c147e9",
            "e5b8f4"
        ]
    },
    {
        "id": "10a19d540375ff7000ffbf00",
        "tags": [
            "teal",
            "purple",
            "orange",
            "yellow",
            "retro",
            "kids"
        ],
        "colors": [
            "10a19d",
            "540375",
            "ff7000",
            "ffbf00"
        ]
    },
    {
        "id": "2b3a55ce7777e8c4c4f2e5e5",
        "tags": [
            "navy",
            "peach",
            "grey",
            "vintage",
            "skin"
        ],
        "colors": [
            "2b3a55",
            "ce7777",
            "e8c4c4",
            "f2e5e5"
        ]
    },
    {
        "id": "3f0071fb2576332fd00002a1",
        "tags": [
            "purple",
            "pink",
            "blue",
            "navy",
            "neon",
            "space",
            "kids"
        ],
        "colors": [
            "3f0071",
            "fb2576",
            "332fd0",
            "0002a1"
        ]
    },
    {
        "id": "fefcf3f5ebe0f0dbdbdba39a",
        "tags": [
            "white",
            "beige",
            "peach",
            "pastel",
            "skin",
            "cream",
            "light"
        ],
        "colors": [
            "fefcf3",
            "f5ebe0",
            "f0dbdb",
            "dba39a"
        ]
    },
    {
        "id": "fed049cffde168b9843d5656",
        "tags": [
            "yellow",
            "mint",
            "green",
            "nature",
            "happy"
        ],
        "colors": [
            "fed049",
            "cffde1",
            "68b984",
            "3d5656"
        ]
    },
    {
        "id": "f3efe043424222222222a39f",
        "tags": [
            "beige",
            "grey",
            "black",
            "teal",
            "wedding",
            "retro"
        ],
        "colors": [
            "f3efe0",
            "434242",
            "222222",
            "22a39f"
        ]
    },
    {
        "id": "a5f1e97fe9defff6bfffebad",
        "tags": [
            "mint",
            "teal",
            "yellow",
            "beige",
            "kids",
            "light",
            "sky"
        ],
        "colors": [
            "a5f1e9",
            "7fe9de",
            "fff6bf",
            "ffebad"
        ]
    },
    {
        "id": "344d676eccafade792f3ecb0",
        "tags": [
            "navy",
            "teal",
            "green",
            "yellow",
            "beige",
            "nature",
            "gradient"
        ],
        "colors": [
            "344d67",
            "6eccaf",
            "ade792",
            "f3ecb0"
        ]
    },
    {
        "id": "2a39909c254dd23369f06292",
        "tags": [
            "navy",
            "maroon",
            "pink",
            "kids",
            "space"
        ],
        "colors": [
            "2a3990",
            "9c254d",
            "d23369",
            "f06292"
        ]
    },
    {
        "id": "00fff600e7ff009eff0014ff",
        "tags": [
            "mint",
            "blue",
            "navy",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "00fff6",
            "00e7ff",
            "009eff",
            "0014ff"
        ]
    },
    {
        "id": "65647c8b7e74c7bca1f1d3b3",
        "tags": [
            "grey",
            "brown",
            "sage",
            "beige",
            "cream",
            "skin",
            "coffee",
            "pastel",
            "earth",
            "fall",
            "winter"
        ],
        "colors": [
            "65647c",
            "8b7e74",
            "c7bca1",
            "f1d3b3"
        ]
    },
    {
        "id": "00005c3b185fc060a1f0caa3",
        "tags": [
            "navy",
            "purple",
            "beige",
            "dark",
            "night"
        ],
        "colors": [
            "00005c",
            "3b185f",
            "c060a1",
            "f0caa3"
        ]
    },
    {
        "id": "e5d9b6a4be7b5f8d4e285430",
        "tags": [
            "beige",
            "green",
            "nature",
            "earth"
        ],
        "colors": [
            "e5d9b6",
            "a4be7b",
            "5f8d4e",
            "285430"
        ]
    },
    {
        "id": "000000282a3a735f32c69749",
        "tags": [
            "black",
            "brown",
            "beige",
            "dark",
            "night"
        ],
        "colors": [
            "000000",
            "282a3a",
            "735f32",
            "c69749"
        ]
    },
    {
        "id": "863a6f975c8dd989b5ffadbc",
        "tags": [
            "maroon",
            "purple",
            "pink",
            "peach",
            "sky",
            "sunset",
            "gradient",
            "warm"
        ],
        "colors": [
            "863a6f",
            "975c8d",
            "d989b5",
            "ffadbc"
        ]
    },
    {
        "id": "ffe15df49d1adc3535b01e68",
        "tags": [
            "yellow",
            "orange",
            "red",
            "purple",
            "sunset",
            "warm",
            "happy",
            "gold"
        ],
        "colors": [
            "ffe15d",
            "f49d1a",
            "dc3535",
            "b01e68"
        ]
    },
    {
        "id": "fbfacddebaceba94d17f669d",
        "tags": [
            "yellow",
            "peach",
            "purple",
            "pastel",
            "vintage",
            "kids",
            "light",
            "cream"
        ],
        "colors": [
            "fbfacd",
            "debace",
            "ba94d1",
            "7f669d"
        ]
    },
    {
        "id": "f5d5aeef9a53c539b4852999",
        "tags": [
            "beige",
            "orange",
            "purple",
            "vintage",
            "kids",
            "wedding"
        ],
        "colors": [
            "f5d5ae",
            "ef9a53",
            "c539b4",
            "852999"
        ]
    },
    {
        "id": "cff5e7a0e4cb59c1bd0d4c92",
        "tags": [
            "mint",
            "teal",
            "blue",
            "navy",
            "cold",
            "sea",
            "sky"
        ],
        "colors": [
            "cff5e7",
            "a0e4cb",
            "59c1bd",
            "0d4c92"
        ]
    },
    {
        "id": "f7a4a4febe8cfffbc1b6e2a1",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "pastel",
            "light",
            "kids",
            "spring",
            "summer",
            "happy",
            "food"
        ],
        "colors": [
            "f7a4a4",
            "febe8c",
            "fffbc1",
            "b6e2a1"
        ]
    },
    {
        "id": "eff5f5d6e4e5497174eb6440",
        "tags": [
            "grey",
            "teal",
            "orange",
            "cold",
            "winter",
            "christmas"
        ],
        "colors": [
            "eff5f5",
            "d6e4e5",
            "497174",
            "eb6440"
        ]
    },
    {
        "id": "3b34867743dbffe9b1fcfdf2",
        "tags": [
            "navy",
            "purple",
            "yellow",
            "white",
            "happy",
            "wedding"
        ],
        "colors": [
            "3b3486",
            "7743db",
            "ffe9b1",
            "fcfdf2"
        ]
    },
    {
        "id": "5571537d8f69a9af7ee6e5a3",
        "tags": [
            "green",
            "sage",
            "nature",
            "earth",
            "cold",
            "gradient"
        ],
        "colors": [
            "557153",
            "7d8f69",
            "a9af7e",
            "e6e5a3"
        ]
    },
    {
        "id": "393e466d9886f2e7d5f7f7f7",
        "tags": [
            "black",
            "teal",
            "beige",
            "white",
            "vintage",
            "cold"
        ],
        "colors": [
            "393e46",
            "6d9886",
            "f2e7d5",
            "f7f7f7"
        ]
    },
    {
        "id": "f2debaffefd60e5e6f3a8891",
        "tags": [
            "beige",
            "teal",
            "wedding",
            "vintage"
        ],
        "colors": [
            "f2deba",
            "ffefd6",
            "0e5e6f",
            "3a8891"
        ]
    },
    {
        "id": "432c7a80489cff8fb1fce2db",
        "tags": [
            "purple",
            "pink",
            "peach",
            "kids",
            "warm"
        ],
        "colors": [
            "432c7a",
            "80489c",
            "ff8fb1",
            "fce2db"
        ]
    },
    {
        "id": "e97777ff9f9ffcddb0fffad7",
        "tags": [
            "red",
            "peach",
            "yellow",
            "pastel",
            "light",
            "kids",
            "skin",
            "warm"
        ],
        "colors": [
            "e97777",
            "ff9f9f",
            "fcddb0",
            "fffad7"
        ]
    },
    {
        "id": "def5e5bcead59ed5c58ec3b0",
        "tags": [
            "mint",
            "teal",
            "cream",
            "cold",
            "light",
            "sky",
            "winter"
        ],
        "colors": [
            "def5e5",
            "bcead5",
            "9ed5c5",
            "8ec3b0"
        ]
    },
    {
        "id": "6c4ab68d72e18d9effb9e0ff",
        "tags": [
            "purple",
            "blue",
            "gradient",
            "winter",
            "cold"
        ],
        "colors": [
            "6c4ab6",
            "8d72e1",
            "8d9eff",
            "b9e0ff"
        ]
    },
    {
        "id": "404258474e6850577a6b728e",
        "tags": [
            "black",
            "navy",
            "grey",
            "dark",
            "winter",
            "night"
        ],
        "colors": [
            "404258",
            "474e68",
            "50577a",
            "6b728e"
        ]
    },
    {
        "id": "ffe1e190a17d829460eeeeee",
        "tags": [
            "pink",
            "sage",
            "green",
            "grey",
            "light",
            "pastel",
            "food",
            "nature"
        ],
        "colors": [
            "ffe1e1",
            "90a17d",
            "829460",
            "eeeeee"
        ]
    },
    {
        "id": "3f3b6c624f829f73aba3c7d6",
        "tags": [
            "navy",
            "purple",
            "blue",
            "night",
            "space",
            "dark",
            "cold",
            "gradient"
        ],
        "colors": [
            "3f3b6c",
            "624f82",
            "9f73ab",
            "a3c7d6"
        ]
    },
    {
        "id": "e14d2afd841f3e6d9c001253",
        "tags": [
            "red",
            "orange",
            "blue",
            "navy",
            "retro",
            "kids"
        ],
        "colors": [
            "e14d2a",
            "fd841f",
            "3e6d9c",
            "001253"
        ]
    },
    {
        "id": "ffb9b9ffddd2ffacc7ff8dc7",
        "tags": [
            "peach",
            "beige",
            "pink",
            "kids",
            "light",
            "pastel",
            "skin",
            "warm",
            "wedding",
            "spring"
        ],
        "colors": [
            "ffb9b9",
            "ffddd2",
            "ffacc7",
            "ff8dc7"
        ]
    },
    {
        "id": "f6f6c9bad1c24fa095153462",
        "tags": [
            "yellow",
            "green",
            "teal",
            "navy",
            "cold",
            "winter"
        ],
        "colors": [
            "f6f6c9",
            "bad1c2",
            "4fa095",
            "153462"
        ]
    },
    {
        "id": "61764b9ba17bcfb997fad6a5",
        "tags": [
            "green",
            "sage",
            "beige",
            "earth",
            "vintage",
            "nature",
            "fall"
        ],
        "colors": [
            "61764b",
            "9ba17b",
            "cfb997",
            "fad6a5"
        ]
    },
    {
        "id": "f0ff4282cd4754b435379237",
        "tags": [
            "green",
            "yellow",
            "summer",
            "neon",
            "happy",
            "nature"
        ],
        "colors": [
            "f0ff42",
            "82cd47",
            "54b435",
            "379237"
        ]
    },
    {
        "id": "b3ffaef8ffdbff6464ff7d7d",
        "tags": [
            "green",
            "yellow",
            "red",
            "peach",
            "light",
            "neon",
            "kids",
            "happy"
        ],
        "colors": [
            "b3ffae",
            "f8ffdb",
            "ff6464",
            "ff7d7d"
        ]
    },
    {
        "id": "0008c12146c7e6cba8fdf0e0",
        "tags": [
            "navy",
            "blue",
            "beige",
            "winter"
        ],
        "colors": [
            "0008c1",
            "2146c7",
            "e6cba8",
            "fdf0e0"
        ]
    },
    {
        "id": "7de5ed81c6e85da7db5837d0",
        "tags": [
            "blue",
            "purple",
            "cold",
            "winter",
            "sky",
            "sea"
        ],
        "colors": [
            "7de5ed",
            "81c6e8",
            "5da7db",
            "5837d0"
        ]
    },
    {
        "id": "3951444e6c50aa8b56f0ebce",
        "tags": [
            "green",
            "brown",
            "beige",
            "earth",
            "nature",
            "wedding",
            "vintage",
            "food"
        ],
        "colors": [
            "395144",
            "4e6c50",
            "aa8b56",
            "f0ebce"
        ]
    },
    {
        "id": "9a1663e0144cff5858ff97c1",
        "tags": [
            "maroon",
            "red",
            "peach",
            "pink",
            "wedding",
            "warm",
            "sunset",
            "gradient"
        ],
        "colors": [
            "9a1663",
            "e0144c",
            "ff5858",
            "ff97c1"
        ]
    },
    {
        "id": "ff8787f8c4b4e5ebb2bce29e",
        "tags": [
            "red",
            "peach",
            "green",
            "yellow",
            "beige",
            "pink",
            "spring",
            "nature",
            "pastel",
            "summer",
            "light",
            "kids",
            "happy",
            "cream"
        ],
        "colors": [
            "ff8787",
            "f8c4b4",
            "e5ebb2",
            "bce29e"
        ]
    },
    {
        "id": "000000cf0a0adc5f00eeeeee",
        "tags": [
            "black",
            "red",
            "orange",
            "grey",
            "white",
            "space",
            "retro",
            "halloween"
        ],
        "colors": [
            "000000",
            "cf0a0a",
            "dc5f00",
            "eeeeee"
        ]
    },
    {
        "id": "00abb33c4048b2b2b2eaeaea",
        "tags": [
            "teal",
            "black",
            "grey",
            "space"
        ],
        "colors": [
            "00abb3",
            "3c4048",
            "b2b2b2",
            "eaeaea"
        ]
    },
    {
        "id": "1d1ce54649ff7978ffc47aff",
        "tags": [
            "blue",
            "purple",
            "night",
            "cold",
            "gradient",
            "sea"
        ],
        "colors": [
            "1d1ce5",
            "4649ff",
            "7978ff",
            "c47aff"
        ]
    },
    {
        "id": "fdfdbdc8ffd4b8e8fcb1afff",
        "tags": [
            "yellow",
            "mint",
            "blue",
            "purple",
            "pastel",
            "light",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "fdfdbd",
            "c8ffd4",
            "b8e8fc",
            "b1afff"
        ]
    },
    {
        "id": "ea047eff6d28fce70000f5ff",
        "tags": [
            "pink",
            "orange",
            "yellow",
            "teal",
            "neon",
            "rainbow",
            "kids",
            "happy"
        ],
        "colors": [
            "ea047e",
            "ff6d28",
            "fce700",
            "00f5ff"
        ]
    },
    {
        "id": "fff8ea9e7676815b5b594545",
        "tags": [
            "beige",
            "brown",
            "pastel",
            "vintage",
            "coffee",
            "earth",
            "cream",
            "fall",
            "warm",
            "wedding",
            "skin"
        ],
        "colors": [
            "fff8ea",
            "9e7676",
            "815b5b",
            "594545"
        ]
    },
    {
        "id": "faf7f0cdfcf6bccef898a8f8",
        "tags": [
            "grey",
            "beige",
            "mint",
            "blue",
            "light",
            "kids",
            "pastel",
            "winter",
            "cold",
            "sky"
        ],
        "colors": [
            "faf7f0",
            "cdfcf6",
            "bccef8",
            "98a8f8"
        ]
    },
    {
        "id": "0000001500503f0071fb2576",
        "tags": [
            "black",
            "navy",
            "purple",
            "pink",
            "space",
            "dark"
        ],
        "colors": [
            "000000",
            "150050",
            "3f0071",
            "fb2576"
        ]
    },
    {
        "id": "425f57749f82a8e890cfff8d",
        "tags": [
            "green",
            "sage",
            "nature",
            "kids",
            "gradient"
        ],
        "colors": [
            "425f57",
            "749f82",
            "a8e890",
            "cfff8d"
        ]
    },
    {
        "id": "ede4e0c8dbbe9f8772665a48",
        "tags": [
            "grey",
            "beige",
            "green",
            "brown",
            "earth",
            "vintage",
            "pastel",
            "nature",
            "warm",
            "fall"
        ],
        "colors": [
            "ede4e0",
            "c8dbbe",
            "9f8772",
            "665a48"
        ]
    },
    {
        "id": "d8d9cfedededff8787e26868",
        "tags": [
            "grey",
            "peach",
            "red",
            "retro",
            "vintage",
            "kids",
            "wedding",
            "christmas"
        ],
        "colors": [
            "d8d9cf",
            "ededed",
            "ff8787",
            "e26868"
        ]
    },
    {
        "id": "ff731dfff7e95f9df71746a2",
        "tags": [
            "orange",
            "beige",
            "blue",
            "navy",
            "kids",
            "retro"
        ],
        "colors": [
            "ff731d",
            "fff7e9",
            "5f9df7",
            "1746a2"
        ]
    },
    {
        "id": "3c2317628e90b4cde6f5efe6",
        "tags": [
            "brown",
            "black",
            "teal",
            "blue",
            "beige",
            "vintage",
            "wedding",
            "winter",
            "gradient"
        ],
        "colors": [
            "3c2317",
            "628e90",
            "b4cde6",
            "f5efe6"
        ]
    },
    {
        "id": "dd5353b73e3edbc8aceddbc0",
        "tags": [
            "red",
            "beige",
            "warm",
            "vintage",
            "food"
        ],
        "colors": [
            "dd5353",
            "b73e3e",
            "dbc8ac",
            "eddbc0"
        ]
    },
    {
        "id": "905e96d58bddff99d7ffd372",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "sunset",
            "kids",
            "retro",
            "wedding"
        ],
        "colors": [
            "905e96",
            "d58bdd",
            "ff99d7",
            "ffd372"
        ]
    },
    {
        "id": "002e94083aa9e1ceb5ffe7cc",
        "tags": [
            "navy",
            "blue",
            "beige",
            "wedding",
            "winter"
        ],
        "colors": [
            "002e94",
            "083aa9",
            "e1ceb5",
            "ffe7cc"
        ]
    },
    {
        "id": "251b37372948ffcacaffecef",
        "tags": [
            "black",
            "peach",
            "pink",
            "vintage",
            "wedding"
        ],
        "colors": [
            "251b37",
            "372948",
            "ffcaca",
            "ffecef"
        ]
    },
    {
        "id": "2192ff38e54d9cff2efdff00",
        "tags": [
            "blue",
            "green",
            "yellow",
            "neon",
            "summer",
            "kids",
            "light"
        ],
        "colors": [
            "2192ff",
            "38e54d",
            "9cff2e",
            "fdff00"
        ]
    },
    {
        "id": "ff577fff884bffd384fff9b0",
        "tags": [
            "pink",
            "orange",
            "yellow",
            "kids",
            "gold",
            "warm"
        ],
        "colors": [
            "ff577f",
            "ff884b",
            "ffd384",
            "fff9b0"
        ]
    },
    {
        "id": "ff74b1ffa1cfffd6eca7ffe4",
        "tags": [
            "pink",
            "mint",
            "kids",
            "happy",
            "light",
            "wedding"
        ],
        "colors": [
            "ff74b1",
            "ffa1cf",
            "ffd6ec",
            "a7ffe4"
        ]
    },
    {
        "id": "06283d256d8547b5ffdff6ff",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "06283d",
            "256d85",
            "47b5ff",
            "dff6ff"
        ]
    },
    {
        "id": "e1ffb1c7f2a4b6e388fcffb2",
        "tags": [
            "green",
            "yellow",
            "light",
            "earth",
            "happy",
            "summer",
            "nature"
        ],
        "colors": [
            "e1ffb1",
            "c7f2a4",
            "b6e388",
            "fcffb2"
        ]
    },
    {
        "id": "8bbccc4c67935c2e7e000000",
        "tags": [
            "blue",
            "teal",
            "purple",
            "black",
            "cold",
            "night",
            "space",
            "winter",
            "sea"
        ],
        "colors": [
            "8bbccc",
            "4c6793",
            "5c2e7e",
            "000000"
        ]
    },
    {
        "id": "00ffd131c6d4ffff00ff1e1e",
        "tags": [
            "mint",
            "blue",
            "yellow",
            "red",
            "kids",
            "neon",
            "rainbow"
        ],
        "colors": [
            "00ffd1",
            "31c6d4",
            "ffff00",
            "ff1e1e"
        ]
    },
    {
        "id": "f8ede3dfd3c3d0b8a87d6e83",
        "tags": [
            "beige",
            "grey",
            "earth",
            "cream",
            "coffee",
            "skin",
            "fall",
            "vintage",
            "pastel"
        ],
        "colors": [
            "f8ede3",
            "dfd3c3",
            "d0b8a8",
            "7d6e83"
        ]
    },
    {
        "id": "f96666674747829460eeeeee",
        "tags": [
            "red",
            "brown",
            "green",
            "grey",
            "vintage",
            "food"
        ],
        "colors": [
            "f96666",
            "674747",
            "829460",
            "eeeeee"
        ]
    },
    {
        "id": "f5efe6e8dfcaaebdca7895b2",
        "tags": [
            "beige",
            "blue",
            "pastel",
            "cream",
            "wedding"
        ],
        "colors": [
            "f5efe6",
            "e8dfca",
            "aebdca",
            "7895b2"
        ]
    },
    {
        "id": "937dc2c689c6ffabe1ffe6f7",
        "tags": [
            "purple",
            "pink",
            "light",
            "kids",
            "wedding",
            "gradient"
        ],
        "colors": [
            "937dc2",
            "c689c6",
            "ffabe1",
            "ffe6f7"
        ]
    },
    {
        "id": "fff5e4ffe3e1ffd1d1ff9494",
        "tags": [
            "yellow",
            "pink",
            "peach",
            "pastel",
            "food",
            "summer",
            "cream",
            "skin"
        ],
        "colors": [
            "fff5e4",
            "ffe3e1",
            "ffd1d1",
            "ff9494"
        ]
    },
    {
        "id": "182747562b08647e68d8d8d8",
        "tags": [
            "navy",
            "brown",
            "sage",
            "grey",
            "dark",
            "night",
            "vintage",
            "halloween",
            "sea"
        ],
        "colors": [
            "182747",
            "562b08",
            "647e68",
            "d8d8d8"
        ]
    },
    {
        "id": "fd841fe14d2acd104d9c2c77",
        "tags": [
            "orange",
            "red",
            "pink",
            "sunset",
            "gold",
            "warm",
            "gradient"
        ],
        "colors": [
            "fd841f",
            "e14d2a",
            "cd104d",
            "9c2c77"
        ]
    },
    {
        "id": "6f38c587a2fbadddd0eeeeee",
        "tags": [
            "purple",
            "blue",
            "teal",
            "grey",
            "space",
            "retro",
            "kids",
            "gradient"
        ],
        "colors": [
            "6f38c5",
            "87a2fb",
            "adddd0",
            "eeeeee"
        ]
    },
    {
        "id": "fa7070fbf2cfc6ebc5a1c298",
        "tags": [
            "peach",
            "yellow",
            "green",
            "sage",
            "food",
            "nature",
            "kids",
            "happy",
            "light",
            "christmas"
        ],
        "colors": [
            "fa7070",
            "fbf2cf",
            "c6ebc5",
            "a1c298"
        ]
    },
    {
        "id": "31e1f7400d51d800a6ff7777",
        "tags": [
            "blue",
            "purple",
            "pink",
            "peach",
            "space",
            "retro",
            "neon"
        ],
        "colors": [
            "31e1f7",
            "400d51",
            "d800a6",
            "ff7777"
        ]
    },
    {
        "id": "ffe9a0367e18f57328cc3636",
        "tags": [
            "yellow",
            "green",
            "orange",
            "red",
            "vintage",
            "kids"
        ],
        "colors": [
            "ffe9a0",
            "367e18",
            "f57328",
            "cc3636"
        ]
    },
    {
        "id": "b1b2ffaac4ffd2daffeef1ff",
        "tags": [
            "purple",
            "blue",
            "cream",
            "light",
            "pastel",
            "cold",
            "sky"
        ],
        "colors": [
            "b1b2ff",
            "aac4ff",
            "d2daff",
            "eef1ff"
        ]
    },
    {
        "id": "c3f8ffabd9fffff6bfffebad",
        "tags": [
            "blue",
            "yellow",
            "happy",
            "light",
            "summer",
            "kids",
            "sky"
        ],
        "colors": [
            "c3f8ff",
            "abd9ff",
            "fff6bf",
            "ffebad"
        ]
    },
    {
        "id": "1818188758ff5cb8e4f2f2f2",
        "tags": [
            "black",
            "purple",
            "blue",
            "grey",
            "space",
            "retro",
            "gradient"
        ],
        "colors": [
            "181818",
            "8758ff",
            "5cb8e4",
            "f2f2f2"
        ]
    },
    {
        "id": "d2001affde00fffae7efefef",
        "tags": [
            "red",
            "yellow",
            "white",
            "grey",
            "kids",
            "retro",
            "warm"
        ],
        "colors": [
            "d2001a",
            "ffde00",
            "fffae7",
            "efefef"
        ]
    },
    {
        "id": "4c0033790252af0171e80f88",
        "tags": [
            "maroon",
            "purple",
            "pink",
            "wedding",
            "dark"
        ],
        "colors": [
            "4c0033",
            "790252",
            "af0171",
            "e80f88"
        ]
    },
    {
        "id": "cdf0eaf9f9f9ecc5fbfaf4b7",
        "tags": [
            "mint",
            "white",
            "purple",
            "yellow",
            "cream",
            "light",
            "pastel",
            "kids",
            "spring",
            "wedding"
        ],
        "colors": [
            "cdf0ea",
            "f9f9f9",
            "ecc5fb",
            "faf4b7"
        ]
    },
    {
        "id": "b7c4cfeee3cbd7c0ae967e76",
        "tags": [
            "blue",
            "beige",
            "brown",
            "pastel",
            "earth",
            "fall",
            "winter",
            "vintage"
        ],
        "colors": [
            "b7c4cf",
            "eee3cb",
            "d7c0ae",
            "967e76"
        ]
    },
    {
        "id": "25316d5f6f9497d2ecfef5ac",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "winter",
            "sky"
        ],
        "colors": [
            "25316d",
            "5f6f94",
            "97d2ec",
            "fef5ac"
        ]
    },
    {
        "id": "1c67583d8361d6cda4eef2e6",
        "tags": [
            "green",
            "beige",
            "food",
            "nature",
            "earth"
        ],
        "colors": [
            "1c6758",
            "3d8361",
            "d6cda4",
            "eef2e6"
        ]
    },
    {
        "id": "645caaa084cabface0ebc7e8",
        "tags": [
            "purple",
            "pink",
            "kids",
            "gradient",
            "sky"
        ],
        "colors": [
            "645caa",
            "a084ca",
            "bface0",
            "ebc7e8"
        ]
    },
    {
        "id": "f07deaa460ed9fc9f3eeeeee",
        "tags": [
            "pink",
            "purple",
            "blue",
            "grey",
            "retro",
            "kids"
        ],
        "colors": [
            "f07dea",
            "a460ed",
            "9fc9f3",
            "eeeeee"
        ]
    },
    {
        "id": "a7d2cbf2d388c98474874c62",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "brown",
            "maroon",
            "earth",
            "kids",
            "pastel",
            "vintage"
        ],
        "colors": [
            "a7d2cb",
            "f2d388",
            "c98474",
            "874c62"
        ]
    },
    {
        "id": "7fbcd2a5f1e9e1ffeeffeeaf",
        "tags": [
            "blue",
            "mint",
            "yellow",
            "summer",
            "happy",
            "kids",
            "light",
            "sky"
        ],
        "colors": [
            "7fbcd2",
            "a5f1e9",
            "e1ffee",
            "ffeeaf"
        ]
    },
    {
        "id": "16213e0f3460533483e94560",
        "tags": [
            "navy",
            "purple",
            "red",
            "dark",
            "space"
        ],
        "colors": [
            "16213e",
            "0f3460",
            "533483",
            "e94560"
        ]
    },
    {
        "id": "f5eddccfd2cffa9494eb1d36",
        "tags": [
            "beige",
            "grey",
            "peach",
            "red",
            "retro"
        ],
        "colors": [
            "f5eddc",
            "cfd2cf",
            "fa9494",
            "eb1d36"
        ]
    },
    {
        "id": "e3c770fecd70ffae6df3e0b5",
        "tags": [
            "yellow",
            "orange",
            "beige",
            "food",
            "nature",
            "warm",
            "light",
            "fall"
        ],
        "colors": [
            "e3c770",
            "fecd70",
            "ffae6d",
            "f3e0b5"
        ]
    },
    {
        "id": "fff5e4ffc4c4ee6983850e35",
        "tags": [
            "beige",
            "peach",
            "pink",
            "maroon",
            "wedding",
            "warm"
        ],
        "colors": [
            "fff5e4",
            "ffc4c4",
            "ee6983",
            "850e35"
        ]
    },
    {
        "id": "ec7272f7a76ce0d98cc3ff99",
        "tags": [
            "red",
            "orange",
            "green",
            "kids",
            "light",
            "spring",
            "gradient"
        ],
        "colors": [
            "ec7272",
            "f7a76c",
            "e0d98c",
            "c3ff99"
        ]
    },
    {
        "id": "472d2d553939704f4fa77979",
        "tags": [
            "brown",
            "dark",
            "coffee",
            "warm",
            "earth",
            "vintage",
            "halloween"
        ],
        "colors": [
            "472d2d",
            "553939",
            "704f4f",
            "a77979"
        ]
    },
    {
        "id": "fdeedcffd8a9f1a661e38b29",
        "tags": [
            "beige",
            "orange",
            "skin",
            "gold",
            "food",
            "warm",
            "fall"
        ],
        "colors": [
            "fdeedc",
            "ffd8a9",
            "f1a661",
            "e38b29"
        ]
    },
    {
        "id": "48383842855b90b77dd2d79f",
        "tags": [
            "black",
            "green",
            "night",
            "winter",
            "nature",
            "gradient"
        ],
        "colors": [
            "483838",
            "42855b",
            "90b77d",
            "d2d79f"
        ]
    },
    {
        "id": "b9fff86fedd6ff9551ff4a4a",
        "tags": [
            "mint",
            "teal",
            "orange",
            "red",
            "retro",
            "neon",
            "kids"
        ],
        "colors": [
            "b9fff8",
            "6fedd6",
            "ff9551",
            "ff4a4a"
        ]
    },
    {
        "id": "a62349d07000c5530096e5d1",
        "tags": [
            "maroon",
            "orange",
            "teal",
            "vintage",
            "christmas"
        ],
        "colors": [
            "a62349",
            "d07000",
            "c55300",
            "96e5d1"
        ]
    },
    {
        "id": "7fb77eb1d7b4f7f6dcffc090",
        "tags": [
            "green",
            "sage",
            "yellow",
            "beige",
            "orange",
            "cream",
            "light",
            "happy",
            "summer"
        ],
        "colors": [
            "7fb77e",
            "b1d7b4",
            "f7f6dc",
            "ffc090"
        ]
    },
    {
        "id": "f94892ff7f3ffbdf0789cffd",
        "tags": [
            "pink",
            "orange",
            "yellow",
            "blue",
            "rainbow",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "f94892",
            "ff7f3f",
            "fbdf07",
            "89cffd"
        ]
    },
    {
        "id": "fff38cf0e161d9cb50c0b236",
        "tags": [
            "yellow",
            "light"
        ],
        "colors": [
            "fff38c",
            "f0e161",
            "d9cb50",
            "c0b236"
        ]
    },
    {
        "id": "781c68319da0ffd39afff5e1",
        "tags": [
            "purple",
            "teal",
            "beige",
            "vintage",
            "wedding"
        ],
        "colors": [
            "781c68",
            "319da0",
            "ffd39a",
            "fff5e1"
        ]
    },
    {
        "id": "277bc0ffb200ffcb42fff4cf",
        "tags": [
            "blue",
            "orange",
            "yellow",
            "happy",
            "summer"
        ],
        "colors": [
            "277bc0",
            "ffb200",
            "ffcb42",
            "fff4cf"
        ]
    },
    {
        "id": "42032cd36b00e6d2aaf1efdc",
        "tags": [
            "black",
            "maroon",
            "orange",
            "beige",
            "gold",
            "vintage",
            "coffee",
            "skin",
            "night"
        ],
        "colors": [
            "42032c",
            "d36b00",
            "e6d2aa",
            "f1efdc"
        ]
    },
    {
        "id": "2934621cd6cefedb39d61c4e",
        "tags": [
            "navy",
            "mint",
            "yellow",
            "red",
            "neon",
            "kids"
        ],
        "colors": [
            "293462",
            "1cd6ce",
            "fedb39",
            "d61c4e"
        ]
    },
    {
        "id": "554994f675a8f29393ffccb3",
        "tags": [
            "purple",
            "pink",
            "peach",
            "pastel",
            "kids",
            "wedding"
        ],
        "colors": [
            "554994",
            "f675a8",
            "f29393",
            "ffccb3"
        ]
    },
    {
        "id": "ac4425224b0cc1d5a4f0f2b6",
        "tags": [
            "brown",
            "green",
            "sage",
            "earth",
            "food",
            "nature"
        ],
        "colors": [
            "ac4425",
            "224b0c",
            "c1d5a4",
            "f0f2b6"
        ]
    },
    {
        "id": "c21010e64848fffde3cfe8a9",
        "tags": [
            "red",
            "white",
            "green",
            "food",
            "kids",
            "summer",
            "christmas"
        ],
        "colors": [
            "c21010",
            "e64848",
            "fffde3",
            "cfe8a9"
        ]
    },
    {
        "id": "820000b9005bff7c7cfee0c0",
        "tags": [
            "maroon",
            "purple",
            "peach",
            "beige",
            "christmas",
            "wedding",
            "warm",
            "gradient",
            "sunset"
        ],
        "colors": [
            "820000",
            "b9005b",
            "ff7c7c",
            "fee0c0"
        ]
    },
    {
        "id": "f7ecdee9dac19ed2c654bab9",
        "tags": [
            "beige",
            "teal",
            "pastel",
            "cream",
            "light"
        ],
        "colors": [
            "f7ecde",
            "e9dac1",
            "9ed2c6",
            "54bab9"
        ]
    },
    {
        "id": "f65a83ff87b2ffe898fff8bc",
        "tags": [
            "red",
            "pink",
            "yellow",
            "sunset",
            "kids",
            "light"
        ],
        "colors": [
            "f65a83",
            "ff87b2",
            "ffe898",
            "fff8bc"
        ]
    },
    {
        "id": "ffb3b3ffdba4ffe9aec1efff",
        "tags": [
            "peach",
            "yellow",
            "blue",
            "pastel",
            "kids",
            "rainbow"
        ],
        "colors": [
            "ffb3b3",
            "ffdba4",
            "ffe9ae",
            "c1efff"
        ]
    },
    {
        "id": "f0eabe21e1e13b9ae13120e0",
        "tags": [
            "beige",
            "mint",
            "blue",
            "navy",
            "summer",
            "gradient"
        ],
        "colors": [
            "f0eabe",
            "21e1e1",
            "3b9ae1",
            "3120e0"
        ]
    },
    {
        "id": "2a09443fa796fec260a10035",
        "tags": [
            "navy",
            "black",
            "teal",
            "yellow",
            "maroon",
            "vintage"
        ],
        "colors": [
            "2a0944",
            "3fa796",
            "fec260",
            "a10035"
        ]
    },
    {
        "id": "002b5b2b4865256d858fe3cf",
        "tags": [
            "navy",
            "blue",
            "teal",
            "mint",
            "cold",
            "winter",
            "gradient",
            "sea"
        ],
        "colors": [
            "002b5b",
            "2b4865",
            "256d85",
            "8fe3cf"
        ]
    },
    {
        "id": "ff1e00e8f9fd59ce8f000000",
        "tags": [
            "red",
            "white",
            "green",
            "black",
            "retro"
        ],
        "colors": [
            "ff1e00",
            "e8f9fd",
            "59ce8f",
            "000000"
        ]
    },
    {
        "id": "f5e8c7ecccb2deb6abac7088",
        "tags": [
            "beige",
            "peach",
            "cream",
            "skin",
            "pastel",
            "warm",
            "earth",
            "fall"
        ],
        "colors": [
            "f5e8c7",
            "ecccb2",
            "deb6ab",
            "ac7088"
        ]
    },
    {
        "id": "a66cff9c9efeafb4ffb1e1ff",
        "tags": [
            "purple",
            "blue",
            "cold",
            "winter",
            "kids",
            "gradient"
        ],
        "colors": [
            "a66cff",
            "9c9efe",
            "afb4ff",
            "b1e1ff"
        ]
    },
    {
        "id": "1c3879607eaaeae3d2f9f5eb",
        "tags": [
            "navy",
            "blue",
            "beige",
            "winter"
        ],
        "colors": [
            "1c3879",
            "607eaa",
            "eae3d2",
            "f9f5eb"
        ]
    },
    {
        "id": "10072031087bfa2fb5ffc23c",
        "tags": [
            "black",
            "purple",
            "pink",
            "yellow",
            "space"
        ],
        "colors": [
            "100720",
            "31087b",
            "fa2fb5",
            "ffc23c"
        ]
    },
    {
        "id": "80558caf7ab3cba0aee4d192",
        "tags": [
            "purple",
            "yellow",
            "pastel",
            "vintage"
        ],
        "colors": [
            "80558c",
            "af7ab3",
            "cba0ae",
            "e4d192"
        ]
    },
    {
        "id": "fcf8e894b49fdf786176549a",
        "tags": [
            "beige",
            "teal",
            "sage",
            "orange",
            "purple",
            "vintage",
            "wedding"
        ],
        "colors": [
            "fcf8e8",
            "94b49f",
            "df7861",
            "76549a"
        ]
    },
    {
        "id": "411530d1512df5c7a9f5e8e4",
        "tags": [
            "black",
            "maroon",
            "orange",
            "beige",
            "coffee",
            "warm",
            "skin",
            "gold"
        ],
        "colors": [
            "411530",
            "d1512d",
            "f5c7a9",
            "f5e8e4"
        ]
    },
    {
        "id": "fce2dbff8fb1b270a27a4495",
        "tags": [
            "peach",
            "pink",
            "purple",
            "kids",
            "retro"
        ],
        "colors": [
            "fce2db",
            "ff8fb1",
            "b270a2",
            "7a4495"
        ]
    },
    {
        "id": "b93160d75281eed180fff89c",
        "tags": [
            "maroon",
            "pink",
            "yellow",
            "happy"
        ],
        "colors": [
            "b93160",
            "d75281",
            "eed180",
            "fff89c"
        ]
    },
    {
        "id": "eae5097dce135bb3182b7a0b",
        "tags": [
            "yellow",
            "green",
            "nature"
        ],
        "colors": [
            "eae509",
            "7dce13",
            "5bb318",
            "2b7a0b"
        ]
    },
    {
        "id": "5800ff0096ff00d7ff72ffff",
        "tags": [
            "purple",
            "blue",
            "mint",
            "neon",
            "cold",
            "gradient"
        ],
        "colors": [
            "5800ff",
            "0096ff",
            "00d7ff",
            "72ffff"
        ]
    },
    {
        "id": "100f0f0f3d3ee2dcc8f1f1f1",
        "tags": [
            "black",
            "teal",
            "beige",
            "night"
        ],
        "colors": [
            "100f0f",
            "0f3d3e",
            "e2dcc8",
            "f1f1f1"
        ]
    },
    {
        "id": "3557645a8f7b81cacfffea11",
        "tags": [
            "navy",
            "teal",
            "sage",
            "blue",
            "yellow",
            "winter"
        ],
        "colors": [
            "355764",
            "5a8f7b",
            "81cacf",
            "ffea11"
        ]
    },
    {
        "id": "76ba99876445ca955ceddfb3",
        "tags": [
            "green",
            "mint",
            "brown",
            "beige",
            "earth"
        ],
        "colors": [
            "76ba99",
            "876445",
            "ca955c",
            "eddfb3"
        ]
    },
    {
        "id": "003865ef5b0cd4f6cc3ccf4e",
        "tags": [
            "navy",
            "orange",
            "green",
            "retro"
        ],
        "colors": [
            "003865",
            "ef5b0c",
            "d4f6cc",
            "3ccf4e"
        ]
    },
    {
        "id": "fefbf6a6d1e67f52833d3c42",
        "tags": [
            "white",
            "blue",
            "purple",
            "black",
            "vintage"
        ],
        "colors": [
            "fefbf6",
            "a6d1e6",
            "7f5283",
            "3d3c42"
        ]
    },
    {
        "id": "2c3333395b64a5c9cae7f6f2",
        "tags": [
            "dark",
            "black",
            "navy",
            "teal",
            "cold",
            "night",
            "gradient",
            "sea"
        ],
        "colors": [
            "2c3333",
            "395b64",
            "a5c9ca",
            "e7f6f2"
        ]
    },
    {
        "id": "fff9caffdeb4ffb4b4b2a4ff",
        "tags": [
            "yellow",
            "peach",
            "purple",
            "light",
            "cream",
            "kids",
            "happy",
            "summer",
            "spring",
            "warm",
            "rainbow"
        ],
        "colors": [
            "fff9ca",
            "ffdeb4",
            "ffb4b4",
            "b2a4ff"
        ]
    },
    {
        "id": "61481ca47e3bbf9742e6b325",
        "tags": [
            "brown",
            "yellow",
            "skin",
            "gold",
            "earth",
            "food",
            "warm",
            "nature",
            "coffee"
        ],
        "colors": [
            "61481c",
            "a47e3b",
            "bf9742",
            "e6b325"
        ]
    },
    {
        "id": "0078aa3ab4f2f2df3af6f6f6",
        "tags": [
            "blue",
            "yellow",
            "grey",
            "kids",
            "summer"
        ],
        "colors": [
            "0078aa",
            "3ab4f2",
            "f2df3a",
            "f6f6f6"
        ]
    },
    {
        "id": "293462d61c4efeb139fff80a",
        "tags": [
            "navy",
            "red",
            "orange",
            "yellow",
            "sunset",
            "gradient"
        ],
        "colors": [
            "293462",
            "d61c4e",
            "feb139",
            "fff80a"
        ]
    },
    {
        "id": "5132527a4069ca4e79ffc18e",
        "tags": [
            "purple",
            "maroon",
            "orange",
            "sunset",
            "warm",
            "wedding",
            "gradient",
            "sky"
        ],
        "colors": [
            "513252",
            "7a4069",
            "ca4e79",
            "ffc18e"
        ]
    },
    {
        "id": "94b49fcee5d0fcf8e8ecb390",
        "tags": [
            "sage",
            "mint",
            "beige",
            "orange",
            "cream",
            "earth",
            "light"
        ],
        "colors": [
            "94b49f",
            "cee5d0",
            "fcf8e8",
            "ecb390"
        ]
    },
    {
        "id": "2319551f4690e8aa42ffe5b4",
        "tags": [
            "navy",
            "blue",
            "orange",
            "winter"
        ],
        "colors": [
            "231955",
            "1f4690",
            "e8aa42",
            "ffe5b4"
        ]
    },
    {
        "id": "ccd6a6dae2b6dfe8ccf7eddb",
        "tags": [
            "green",
            "sage",
            "beige",
            "light",
            "cream",
            "spring",
            "nature"
        ],
        "colors": [
            "ccd6a6",
            "dae2b6",
            "dfe8cc",
            "f7eddb"
        ]
    },
    {
        "id": "495c837a86b6a8a4cec8b6e2",
        "tags": [
            "blue",
            "purple",
            "night",
            "cold",
            "gradient"
        ],
        "colors": [
            "495c83",
            "7a86b6",
            "a8a4ce",
            "c8b6e2"
        ]
    },
    {
        "id": "f5eddccfd2cfa2b5bbeb1d36",
        "tags": [
            "beige",
            "grey",
            "red",
            "retro"
        ],
        "colors": [
            "f5eddc",
            "cfd2cf",
            "a2b5bb",
            "eb1d36"
        ]
    },
    {
        "id": "d9f8c4f9f9c5fad9a1f37878",
        "tags": [
            "green",
            "yellow",
            "orange",
            "red",
            "light",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "d9f8c4",
            "f9f9c5",
            "fad9a1",
            "f37878"
        ]
    },
    {
        "id": "6e85b7b2c8dfc4d7e0f8f9d7",
        "tags": [
            "blue",
            "yellow",
            "light",
            "pastel",
            "sky"
        ],
        "colors": [
            "6e85b7",
            "b2c8df",
            "c4d7e0",
            "f8f9d7"
        ]
    },
    {
        "id": "898aa6c9bbcfb7d3dfd6efed",
        "tags": [
            "purple",
            "blue",
            "teal",
            "pastel"
        ],
        "colors": [
            "898aa6",
            "c9bbcf",
            "b7d3df",
            "d6efed"
        ]
    },
    {
        "id": "66bfbfeaf6f6ffffffff0063",
        "tags": [
            "teal",
            "white",
            "red"
        ],
        "colors": [
            "66bfbf",
            "eaf6f6",
            "ffffff",
            "ff0063"
        ]
    },
    {
        "id": "abc9ffffdedeff8b8beb4747",
        "tags": [
            "blue",
            "peach",
            "red",
            "kids"
        ],
        "colors": [
            "abc9ff",
            "ffdede",
            "ff8b8b",
            "eb4747"
        ]
    },
    {
        "id": "3330e4f637ecfbb454faea48",
        "tags": [
            "blue",
            "purple",
            "orange",
            "yellow",
            "neon",
            "kids"
        ],
        "colors": [
            "3330e4",
            "f637ec",
            "fbb454",
            "faea48"
        ]
    },
    {
        "id": "f5f0bbc4dfaa90c8ac73a9ad",
        "tags": [
            "yellow",
            "green",
            "teal",
            "blue",
            "nature",
            "cold",
            "pastel",
            "summer",
            "happy"
        ],
        "colors": [
            "f5f0bb",
            "c4dfaa",
            "90c8ac",
            "73a9ad"
        ]
    },
    {
        "id": "377d71fbc5c5fba1a18879b0",
        "tags": [
            "teal",
            "pink",
            "purple",
            "food",
            "vintage"
        ],
        "colors": [
            "377d71",
            "fbc5c5",
            "fba1a1",
            "8879b0"
        ]
    },
    {
        "id": "f0ebe3e4dccf7d9d9c576f72",
        "tags": [
            "beige",
            "grey",
            "teal",
            "vintage",
            "pastel"
        ],
        "colors": [
            "f0ebe3",
            "e4dccf",
            "7d9d9c",
            "576f72"
        ]
    },
    {
        "id": "937dc2c689c6e8a0bffcc5c0",
        "tags": [
            "purple",
            "pink",
            "peach",
            "wedding",
            "sky"
        ],
        "colors": [
            "937dc2",
            "c689c6",
            "e8a0bf",
            "fcc5c0"
        ]
    },
    {
        "id": "ffe7bfffc4c4ff869ea10035",
        "tags": [
            "yellow",
            "peach",
            "pink",
            "maroon",
            "warm",
            "kids"
        ],
        "colors": [
            "ffe7bf",
            "ffc4c4",
            "ff869e",
            "a10035"
        ]
    },
    {
        "id": "2c36393f4e4fa27b5cdcd7c9",
        "tags": [
            "navy",
            "brown",
            "earth",
            "warm",
            "nature",
            "fall",
            "coffee",
            "dark",
            "vintage",
            "night"
        ],
        "colors": [
            "2c3639",
            "3f4e4f",
            "a27b5c",
            "dcd7c9"
        ]
    },
    {
        "id": "610c63810955ee81b3fff9d7",
        "tags": [
            "purple",
            "maroon",
            "pink",
            "yellow",
            "space",
            "sunset",
            "gradient"
        ],
        "colors": [
            "610c63",
            "810955",
            "ee81b3",
            "fff9d7"
        ]
    },
    {
        "id": "f2d7d9d3cedf9cb4cc748da6",
        "tags": [
            "peach",
            "grey",
            "blue",
            "pastel",
            "cream",
            "light",
            "sky"
        ],
        "colors": [
            "f2d7d9",
            "d3cedf",
            "9cb4cc",
            "748da6"
        ]
    },
    {
        "id": "0000001a4d2eff9f29faf3e3",
        "tags": [
            "black",
            "green",
            "orange",
            "beige",
            "space",
            "retro"
        ],
        "colors": [
            "000000",
            "1a4d2e",
            "ff9f29",
            "faf3e3"
        ]
    },
    {
        "id": "54bab918978fe9dac1f7ecde",
        "tags": [
            "teal",
            "beige",
            "vintage"
        ],
        "colors": [
            "54bab9",
            "18978f",
            "e9dac1",
            "f7ecde"
        ]
    },
    {
        "id": "dfbb9df7e2d69dd6dfa084cf",
        "tags": [
            "brown",
            "beige",
            "teal",
            "purple",
            "vintage",
            "kids",
            "wedding"
        ],
        "colors": [
            "dfbb9d",
            "f7e2d6",
            "9dd6df",
            "a084cf"
        ]
    },
    {
        "id": "76ba99adcf9fced89effdcae",
        "tags": [
            "green",
            "beige",
            "spring",
            "nature",
            "summer",
            "light",
            "happy"
        ],
        "colors": [
            "76ba99",
            "adcf9f",
            "ced89e",
            "ffdcae"
        ]
    },
    {
        "id": "87805eb09b71d8cca3eddfb3",
        "tags": [
            "brown",
            "beige",
            "coffee",
            "warm",
            "skin",
            "vintage",
            "food",
            "earth",
            "cream"
        ],
        "colors": [
            "87805e",
            "b09b71",
            "d8cca3",
            "eddfb3"
        ]
    },
    {
        "id": "ff7396f4e06dffffdec499ba",
        "tags": [
            "pink",
            "yellow",
            "purple",
            "light",
            "spring",
            "happy",
            "kids"
        ],
        "colors": [
            "ff7396",
            "f4e06d",
            "ffffde",
            "c499ba"
        ]
    },
    {
        "id": "4c3a51774360b25068e7ab79",
        "tags": [
            "black",
            "maroon",
            "red",
            "orange",
            "dark",
            "warm",
            "sunset",
            "halloween",
            "skin"
        ],
        "colors": [
            "4c3a51",
            "774360",
            "b25068",
            "e7ab79"
        ]
    },
    {
        "id": "f9f2ed3ab0ffffb562f87474",
        "tags": [
            "white",
            "beige",
            "blue",
            "orange",
            "red",
            "kids",
            "happy",
            "retro"
        ],
        "colors": [
            "f9f2ed",
            "3ab0ff",
            "ffb562",
            "f87474"
        ]
    },
    {
        "id": "f7ec093ec70b3b44f6a149fa",
        "tags": [
            "yellow",
            "green",
            "blue",
            "purple",
            "neon",
            "kids"
        ],
        "colors": [
            "f7ec09",
            "3ec70b",
            "3b44f6",
            "a149fa"
        ]
    },
    {
        "id": "f6e3c5a0d9956cc4a14cacbc",
        "tags": [
            "beige",
            "green",
            "teal",
            "blue",
            "nature",
            "vintage",
            "kids",
            "summer"
        ],
        "colors": [
            "f6e3c5",
            "a0d995",
            "6cc4a1",
            "4cacbc"
        ]
    },
    {
        "id": "53bf9df94c66bd4291ffc54d",
        "tags": [
            "teal",
            "red",
            "purple",
            "yellow",
            "kids",
            "happy",
            "rainbow"
        ],
        "colors": [
            "53bf9d",
            "f94c66",
            "bd4291",
            "ffc54d"
        ]
    },
    {
        "id": "1b243051557e816797d6d5a8",
        "tags": [
            "black",
            "navy",
            "purple",
            "beige",
            "night",
            "dark",
            "vintage"
        ],
        "colors": [
            "1b2430",
            "51557e",
            "816797",
            "d6d5a8"
        ]
    },
    {
        "id": "d3ebcdaedbce839aa8635666",
        "tags": [
            "green",
            "mint",
            "teal",
            "winter",
            "cold"
        ],
        "colors": [
            "d3ebcd",
            "aedbce",
            "839aa8",
            "635666"
        ]
    },
    {
        "id": "fcf8e894b49fecb390df7861",
        "tags": [
            "white",
            "beige",
            "sage",
            "peach",
            "orange",
            "food",
            "vintage",
            "wedding",
            "fall"
        ],
        "colors": [
            "fcf8e8",
            "94b49f",
            "ecb390",
            "df7861"
        ]
    },
    {
        "id": "06283d1363df47b5ffdff6ff",
        "tags": [
            "navy",
            "blue",
            "space",
            "winter",
            "cold",
            "gradient",
            "sky"
        ],
        "colors": [
            "06283d",
            "1363df",
            "47b5ff",
            "dff6ff"
        ]
    },
    {
        "id": "1f46903a5ba0ffa500ffe5b4",
        "tags": [
            "navy",
            "orange",
            "beige",
            "kids"
        ],
        "colors": [
            "1f4690",
            "3a5ba0",
            "ffa500",
            "ffe5b4"
        ]
    },
    {
        "id": "f1541200000034b3f1eeeeee",
        "tags": [
            "red",
            "black",
            "blue",
            "grey",
            "space"
        ],
        "colors": [
            "f15412",
            "000000",
            "34b3f1",
            "eeeeee"
        ]
    },
    {
        "id": "9eb23bc7d36ffcf9c6e0deca",
        "tags": [
            "green",
            "yellow",
            "grey",
            "nature",
            "happy",
            "light",
            "food"
        ],
        "colors": [
            "9eb23b",
            "c7d36f",
            "fcf9c6",
            "e0deca"
        ]
    },
    {
        "id": "cdf0eaf9f9f9f6c6eafaf4b7",
        "tags": [
            "teal",
            "white",
            "pink",
            "yellow",
            "light",
            "cream",
            "happy",
            "kids",
            "rainbow",
            "pastel",
            "spring"
        ],
        "colors": [
            "cdf0ea",
            "f9f9f9",
            "f6c6ea",
            "faf4b7"
        ]
    },
    {
        "id": "ffe6e6f2d1d1daeaf1c6dce4",
        "tags": [
            "pink",
            "peach",
            "blue",
            "pastel",
            "skin",
            "light",
            "kids"
        ],
        "colors": [
            "ffe6e6",
            "f2d1d1",
            "daeaf1",
            "c6dce4"
        ]
    },
    {
        "id": "bdf2d54b5d673c2c3eff06b7",
        "tags": [
            "mint",
            "navy",
            "pink",
            "retro"
        ],
        "colors": [
            "bdf2d5",
            "4b5d67",
            "3c2c3e",
            "ff06b7"
        ]
    },
    {
        "id": "f6fbf4f5df995fd0684b8673",
        "tags": [
            "white",
            "yellow",
            "green",
            "nature"
        ],
        "colors": [
            "f6fbf4",
            "f5df99",
            "5fd068",
            "4b8673"
        ]
    },
    {
        "id": "990000ff5b00d4d925ffee63",
        "tags": [
            "maroon",
            "red",
            "orange",
            "green",
            "yellow",
            "gold",
            "food",
            "warm",
            "christmas",
            "halloween"
        ],
        "colors": [
            "990000",
            "ff5b00",
            "d4d925",
            "ffee63"
        ]
    },
    {
        "id": "7c3e66f2ebe9a5becc243a73",
        "tags": [
            "maroon",
            "beige",
            "blue",
            "navy",
            "vintage",
            "wedding"
        ],
        "colors": [
            "7c3e66",
            "f2ebe9",
            "a5becc",
            "243a73"
        ]
    },
    {
        "id": "fef9a7fac213f77e21d61c4e",
        "tags": [
            "yellow",
            "orange",
            "red",
            "summer",
            "sunset",
            "warm",
            "gold"
        ],
        "colors": [
            "fef9a7",
            "fac213",
            "f77e21",
            "d61c4e"
        ]
    },
    {
        "id": "37e2d5590696c70a80fbcb0a",
        "tags": [
            "mint",
            "purple",
            "maroon",
            "yellow",
            "rainbow",
            "kids",
            "retro",
            "neon"
        ],
        "colors": [
            "37e2d5",
            "590696",
            "c70a80",
            "fbcb0a"
        ]
    },
    {
        "id": "ffcc8fffdaafa760ffca82ff",
        "tags": [
            "beige",
            "purple",
            "retro",
            "happy"
        ],
        "colors": [
            "ffcc8f",
            "ffdaaf",
            "a760ff",
            "ca82ff"
        ]
    },
    {
        "id": "371b584c35755b4b8a7858a6",
        "tags": [
            "navy",
            "purple",
            "night",
            "dark",
            "halloween",
            "cold"
        ],
        "colors": [
            "371b58",
            "4c3575",
            "5b4b8a",
            "7858a6"
        ]
    },
    {
        "id": "c2ded1ece5c7cdc2ae354259",
        "tags": [
            "mint",
            "teal",
            "beige",
            "navy",
            "pastel",
            "cream",
            "light",
            "wedding",
            "vintage"
        ],
        "colors": [
            "c2ded1",
            "ece5c7",
            "cdc2ae",
            "354259"
        ]
    },
    {
        "id": "f47c7cef9f9ffad4d4fff2f2",
        "tags": [
            "red",
            "peach",
            "light",
            "cream",
            "food",
            "skin",
            "kids"
        ],
        "colors": [
            "f47c7c",
            "ef9f9f",
            "fad4d4",
            "fff2f2"
        ]
    },
    {
        "id": "e9d5ca8273974d4c7d363062",
        "tags": [
            "beige",
            "purple",
            "navy",
            "night",
            "vintage",
            "wedding",
            "gradient"
        ],
        "colors": [
            "e9d5ca",
            "827397",
            "4d4c7d",
            "363062"
        ]
    },
    {
        "id": "293462f24c4cec9b3bf7d716",
        "tags": [
            "navy",
            "red",
            "orange",
            "yellow",
            "rainbow",
            "sunset"
        ],
        "colors": [
            "293462",
            "f24c4c",
            "ec9b3b",
            "f7d716"
        ]
    },
    {
        "id": "ffe3a9ffc3c3ff8c8cff5d5d",
        "tags": [
            "yellow",
            "peach",
            "red",
            "summer",
            "happy",
            "kids",
            "light",
            "warm",
            "spring"
        ],
        "colors": [
            "ffe3a9",
            "ffc3c3",
            "ff8c8c",
            "ff5d5d"
        ]
    },
    {
        "id": "809a6fa25b5bcc9c75d5d8b5",
        "tags": [
            "sage",
            "maroon",
            "beige",
            "fall",
            "earth",
            "summer",
            "vintage",
            "nature"
        ],
        "colors": [
            "809a6f",
            "a25b5b",
            "cc9c75",
            "d5d8b5"
        ]
    },
    {
        "id": "242f9b646fd49ba3ebdbdffd",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter"
        ],
        "colors": [
            "242f9b",
            "646fd4",
            "9ba3eb",
            "dbdffd"
        ]
    },
    {
        "id": "f4bfbfffd9c0faf0d78cc0de",
        "tags": [
            "peach",
            "beige",
            "yellow",
            "blue",
            "cream",
            "pastel",
            "light",
            "kids",
            "happy",
            "summer"
        ],
        "colors": [
            "f4bfbf",
            "ffd9c0",
            "faf0d7",
            "8cc0de"
        ]
    },
    {
        "id": "00ffab14c38eb8f1b0e3fcbf",
        "tags": [
            "mint",
            "green",
            "neon",
            "kids",
            "light"
        ],
        "colors": [
            "00ffab",
            "14c38e",
            "b8f1b0",
            "e3fcbf"
        ]
    },
    {
        "id": "92b4ecffffffffe69affd24c",
        "tags": [
            "blue",
            "white",
            "yellow",
            "summer",
            "light",
            "happy"
        ],
        "colors": [
            "92b4ec",
            "ffffff",
            "ffe69a",
            "ffd24c"
        ]
    },
    {
        "id": "2e0249570a57a91079f806cc",
        "tags": [
            "black",
            "purple",
            "pink",
            "neon",
            "space",
            "dark",
            "sky"
        ],
        "colors": [
            "2e0249",
            "570a57",
            "a91079",
            "f806cc"
        ]
    },
    {
        "id": "9a86a4b1bce6b7e5ddf1f0c0",
        "tags": [
            "purple",
            "blue",
            "teal",
            "mint",
            "yellow",
            "pastel",
            "earth",
            "vintage",
            "light"
        ],
        "colors": [
            "9a86a4",
            "b1bce6",
            "b7e5dd",
            "f1f0c0"
        ]
    },
    {
        "id": "2f8f9d3bacb682dbd8b3e8e5",
        "tags": [
            "teal",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "2f8f9d",
            "3bacb6",
            "82dbd8",
            "b3e8e5"
        ]
    },
    {
        "id": "f73d9316003b413f427f8487",
        "tags": [
            "pink",
            "black",
            "grey",
            "retro",
            "dark",
            "space"
        ],
        "colors": [
            "f73d93",
            "16003b",
            "413f42",
            "7f8487"
        ]
    },
    {
        "id": "7d1e6aeeb0b0ffe59dbde6f1",
        "tags": [
            "purple",
            "peach",
            "yellow",
            "blue",
            "kids",
            "vintage",
            "retro",
            "wedding"
        ],
        "colors": [
            "7d1e6a",
            "eeb0b0",
            "ffe59d",
            "bde6f1"
        ]
    },
    {
        "id": "6a67ce947ec3b689c0eef3d2",
        "tags": [
            "blue",
            "purple",
            "yellow",
            "wedding",
            "retro"
        ],
        "colors": [
            "6a67ce",
            "947ec3",
            "b689c0",
            "eef3d2"
        ]
    },
    {
        "id": "15133c73777bec994bf1eee9",
        "tags": [
            "black",
            "grey",
            "orange",
            "vintage",
            "gold"
        ],
        "colors": [
            "15133c",
            "73777b",
            "ec994b",
            "f1eee9"
        ]
    },
    {
        "id": "5f71616d8b74efead8d0c9c0",
        "tags": [
            "green",
            "sage",
            "beige",
            "grey",
            "earth",
            "nature",
            "pastel",
            "vintage"
        ],
        "colors": [
            "5f7161",
            "6d8b74",
            "efead8",
            "d0c9c0"
        ]
    },
    {
        "id": "f9ceeef9f3eeccf3ee97c4b8",
        "tags": [
            "pink",
            "beige",
            "white",
            "teal",
            "pastel",
            "light",
            "kids",
            "cream",
            "spring",
            "vintage",
            "wedding"
        ],
        "colors": [
            "f9ceee",
            "f9f3ee",
            "ccf3ee",
            "97c4b8"
        ]
    },
    {
        "id": "541690ff4949ff8d29ffcd38",
        "tags": [
            "purple",
            "red",
            "orange",
            "yellow",
            "neon",
            "kids",
            "gradient"
        ],
        "colors": [
            "541690",
            "ff4949",
            "ff8d29",
            "ffcd38"
        ]
    },
    {
        "id": "764af19772fbf2f2f2f32424",
        "tags": [
            "purple",
            "grey",
            "red",
            "space",
            "retro"
        ],
        "colors": [
            "764af1",
            "9772fb",
            "f2f2f2",
            "f32424"
        ]
    },
    {
        "id": "eb5353f9d92336ae7c187498",
        "tags": [
            "red",
            "yellow",
            "green",
            "blue",
            "rainbow",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "eb5353",
            "f9d923",
            "36ae7c",
            "187498"
        ]
    },
    {
        "id": "ffef82efd345babd4282954b",
        "tags": [
            "yellow",
            "green",
            "nature",
            "summer",
            "food",
            "vintage"
        ],
        "colors": [
            "ffef82",
            "efd345",
            "babd42",
            "82954b"
        ]
    },
    {
        "id": "68a7ad99c4c8e5cb9feee4ab",
        "tags": [
            "teal",
            "blue",
            "beige",
            "winter",
            "pastel",
            "kids",
            "sky"
        ],
        "colors": [
            "68a7ad",
            "99c4c8",
            "e5cb9f",
            "eee4ab"
        ]
    },
    {
        "id": "e8f9fd79dae80aa1dd2155cd",
        "tags": [
            "blue",
            "cold",
            "sky"
        ],
        "colors": [
            "e8f9fd",
            "79dae8",
            "0aa1dd",
            "2155cd"
        ]
    },
    {
        "id": "112b3c205375f66b0eefefef",
        "tags": [
            "orange",
            "navy",
            "blue",
            "grey",
            "winter"
        ],
        "colors": [
            "112b3c",
            "205375",
            "f66b0e",
            "efefef"
        ]
    },
    {
        "id": "c4ddff7fb5ff001d6efee2c5",
        "tags": [
            "blue",
            "navy",
            "beige",
            "winter",
            "cold"
        ],
        "colors": [
            "c4ddff",
            "7fb5ff",
            "001d6e",
            "fee2c5"
        ]
    },
    {
        "id": "f9ebc8fefbe7dae5d0a0bcc2",
        "tags": [
            "yellow",
            "beige",
            "pastel",
            "light",
            "cream",
            "vintage"
        ],
        "colors": [
            "f9ebc8",
            "fefbe7",
            "dae5d0",
            "a0bcc2"
        ]
    },
    {
        "id": "251d3a2a2550e04d01ff7700",
        "tags": [
            "black",
            "navy",
            "orange",
            "space"
        ],
        "colors": [
            "251d3a",
            "2a2550",
            "e04d01",
            "ff7700"
        ]
    },
    {
        "id": "006e7ff8cb2eee5007b22727",
        "tags": [
            "teal",
            "yellow",
            "red",
            "maroon",
            "retro",
            "kids"
        ],
        "colors": [
            "006e7f",
            "f8cb2e",
            "ee5007",
            "b22727"
        ]
    },
    {
        "id": "446a4682a284e4aec5ffc4dd",
        "tags": [
            "green",
            "sage",
            "pink",
            "food",
            "nature",
            "christmas"
        ],
        "colors": [
            "446a46",
            "82a284",
            "e4aec5",
            "ffc4dd"
        ]
    },
    {
        "id": "e0d8b0fcffe7dea057ce9461",
        "tags": [
            "beige",
            "white",
            "orange",
            "coffee",
            "warm",
            "skin",
            "gold",
            "food",
            "vintage"
        ],
        "colors": [
            "e0d8b0",
            "fcffe7",
            "dea057",
            "ce9461"
        ]
    },
    {
        "id": "f8ecd1deb6abac7d8885586f",
        "tags": [
            "beige",
            "peach",
            "purple",
            "vintage",
            "pastel",
            "coffee",
            "skin",
            "gradient"
        ],
        "colors": [
            "f8ecd1",
            "deb6ab",
            "ac7d88",
            "85586f"
        ]
    },
    {
        "id": "ab46d2ff6fb555d8c1fcf69c",
        "tags": [
            "purple",
            "pink",
            "teal",
            "yellow",
            "kids",
            "happy",
            "rainbow"
        ],
        "colors": [
            "ab46d2",
            "ff6fb5",
            "55d8c1",
            "fcf69c"
        ]
    },
    {
        "id": "a85cf95534a54b7be56fdfdf",
        "tags": [
            "purple",
            "blue",
            "teal",
            "cold"
        ],
        "colors": [
            "a85cf9",
            "5534a5",
            "4b7be5",
            "6fdfdf"
        ]
    },
    {
        "id": "b4ff9ff9ffa4ffd59effa1a1",
        "tags": [
            "green",
            "yellow",
            "orange",
            "peach",
            "rainbow",
            "spring",
            "happy",
            "light"
        ],
        "colors": [
            "b4ff9f",
            "f9ffa4",
            "ffd59e",
            "ffa1a1"
        ]
    },
    {
        "id": "e9efc0b4e19783bd754e944f",
        "tags": [
            "green",
            "nature"
        ],
        "colors": [
            "e9efc0",
            "b4e197",
            "83bd75",
            "4e944f"
        ]
    },
    {
        "id": "005555069a8ea1e3d8f7ff93",
        "tags": [
            "teal",
            "blue",
            "yellow",
            "cold",
            "gradient",
            "sea"
        ],
        "colors": [
            "005555",
            "069a8e",
            "a1e3d8",
            "f7ff93"
        ]
    },
    {
        "id": "125b50f8b400faf5e4ff6363",
        "tags": [
            "teal",
            "orange",
            "white",
            "red",
            "vintage"
        ],
        "colors": [
            "125b50",
            "f8b400",
            "faf5e4",
            "ff6363"
        ]
    },
    {
        "id": "ede6db417d7a1d5c631a3c40",
        "tags": [
            "beige",
            "teal",
            "vintage",
            "wedding"
        ],
        "colors": [
            "ede6db",
            "417d7a",
            "1d5c63",
            "1a3c40"
        ]
    },
    {
        "id": "e9d5da8273974d4c7d363062",
        "tags": [
            "purple",
            "navy",
            "vintage",
            "winter",
            "night",
            "space"
        ],
        "colors": [
            "e9d5da",
            "827397",
            "4d4c7d",
            "363062"
        ]
    },
    {
        "id": "001e6c035397e8630afcd900",
        "tags": [
            "navy",
            "blue",
            "orange",
            "yellow",
            "space"
        ],
        "colors": [
            "001e6c",
            "035397",
            "e8630a",
            "fcd900"
        ]
    },
    {
        "id": "8e3200a64b2ad7a86effebc1",
        "tags": [
            "maroon",
            "brown",
            "beige",
            "coffee",
            "skin",
            "earth",
            "vintage",
            "gold",
            "warm",
            "gradient"
        ],
        "colors": [
            "8e3200",
            "a64b2a",
            "d7a86e",
            "ffebc1"
        ]
    },
    {
        "id": "40dfefb9f8d3fffbe7e78ea9",
        "tags": [
            "blue",
            "mint",
            "beige",
            "red",
            "kids",
            "happy",
            "light"
        ],
        "colors": [
            "40dfef",
            "b9f8d3",
            "fffbe7",
            "e78ea9"
        ]
    },
    {
        "id": "383838066163cdbe78f2f2f2",
        "tags": [
            "black",
            "teal",
            "yellow",
            "grey",
            "vintage"
        ],
        "colors": [
            "383838",
            "066163",
            "cdbe78",
            "f2f2f2"
        ]
    },
    {
        "id": "143f6bf55353feb139f6f54d",
        "tags": [
            "navy",
            "red",
            "orange",
            "yellow",
            "sunset",
            "neon",
            "gradient"
        ],
        "colors": [
            "143f6b",
            "f55353",
            "feb139",
            "f6f54d"
        ]
    },
    {
        "id": "9fc088e8c07dcc704b614124",
        "tags": [
            "green",
            "orange",
            "brown",
            "food",
            "earth",
            "warm",
            "nature",
            "fall"
        ],
        "colors": [
            "9fc088",
            "e8c07d",
            "cc704b",
            "614124"
        ]
    },
    {
        "id": "06113cff8c32ddddddeeeeee",
        "tags": [
            "black",
            "orange",
            "grey",
            "space"
        ],
        "colors": [
            "06113c",
            "ff8c32",
            "dddddd",
            "eeeeee"
        ]
    },
    {
        "id": "e6ba95fafdd6e4e9bea2b38b",
        "tags": [
            "peach",
            "beige",
            "green",
            "sage",
            "vintage",
            "nature",
            "pastel",
            "light",
            "cream",
            "wedding"
        ],
        "colors": [
            "e6ba95",
            "fafdd6",
            "e4e9be",
            "a2b38b"
        ]
    },
    {
        "id": "ff5f00b2060000092ceeeeee",
        "tags": [
            "orange",
            "red",
            "maroon",
            "black",
            "grey",
            "space",
            "gold"
        ],
        "colors": [
            "ff5f00",
            "b20600",
            "00092c",
            "eeeeee"
        ]
    },
    {
        "id": "f1ddbf525e7578938a92ba92",
        "tags": [
            "beige",
            "navy",
            "green",
            "retro",
            "pastel"
        ],
        "colors": [
            "f1ddbf",
            "525e75",
            "78938a",
            "92ba92"
        ]
    },
    {
        "id": "ffeeeefff6eaf7e9d7ebd8c3",
        "tags": [
            "pink",
            "beige",
            "kids",
            "skin",
            "light",
            "cream"
        ],
        "colors": [
            "ffeeee",
            "fff6ea",
            "f7e9d7",
            "ebd8c3"
        ]
    },
    {
        "id": "4700d89900f0f900bfff85b3",
        "tags": [
            "blue",
            "purple",
            "pink",
            "peach",
            "neon",
            "happy",
            "gradient"
        ],
        "colors": [
            "4700d8",
            "9900f0",
            "f900bf",
            "ff85b3"
        ]
    },
    {
        "id": "24788143919b30aadd00ffc6",
        "tags": [],
        "colors": [
            "247881",
            "43919b",
            "30aadd",
            "00ffc6"
        ]
    },
    {
        "id": "ffd36efff56d99ffcd9fb4ff",
        "tags": [
            "beige",
            "orange",
            "yellow",
            "mint",
            "blue",
            "summer",
            "happy",
            "neon"
        ],
        "colors": [
            "ffd36e",
            "fff56d",
            "99ffcd",
            "9fb4ff"
        ]
    },
    {
        "id": "0067780093ab00afc1ffd124",
        "tags": [
            "teal",
            "yellow",
            "cold"
        ],
        "colors": [
            "006778",
            "0093ab",
            "00afc1",
            "ffd124"
        ]
    },
    {
        "id": "22577e5584ac95d1ccfaffaf",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "winter",
            "cold",
            "sky",
            "sea"
        ],
        "colors": [
            "22577e",
            "5584ac",
            "95d1cc",
            "faffaf"
        ]
    },
    {
        "id": "333c83f24a72fdaf75eaea7f",
        "tags": [
            "navy",
            "red",
            "orange",
            "yellow",
            "rainbow",
            "kids",
            "gradient"
        ],
        "colors": [
            "333c83",
            "f24a72",
            "fdaf75",
            "eaea7f"
        ]
    },
    {
        "id": "8fbdd3e4d1b9be8c63a97155",
        "tags": [
            "blue",
            "beige",
            "brown",
            "vintage",
            "nature",
            "earth",
            "pastel",
            "fall"
        ],
        "colors": [
            "8fbdd3",
            "e4d1b9",
            "be8c63",
            "a97155"
        ]
    },
    {
        "id": "b6ffcef6ffa4fdd7aaffa8a8",
        "tags": [
            "mint",
            "green",
            "yellow",
            "peach",
            "red",
            "happy",
            "light",
            "spring"
        ],
        "colors": [
            "b6ffce",
            "f6ffa4",
            "fdd7aa",
            "ffa8a8"
        ]
    },
    {
        "id": "8d8daadfdfdef7f5f2f56d91",
        "tags": [
            "grey",
            "white",
            "red",
            "retro"
        ],
        "colors": [
            "8d8daa",
            "dfdfde",
            "f7f5f2",
            "f56d91"
        ]
    },
    {
        "id": "733c3c8479e1b4ece3fff8d5",
        "tags": [
            "brown",
            "blue",
            "mint",
            "yellow",
            "vintage"
        ],
        "colors": [
            "733c3c",
            "8479e1",
            "b4ece3",
            "fff8d5"
        ]
    },
    {
        "id": "fd5d5dff8080fff7bcc0eda6",
        "tags": [
            "red",
            "peach",
            "yellow",
            "green",
            "spring",
            "happy",
            "kids",
            "light",
            "food"
        ],
        "colors": [
            "fd5d5d",
            "ff8080",
            "fff7bc",
            "c0eda6"
        ]
    },
    {
        "id": "fbd6d2f190b7ce49bfa63ec5",
        "tags": [
            "beige",
            "peach",
            "pink",
            "purple",
            "wedding",
            "sunset",
            "gradient"
        ],
        "colors": [
            "fbd6d2",
            "f190b7",
            "ce49bf",
            "a63ec5"
        ]
    },
    {
        "id": "ff6b6bffd93d6bcb774d96ff",
        "tags": [
            "red",
            "yellow",
            "green",
            "blue",
            "rainbow",
            "kids"
        ],
        "colors": [
            "ff6b6b",
            "ffd93d",
            "6bcb77",
            "4d96ff"
        ]
    },
    {
        "id": "3a3845f7ccacc69b7b826f66",
        "tags": [
            "black",
            "beige",
            "brown",
            "vintage",
            "night",
            "coffee",
            "skin",
            "warm"
        ],
        "colors": [
            "3a3845",
            "f7ccac",
            "c69b7b",
            "826f66"
        ]
    },
    {
        "id": "fad9e6e4aec55f7464243d25",
        "tags": [
            "pink",
            "green",
            "nature",
            "wedding"
        ],
        "colors": [
            "fad9e6",
            "e4aec5",
            "5f7464",
            "243d25"
        ]
    },
    {
        "id": "46244c712b75c74b50d49b54",
        "tags": [
            "purple",
            "red",
            "yellow",
            "dark",
            "night",
            "warm",
            "gradient"
        ],
        "colors": [
            "46244c",
            "712b75",
            "c74b50",
            "d49b54"
        ]
    },
    {
        "id": "557b8339aea9a2d5abe5efc1",
        "tags": [
            "teal",
            "green",
            "cold",
            "gradient"
        ],
        "colors": [
            "557b83",
            "39aea9",
            "a2d5ab",
            "e5efc1"
        ]
    },
    {
        "id": "f7e2e261a4bc5b7db11a132f",
        "tags": [
            "peach",
            "blue",
            "black",
            "cold",
            "vintage"
        ],
        "colors": [
            "f7e2e2",
            "61a4bc",
            "5b7db1",
            "1a132f"
        ]
    },
    {
        "id": "97dbaec3e5aef1e1a6f4bbbb",
        "tags": [
            "green",
            "yellow",
            "beige",
            "peach",
            "spring",
            "summer",
            "light"
        ],
        "colors": [
            "97dbae",
            "c3e5ae",
            "f1e1a6",
            "f4bbbb"
        ]
    },
    {
        "id": "dab88bf3e9ddfdf6ecb7cadb",
        "tags": [
            "beige",
            "blue",
            "cream",
            "pastel",
            "coffee",
            "fall",
            "gold",
            "skin"
        ],
        "colors": [
            "dab88b",
            "f3e9dd",
            "fdf6ec",
            "b7cadb"
        ]
    },
    {
        "id": "332fd09254c8e15fed6edcd9",
        "tags": [
            "blue",
            "purple",
            "pink",
            "teal",
            "neon",
            "kids"
        ],
        "colors": [
            "332fd0",
            "9254c8",
            "e15fed",
            "6edcd9"
        ]
    },
    {
        "id": "180a0a711a75f10086f582a7",
        "tags": [
            "black",
            "purple",
            "pink",
            "space",
            "dark"
        ],
        "colors": [
            "180a0a",
            "711a75",
            "f10086",
            "f582a7"
        ]
    },
    {
        "id": "062c3005595be2d784f5f5f5",
        "tags": [
            "teal",
            "yellow",
            "white"
        ],
        "colors": [
            "062c30",
            "05595b",
            "e2d784",
            "f5f5f5"
        ]
    },
    {
        "id": "6fb2d285c88aebd671eeeeee",
        "tags": [],
        "colors": [
            "6fb2d2",
            "85c88a",
            "ebd671",
            "eeeeee"
        ]
    },
    {
        "id": "4d77ff56bbf15ee6ebf2fa5a",
        "tags": [
            "blue",
            "teal",
            "yellow",
            "happy",
            "neon",
            "sky"
        ],
        "colors": [
            "4d77ff",
            "56bbf1",
            "5ee6eb",
            "f2fa5a"
        ]
    },
    {
        "id": "1b1a17f0a500e45826e6d5b8",
        "tags": [
            "black",
            "orange",
            "beige",
            "gold",
            "fall"
        ],
        "colors": [
            "1b1a17",
            "f0a500",
            "e45826",
            "e6d5b8"
        ]
    },
    {
        "id": "f6e7d8f68989c65d7b874356",
        "tags": [
            "beige",
            "red",
            "pink",
            "maroon",
            "skin",
            "retro",
            "coffee",
            "sunset",
            "warm",
            "gradient"
        ],
        "colors": [
            "f6e7d8",
            "f68989",
            "c65d7b",
            "874356"
        ]
    },
    {
        "id": "f4fcd9c5d8a4bb9981534340",
        "tags": [
            "green",
            "sage",
            "brown",
            "earth",
            "winter",
            "nature"
        ],
        "colors": [
            "f4fcd9",
            "c5d8a4",
            "bb9981",
            "534340"
        ]
    },
    {
        "id": "0e3edaf473b9ffbde6ffddee",
        "tags": [
            "blue",
            "pink",
            "wedding",
            "kids"
        ],
        "colors": [
            "0e3eda",
            "f473b9",
            "ffbde6",
            "ffddee"
        ]
    },
    {
        "id": "0e185f2fa4ff00ffdde8ffc2",
        "tags": [
            "navy",
            "blue",
            "mint",
            "green",
            "neon",
            "cold"
        ],
        "colors": [
            "0e185f",
            "2fa4ff",
            "00ffdd",
            "e8ffc2"
        ]
    },
    {
        "id": "630606890f0de83a14d9ce3f",
        "tags": [
            "maroon",
            "red",
            "warm"
        ],
        "colors": [
            "630606",
            "890f0d",
            "e83a14",
            "d9ce3f"
        ]
    },
    {
        "id": "e2dea9d18ce0eca6a6eeeeee",
        "tags": [
            "beige",
            "purple",
            "peach",
            "grey",
            "pastel",
            "light",
            "cream"
        ],
        "colors": [
            "e2dea9",
            "d18ce0",
            "eca6a6",
            "eeeeee"
        ]
    },
    {
        "id": "01926700c897ffd365fdffa9",
        "tags": [
            "green",
            "teal",
            "yellow",
            "nature"
        ],
        "colors": [
            "019267",
            "00c897",
            "ffd365",
            "fdffa9"
        ]
    },
    {
        "id": "effffdb8fff985f4ff42c2ff",
        "tags": [
            "teal",
            "blue",
            "cold",
            "winter",
            "light",
            "sky"
        ],
        "colors": [
            "effffd",
            "b8fff9",
            "85f4ff",
            "42c2ff"
        ]
    },
    {
        "id": "ad8b73ceab93e3caa5fffbe9",
        "tags": [
            "brown",
            "beige",
            "cream",
            "coffee",
            "fall",
            "pastel",
            "vintage",
            "warm",
            "earth",
            "light",
            "skin"
        ],
        "colors": [
            "ad8b73",
            "ceab93",
            "e3caa5",
            "fffbe9"
        ]
    },
    {
        "id": "5463ffecececffc300ff1818",
        "tags": [
            "blue",
            "grey",
            "yellow",
            "red",
            "kids"
        ],
        "colors": [
            "5463ff",
            "ececec",
            "ffc300",
            "ff1818"
        ]
    },
    {
        "id": "533e85488fb14fd3c4c1f8cf",
        "tags": [
            "purple",
            "blue",
            "teal",
            "green",
            "mint",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "533e85",
            "488fb1",
            "4fd3c4",
            "c1f8cf"
        ]
    },
    {
        "id": "9adcfffff89affb2a6ff8aae",
        "tags": [
            "blue",
            "yellow",
            "peach",
            "pink",
            "happy",
            "kids",
            "rainbow",
            "pastel"
        ],
        "colors": [
            "9adcff",
            "fff89a",
            "ffb2a6",
            "ff8aae"
        ]
    },
    {
        "id": "151d3bd821486ebf8bdadbbd",
        "tags": [
            "navy",
            "red",
            "teal",
            "beige",
            "retro"
        ],
        "colors": [
            "151d3b",
            "d82148",
            "6ebf8b",
            "dadbbd"
        ]
    },
    {
        "id": "0513672d31fa5d8bf4dff6ff",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter",
            "wedding",
            "gradient"
        ],
        "colors": [
            "051367",
            "2d31fa",
            "5d8bf4",
            "dff6ff"
        ]
    },
    {
        "id": "f7f7f7ffb72bffe61bb5fe83",
        "tags": [
            "white",
            "orange",
            "yellow",
            "green",
            "light",
            "happy",
            "summer",
            "nature"
        ],
        "colors": [
            "f7f7f7",
            "ffb72b",
            "ffe61b",
            "b5fe83"
        ]
    },
    {
        "id": "eeeddee0ddaa203239141e27",
        "tags": [
            "beige",
            "black",
            "vintage",
            "wedding"
        ],
        "colors": [
            "eeedde",
            "e0ddaa",
            "203239",
            "141e27"
        ]
    },
    {
        "id": "5902ece04db0f2c9e1fffa4d",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "kids"
        ],
        "colors": [
            "5902ec",
            "e04db0",
            "f2c9e1",
            "fffa4d"
        ]
    },
    {
        "id": "1c0a00361500603601cc9544",
        "tags": [
            "black",
            "brown",
            "skin",
            "fall",
            "warm",
            "coffee",
            "earth",
            "vintage"
        ],
        "colors": [
            "1c0a00",
            "361500",
            "603601",
            "cc9544"
        ]
    },
    {
        "id": "ffd32d008e89085e7d084594",
        "tags": [
            "yellow",
            "teal",
            "blue"
        ],
        "colors": [
            "ffd32d",
            "008e89",
            "085e7d",
            "084594"
        ]
    },
    {
        "id": "65c18cc1f4c5ffbed8ff7ba9",
        "tags": [
            "green",
            "mint",
            "pink",
            "spring",
            "happy",
            "food",
            "light"
        ],
        "colors": [
            "65c18c",
            "c1f4c5",
            "ffbed8",
            "ff7ba9"
        ]
    },
    {
        "id": "e5e3c9b4cfb094b49f789395",
        "tags": [
            "beige",
            "sage",
            "teal",
            "cream",
            "earth",
            "pastel",
            "vintage"
        ],
        "colors": [
            "e5e3c9",
            "b4cfb0",
            "94b49f",
            "789395"
        ]
    },
    {
        "id": "573391357c3cef6d6dffe6ab",
        "tags": [
            "purple",
            "green",
            "red",
            "yellow",
            "kids"
        ],
        "colors": [
            "573391",
            "357c3c",
            "ef6d6d",
            "ffe6ab"
        ]
    },
    {
        "id": "13948786c6f4fff1ced29d2b",
        "tags": [
            "teal",
            "blue",
            "yellow",
            "beige"
        ],
        "colors": [
            "139487",
            "86c6f4",
            "fff1ce",
            "d29d2b"
        ]
    },
    {
        "id": "bffff0f0ffc2ffe4c0ffbbbb",
        "tags": [
            "mint",
            "orange",
            "peach",
            "red",
            "light",
            "rainbow",
            "spring"
        ],
        "colors": [
            "bffff0",
            "f0ffc2",
            "ffe4c0",
            "ffbbbb"
        ]
    },
    {
        "id": "49537174959a98b4aaf1e0ac",
        "tags": [
            "navy",
            "teal",
            "sage",
            "beige",
            "vintage",
            "wedding"
        ],
        "colors": [
            "495371",
            "74959a",
            "98b4aa",
            "f1e0ac"
        ]
    },
    {
        "id": "1c658c398ab9d8d2cbeeeeee",
        "tags": [
            "blue",
            "beige",
            "grey",
            "winter",
            "cold"
        ],
        "colors": [
            "1c658c",
            "398ab9",
            "d8d2cb",
            "eeeeee"
        ]
    },
    {
        "id": "524a4efdeff4ffc0d3ff5c8d",
        "tags": [
            "black",
            "white",
            "pink"
        ],
        "colors": [
            "524a4e",
            "fdeff4",
            "ffc0d3",
            "ff5c8d"
        ]
    },
    {
        "id": "03045e00b4d890e0efcaf0f8",
        "tags": [
            "navy",
            "blue",
            "cold",
            "space"
        ],
        "colors": [
            "03045e",
            "00b4d8",
            "90e0ef",
            "caf0f8"
        ]
    },
    {
        "id": "362706464e2eacb992e9e5d6",
        "tags": [
            "brown",
            "green",
            "sage",
            "beige",
            "earth",
            "nature",
            "food",
            "vintage"
        ],
        "colors": [
            "362706",
            "464e2e",
            "acb992",
            "e9e5d6"
        ]
    },
    {
        "id": "21325e3e497af1d00af0f0f0",
        "tags": [
            "navy",
            "yellow",
            "grey",
            "night"
        ],
        "colors": [
            "21325e",
            "3e497a",
            "f1d00a",
            "f0f0f0"
        ]
    },
    {
        "id": "6a5495ed5edd8bdb81e7ed9b",
        "tags": [
            "purple",
            "pink",
            "green",
            "yellow",
            "retro",
            "happy"
        ],
        "colors": [
            "6a5495",
            "ed5edd",
            "8bdb81",
            "e7ed9b"
        ]
    },
    {
        "id": "bb6464cdb699c3dbd9c8f2ef",
        "tags": [
            "red",
            "brown",
            "beige",
            "teal",
            "pastel",
            "retro",
            "vintage",
            "nature"
        ],
        "colors": [
            "bb6464",
            "cdb699",
            "c3dbd9",
            "c8f2ef"
        ]
    },
    {
        "id": "7882a4c0a080d1d1d1efefef",
        "tags": [
            "blue",
            "brown",
            "grey",
            "cream",
            "earth",
            "pastel",
            "vintage"
        ],
        "colors": [
            "7882a4",
            "c0a080",
            "d1d1d1",
            "efefef"
        ]
    },
    {
        "id": "2c3333395b642666cff5f2e7",
        "tags": [
            "black",
            "teal",
            "blue",
            "beige",
            "night"
        ],
        "colors": [
            "2c3333",
            "395b64",
            "2666cf",
            "f5f2e7"
        ]
    },
    {
        "id": "8a39e19c51e0b667f1ecc488",
        "tags": [
            "purple",
            "beige",
            "kids"
        ],
        "colors": [
            "8a39e1",
            "9c51e0",
            "b667f1",
            "ecc488"
        ]
    },
    {
        "id": "f76e11ff9f45ffbc80fc4f4f",
        "tags": [
            "orange",
            "red",
            "sunset",
            "warm"
        ],
        "colors": [
            "f76e11",
            "ff9f45",
            "ffbc80",
            "fc4f4f"
        ]
    },
    {
        "id": "fbf8f1f7ecdee9dac154bab9",
        "tags": [
            "beige",
            "teal",
            "cream",
            "light",
            "vintage",
            "pastel",
            "coffee",
            "wedding"
        ],
        "colors": [
            "fbf8f1",
            "f7ecde",
            "e9dac1",
            "54bab9"
        ]
    },
    {
        "id": "d3eca7a1b57db3303019282f",
        "tags": [
            "green",
            "red",
            "black",
            "nature",
            "retro",
            "christmas"
        ],
        "colors": [
            "d3eca7",
            "a1b57d",
            "b33030",
            "19282f"
        ]
    },
    {
        "id": "ffeddbedcdbbe3b7a0bf9270",
        "tags": [
            "beige",
            "peach",
            "brown",
            "skin",
            "cream",
            "earth",
            "kids",
            "warm",
            "coffee",
            "vintage",
            "gold"
        ],
        "colors": [
            "ffeddb",
            "edcdbb",
            "e3b7a0",
            "bf9270"
        ]
    },
    {
        "id": "313552b8405e2eb086eee6ce",
        "tags": [
            "navy",
            "red",
            "maroon",
            "green",
            "beige",
            "retro"
        ],
        "colors": [
            "313552",
            "b8405e",
            "2eb086",
            "eee6ce"
        ]
    },
    {
        "id": "219f94c1deaef2f5c8e8e8a6",
        "tags": [
            "teal",
            "green",
            "yellow",
            "light",
            "winter",
            "kids"
        ],
        "colors": [
            "219f94",
            "c1deae",
            "f2f5c8",
            "e8e8a6"
        ]
    },
    {
        "id": "323232fa4eabfe83c6fff2f9",
        "tags": [
            "black",
            "pink",
            "white",
            "kids"
        ],
        "colors": [
            "323232",
            "fa4eab",
            "fe83c6",
            "fff2f9"
        ]
    },
    {
        "id": "fdebf7fbcaffffadf0fc28fb",
        "tags": [
            "pink",
            "purple",
            "kids"
        ],
        "colors": [
            "fdebf7",
            "fbcaff",
            "ffadf0",
            "fc28fb"
        ]
    },
    {
        "id": "655d8a7897abd885a3fdceb9",
        "tags": [
            "purple",
            "teal",
            "pink",
            "beige",
            "pastel",
            "vintage"
        ],
        "colors": [
            "655d8a",
            "7897ab",
            "d885a3",
            "fdceb9"
        ]
    },
    {
        "id": "1572a19ad0ecefdad7e3bec6",
        "tags": [
            "blue",
            "beige",
            "peach",
            "winter",
            "vintage",
            "pastel"
        ],
        "colors": [
            "1572a1",
            "9ad0ec",
            "efdad7",
            "e3bec6"
        ]
    },
    {
        "id": "1a1a402700827a0bc0fa58b6",
        "tags": [
            "black",
            "navy",
            "purple",
            "pink",
            "space",
            "dark",
            "halloween"
        ],
        "colors": [
            "1a1a40",
            "270082",
            "7a0bc0",
            "fa58b6"
        ]
    },
    {
        "id": "f9e4d4d67d3e9c0f48470d21",
        "tags": [
            "beige",
            "orange",
            "maroon",
            "brown",
            "gold",
            "skin",
            "food",
            "summer",
            "coffee",
            "warm",
            "fall"
        ],
        "colors": [
            "f9e4d4",
            "d67d3e",
            "9c0f48",
            "470d21"
        ]
    },
    {
        "id": "c0d8c0f5eedcdd4a48ecb390",
        "tags": [
            "sage",
            "beige",
            "white",
            "red",
            "orange",
            "vintage",
            "food",
            "happy",
            "fall",
            "christmas"
        ],
        "colors": [
            "c0d8c0",
            "f5eedc",
            "dd4a48",
            "ecb390"
        ]
    },
    {
        "id": "f3c5c5c1a3a3886f6f694e4e",
        "tags": [
            "pink",
            "grey",
            "brown",
            "cream",
            "pastel",
            "vintage",
            "skin",
            "warm"
        ],
        "colors": [
            "f3c5c5",
            "c1a3a3",
            "886f6f",
            "694e4e"
        ]
    },
    {
        "id": "04156211468fda1212eeeeee",
        "tags": [
            "navy",
            "blue",
            "red",
            "grey",
            "white",
            "space"
        ],
        "colors": [
            "041562",
            "11468f",
            "da1212",
            "eeeeee"
        ]
    },
    {
        "id": "ffe162ff646491c483eeeeee",
        "tags": [
            "yellow",
            "red",
            "green",
            "grey",
            "neon",
            "kids",
            "happy",
            "retro",
            "spring"
        ],
        "colors": [
            "ffe162",
            "ff6464",
            "91c483",
            "eeeeee"
        ]
    },
    {
        "id": "e60965f94892ffa1c9fbe5e5",
        "tags": [
            "red",
            "pink",
            "beige",
            "kids",
            "gradient"
        ],
        "colors": [
            "e60965",
            "f94892",
            "ffa1c9",
            "fbe5e5"
        ]
    },
    {
        "id": "6326269d5353bf8b67dacc96",
        "tags": [
            "brown",
            "beige",
            "coffee",
            "warm",
            "vintage",
            "night",
            "pastel",
            "earth",
            "food",
            "nature",
            "fall",
            "skin"
        ],
        "colors": [
            "632626",
            "9d5353",
            "bf8b67",
            "dacc96"
        ]
    },
    {
        "id": "0000005800ffe900ffffc600",
        "tags": [
            "black",
            "purple",
            "pink",
            "yellow",
            "neon",
            "space"
        ],
        "colors": [
            "000000",
            "5800ff",
            "e900ff",
            "ffc600"
        ]
    },
    {
        "id": "24a19cfaeee7325288d96098",
        "tags": [
            "teal",
            "white",
            "navy",
            "pink",
            "retro",
            "wedding",
            "kids"
        ],
        "colors": [
            "24a19c",
            "faeee7",
            "325288",
            "d96098"
        ]
    },
    {
        "id": "6867aca267acce7bb0ffbcd1",
        "tags": [
            "purple",
            "pink",
            "pastel",
            "space",
            "gradient"
        ],
        "colors": [
            "6867ac",
            "a267ac",
            "ce7bb0",
            "ffbcd1"
        ]
    },
    {
        "id": "ff008ed227796128970c1e7f",
        "tags": [
            "pink",
            "maroon",
            "purple",
            "navy",
            "neon",
            "happy"
        ],
        "colors": [
            "ff008e",
            "d22779",
            "612897",
            "0c1e7f"
        ]
    },
    {
        "id": "96ceb4ffeeadd9534fffad60",
        "tags": [
            "teal",
            "yellow",
            "red",
            "orange",
            "retro",
            "kids",
            "happy",
            "rainbow",
            "spring",
            "nature",
            "food"
        ],
        "colors": [
            "96ceb4",
            "ffeead",
            "d9534f",
            "ffad60"
        ]
    },
    {
        "id": "4c0027570530750550980f5a",
        "tags": [
            "maroon",
            "purple",
            "dark",
            "night",
            "vintage",
            "skin",
            "halloween"
        ],
        "colors": [
            "4c0027",
            "570530",
            "750550",
            "980f5a"
        ]
    },
    {
        "id": "ff6363ffab76fffda2baffb4",
        "tags": [
            "red",
            "orange",
            "yellow",
            "mint",
            "green",
            "neon",
            "happy",
            "kids",
            "rainbow",
            "light",
            "spring"
        ],
        "colors": [
            "ff6363",
            "ffab76",
            "fffda2",
            "baffb4"
        ]
    },
    {
        "id": "8946a6b762c1ea99d5ffcddd",
        "tags": [
            "purple",
            "pink",
            "kids"
        ],
        "colors": [
            "8946a6",
            "b762c1",
            "ea99d5",
            "ffcddd"
        ]
    },
    {
        "id": "d9d7f1fffddee7fbbeffcbcb",
        "tags": [
            "blue",
            "yellow",
            "green",
            "peach",
            "pastel",
            "summer",
            "light",
            "cream",
            "happy",
            "rainbow"
        ],
        "colors": [
            "d9d7f1",
            "fffdde",
            "e7fbbe",
            "ffcbcb"
        ]
    },
    {
        "id": "07222735858b4fbdbaaefeff",
        "tags": [],
        "colors": [
            "072227",
            "35858b",
            "4fbdba",
            "aefeff"
        ]
    },
    {
        "id": "d3dedc92a9bd7c99acffefef",
        "tags": [
            "teal",
            "grey",
            "pastel",
            "cold",
            "cream"
        ],
        "colors": [
            "d3dedc",
            "92a9bd",
            "7c99ac",
            "ffefef"
        ]
    },
    {
        "id": "362222b3541effccd2ffeded",
        "tags": [
            "brown",
            "orange",
            "peach",
            "pink",
            "vintage",
            "warm",
            "skin",
            "food",
            "wedding"
        ],
        "colors": [
            "362222",
            "b3541e",
            "ffccd2",
            "ffeded"
        ]
    },
    {
        "id": "876445ca965ceec373f4dfba",
        "tags": [
            "brown",
            "beige",
            "pastel",
            "gold",
            "coffee",
            "nature",
            "warm",
            "fall",
            "earth",
            "vintage",
            "skin"
        ],
        "colors": [
            "876445",
            "ca965c",
            "eec373",
            "f4dfba"
        ]
    },
    {
        "id": "781c689a0680ffd39afff5e1",
        "tags": [
            "purple",
            "yellow",
            "happy",
            "wedding"
        ],
        "colors": [
            "781c68",
            "9a0680",
            "ffd39a",
            "fff5e1"
        ]
    },
    {
        "id": "fff89affc900086e7d1a5f7a",
        "tags": [
            "yellow",
            "teal",
            "navy",
            "happy"
        ],
        "colors": [
            "fff89a",
            "ffc900",
            "086e7d",
            "1a5f7a"
        ]
    },
    {
        "id": "feece9ccd1e4fe7e6d2f3a8f",
        "tags": [
            "peach",
            "grey",
            "orange",
            "navy",
            "vintage",
            "kids",
            "wedding"
        ],
        "colors": [
            "feece9",
            "ccd1e4",
            "fe7e6d",
            "2f3a8f"
        ]
    },
    {
        "id": "0f0e0e5412128b9a46eeeeee",
        "tags": [
            "black",
            "maroon",
            "green",
            "grey",
            "dark",
            "vintage",
            "food",
            "winter",
            "halloween"
        ],
        "colors": [
            "0f0e0e",
            "541212",
            "8b9a46",
            "eeeeee"
        ]
    },
    {
        "id": "f9d371f47340ef2f888843f2",
        "tags": [
            "yellow",
            "orange",
            "pink",
            "purple",
            "neon",
            "happy",
            "rainbow"
        ],
        "colors": [
            "f9d371",
            "f47340",
            "ef2f88",
            "8843f2"
        ]
    },
    {
        "id": "d77fa1baabdad6e5fafff9f9",
        "tags": [
            "pink",
            "purple",
            "blue",
            "white",
            "pastel",
            "skin",
            "kids",
            "wedding",
            "cream",
            "light"
        ],
        "colors": [
            "d77fa1",
            "baabda",
            "d6e5fa",
            "fff9f9"
        ]
    },
    {
        "id": "fff8f3a3e4db1c6dd0fed1ef",
        "tags": [
            "white",
            "teal",
            "blue",
            "pink",
            "retro",
            "summer",
            "light",
            "wedding"
        ],
        "colors": [
            "fff8f3",
            "a3e4db",
            "1c6dd0",
            "fed1ef"
        ]
    },
    {
        "id": "7900ff548cff93ffd8cfffdc",
        "tags": [
            "purple",
            "blue",
            "mint",
            "green",
            "neon",
            "space",
            "retro"
        ],
        "colors": [
            "7900ff",
            "548cff",
            "93ffd8",
            "cfffdc"
        ]
    },
    {
        "id": "ea5c2bff7f3ff6d86095cd41",
        "tags": [
            "orange",
            "yellow",
            "green",
            "food",
            "nature",
            "warm",
            "gold",
            "fall"
        ],
        "colors": [
            "ea5c2b",
            "ff7f3f",
            "f6d860",
            "95cd41"
        ]
    },
    {
        "id": "f3c892fff1bda3da8d146356",
        "tags": [
            "orange",
            "yellow",
            "green",
            "food",
            "nature",
            "kids",
            "earth"
        ],
        "colors": [
            "f3c892",
            "fff1bd",
            "a3da8d",
            "146356"
        ]
    },
    {
        "id": "ff5959676fa3cddeffeef2ff",
        "tags": [
            "red",
            "blue",
            "white",
            "retro"
        ],
        "colors": [
            "ff5959",
            "676fa3",
            "cddeff",
            "eef2ff"
        ]
    },
    {
        "id": "db6b97f2ffe9a6cf98557c55",
        "tags": [
            "pink",
            "green",
            "nature",
            "kids",
            "wedding",
            "winter",
            "vintage",
            "christmas"
        ],
        "colors": [
            "db6b97",
            "f2ffe9",
            "a6cf98",
            "557c55"
        ]
    },
    {
        "id": "ffbd353fa7968267be502064",
        "tags": [
            "yellow",
            "teal",
            "purple",
            "vintage"
        ],
        "colors": [
            "ffbd35",
            "3fa796",
            "8267be",
            "502064"
        ]
    },
    {
        "id": "37066535589af14a16fc9918",
        "tags": [
            "purple",
            "blue",
            "orange",
            "space"
        ],
        "colors": [
            "370665",
            "35589a",
            "f14a16",
            "fc9918"
        ]
    },
    {
        "id": "000b499b0000ff7272ffb5b5",
        "tags": [
            "navy",
            "maroon",
            "red",
            "pink",
            "peach",
            "night"
        ],
        "colors": [
            "000b49",
            "9b0000",
            "ff7272",
            "ffb5b5"
        ]
    },
    {
        "id": "f0ece3dfd3c3c7b198a68dad",
        "tags": [
            "beige",
            "purple",
            "coffee",
            "pastel",
            "skin",
            "cream",
            "earth",
            "warm",
            "light"
        ],
        "colors": [
            "f0ece3",
            "dfd3c3",
            "c7b198",
            "a68dad"
        ]
    },
    {
        "id": "f5f5f5f0545430475e121212",
        "tags": [
            "white",
            "red",
            "navy",
            "black",
            "winter",
            "retro",
            "wedding",
            "christmas"
        ],
        "colors": [
            "f5f5f5",
            "f05454",
            "30475e",
            "121212"
        ]
    },
    {
        "id": "1a374d4068826998abb1d0e0",
        "tags": [
            "navy",
            "blue",
            "cold",
            "wedding",
            "winter",
            "sea"
        ],
        "colors": [
            "1a374d",
            "406882",
            "6998ab",
            "b1d0e0"
        ]
    },
    {
        "id": "ff1700ff8e00ffe40006ff00",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "neon",
            "rainbow",
            "kids",
            "happy",
            "spring"
        ],
        "colors": [
            "ff1700",
            "ff8e00",
            "ffe400",
            "06ff00"
        ]
    },
    {
        "id": "3e8e7e7cd1b8fabb51faedc6",
        "tags": [
            "teal",
            "orange",
            "beige",
            "kids",
            "retro"
        ],
        "colors": [
            "3e8e7e",
            "7cd1b8",
            "fabb51",
            "faedc6"
        ]
    },
    {
        "id": "1919192d4263c84b31ecdbba",
        "tags": [
            "black",
            "navy",
            "red",
            "beige",
            "dark",
            "halloween",
            "winter",
            "vintage"
        ],
        "colors": [
            "191919",
            "2d4263",
            "c84b31",
            "ecdbba"
        ]
    },
    {
        "id": "fee3ecf9c5d5f999b7f2789f",
        "tags": [
            "pink",
            "skin",
            "kids",
            "light",
            "spring",
            "wedding"
        ],
        "colors": [
            "fee3ec",
            "f9c5d5",
            "f999b7",
            "f2789f"
        ]
    },
    {
        "id": "4c3f919145b6b958a5ff5677",
        "tags": [
            "navy",
            "purple",
            "peach",
            "sunset",
            "space",
            "cold",
            "gradient"
        ],
        "colors": [
            "4c3f91",
            "9145b6",
            "b958a5",
            "ff5677"
        ]
    },
    {
        "id": "041c3204293a064663ecb365",
        "tags": [
            "black",
            "navy",
            "orange",
            "dark",
            "night",
            "winter",
            "cold"
        ],
        "colors": [
            "041c32",
            "04293a",
            "064663",
            "ecb365"
        ]
    },
    {
        "id": "781d42a3423cde834df0d290",
        "tags": [
            "maroon",
            "brown",
            "orange",
            "beige",
            "gold",
            "skin",
            "vintage",
            "warm",
            "coffee",
            "sunset",
            "christmas"
        ],
        "colors": [
            "781d42",
            "a3423c",
            "de834d",
            "f0d290"
        ]
    },
    {
        "id": "edd2f3fffcdc84dfff516beb",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "kids",
            "light",
            "happy"
        ],
        "colors": [
            "edd2f3",
            "fffcdc",
            "84dfff",
            "516beb"
        ]
    },
    {
        "id": "040303461111a13333b3541e",
        "tags": [
            "black",
            "maroon",
            "red",
            "orange",
            "brown",
            "dark",
            "night",
            "halloween",
            "coffee",
            "warm"
        ],
        "colors": [
            "040303",
            "461111",
            "a13333",
            "b3541e"
        ]
    },
    {
        "id": "22577e5584ac95d1ccf6f2d4",
        "tags": [
            "navy",
            "blue",
            "teal",
            "beige",
            "kids",
            "cold",
            "winter",
            "gradient",
            "sky"
        ],
        "colors": [
            "22577e",
            "5584ac",
            "95d1cc",
            "f6f2d4"
        ]
    },
    {
        "id": "8e806ac3b091e4cda7ffe6bc",
        "tags": [
            "brown",
            "beige",
            "cream",
            "vintage",
            "skin",
            "coffee",
            "warm",
            "pastel",
            "light",
            "earth"
        ],
        "colors": [
            "8e806a",
            "c3b091",
            "e4cda7",
            "ffe6bc"
        ]
    },
    {
        "id": "064635519259f0bb62f4eea9",
        "tags": [
            "green",
            "orange",
            "yellow",
            "vintage",
            "nature",
            "kids",
            "food",
            "spring"
        ],
        "colors": [
            "064635",
            "519259",
            "f0bb62",
            "f4eea9"
        ]
    },
    {
        "id": "97bfb4f5eedcdd4a484f091d",
        "tags": [
            "teal",
            "beige",
            "red",
            "maroon",
            "vintage",
            "christmas",
            "kids"
        ],
        "colors": [
            "97bfb4",
            "f5eedc",
            "dd4a48",
            "4f091d"
        ]
    },
    {
        "id": "161853292c6dfaedf0ec255a",
        "tags": [
            "navy",
            "white",
            "red",
            "wedding",
            "christmas",
            "space",
            "retro"
        ],
        "colors": [
            "161853",
            "292c6d",
            "faedf0",
            "ec255a"
        ]
    },
    {
        "id": "ffafaffbffe2ffebccff9999",
        "tags": [
            "pink",
            "peach",
            "yellow",
            "red",
            "light",
            "happy",
            "spring"
        ],
        "colors": [
            "ffafaf",
            "fbffe2",
            "ffebcc",
            "ff9999"
        ]
    },
    {
        "id": "d3e4cd99a799f2ddc1e2c2b9",
        "tags": [
            "sage",
            "beige",
            "winter",
            "nature",
            "fall",
            "cream",
            "pastel"
        ],
        "colors": [
            "d3e4cd",
            "99a799",
            "f2ddc1",
            "e2c2b9"
        ]
    },
    {
        "id": "000957344cb7577bc1ebe645",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "winter",
            "cold",
            "night"
        ],
        "colors": [
            "000957",
            "344cb7",
            "577bc1",
            "ebe645"
        ]
    },
    {
        "id": "9a068079018c4c0070160040",
        "tags": [
            "purple",
            "navy",
            "black",
            "dark",
            "space"
        ],
        "colors": [
            "9a0680",
            "79018c",
            "4c0070",
            "160040"
        ]
    },
    {
        "id": "6e3cbc7267cb98bae7b8e4f0",
        "tags": [
            "purple",
            "blue",
            "teal",
            "cold",
            "space"
        ],
        "colors": [
            "6e3cbc",
            "7267cb",
            "98bae7",
            "b8e4f0"
        ]
    },
    {
        "id": "d47ae8f4beeea8ece7fdff8f",
        "tags": [
            "purple",
            "pink",
            "teal",
            "yellow",
            "happy",
            "kids"
        ],
        "colors": [
            "d47ae8",
            "f4beee",
            "a8ece7",
            "fdff8f"
        ]
    },
    {
        "id": "dad992e6df9af3ed9efffea9",
        "tags": [
            "yellow",
            "green",
            "cream",
            "nature",
            "kids",
            "fall",
            "light"
        ],
        "colors": [
            "dad992",
            "e6df9a",
            "f3ed9e",
            "fffea9"
        ]
    },
    {
        "id": "0f2c67cd1818f3950df4e185",
        "tags": [
            "navy",
            "red",
            "orange",
            "yellow",
            "sunset"
        ],
        "colors": [
            "0f2c67",
            "cd1818",
            "f3950d",
            "f4e185"
        ]
    },
    {
        "id": "ffcc1d0b4619116530e8e8cc",
        "tags": [
            "yellow",
            "green",
            "beige",
            "food",
            "nature",
            "kids"
        ],
        "colors": [
            "ffcc1d",
            "0b4619",
            "116530",
            "e8e8cc"
        ]
    },
    {
        "id": "f90716ff5403ffca03fff323",
        "tags": [
            "red",
            "orange",
            "yellow",
            "neon",
            "gold",
            "happy"
        ],
        "colors": [
            "f90716",
            "ff5403",
            "ffca03",
            "fff323"
        ]
    },
    {
        "id": "ff87caffc4e1eaeaeaeed7ce",
        "tags": [
            "pink",
            "grey",
            "beige",
            "pastel",
            "kids"
        ],
        "colors": [
            "ff87ca",
            "ffc4e1",
            "eaeaea",
            "eed7ce"
        ]
    },
    {
        "id": "2e4c6d396eb0daddfcfc997c",
        "tags": [
            "navy",
            "blue",
            "orange",
            "vintage",
            "wedding"
        ],
        "colors": [
            "2e4c6d",
            "396eb0",
            "daddfc",
            "fc997c"
        ]
    },
    {
        "id": "f7f7f7ffbc97ff7800ffe300",
        "tags": [
            "white",
            "grey",
            "peach",
            "orange",
            "yellow",
            "gold",
            "warm"
        ],
        "colors": [
            "f7f7f7",
            "ffbc97",
            "ff7800",
            "ffe300"
        ]
    },
    {
        "id": "009dae71dfe7c2fff9ffe652",
        "tags": [
            "teal",
            "yellow",
            "winter",
            "cold",
            "retro"
        ],
        "colors": [
            "009dae",
            "71dfe7",
            "c2fff9",
            "ffe652"
        ]
    },
    {
        "id": "d06224ae431e8a8635e9c891",
        "tags": [
            "orange",
            "brown",
            "green",
            "beige",
            "fall",
            "retro",
            "vintage",
            "earth",
            "nature",
            "coffee"
        ],
        "colors": [
            "d06224",
            "ae431e",
            "8a8635",
            "e9c891"
        ]
    },
    {
        "id": "66806ab4c6a6ffc286fff1af",
        "tags": [
            "sage",
            "orange",
            "beige",
            "earth",
            "fall",
            "nature"
        ],
        "colors": [
            "66806a",
            "b4c6a6",
            "ffc286",
            "fff1af"
        ]
    },
    {
        "id": "000000f58840b85252eadede",
        "tags": [
            "black",
            "orange",
            "grey",
            "gold",
            "night",
            "halloween"
        ],
        "colors": [
            "000000",
            "f58840",
            "b85252",
            "eadede"
        ]
    },
    {
        "id": "e6cca9533535ae4ccfff6d6d",
        "tags": [
            "beige",
            "brown",
            "purple",
            "peach",
            "kids",
            "retro",
            "vintage"
        ],
        "colors": [
            "e6cca9",
            "533535",
            "ae4ccf",
            "ff6d6d"
        ]
    },
    {
        "id": "ffce45d4ac2bb05e277e370c",
        "tags": [
            "yellow",
            "brown",
            "warm",
            "food",
            "gold"
        ],
        "colors": [
            "ffce45",
            "d4ac2b",
            "b05e27",
            "7e370c"
        ]
    },
    {
        "id": "2c272e753188e599349ae66e",
        "tags": [
            "black",
            "purple",
            "orange",
            "green",
            "space",
            "retro"
        ],
        "colors": [
            "2c272e",
            "753188",
            "e59934",
            "9ae66e"
        ]
    },
    {
        "id": "142f43ffab4cff5f7eb000b9",
        "tags": [
            "navy",
            "orange",
            "pink",
            "purple",
            "retro",
            "space"
        ],
        "colors": [
            "142f43",
            "ffab4c",
            "ff5f7e",
            "b000b9"
        ]
    },
    {
        "id": "b983ff94b3fd94daff99feff",
        "tags": [
            "purple",
            "blue",
            "teal",
            "pastel",
            "neon",
            "kids",
            "cold",
            "gradient"
        ],
        "colors": [
            "b983ff",
            "94b3fd",
            "94daff",
            "99feff"
        ]
    },
    {
        "id": "fbf46db4fe9877e4d4998ceb",
        "tags": [
            "yellow",
            "green",
            "mint",
            "teal",
            "purple",
            "neon",
            "spring",
            "happy"
        ],
        "colors": [
            "fbf46d",
            "b4fe98",
            "77e4d4",
            "998ceb"
        ]
    },
    {
        "id": "5441796166b332c1cd17d7a0",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "winter"
        ],
        "colors": [
            "544179",
            "6166b3",
            "32c1cd",
            "17d7a0"
        ]
    },
    {
        "id": "f0e9d2e6ddc4678983181d31",
        "tags": [
            "beige",
            "teal",
            "navy",
            "cream",
            "winter",
            "cold",
            "wedding"
        ],
        "colors": [
            "f0e9d2",
            "e6ddc4",
            "678983",
            "181d31"
        ]
    },
    {
        "id": "c85c5cf9975dfbd148b2ea70",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "food",
            "kids",
            "nature"
        ],
        "colors": [
            "c85c5c",
            "f9975d",
            "fbd148",
            "b2ea70"
        ]
    },
    {
        "id": "9d5c0de5890af7d08afafafa",
        "tags": [
            "brown",
            "orange",
            "beige",
            "white",
            "earth",
            "gold",
            "skin",
            "coffee",
            "nature",
            "warm",
            "fall"
        ],
        "colors": [
            "9d5c0d",
            "e5890a",
            "f7d08a",
            "fafafa"
        ]
    },
    {
        "id": "89b5af96c7c1ded9c4d0cab2",
        "tags": [
            "teal",
            "beige",
            "pastel",
            "vintage",
            "cream"
        ],
        "colors": [
            "89b5af",
            "96c7c1",
            "ded9c4",
            "d0cab2"
        ]
    },
    {
        "id": "000000aa14f0bc8cf2eeeeee",
        "tags": [
            "black",
            "purple",
            "grey",
            "space"
        ],
        "colors": [
            "000000",
            "aa14f0",
            "bc8cf2",
            "eeeeee"
        ]
    },
    {
        "id": "eeebddd8b6a4630000000000",
        "tags": [
            "beige",
            "maroon",
            "black",
            "wedding",
            "vintage",
            "warm"
        ],
        "colors": [
            "eeebdd",
            "d8b6a4",
            "630000",
            "000000"
        ]
    },
    {
        "id": "2f86a634be822fdd92f2f013",
        "tags": [
            "blue",
            "green",
            "yellow",
            "happy",
            "summer"
        ],
        "colors": [
            "2f86a6",
            "34be82",
            "2fdd92",
            "f2f013"
        ]
    },
    {
        "id": "b91646dfd8cafbf3e4105652",
        "tags": [
            "red",
            "maroon",
            "beige",
            "teal",
            "vintage"
        ],
        "colors": [
            "b91646",
            "dfd8ca",
            "fbf3e4",
            "105652"
        ]
    },
    {
        "id": "1f1d363f3351864879e9a6a6",
        "tags": [
            "black",
            "navy",
            "purple",
            "peach",
            "night",
            "space",
            "dark",
            "halloween",
            "gradient"
        ],
        "colors": [
            "1f1d36",
            "3f3351",
            "864879",
            "e9a6a6"
        ]
    },
    {
        "id": "cee5d0f3f0d7fed2aaffbf86",
        "tags": [
            "sage",
            "beige",
            "orange",
            "nature",
            "cream",
            "light",
            "kids",
            "fall"
        ],
        "colors": [
            "cee5d0",
            "f3f0d7",
            "fed2aa",
            "ffbf86"
        ]
    },
    {
        "id": "000d6b9c19e0ff5da299ddcc",
        "tags": [
            "navy",
            "purple",
            "pink",
            "teal",
            "neon",
            "kids",
            "space"
        ],
        "colors": [
            "000d6b",
            "9c19e0",
            "ff5da2",
            "99ddcc"
        ]
    },
    {
        "id": "88e0ef161e54ff5151ff9b6a",
        "tags": [
            "blue",
            "navy",
            "red",
            "orange",
            "space"
        ],
        "colors": [
            "88e0ef",
            "161e54",
            "ff5151",
            "ff9b6a"
        ]
    },
    {
        "id": "4834346b4f4feed6c4fff3e4",
        "tags": [
            "brown",
            "beige",
            "warm",
            "nature",
            "earth",
            "skin",
            "fall",
            "coffee"
        ],
        "colors": [
            "483434",
            "6b4f4f",
            "eed6c4",
            "fff3e4"
        ]
    },
    {
        "id": "49ff00fbff00ff9300ff0000",
        "tags": [
            "green",
            "yellow",
            "orange",
            "red",
            "neon",
            "kids"
        ],
        "colors": [
            "49ff00",
            "fbff00",
            "ff9300",
            "ff0000"
        ]
    },
    {
        "id": "f6d7a7f6eabec8e3d487aaaa",
        "tags": [
            "beige",
            "yellow",
            "teal",
            "light",
            "cream",
            "pastel",
            "vintage"
        ],
        "colors": [
            "f6d7a7",
            "f6eabe",
            "c8e3d4",
            "87aaaa"
        ]
    },
    {
        "id": "090910a9333ae1578af8df8b",
        "tags": [
            "black",
            "maroon",
            "red",
            "pink",
            "yellow"
        ],
        "colors": [
            "090910",
            "a9333a",
            "e1578a",
            "f8df8b"
        ]
    },
    {
        "id": "125c133e7c17f4a442e8e1d9",
        "tags": [
            "green",
            "summer",
            "orange",
            "grey",
            "nature",
            "kids"
        ],
        "colors": [
            "125c13",
            "3e7c17",
            "f4a442",
            "e8e1d9"
        ]
    },
    {
        "id": "fef5edd3e4cdadc2a999a799",
        "tags": [
            "beige",
            "sage",
            "pastel",
            "cream",
            "earth",
            "light",
            "gradient"
        ],
        "colors": [
            "fef5ed",
            "d3e4cd",
            "adc2a9",
            "99a799"
        ]
    },
    {
        "id": "e26a2cff8243fda65dffd07f",
        "tags": [
            "orange",
            "beige",
            "gold",
            "summer",
            "warm"
        ],
        "colors": [
            "e26a2c",
            "ff8243",
            "fda65d",
            "ffd07f"
        ]
    },
    {
        "id": "0000003e065f700b978e05c2",
        "tags": [
            "black",
            "purple",
            "night",
            "dark"
        ],
        "colors": [
            "000000",
            "3e065f",
            "700b97",
            "8e05c2"
        ]
    },
    {
        "id": "c36a2de2c275eadca6fbfbfb",
        "tags": [
            "brown",
            "orange",
            "beige",
            "white",
            "skin",
            "gold",
            "warm",
            "food",
            "fall",
            "coffee"
        ],
        "colors": [
            "c36a2d",
            "e2c275",
            "eadca6",
            "fbfbfb"
        ]
    },
    {
        "id": "ffe699fff9b6ff9292ffccd2",
        "tags": [
            "yellow",
            "beige",
            "peach",
            "pink",
            "light",
            "happy",
            "spring",
            "summer",
            "kids"
        ],
        "colors": [
            "ffe699",
            "fff9b6",
            "ff9292",
            "ffccd2"
        ]
    },
    {
        "id": "191a191e51284e9f3dd8e9a8",
        "tags": [
            "black",
            "green",
            "dark"
        ],
        "colors": [
            "191a19",
            "1e5128",
            "4e9f3d",
            "d8e9a8"
        ]
    },
    {
        "id": "ffa6d58e05059cc094fff7e0",
        "tags": [
            "pink",
            "maroon",
            "green",
            "beige",
            "kids",
            "retro"
        ],
        "colors": [
            "ffa6d5",
            "8e0505",
            "9cc094",
            "fff7e0"
        ]
    },
    {
        "id": "193498113cfc1597e569dadb",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "sea"
        ],
        "colors": [
            "193498",
            "113cfc",
            "1597e5",
            "69dadb"
        ]
    },
    {
        "id": "09009b0f00ffd98c00ffa400",
        "tags": [
            "navy",
            "blue",
            "orange"
        ],
        "colors": [
            "09009b",
            "0f00ff",
            "d98c00",
            "ffa400"
        ]
    },
    {
        "id": "d1e8e4c37b89bccc9aeae7c6",
        "tags": [
            "blue",
            "maroon",
            "green",
            "beige",
            "nature",
            "pastel",
            "kids",
            "cream",
            "food",
            "vintage",
            "wedding"
        ],
        "colors": [
            "d1e8e4",
            "c37b89",
            "bccc9a",
            "eae7c6"
        ]
    },
    {
        "id": "6c4a4ac89595ddbebeededed",
        "tags": [
            "brown",
            "pink",
            "grey",
            "skin",
            "cream"
        ],
        "colors": [
            "6c4a4a",
            "c89595",
            "ddbebe",
            "ededed"
        ]
    },
    {
        "id": "0913539d84b7d5d5d5b2f9fc",
        "tags": [
            "navy",
            "purple",
            "grey",
            "teal",
            "retro",
            "space"
        ],
        "colors": [
            "091353",
            "9d84b7",
            "d5d5d5",
            "b2f9fc"
        ]
    },
    {
        "id": "e5dcc3c7bea2aaa4929a9483",
        "tags": [
            "beige",
            "grey",
            "food",
            "nature",
            "cream",
            "earth",
            "fall"
        ],
        "colors": [
            "e5dcc3",
            "c7bea2",
            "aaa492",
            "9a9483"
        ]
    },
    {
        "id": "e02401f78812ab6d2351050f",
        "tags": [
            "red",
            "orange",
            "maroon",
            "gold",
            "warm",
            "halloween"
        ],
        "colors": [
            "e02401",
            "f78812",
            "ab6d23",
            "51050f"
        ]
    },
    {
        "id": "a2d2fffef9efff865efee440",
        "tags": [
            "blue",
            "white",
            "peach",
            "yellow",
            "kids",
            "happy",
            "summer",
            "retro"
        ],
        "colors": [
            "a2d2ff",
            "fef9ef",
            "ff865e",
            "fee440"
        ]
    },
    {
        "id": "0000003d0000950101ff0000",
        "tags": [
            "black",
            "maroon",
            "red",
            "dark",
            "night",
            "space",
            "halloween"
        ],
        "colors": [
            "000000",
            "3d0000",
            "950101",
            "ff0000"
        ]
    },
    {
        "id": "eadeb8cfb784c56824a09f57",
        "tags": [
            "beige",
            "brown",
            "green",
            "fall",
            "earth",
            "nature",
            "food"
        ],
        "colors": [
            "eadeb8",
            "cfb784",
            "c56824",
            "a09f57"
        ]
    },
    {
        "id": "ff007517277477d970eeeeee",
        "tags": [
            "red",
            "navy",
            "green",
            "grey",
            "neon",
            "retro"
        ],
        "colors": [
            "ff0075",
            "172774",
            "77d970",
            "eeeeee"
        ]
    },
    {
        "id": "f9f3dfcdf2caffdefaffc898",
        "tags": [
            "beige",
            "mint",
            "green",
            "pink",
            "orange",
            "light",
            "happy",
            "pastel",
            "spring"
        ],
        "colors": [
            "f9f3df",
            "cdf2ca",
            "ffdefa",
            "ffc898"
        ]
    },
    {
        "id": "2c289139a3881c7947fffd95",
        "tags": [
            "navy",
            "blue",
            "green",
            "yellow",
            "retro",
            "kids"
        ],
        "colors": [
            "2c2891",
            "39a388",
            "1c7947",
            "fffd95"
        ]
    },
    {
        "id": "1c0c5b3d2c8d916bbfc996cc",
        "tags": [
            "navy",
            "purple",
            "night",
            "dark",
            "cold",
            "gradient"
        ],
        "colors": [
            "1c0c5b",
            "3d2c8d",
            "916bbf",
            "c996cc"
        ]
    },
    {
        "id": "2121216d9886d9cab3f6f6f6",
        "tags": [
            "black",
            "teal",
            "beige",
            "grey",
            "white",
            "nature",
            "earth",
            "fall"
        ],
        "colors": [
            "212121",
            "6d9886",
            "d9cab3",
            "f6f6f6"
        ]
    },
    {
        "id": "dbd0c0faeee0f9e4c8f9cf93",
        "tags": [
            "beige",
            "peach",
            "orange",
            "cream",
            "light",
            "kids",
            "food",
            "summer",
            "vintage",
            "skin",
            "warm",
            "coffee"
        ],
        "colors": [
            "dbd0c0",
            "faeee0",
            "f9e4c8",
            "f9cf93"
        ]
    },
    {
        "id": "f5c6a5ff7777a2416b852747",
        "tags": [
            "beige",
            "peach",
            "purple",
            "maroon",
            "vintage",
            "warm",
            "gold"
        ],
        "colors": [
            "f5c6a5",
            "ff7777",
            "a2416b",
            "852747"
        ]
    },
    {
        "id": "f0a500334756082032000000",
        "tags": [
            "orange",
            "navy",
            "black",
            "space"
        ],
        "colors": [
            "f0a500",
            "334756",
            "082032",
            "000000"
        ]
    },
    {
        "id": "fef1e6f9d5a7ffb08590aacb",
        "tags": [
            "beige",
            "peach",
            "orange",
            "blue",
            "warm",
            "wedding",
            "spring",
            "happy"
        ],
        "colors": [
            "fef1e6",
            "f9d5a7",
            "ffb085",
            "90aacb"
        ]
    },
    {
        "id": "3f0713b24080ecac5dfff9b2",
        "tags": [
            "maroon",
            "purple",
            "orange",
            "yellow",
            "sunset",
            "space"
        ],
        "colors": [
            "3f0713",
            "b24080",
            "ecac5d",
            "fff9b2"
        ]
    },
    {
        "id": "32502e406343ece7b4f3efcc",
        "tags": [
            "green",
            "yellow",
            "beige",
            "nature",
            "food"
        ],
        "colors": [
            "32502e",
            "406343",
            "ece7b4",
            "f3efcc"
        ]
    },
    {
        "id": "14279b3d56b25c7aeae6e6e6",
        "tags": [
            "navy",
            "blue",
            "grey",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "14279b",
            "3d56b2",
            "5c7aea",
            "e6e6e6"
        ]
    },
    {
        "id": "c6d57ed57e7ea2cdcdffe1af",
        "tags": [
            "green",
            "red",
            "teal",
            "beige",
            "retro",
            "earth",
            "nature",
            "kids",
            "pastel"
        ],
        "colors": [
            "c6d57e",
            "d57e7e",
            "a2cdcd",
            "ffe1af"
        ]
    },
    {
        "id": "cee5d0f3f0d7e0c097ff7878",
        "tags": [
            "teal",
            "sage",
            "beige",
            "brown",
            "red",
            "happy",
            "summer",
            "pastel"
        ],
        "colors": [
            "cee5d0",
            "f3f0d7",
            "e0c097",
            "ff7878"
        ]
    },
    {
        "id": "1db9c37027a0c32badf56fad",
        "tags": [
            "teal",
            "purple",
            "pink",
            "kids",
            "neon"
        ],
        "colors": [
            "1db9c3",
            "7027a0",
            "c32bad",
            "f56fad"
        ]
    },
    {
        "id": "fbf4e9b1e6936ecb63ec9cd3",
        "tags": [
            "beige",
            "green",
            "pink",
            "kids",
            "spring",
            "happy",
            "nature"
        ],
        "colors": [
            "fbf4e9",
            "b1e693",
            "6ecb63",
            "ec9cd3"
        ]
    },
    {
        "id": "ff5c58fe8f8ffcd2d1ffedd3",
        "tags": [
            "red",
            "peach",
            "beige",
            "warm"
        ],
        "colors": [
            "ff5c58",
            "fe8f8f",
            "fcd2d1",
            "ffedd3"
        ]
    },
    {
        "id": "4b3869664e8863b4b8a9e4d7",
        "tags": [
            "purple",
            "teal",
            "cold",
            "sky"
        ],
        "colors": [
            "4b3869",
            "664e88",
            "63b4b8",
            "a9e4d7"
        ]
    },
    {
        "id": "316b836d82998ca1a5d5bfbf",
        "tags": [
            "teal",
            "grey",
            "pastel",
            "gradient",
            "sea"
        ],
        "colors": [
            "316b83",
            "6d8299",
            "8ca1a5",
            "d5bfbf"
        ]
    },
    {
        "id": "fcffa6c1ffd7b5deffcab8ff",
        "tags": [
            "yellow",
            "mint",
            "blue",
            "purple",
            "light",
            "kids",
            "spring",
            "pastel"
        ],
        "colors": [
            "fcffa6",
            "c1ffd7",
            "b5deff",
            "cab8ff"
        ]
    },
    {
        "id": "ff00e4ed50f1fdb9fcffeded",
        "tags": [
            "purple",
            "pink",
            "beige",
            "happy",
            "neon"
        ],
        "colors": [
            "ff00e4",
            "ed50f1",
            "fdb9fc",
            "ffeded"
        ]
    },
    {
        "id": "f3d5c0d4b499889eaf506d84",
        "tags": [
            "beige",
            "brown",
            "blue",
            "vintage",
            "earth",
            "wedding",
            "fall"
        ],
        "colors": [
            "f3d5c0",
            "d4b499",
            "889eaf",
            "506d84"
        ]
    },
    {
        "id": "ffadadffdac7ffefbcfffeb7",
        "tags": [
            "peach",
            "yellow",
            "light",
            "cream",
            "warm",
            "happy"
        ],
        "colors": [
            "ffadad",
            "ffdac7",
            "ffefbc",
            "fffeb7"
        ]
    },
    {
        "id": "0000001500503f0071610094",
        "tags": [
            "black",
            "navy",
            "purple",
            "halloween",
            "dark",
            "night"
        ],
        "colors": [
            "000000",
            "150050",
            "3f0071",
            "610094"
        ]
    },
    {
        "id": "fdd2bfb97a958236cb290fba",
        "tags": [
            "peach",
            "purple",
            "blue",
            "retro"
        ],
        "colors": [
            "fdd2bf",
            "b97a95",
            "8236cb",
            "290fba"
        ]
    },
    {
        "id": "f9f3dffdfce5d7e9f7f4d19b",
        "tags": [
            "beige",
            "yellow",
            "blue",
            "orange",
            "light",
            "skin",
            "food",
            "summer",
            "pastel",
            "kids"
        ],
        "colors": [
            "f9f3df",
            "fdfce5",
            "d7e9f7",
            "f4d19b"
        ]
    },
    {
        "id": "4a403aa45d5dffc069efefef",
        "tags": [
            "brown",
            "maroon",
            "orange",
            "white",
            "grey",
            "gold",
            "warm"
        ],
        "colors": [
            "4a403a",
            "a45d5d",
            "ffc069",
            "efefef"
        ]
    },
    {
        "id": "79b4b7fefbf3f8f0df9d9d9d",
        "tags": [
            "teal",
            "white",
            "beige",
            "grey",
            "light",
            "cream",
            "pastel",
            "wedding"
        ],
        "colors": [
            "79b4b7",
            "fefbf3",
            "f8f0df",
            "9d9d9d"
        ]
    },
    {
        "id": "e2c2b9bfd8b8e7eab5f1f7e7",
        "tags": [
            "peach",
            "green",
            "nature",
            "vintage",
            "light",
            "pastel",
            "kids"
        ],
        "colors": [
            "e2c2b9",
            "bfd8b8",
            "e7eab5",
            "f1f7e7"
        ]
    },
    {
        "id": "d4ecdd345b63152d35112031",
        "tags": [
            "teal",
            "navy",
            "black",
            "winter",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "d4ecdd",
            "345b63",
            "152d35",
            "112031"
        ]
    },
    {
        "id": "00a19dfff8e5ffb344e05d5d",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "red",
            "happy"
        ],
        "colors": [
            "00a19d",
            "fff8e5",
            "ffb344",
            "e05d5d"
        ]
    },
    {
        "id": "3b0000ff0000ff95c5fff6cd",
        "tags": [
            "maroon",
            "red",
            "pink",
            "yellow",
            "neon"
        ],
        "colors": [
            "3b0000",
            "ff0000",
            "ff95c5",
            "fff6cd"
        ]
    },
    {
        "id": "6f69ac95dac1ffeba1fd6f96",
        "tags": [
            "navy",
            "teal",
            "yellow",
            "pink",
            "kids",
            "rainbow",
            "happy"
        ],
        "colors": [
            "6f69ac",
            "95dac1",
            "ffeba1",
            "fd6f96"
        ]
    },
    {
        "id": "ffb319ffe194e8f6efb8dfd8",
        "tags": [
            "orange",
            "beige",
            "blue",
            "light",
            "summer",
            "happy"
        ],
        "colors": [
            "ffb319",
            "ffe194",
            "e8f6ef",
            "b8dfd8"
        ]
    },
    {
        "id": "22577a38a3a557cc9980ed99",
        "tags": [
            "navy",
            "blue",
            "teal",
            "green",
            "mint",
            "cold",
            "sea"
        ],
        "colors": [
            "22577a",
            "38a3a5",
            "57cc99",
            "80ed99"
        ]
    },
    {
        "id": "911f27630a10fcf0c8face7f",
        "tags": [
            "red",
            "maroon",
            "beige",
            "coffee",
            "warm",
            "food"
        ],
        "colors": [
            "911f27",
            "630a10",
            "fcf0c8",
            "face7f"
        ]
    },
    {
        "id": "2a09443b185fa12568fec260",
        "tags": [
            "navy",
            "purple",
            "yellow",
            "dark",
            "space",
            "night"
        ],
        "colors": [
            "2a0944",
            "3b185f",
            "a12568",
            "fec260"
        ]
    },
    {
        "id": "f0e5cff7f6f2c8c6c64b6587",
        "tags": [
            "beige",
            "white",
            "grey",
            "navy",
            "coffee",
            "cream",
            "vintage"
        ],
        "colors": [
            "f0e5cf",
            "f7f6f2",
            "c8c6c6",
            "4b6587"
        ]
    },
    {
        "id": "7eb5a6c3683986340ae8d0b3",
        "tags": [
            "teal",
            "orange",
            "brown",
            "beige",
            "earth",
            "vintage",
            "fall"
        ],
        "colors": [
            "7eb5a6",
            "c36839",
            "86340a",
            "e8d0b3"
        ]
    },
    {
        "id": "1e31632d46b9f037a5f8f8f8",
        "tags": [
            "navy",
            "blue",
            "pink",
            "white",
            "neon",
            "kids",
            "wedding"
        ],
        "colors": [
            "1e3163",
            "2d46b9",
            "f037a5",
            "f8f8f8"
        ]
    },
    {
        "id": "cee5d0f3f0d7f7d59c5e454b",
        "tags": [
            "sage",
            "beige",
            "pastel",
            "earth",
            "light"
        ],
        "colors": [
            "cee5d0",
            "f3f0d7",
            "f7d59c",
            "5e454b"
        ]
    },
    {
        "id": "3db2ffffeddaffb830ff2442",
        "tags": [
            "blue",
            "beige",
            "orange",
            "red",
            "summer",
            "happy",
            "kids",
            "rainbow"
        ],
        "colors": [
            "3db2ff",
            "ffedda",
            "ffb830",
            "ff2442"
        ]
    },
    {
        "id": "93b5c6c9ccd5e4d8dcffe3e3",
        "tags": [
            "blue",
            "grey",
            "pink",
            "vintage",
            "cold",
            "cream",
            "light",
            "wedding",
            "sky"
        ],
        "colors": [
            "93b5c6",
            "c9ccd5",
            "e4d8dc",
            "ffe3e3"
        ]
    },
    {
        "id": "4205167d1935b42b51e63e6d",
        "tags": [
            "maroon",
            "red",
            "night",
            "dark",
            "warm",
            "halloween"
        ],
        "colors": [
            "420516",
            "7d1935",
            "b42b51",
            "e63e6d"
        ]
    },
    {
        "id": "f3f1f5f0d9ffbfa2db7f7c82",
        "tags": [
            "grey",
            "purple",
            "pastel",
            "kids",
            "cold"
        ],
        "colors": [
            "f3f1f5",
            "f0d9ff",
            "bfa2db",
            "7f7c82"
        ]
    },
    {
        "id": "865439c68b59fcdec08fc1d4",
        "tags": [
            "brown",
            "beige",
            "blue",
            "coffee",
            "skin"
        ],
        "colors": [
            "865439",
            "c68b59",
            "fcdec0",
            "8fc1d4"
        ]
    },
    {
        "id": "1700553e00ffae00fbb5ffd9",
        "tags": [
            "navy",
            "blue",
            "purple",
            "mint",
            "neon",
            "space",
            "cold",
            "gradient"
        ],
        "colors": [
            "170055",
            "3e00ff",
            "ae00fb",
            "b5ffd9"
        ]
    },
    {
        "id": "297f87fff7aef6d167df2e2e",
        "tags": [
            "teal",
            "yellow",
            "red",
            "happy"
        ],
        "colors": [
            "297f87",
            "fff7ae",
            "f6d167",
            "df2e2e"
        ]
    },
    {
        "id": "e7e0c9c1cfc06b7aa111324d",
        "tags": [
            "beige",
            "teal",
            "blue",
            "navy",
            "vintage",
            "pastel",
            "fall"
        ],
        "colors": [
            "e7e0c9",
            "c1cfc0",
            "6b7aa1",
            "11324d"
        ]
    },
    {
        "id": "11052c3d087bf43b86ffe459",
        "tags": [
            "black",
            "purple",
            "pink",
            "yellow",
            "space",
            "retro"
        ],
        "colors": [
            "11052c",
            "3d087b",
            "f43b86",
            "ffe459"
        ]
    },
    {
        "id": "fdd2bfff6b6bb61919012443",
        "tags": [
            "peach",
            "beige",
            "red",
            "navy"
        ],
        "colors": [
            "fdd2bf",
            "ff6b6b",
            "b61919",
            "012443"
        ]
    },
    {
        "id": "ffdedefdf5caffdfaff2bb7b",
        "tags": [
            "pink",
            "peach",
            "yellow",
            "orange",
            "light",
            "happy",
            "spring"
        ],
        "colors": [
            "ffdede",
            "fdf5ca",
            "ffdfaf",
            "f2bb7b"
        ]
    },
    {
        "id": "7fc8a9d5eebb5f7a61444941",
        "tags": [
            "teal",
            "mint",
            "green",
            "grey",
            "nature",
            "cold",
            "sea"
        ],
        "colors": [
            "7fc8a9",
            "d5eebb",
            "5f7a61",
            "444941"
        ]
    },
    {
        "id": "f6a9a9ffbf86fff47dc2f784",
        "tags": [
            "peach",
            "orange",
            "yellow",
            "green",
            "kids",
            "happy",
            "light"
        ],
        "colors": [
            "f6a9a9",
            "ffbf86",
            "fff47d",
            "c2f784"
        ]
    },
    {
        "id": "261c2c3e2c415c527f6e85b2",
        "tags": [
            "black",
            "navy",
            "blue",
            "dark",
            "night",
            "cold"
        ],
        "colors": [
            "261c2c",
            "3e2c41",
            "5c527f",
            "6e85b2"
        ]
    },
    {
        "id": "f5e8c7deba9d9e77776f4c5b",
        "tags": [
            "beige",
            "yellow",
            "brown",
            "cream",
            "coffee",
            "food",
            "warm",
            "vintage",
            "skin",
            "pastel",
            "fall"
        ],
        "colors": [
            "f5e8c7",
            "deba9d",
            "9e7777",
            "6f4c5b"
        ]
    },
    {
        "id": "464660368b85b4b897f1e9e5",
        "tags": [
            "navy",
            "teal",
            "green",
            "beige",
            "retro",
            "gradient"
        ],
        "colors": [
            "464660",
            "368b85",
            "b4b897",
            "f1e9e5"
        ]
    },
    {
        "id": "2d24245c3d2eb85c38e0c097",
        "tags": [
            "black",
            "brown",
            "orange",
            "beige",
            "coffee",
            "warm",
            "skin",
            "dark",
            "earth",
            "fall"
        ],
        "colors": [
            "2d2424",
            "5c3d2e",
            "b85c38",
            "e0c097"
        ]
    },
    {
        "id": "ffe6e6ff2626bd1616000000",
        "tags": [
            "pink",
            "red",
            "maroon",
            "black"
        ],
        "colors": [
            "ffe6e6",
            "ff2626",
            "bd1616",
            "000000"
        ]
    },
    {
        "id": "0023660f52bafa8072ffdab9",
        "tags": [
            "navy",
            "blue",
            "peach",
            "beige",
            "kids"
        ],
        "colors": [
            "002366",
            "0f52ba",
            "fa8072",
            "ffdab9"
        ]
    },
    {
        "id": "c3ba85dad5abf0f0cbfeffe2",
        "tags": [
            "yellow",
            "beige",
            "cream",
            "nature",
            "food"
        ],
        "colors": [
            "c3ba85",
            "dad5ab",
            "f0f0cb",
            "feffe2"
        ]
    },
    {
        "id": "986d8e87a8a4d9cab3efe3d0",
        "tags": [
            "purple",
            "teal",
            "beige",
            "vintage",
            "pastel",
            "kids"
        ],
        "colors": [
            "986d8e",
            "87a8a4",
            "d9cab3",
            "efe3d0"
        ]
    },
    {
        "id": "ff4848ffd371c2ffd99ddac6",
        "tags": [
            "red",
            "yellow",
            "mint",
            "teal",
            "happy",
            "rainbow",
            "neon"
        ],
        "colors": [
            "ff4848",
            "ffd371",
            "c2ffd9",
            "9ddac6"
        ]
    },
    {
        "id": "64c9cffde49cffb740df711b",
        "tags": [
            "blue",
            "yellow",
            "beige",
            "orange",
            "happy",
            "summer"
        ],
        "colors": [
            "64c9cf",
            "fde49c",
            "ffb740",
            "df711b"
        ]
    },
    {
        "id": "0820322c394b334756ff4c29",
        "tags": [
            "black",
            "navy",
            "orange",
            "space",
            "dark"
        ],
        "colors": [
            "082032",
            "2c394b",
            "334756",
            "ff4c29"
        ]
    },
    {
        "id": "fdefeff4dfd0dad0c2cdbba7",
        "tags": [
            "pink",
            "beige",
            "brown",
            "pastel",
            "cream",
            "coffee",
            "light",
            "skin"
        ],
        "colors": [
            "fdefef",
            "f4dfd0",
            "dad0c2",
            "cdbba7"
        ]
    },
    {
        "id": "000000bd4b4befb7b7eeeeee",
        "tags": [
            "black",
            "maroon",
            "peach",
            "pink",
            "grey",
            "vintage"
        ],
        "colors": [
            "000000",
            "bd4b4b",
            "efb7b7",
            "eeeeee"
        ]
    },
    {
        "id": "512d6df8485eeeeeee00c1d4",
        "tags": [
            "purple",
            "red",
            "white",
            "teal",
            "retro",
            "kids"
        ],
        "colors": [
            "512d6d",
            "f8485e",
            "eeeeee",
            "00c1d4"
        ]
    },
    {
        "id": "28ffbfbcffb9f5fdb0f7e6ad",
        "tags": [
            "mint",
            "green",
            "yellow",
            "beige",
            "neon",
            "happy",
            "light",
            "summer"
        ],
        "colors": [
            "28ffbf",
            "bcffb9",
            "f5fdb0",
            "f7e6ad"
        ]
    },
    {
        "id": "001e6c0353975089c6ffaa4c",
        "tags": [
            "navy",
            "blue",
            "orange",
            "night"
        ],
        "colors": [
            "001e6c",
            "035397",
            "5089c6",
            "ffaa4c"
        ]
    },
    {
        "id": "716f81b97a95f6ae99f2e1c1",
        "tags": [
            "grey",
            "purple",
            "peach",
            "orange",
            "beige",
            "fall",
            "pastel",
            "vintage",
            "gradient"
        ],
        "colors": [
            "716f81",
            "b97a95",
            "f6ae99",
            "f2e1c1"
        ]
    },
    {
        "id": "0cecddfff338ff67e7c400ff",
        "tags": [
            "teal",
            "yellow",
            "pink",
            "purple",
            "neon",
            "kids"
        ],
        "colors": [
            "0cecdd",
            "fff338",
            "ff67e7",
            "c400ff"
        ]
    },
    {
        "id": "00363805505253b8bbf3f2c9",
        "tags": [
            "teal",
            "blue",
            "yellow",
            "beige",
            "cold"
        ],
        "colors": [
            "003638",
            "055052",
            "53b8bb",
            "f3f2c9"
        ]
    },
    {
        "id": "753422b05b3bd79771ffebc9",
        "tags": [
            "brown",
            "beige",
            "earth",
            "coffee",
            "warm",
            "fall",
            "skin"
        ],
        "colors": [
            "753422",
            "b05b3b",
            "d79771",
            "ffebc9"
        ]
    },
    {
        "id": "b980f0fe9898f5e79de5fbb8",
        "tags": [
            "purple",
            "peach",
            "yellow",
            "green",
            "happy",
            "light"
        ],
        "colors": [
            "b980f0",
            "fe9898",
            "f5e79d",
            "e5fbb8"
        ]
    },
    {
        "id": "faff00ff3f008e2657eeeeee",
        "tags": [
            "yellow",
            "red",
            "purple",
            "grey",
            "white",
            "kids"
        ],
        "colors": [
            "faff00",
            "ff3f00",
            "8e2657",
            "eeeeee"
        ]
    },
    {
        "id": "628395262a53ffa0a0ffe3e3",
        "tags": [
            "navy",
            "peach",
            "pink",
            "kids",
            "retro"
        ],
        "colors": [
            "628395",
            "262a53",
            "ffa0a0",
            "ffe3e3"
        ]
    },
    {
        "id": "faad80ff6767ff3d68a73489",
        "tags": [
            "orange",
            "peach",
            "red",
            "purple",
            "warm",
            "kids"
        ],
        "colors": [
            "faad80",
            "ff6767",
            "ff3d68",
            "a73489"
        ]
    },
    {
        "id": "0f044c141e61787a91eeeeee",
        "tags": [
            "navy",
            "grey",
            "white",
            "night",
            "winter",
            "dark"
        ],
        "colors": [
            "0f044c",
            "141e61",
            "787a91",
            "eeeeee"
        ]
    },
    {
        "id": "fcd8d4fdf6f0f8e2cff5c6aa",
        "tags": [
            "pink",
            "white",
            "peach",
            "beige",
            "skin",
            "kids",
            "light",
            "cream",
            "warm"
        ],
        "colors": [
            "fcd8d4",
            "fdf6f0",
            "f8e2cf",
            "f5c6aa"
        ]
    },
    {
        "id": "54436b50cb9371efa3acffad",
        "tags": [
            "green",
            "mint",
            "nature"
        ],
        "colors": [
            "54436b",
            "50cb93",
            "71efa3",
            "acffad"
        ]
    },
    {
        "id": "a03c78ed8e7ccdf3a293d9a3",
        "tags": [
            "purple",
            "peach",
            "green",
            "summer",
            "kids"
        ],
        "colors": [
            "a03c78",
            "ed8e7c",
            "cdf3a2",
            "93d9a3"
        ]
    },
    {
        "id": "f1ecc3c9d8b657837b515e63",
        "tags": [
            "beige",
            "sage",
            "green",
            "vintage",
            "wedding"
        ],
        "colors": [
            "f1ecc3",
            "c9d8b6",
            "57837b",
            "515e63"
        ]
    },
    {
        "id": "2c2e43595260b2b1b9ffd523",
        "tags": [
            "black",
            "grey",
            "yellow",
            "space",
            "night"
        ],
        "colors": [
            "2c2e43",
            "595260",
            "b2b1b9",
            "ffd523"
        ]
    },
    {
        "id": "7c83fd96baff7dedff88fff7",
        "tags": [
            "blue",
            "teal",
            "cold",
            "winter",
            "neon",
            "sky"
        ],
        "colors": [
            "7c83fd",
            "96baff",
            "7dedff",
            "88fff7"
        ]
    },
    {
        "id": "d9dd6becefa4d54c4c8d2828",
        "tags": [
            "green",
            "red",
            "maroon",
            "food",
            "kids"
        ],
        "colors": [
            "d9dd6b",
            "ecefa4",
            "d54c4c",
            "8d2828"
        ]
    },
    {
        "id": "334257476072548ca8eeeeee",
        "tags": [
            "navy",
            "blue",
            "white",
            "grey",
            "night",
            "sea"
        ],
        "colors": [
            "334257",
            "476072",
            "548ca8",
            "eeeeee"
        ]
    },
    {
        "id": "ffeacaffbcbcf08fc0835151",
        "tags": [
            "beige",
            "peach",
            "pink",
            "brown",
            "skin",
            "happy"
        ],
        "colors": [
            "ffeaca",
            "ffbcbc",
            "f08fc0",
            "835151"
        ]
    },
    {
        "id": "362222171010423f3e2b2b2b",
        "tags": [
            "brown",
            "black",
            "grey",
            "night",
            "dark",
            "vintage"
        ],
        "colors": [
            "362222",
            "171010",
            "423f3e",
            "2b2b2b"
        ]
    },
    {
        "id": "fdd2bfe98580df5e5e492f10",
        "tags": [
            "peach",
            "red",
            "brown",
            "warm"
        ],
        "colors": [
            "fdd2bf",
            "e98580",
            "df5e5e",
            "492f10"
        ]
    },
    {
        "id": "ecd6625d8233284e783e215d",
        "tags": [
            "yellow",
            "green",
            "navy",
            "purple",
            "nature"
        ],
        "colors": [
            "ecd662",
            "5d8233",
            "284e78",
            "3e215d"
        ]
    },
    {
        "id": "3c51869b72aac6b4cefff5de",
        "tags": [
            "navy",
            "purple",
            "beige",
            "wedding",
            "gradient"
        ],
        "colors": [
            "3c5186",
            "9b72aa",
            "c6b4ce",
            "fff5de"
        ]
    },
    {
        "id": "4f0e0ebb8760ffdadafff1f1",
        "tags": [
            "maroon",
            "brown",
            "pink",
            "white",
            "coffee"
        ],
        "colors": [
            "4f0e0e",
            "bb8760",
            "ffdada",
            "fff1f1"
        ]
    },
    {
        "id": "fef7dce6ddc6c2b8a3a19882",
        "tags": [
            "yellow",
            "beige",
            "warm",
            "coffee",
            "cream",
            "light",
            "summer",
            "fall"
        ],
        "colors": [
            "fef7dc",
            "e6ddc6",
            "c2b8a3",
            "a19882"
        ]
    },
    {
        "id": "b5eaeaedf6e5ffbcbcf38ba0",
        "tags": [
            "blue",
            "red",
            "light",
            "summer",
            "spring",
            "pastel",
            "kids",
            "happy"
        ],
        "colors": [
            "b5eaea",
            "edf6e5",
            "ffbcbc",
            "f38ba0"
        ]
    },
    {
        "id": "faebe0c9e4c5b5cda3c1ac95",
        "tags": [
            "beige",
            "green",
            "brown",
            "pastel",
            "light",
            "summer",
            "earth",
            "nature",
            "food"
        ],
        "colors": [
            "faebe0",
            "c9e4c5",
            "b5cda3",
            "c1ac95"
        ]
    },
    {
        "id": "ffe194e8f6efb8dfd84c4c6d",
        "tags": [
            "yellow",
            "blue",
            "light",
            "summer"
        ],
        "colors": [
            "ffe194",
            "e8f6ef",
            "b8dfd8",
            "4c4c6d"
        ]
    },
    {
        "id": "78dec7d62ad0fb7afcfbc7f7",
        "tags": [
            "purple",
            "pink",
            "teal",
            "vintage",
            "neon",
            "happy",
            "kids"
        ],
        "colors": [
            "78dec7",
            "d62ad0",
            "fb7afc",
            "fbc7f7"
        ]
    },
    {
        "id": "cdf0eaf9f9f9f7dbf0beaee2",
        "tags": [
            "teal",
            "white",
            "pink",
            "purple",
            "light",
            "spring",
            "wedding",
            "pastel",
            "kids",
            "sky"
        ],
        "colors": [
            "cdf0ea",
            "f9f9f9",
            "f7dbf0",
            "beaee2"
        ]
    },
    {
        "id": "52006acd113bff7600ffa900",
        "tags": [
            "purple",
            "red",
            "orange",
            "sunset",
            "warm",
            "rainbow",
            "halloween",
            "gradient"
        ],
        "colors": [
            "52006a",
            "cd113b",
            "ff7600",
            "ffa900"
        ]
    },
    {
        "id": "f7dad9fff5dad6d2c45d534a",
        "tags": [
            "pink",
            "yellow",
            "vintage",
            "pastel",
            "cream",
            "wedding",
            "skin"
        ],
        "colors": [
            "f7dad9",
            "fff5da",
            "d6d2c4",
            "5d534a"
        ]
    },
    {
        "id": "0a1931185adbffc947efefef",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "retro",
            "space",
            "cold"
        ],
        "colors": [
            "0a1931",
            "185adb",
            "ffc947",
            "efefef"
        ]
    },
    {
        "id": "402218865439c68b59d7b19d",
        "tags": [
            "brown",
            "beige",
            "earth",
            "coffee",
            "skin",
            "warm",
            "food"
        ],
        "colors": [
            "402218",
            "865439",
            "c68b59",
            "d7b19d"
        ]
    },
    {
        "id": "05374239a2dba2dbfae8f0f2",
        "tags": [
            "navy",
            "blue",
            "grey",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "053742",
            "39a2db",
            "a2dbfa",
            "e8f0f2"
        ]
    },
    {
        "id": "f0d9e7ff94cca239ea5c33f6",
        "tags": [
            "pink",
            "purple",
            "neon",
            "happy",
            "gradient"
        ],
        "colors": [
            "f0d9e7",
            "ff94cc",
            "a239ea",
            "5c33f6"
        ]
    },
    {
        "id": "171717444444da0037ededed",
        "tags": [
            "black",
            "grey",
            "red",
            "dark",
            "night"
        ],
        "colors": [
            "171717",
            "444444",
            "da0037",
            "ededed"
        ]
    },
    {
        "id": "d83a56ff616dffeac966de93",
        "tags": [
            "red",
            "beige",
            "mint",
            "green",
            "spring",
            "summer",
            "kids",
            "happy",
            "nature"
        ],
        "colors": [
            "d83a56",
            "ff616d",
            "ffeac9",
            "66de93"
        ]
    },
    {
        "id": "cdf0eaf9f9f9f6c6eac490e4",
        "tags": [
            "teal",
            "white",
            "pink",
            "purple",
            "light",
            "pastel",
            "cream"
        ],
        "colors": [
            "cdf0ea",
            "f9f9f9",
            "f6c6ea",
            "c490e4"
        ]
    },
    {
        "id": "5f939a3a6351a0937df2edd7",
        "tags": [
            "teal",
            "green",
            "brown",
            "beige",
            "pastel",
            "earth",
            "retro"
        ],
        "colors": [
            "5f939a",
            "3a6351",
            "a0937d",
            "f2edd7"
        ]
    },
    {
        "id": "558776a3a8477f8b52eae2b6",
        "tags": [
            "green",
            "beige",
            "summer",
            "nature",
            "food",
            "vintage"
        ],
        "colors": [
            "558776",
            "a3a847",
            "7f8b52",
            "eae2b6"
        ]
    },
    {
        "id": "e99497f3c583e8e46eb3e283",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "light",
            "spring",
            "rainbow",
            "kids"
        ],
        "colors": [
            "e99497",
            "f3c583",
            "e8e46e",
            "b3e283"
        ]
    },
    {
        "id": "faf1e6ffc074b6c86701937c",
        "tags": [
            "beige",
            "orange",
            "green",
            "spring",
            "nature",
            "summer",
            "food"
        ],
        "colors": [
            "faf1e6",
            "ffc074",
            "b6c867",
            "01937c"
        ]
    },
    {
        "id": "04009a77acf13edbf0f0ebcc",
        "tags": [],
        "colors": [
            "04009a",
            "77acf1",
            "3edbf0",
            "f0ebcc"
        ]
    },
    {
        "id": "343a407952b3ffc107e1e8eb",
        "tags": [
            "black",
            "purple",
            "yellow",
            "grey",
            "retro",
            "space",
            "cold"
        ],
        "colors": [
            "343a40",
            "7952b3",
            "ffc107",
            "e1e8eb"
        ]
    },
    {
        "id": "7d5a50b4846ce5b299fcdec0",
        "tags": [
            "brown",
            "beige",
            "skin",
            "warm",
            "food",
            "vintage",
            "fall",
            "earth",
            "gradient"
        ],
        "colors": [
            "7d5a50",
            "b4846c",
            "e5b299",
            "fcdec0"
        ]
    },
    {
        "id": "dddddd125d983c8dadf5a962",
        "tags": [
            "grey",
            "blue",
            "orange",
            "retro",
            "wedding"
        ],
        "colors": [
            "dddddd",
            "125d98",
            "3c8dad",
            "f5a962"
        ]
    },
    {
        "id": "ffeedbffd8ccffbd9b0a1d37",
        "tags": [
            "skin",
            "beige",
            "peach",
            "black",
            "warm",
            "food"
        ],
        "colors": [
            "ffeedb",
            "ffd8cc",
            "ffbd9b",
            "0a1d37"
        ]
    },
    {
        "id": "161616346751c84b31ecdbba",
        "tags": [
            "vintage",
            "black",
            "green",
            "orange",
            "dark",
            "nature"
        ],
        "colors": [
            "161616",
            "346751",
            "c84b31",
            "ecdbba"
        ]
    },
    {
        "id": "cee5d0f3f0d7d8b3845e454b",
        "tags": [
            "mint",
            "beige",
            "brown",
            "vintage",
            "pastel",
            "earth",
            "nature",
            "cream",
            "summer"
        ],
        "colors": [
            "cee5d0",
            "f3f0d7",
            "d8b384",
            "5e454b"
        ]
    },
    {
        "id": "293b5f47597edbe6fdb2ab8c",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter",
            "night",
            "wedding"
        ],
        "colors": [
            "293b5f",
            "47597e",
            "dbe6fd",
            "b2ab8c"
        ]
    },
    {
        "id": "2f5d625e8b7ea7c4bcdfeeea",
        "tags": [
            "green",
            "vintage",
            "nature",
            "sea"
        ],
        "colors": [
            "2f5d62",
            "5e8b7e",
            "a7c4bc",
            "dfeeea"
        ]
    },
    {
        "id": "03256c2541b21768ace5d549",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "kids"
        ],
        "colors": [
            "03256c",
            "2541b2",
            "1768ac",
            "e5d549"
        ]
    },
    {
        "id": "fff5ebdeedf0f4c7abb2b8a3",
        "tags": [
            "pastel",
            "light",
            "vintage",
            "cream",
            "nature",
            "kids",
            "summer"
        ],
        "colors": [
            "fff5eb",
            "deedf0",
            "f4c7ab",
            "b2b8a3"
        ]
    },
    {
        "id": "231e2339a6a3deeeeabf1363",
        "tags": [
            "black",
            "teal",
            "retro",
            "space"
        ],
        "colors": [
            "231e23",
            "39a6a3",
            "deeeea",
            "bf1363"
        ]
    },
    {
        "id": "2323232940d339a9cbffeda3",
        "tags": [
            "black",
            "blue",
            "yellow",
            "retro"
        ],
        "colors": [
            "232323",
            "2940d3",
            "39a9cb",
            "ffeda3"
        ]
    },
    {
        "id": "ffed99f6b8b8ac66cc3b14a7",
        "tags": [
            "yellow",
            "purple",
            "peach",
            "wedding",
            "rainbow",
            "sunset",
            "happy"
        ],
        "colors": [
            "ffed99",
            "f6b8b8",
            "ac66cc",
            "3b14a7"
        ]
    },
    {
        "id": "f5e6cafb9300f54748343f56",
        "tags": [
            "orange",
            "red",
            "skin",
            "warm",
            "kids",
            "gradient"
        ],
        "colors": [
            "f5e6ca",
            "fb9300",
            "f54748",
            "343f56"
        ]
    },
    {
        "id": "fff5fdff96ad005a8d022e57",
        "tags": [
            "white",
            "pink",
            "blue",
            "navy",
            "wedding"
        ],
        "colors": [
            "fff5fd",
            "ff96ad",
            "005a8d",
            "022e57"
        ]
    },
    {
        "id": "f9dfdc0a81ab0c4271000000",
        "tags": [
            "peach",
            "blue",
            "navy",
            "black",
            "vintage",
            "wedding"
        ],
        "colors": [
            "f9dfdc",
            "0a81ab",
            "0c4271",
            "000000"
        ]
    },
    {
        "id": "00ead3fff5b7ff449f005f99",
        "tags": [
            "teal",
            "yellow",
            "pink",
            "blue",
            "neon",
            "happy",
            "kids",
            "rainbow"
        ],
        "colors": [
            "00ead3",
            "fff5b7",
            "ff449f",
            "005f99"
        ]
    },
    {
        "id": "eba83abb371afff8d9d5dbb3",
        "tags": [
            "orange",
            "red",
            "vintage",
            "spring",
            "nature",
            "kids",
            "food",
            "gold"
        ],
        "colors": [
            "eba83a",
            "bb371a",
            "fff8d9",
            "d5dbb3"
        ]
    },
    {
        "id": "caf7e3f8ededf6dfebe4bad4",
        "tags": [
            "mint",
            "pink",
            "light",
            "pastel",
            "cream",
            "kids",
            "skin"
        ],
        "colors": [
            "caf7e3",
            "f8eded",
            "f6dfeb",
            "e4bad4"
        ]
    },
    {
        "id": "4a1c40962d2de798aef6e5e9",
        "tags": [
            "purple",
            "maroon",
            "pink",
            "gradient"
        ],
        "colors": [
            "4a1c40",
            "962d2d",
            "e798ae",
            "f6e5e9"
        ]
    },
    {
        "id": "0a1931185adbffc947feddbe",
        "tags": [
            "black",
            "blue",
            "yellow",
            "sunset",
            "space"
        ],
        "colors": [
            "0a1931",
            "185adb",
            "ffc947",
            "feddbe"
        ]
    },
    {
        "id": "99154effc93cffddccffbbcc",
        "tags": [
            "red",
            "yellow",
            "pink",
            "retro",
            "food",
            "gold"
        ],
        "colors": [
            "99154e",
            "ffc93c",
            "ffddcc",
            "ffbbcc"
        ]
    },
    {
        "id": "ba135df4cca4d99879000000",
        "tags": [
            "red",
            "beige",
            "black",
            "skin"
        ],
        "colors": [
            "ba135d",
            "f4cca4",
            "d99879",
            "000000"
        ]
    },
    {
        "id": "e93b81f5abc9ffe5e2b6c9f0",
        "tags": [
            "pink",
            "blue",
            "light",
            "skin",
            "kids"
        ],
        "colors": [
            "e93b81",
            "f5abc9",
            "ffe5e2",
            "b6c9f0"
        ]
    },
    {
        "id": "480032005792fc92e3f2f4c3",
        "tags": [
            "blue",
            "pink",
            "yellow",
            "retro",
            "neon",
            "rainbow"
        ],
        "colors": [
            "480032",
            "005792",
            "fc92e3",
            "f2f4c3"
        ]
    },
    {
        "id": "867ae9fff5abffceadc449c2",
        "tags": [
            "yellow",
            "purple",
            "light",
            "happy",
            "spring"
        ],
        "colors": [
            "867ae9",
            "fff5ab",
            "ffcead",
            "c449c2"
        ]
    },
    {
        "id": "faf1e6fdfaf6e4efe7064420",
        "tags": [
            "beige",
            "white",
            "green",
            "pastel",
            "light",
            "wedding",
            "cream",
            "nature",
            "food"
        ],
        "colors": [
            "faf1e6",
            "fdfaf6",
            "e4efe7",
            "064420"
        ]
    },
    {
        "id": "f7fd04f9b208f98404fc5404",
        "tags": [
            "yellow",
            "orange",
            "red",
            "sunset",
            "warm",
            "gold",
            "neon",
            "happy",
            "summer"
        ],
        "colors": [
            "f7fd04",
            "f9b208",
            "f98404",
            "fc5404"
        ]
    },
    {
        "id": "fbc6a4f4a9a8ce97b0afb9c8",
        "tags": [
            "orange",
            "peach",
            "pastel",
            "coffee",
            "cream",
            "skin"
        ],
        "colors": [
            "fbc6a4",
            "f4a9a8",
            "ce97b0",
            "afb9c8"
        ]
    },
    {
        "id": "233e8b1eae98a9f1dfffffc7",
        "tags": [
            "navy",
            "teal",
            "mint",
            "yellow",
            "summer",
            "neon",
            "happy",
            "gradient"
        ],
        "colors": [
            "233e8b",
            "1eae98",
            "a9f1df",
            "ffffc7"
        ]
    },
    {
        "id": "94d0cceec4c4f29191d1d9d9",
        "tags": [
            "teal",
            "peach",
            "grey",
            "pastel",
            "vintage",
            "skin"
        ],
        "colors": [
            "94d0cc",
            "eec4c4",
            "f29191",
            "d1d9d9"
        ]
    },
    {
        "id": "cc9b6df1ca89f2dac3c8c2bc",
        "tags": [
            "brown",
            "beige",
            "grey",
            "skin",
            "pastel",
            "warm",
            "gold",
            "coffee",
            "light",
            "fall",
            "kids"
        ],
        "colors": [
            "cc9b6d",
            "f1ca89",
            "f2dac3",
            "c8c2bc"
        ]
    },
    {
        "id": "f55c479fe6a04aa96c564a4a",
        "tags": [
            "red",
            "green",
            "grey",
            "spring",
            "nature",
            "retro"
        ],
        "colors": [
            "f55c47",
            "9fe6a0",
            "4aa96c",
            "564a4a"
        ]
    },
    {
        "id": "21094e5112814ca1a3a5e1ad",
        "tags": [
            "black",
            "purple",
            "teal",
            "green",
            "cold",
            "night",
            "winter",
            "gradient",
            "sea"
        ],
        "colors": [
            "21094e",
            "511281",
            "4ca1a3",
            "a5e1ad"
        ]
    },
    {
        "id": "907fa4a58faaa6d6d6ededd0",
        "tags": [
            "purple",
            "teal",
            "pastel",
            "wedding",
            "light",
            "vintage"
        ],
        "colors": [
            "907fa4",
            "a58faa",
            "a6d6d6",
            "ededd0"
        ]
    },
    {
        "id": "faf3f3e1e5eaa7bbc7da7f8f",
        "tags": [
            "grey",
            "red",
            "light",
            "vintage",
            "wedding",
            "cream",
            "cold"
        ],
        "colors": [
            "faf3f3",
            "e1e5ea",
            "a7bbc7",
            "da7f8f"
        ]
    },
    {
        "id": "faf2da8e97754a503de28f83",
        "tags": [
            "beige",
            "green",
            "red",
            "retro",
            "nature",
            "summer",
            "food"
        ],
        "colors": [
            "faf2da",
            "8e9775",
            "4a503d",
            "e28f83"
        ]
    },
    {
        "id": "fffbdfc6ffc134656d334443",
        "tags": [
            "yellow",
            "mint",
            "green",
            "teal"
        ],
        "colors": [
            "fffbdf",
            "c6ffc1",
            "34656d",
            "334443"
        ]
    },
    {
        "id": "e1701af7a440f6dcbfaaaaaa",
        "tags": [
            "orange",
            "grey",
            "beige",
            "gold",
            "warm",
            "kids"
        ],
        "colors": [
            "e1701a",
            "f7a440",
            "f6dcbf",
            "aaaaaa"
        ]
    },
    {
        "id": "a0937de7d4b5f6e6cbe3cdc1",
        "tags": [
            "beige",
            "brown",
            "pastel",
            "light",
            "coffee",
            "cream",
            "fall",
            "earth"
        ],
        "colors": [
            "a0937d",
            "e7d4b5",
            "f6e6cb",
            "e3cdc1"
        ]
    },
    {
        "id": "f0ebcc3d84b8344fa13f3697",
        "tags": [
            "beige",
            "blue",
            "summer",
            "wedding",
            "winter"
        ],
        "colors": [
            "f0ebcc",
            "3d84b8",
            "344fa1",
            "3f3697"
        ]
    },
    {
        "id": "de89717b6079a7d0cdffe9d6",
        "tags": [
            "peach",
            "purple",
            "teal",
            "vintage",
            "pastel",
            "earth",
            "kids",
            "fall",
            "halloween",
            "retro"
        ],
        "colors": [
            "de8971",
            "7b6079",
            "a7d0cd",
            "ffe9d6"
        ]
    },
    {
        "id": "76616187a7b3cdc7bee1f1dd",
        "tags": [
            "brown",
            "blue",
            "grey",
            "pastel",
            "vintage",
            "cream",
            "winter",
            "fall",
            "cold",
            "gradient"
        ],
        "colors": [
            "766161",
            "87a7b3",
            "cdc7be",
            "e1f1dd"
        ]
    },
    {
        "id": "04009a77acf13edbf0c0fefc",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "neon",
            "happy",
            "winter",
            "space"
        ],
        "colors": [
            "04009a",
            "77acf1",
            "3edbf0",
            "c0fefc"
        ]
    },
    {
        "id": "ffc996ff84749f5f80583d72",
        "tags": [
            "orange",
            "purple",
            "warm",
            "sunset",
            "retro",
            "skin",
            "kids",
            "halloween"
        ],
        "colors": [
            "ffc996",
            "ff8474",
            "9f5f80",
            "583d72"
        ]
    },
    {
        "id": "393e4600adb5aad8d3eeeeee",
        "tags": [
            "teal",
            "grey",
            "cold",
            "winter",
            "space",
            "gradient"
        ],
        "colors": [
            "393e46",
            "00adb5",
            "aad8d3",
            "eeeeee"
        ]
    },
    {
        "id": "f5f7b21cc5dc890596cf0000",
        "tags": [
            "yellow",
            "blue",
            "purple",
            "red",
            "rainbow",
            "happy",
            "kids",
            "summer",
            "neon"
        ],
        "colors": [
            "f5f7b2",
            "1cc5dc",
            "890596",
            "cf0000"
        ]
    },
    {
        "id": "23049daa2ee6ff79cdffdf6b",
        "tags": [
            "navy",
            "purple",
            "pink",
            "yellow",
            "rainbow",
            "happy",
            "kids",
            "neon",
            "gradient"
        ],
        "colors": [
            "23049d",
            "aa2ee6",
            "ff79cd",
            "ffdf6b"
        ]
    },
    {
        "id": "72147ef21170fa9905ff5200",
        "tags": [
            "purple",
            "pink",
            "orange",
            "kids",
            "space",
            "neon",
            "warm",
            "sunset"
        ],
        "colors": [
            "72147e",
            "f21170",
            "fa9905",
            "ff5200"
        ]
    },
    {
        "id": "02475e687980f3bda1fefecc",
        "tags": [
            "peach",
            "grey",
            "earth",
            "winter",
            "wedding",
            "gradient"
        ],
        "colors": [
            "02475e",
            "687980",
            "f3bda1",
            "fefecc"
        ]
    },
    {
        "id": "fcecddffc288fea82fff6701",
        "tags": [
            "beige",
            "orange",
            "skin",
            "warm",
            "gold",
            "cream",
            "sunset",
            "light",
            "retro",
            "kids"
        ],
        "colors": [
            "fcecdd",
            "ffc288",
            "fea82f",
            "ff6701"
        ]
    },
    {
        "id": "999b84926e6fca8a8be6c4c0",
        "tags": [
            "sage",
            "brown",
            "peach",
            "skin",
            "earth",
            "retro"
        ],
        "colors": [
            "999b84",
            "926e6f",
            "ca8a8b",
            "e6c4c0"
        ]
    },
    {
        "id": "5b6d5bca8a8be2bcb7f6e6e4",
        "tags": [
            "sage",
            "peach",
            "skin",
            "vintage",
            "nature",
            "food",
            "pastel"
        ],
        "colors": [
            "5b6d5b",
            "ca8a8b",
            "e2bcb7",
            "f6e6e4"
        ]
    },
    {
        "id": "325288f4eee8f5cebe114e60",
        "tags": [
            "navy",
            "peach",
            "retro",
            "wedding",
            "winter"
        ],
        "colors": [
            "325288",
            "f4eee8",
            "f5cebe",
            "114e60"
        ]
    },
    {
        "id": "542e71fb3640fdca40a799b7",
        "tags": [
            "purple",
            "red",
            "yellow",
            "kids",
            "neon",
            "rainbow",
            "space"
        ],
        "colors": [
            "542e71",
            "fb3640",
            "fdca40",
            "a799b7"
        ]
    },
    {
        "id": "c67aced8f8b7ff9a8cce1f6a",
        "tags": [
            "purple",
            "mint",
            "green",
            "orange",
            "maroon",
            "neon",
            "rainbow",
            "happy",
            "kids",
            "summer"
        ],
        "colors": [
            "c67ace",
            "d8f8b7",
            "ff9a8c",
            "ce1f6a"
        ]
    },
    {
        "id": "eca3f5fdbaf8b0efebedffa9",
        "tags": [
            "purple",
            "pink",
            "teal",
            "green",
            "light",
            "kids"
        ],
        "colors": [
            "eca3f5",
            "fdbaf8",
            "b0efeb",
            "edffa9"
        ]
    },
    {
        "id": "fbe0c48ab6d62978b50061a8",
        "tags": [
            "beige",
            "blue",
            "summer",
            "winter"
        ],
        "colors": [
            "fbe0c4",
            "8ab6d6",
            "2978b5",
            "0061a8"
        ]
    },
    {
        "id": "f0e3caff8303a357091b1a17",
        "tags": [
            "beige",
            "orange",
            "brown",
            "black",
            "skin",
            "warm",
            "gold",
            "coffee",
            "food",
            "summer",
            "sunset"
        ],
        "colors": [
            "f0e3ca",
            "ff8303",
            "a35709",
            "1b1a17"
        ]
    },
    {
        "id": "f8f5f1f8a4885aa89745526c",
        "tags": [
            "grey",
            "peach",
            "teal",
            "navy",
            "retro",
            "vintage",
            "kids",
            "fall",
            "earth"
        ],
        "colors": [
            "f8f5f1",
            "f8a488",
            "5aa897",
            "45526c"
        ]
    },
    {
        "id": "d8e3e751c4d3126e82132c33",
        "tags": [
            "grey",
            "blue",
            "navy",
            "cold",
            "winter",
            "night",
            "space"
        ],
        "colors": [
            "d8e3e7",
            "51c4d3",
            "126e82",
            "132c33"
        ]
    },
    {
        "id": "194350ff8882ffc2b49dbeb9",
        "tags": [
            "peach",
            "teal",
            "vintage",
            "wedding",
            "kids"
        ],
        "colors": [
            "194350",
            "ff8882",
            "ffc2b4",
            "9dbeb9"
        ]
    },
    {
        "id": "845460ead3cbbdc7c92b4f60",
        "tags": [
            "maroon",
            "grey",
            "vintage",
            "earth",
            "warm"
        ],
        "colors": [
            "845460",
            "ead3cb",
            "bdc7c9",
            "2b4f60"
        ]
    },
    {
        "id": "4b778d28b5b58fd9a8d2e69c",
        "tags": [
            "blue",
            "teal",
            "green",
            "summer",
            "nature",
            "happy",
            "sea"
        ],
        "colors": [
            "4b778d",
            "28b5b5",
            "8fd9a8",
            "d2e69c"
        ]
    },
    {
        "id": "206a5d81b214ffcc29f58634",
        "tags": [
            "green",
            "yellow",
            "orange",
            "summer",
            "spring",
            "nature",
            "food",
            "kids"
        ],
        "colors": [
            "206a5d",
            "81b214",
            "ffcc29",
            "f58634"
        ]
    },
    {
        "id": "98ddcad5ecc2ffd3b4ffaaa7",
        "tags": [
            "teal",
            "mint",
            "orange",
            "peach",
            "pastel",
            "spring",
            "light",
            "rainbow",
            "kids",
            "cream"
        ],
        "colors": [
            "98ddca",
            "d5ecc2",
            "ffd3b4",
            "ffaaa7"
        ]
    },
    {
        "id": "eeebddce12128100001b1717",
        "tags": [
            "beige",
            "red",
            "maroon",
            "black",
            "wedding"
        ],
        "colors": [
            "eeebdd",
            "ce1212",
            "810000",
            "1b1717"
        ]
    },
    {
        "id": "f8ede3bdd2b6a2b29f798777",
        "tags": [
            "beige",
            "sage",
            "grey",
            "pastel",
            "earth",
            "nature",
            "kids",
            "food",
            "light",
            "fall"
        ],
        "colors": [
            "f8ede3",
            "bdd2b6",
            "a2b29f",
            "798777"
        ]
    },
    {
        "id": "7b113a150e561597bb8fd6e1",
        "tags": [
            "maroon",
            "navy",
            "blue",
            "dark",
            "night",
            "winter"
        ],
        "colors": [
            "7b113a",
            "150e56",
            "1597bb",
            "8fd6e1"
        ]
    },
    {
        "id": "f7f3e9a3d2ca5eaaa8f05945",
        "tags": [
            "beige",
            "teal",
            "orange",
            "vintage",
            "kids",
            "cream",
            "summer"
        ],
        "colors": [
            "f7f3e9",
            "a3d2ca",
            "5eaaa8",
            "f05945"
        ]
    },
    {
        "id": "bfcba85b8a7256776c464f41",
        "tags": [
            "sage",
            "green",
            "earth",
            "nature",
            "winter",
            "vintage",
            "sea"
        ],
        "colors": [
            "bfcba8",
            "5b8a72",
            "56776c",
            "464f41"
        ]
    },
    {
        "id": "feffdeddffbc91c78852734d",
        "tags": [
            "green",
            "light",
            "summer",
            "neon",
            "nature",
            "spring"
        ],
        "colors": [
            "feffde",
            "ddffbc",
            "91c788",
            "52734d"
        ]
    },
    {
        "id": "2f5d62364547ffe268ffb037",
        "tags": [
            "teal",
            "yellow",
            "orange"
        ],
        "colors": [
            "2f5d62",
            "364547",
            "ffe268",
            "ffb037"
        ]
    },
    {
        "id": "5f939ad8ac9ceac8af1b2021",
        "tags": [
            "blue",
            "peach",
            "black",
            "skin",
            "vintage",
            "earth",
            "coffee"
        ],
        "colors": [
            "5f939a",
            "d8ac9c",
            "eac8af",
            "1b2021"
        ]
    },
    {
        "id": "1e6f5c28967229bb89e6dd3b",
        "tags": [
            "green",
            "yellow",
            "nature",
            "happy",
            "food",
            "summer"
        ],
        "colors": [
            "1e6f5c",
            "289672",
            "29bb89",
            "e6dd3b"
        ]
    },
    {
        "id": "864000d44000ff7a00ffefcf",
        "tags": [
            "brown",
            "red",
            "orange",
            "warm",
            "skin",
            "gold",
            "kids",
            "fall",
            "halloween",
            "food",
            "sunset",
            "gradient"
        ],
        "colors": [
            "864000",
            "d44000",
            "ff7a00",
            "ffefcf"
        ]
    },
    {
        "id": "184d4796bb7cfad586c64756",
        "tags": [
            "green",
            "yellow",
            "red",
            "spring",
            "rainbow",
            "kids",
            "summer",
            "food"
        ],
        "colors": [
            "184d47",
            "96bb7c",
            "fad586",
            "c64756"
        ]
    },
    {
        "id": "eeb76be2703a9c3d54310b0b",
        "tags": [
            "orange",
            "black",
            "skin",
            "gold",
            "dark",
            "fall",
            "halloween",
            "sunset",
            "night",
            "warm",
            "coffee"
        ],
        "colors": [
            "eeb76b",
            "e2703a",
            "9c3d54",
            "310b0b"
        ]
    },
    {
        "id": "9ede73f7ea00e48900be0000",
        "tags": [
            "green",
            "yellow",
            "orange",
            "red",
            "neon",
            "happy",
            "kids",
            "food",
            "spring",
            "rainbow",
            "summer"
        ],
        "colors": [
            "9ede73",
            "f7ea00",
            "e48900",
            "be0000"
        ]
    },
    {
        "id": "ffc93cdbf6e99ddfd331326f",
        "tags": [
            "yellow",
            "teal",
            "navy",
            "summer",
            "retro",
            "happy",
            "cold"
        ],
        "colors": [
            "ffc93c",
            "dbf6e9",
            "9ddfd3",
            "31326f"
        ]
    },
    {
        "id": "f3f4ed536162424642c06014",
        "tags": [
            "grey",
            "orange",
            "vintage",
            "winter",
            "space",
            "night",
            "wedding",
            "cold",
            "coffee",
            "cream"
        ],
        "colors": [
            "f3f4ed",
            "536162",
            "424642",
            "c06014"
        ]
    },
    {
        "id": "9e9d89e4d3cfe2bcb7b67162",
        "tags": [
            "sage",
            "grey",
            "pink",
            "peach",
            "skin",
            "pastel",
            "light",
            "coffee",
            "cream",
            "kids",
            "fall"
        ],
        "colors": [
            "9e9d89",
            "e4d3cf",
            "e2bcb7",
            "b67162"
        ]
    },
    {
        "id": "151515301b3f3c415cb4a5a5",
        "tags": [
            "black",
            "purple",
            "grey",
            "dark",
            "space",
            "night",
            "vintage",
            "halloween"
        ],
        "colors": [
            "151515",
            "301b3f",
            "3c415c",
            "b4a5a5"
        ]
    },
    {
        "id": "f8f5f1e9896a387c6d343f56",
        "tags": [
            "white",
            "orange",
            "teal",
            "navy",
            "retro",
            "kids"
        ],
        "colors": [
            "f8f5f1",
            "e9896a",
            "387c6d",
            "343f56"
        ]
    },
    {
        "id": "f8f4e18978534e3620c8eed9",
        "tags": [
            "beige",
            "brown",
            "teal",
            "vintage",
            "wedding",
            "earth",
            "winter"
        ],
        "colors": [
            "f8f4e1",
            "897853",
            "4e3620",
            "c8eed9"
        ]
    },
    {
        "id": "ccffbd7eca9c40394a1c1427",
        "tags": [
            "mint",
            "green",
            "black",
            "neon",
            "space",
            "nature",
            "cold"
        ],
        "colors": [
            "ccffbd",
            "7eca9c",
            "40394a",
            "1c1427"
        ]
    },
    {
        "id": "eeebdd8100006300001b1717",
        "tags": [
            "beige",
            "maroon",
            "black",
            "wedding",
            "coffee",
            "vintage",
            "christmas"
        ],
        "colors": [
            "eeebdd",
            "810000",
            "630000",
            "1b1717"
        ]
    },
    {
        "id": "fed049007580282846d8ebe4",
        "tags": [
            "yellow",
            "teal",
            "navy",
            "summer",
            "happy",
            "kids"
        ],
        "colors": [
            "fed049",
            "007580",
            "282846",
            "d8ebe4"
        ]
    },
    {
        "id": "caf7e3edffecf6dfebe4bad4",
        "tags": [
            "mint",
            "pink",
            "pastel",
            "light",
            "happy",
            "kids",
            "cream",
            "spring"
        ],
        "colors": [
            "caf7e3",
            "edffec",
            "f6dfeb",
            "e4bad4"
        ]
    },
    {
        "id": "f39189bb80826e7582046582",
        "tags": [
            "peach",
            "blue",
            "pastel",
            "night",
            "sunset",
            "fall"
        ],
        "colors": [
            "f39189",
            "bb8082",
            "6e7582",
            "046582"
        ]
    },
    {
        "id": "8658588e7f7fbbbbbbe2d5d5",
        "tags": [
            "coffee",
            "brown",
            "grey",
            "pastel",
            "cream",
            "winter",
            "vintage"
        ],
        "colors": [
            "865858",
            "8e7f7f",
            "bbbbbb",
            "e2d5d5"
        ]
    },
    {
        "id": "3a6351f2edd7e48257393232",
        "tags": [
            "green",
            "beige",
            "orange",
            "black",
            "retro",
            "kids"
        ],
        "colors": [
            "3a6351",
            "f2edd7",
            "e48257",
            "393232"
        ]
    },
    {
        "id": "cdc733966c3bd0af84ffe6ca",
        "tags": [
            "sage",
            "brown",
            "beige",
            "light",
            "summer",
            "food",
            "nature",
            "skin",
            "kids"
        ],
        "colors": [
            "cdc733",
            "966c3b",
            "d0af84",
            "ffe6ca"
        ]
    },
    {
        "id": "fbe6c2f0c929f48b29ac0d0d",
        "tags": [
            "beige",
            "yellow",
            "orange",
            "maroon",
            "warm",
            "summer",
            "sunset",
            "gold"
        ],
        "colors": [
            "fbe6c2",
            "f0c929",
            "f48b29",
            "ac0d0d"
        ]
    },
    {
        "id": "f0e4d7f5c0c0ff71719fd8df",
        "tags": [
            "beige",
            "pink",
            "blue",
            "pastel",
            "light",
            "kids",
            "vintage",
            "cream"
        ],
        "colors": [
            "f0e4d7",
            "f5c0c0",
            "ff7171",
            "9fd8df"
        ]
    },
    {
        "id": "1f441ecee6b49ecca49b3675",
        "tags": [
            "green",
            "purple",
            "retro",
            "nature",
            "winter",
            "kids"
        ],
        "colors": [
            "1f441e",
            "cee6b4",
            "9ecca4",
            "9b3675"
        ]
    },
    {
        "id": "693c72c15050d97642d49d42",
        "tags": [
            "purple",
            "red",
            "orange",
            "sunset",
            "rainbow",
            "retro"
        ],
        "colors": [
            "693c72",
            "c15050",
            "d97642",
            "d49d42"
        ]
    },
    {
        "id": "440a6793329eb4aee8ffe3fe",
        "tags": [
            "purple",
            "pink",
            "neon",
            "happy",
            "cold",
            "wedding",
            "space",
            "gradient"
        ],
        "colors": [
            "440a67",
            "93329e",
            "b4aee8",
            "ffe3fe"
        ]
    },
    {
        "id": "c8c6a792967d6e7c7c435560",
        "tags": [
            "sage",
            "grey",
            "navy",
            "pastel",
            "cold",
            "cream",
            "winter"
        ],
        "colors": [
            "c8c6a7",
            "92967d",
            "6e7c7c",
            "435560"
        ]
    },
    {
        "id": "e4fbffb8b5ff7868e6edeef7",
        "tags": [
            "blue",
            "purple",
            "grey",
            "neon",
            "light",
            "cold",
            "happy",
            "winter",
            "sky"
        ],
        "colors": [
            "e4fbff",
            "b8b5ff",
            "7868e6",
            "edeef7"
        ]
    },
    {
        "id": "26001b810034ff005cfff600",
        "tags": [
            "black",
            "maroon",
            "red",
            "yellow",
            "neon",
            "sunset",
            "space"
        ],
        "colors": [
            "26001b",
            "810034",
            "ff005c",
            "fff600"
        ]
    },
    {
        "id": "78c4d48f4f4fb7657bf2b4b4",
        "tags": [
            "blue",
            "brown",
            "peach",
            "vintage",
            "wedding",
            "skin",
            "kids"
        ],
        "colors": [
            "78c4d4",
            "8f4f4f",
            "b7657b",
            "f2b4b4"
        ]
    },
    {
        "id": "ddddddf9f3f3f7d9d9f25287",
        "tags": [
            "grey",
            "white",
            "pink",
            "skin",
            "light",
            "happy",
            "wedding",
            "cream"
        ],
        "colors": [
            "dddddd",
            "f9f3f3",
            "f7d9d9",
            "f25287"
        ]
    },
    {
        "id": "43352002595500917cfde8cd",
        "tags": [
            "brown",
            "green",
            "beige",
            "winter",
            "nature",
            "retro",
            "gradient"
        ],
        "colors": [
            "433520",
            "025955",
            "00917c",
            "fde8cd"
        ]
    },
    {
        "id": "8c0000bd2000fa1e0effbe0f",
        "tags": [
            "maroon",
            "red",
            "yellow",
            "warm",
            "sunset",
            "happy",
            "gold",
            "neon"
        ],
        "colors": [
            "8c0000",
            "bd2000",
            "fa1e0e",
            "ffbe0f"
        ]
    },
    {
        "id": "7638578f4068bfb051eff0b6",
        "tags": [
            "purple",
            "pastel",
            "retro",
            "wedding",
            "kids"
        ],
        "colors": [
            "763857",
            "8f4068",
            "bfb051",
            "eff0b6"
        ]
    },
    {
        "id": "ffab73ffd384fff9b0ffaec0",
        "tags": [
            "orange",
            "yellow",
            "pink",
            "light",
            "gold",
            "happy",
            "kids",
            "warm",
            "skin",
            "summer",
            "food"
        ],
        "colors": [
            "ffab73",
            "ffd384",
            "fff9b0",
            "ffaec0"
        ]
    },
    {
        "id": "aa2b1dcc561eef8d32beca5c",
        "tags": [
            "maroon",
            "red",
            "orange",
            "green",
            "warm",
            "food",
            "nature",
            "spring",
            "fall",
            "halloween",
            "christmas",
            "kids"
        ],
        "colors": [
            "aa2b1d",
            "cc561e",
            "ef8d32",
            "beca5c"
        ]
    },
    {
        "id": "28527a8ac4d0f4d160fbeeac",
        "tags": [
            "blue",
            "yellow",
            "summer",
            "happy"
        ],
        "colors": [
            "28527a",
            "8ac4d0",
            "f4d160",
            "fbeeac"
        ]
    },
    {
        "id": "4a3933f0a500e45826e6d5b8",
        "tags": [
            "black",
            "orange",
            "beige",
            "gold",
            "vintage",
            "warm",
            "night",
            "skin",
            "coffee"
        ],
        "colors": [
            "4a3933",
            "f0a500",
            "e45826",
            "e6d5b8"
        ]
    },
    {
        "id": "413c694a47a3709fb0a7c5eb",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "winter",
            "night",
            "sea"
        ],
        "colors": [
            "413c69",
            "4a47a3",
            "709fb0",
            "a7c5eb"
        ]
    },
    {
        "id": "f14668ffd8806b011f290149",
        "tags": [
            "pink",
            "yellow",
            "maroon",
            "navy",
            "retro"
        ],
        "colors": [
            "f14668",
            "ffd880",
            "6b011f",
            "290149"
        ]
    },
    {
        "id": "85603f9e7540bd9354e3d18a",
        "tags": [
            "brown",
            "pastel",
            "skin",
            "earth",
            "coffee",
            "nature",
            "warm",
            "fall",
            "food",
            "gradient"
        ],
        "colors": [
            "85603f",
            "9e7540",
            "bd9354",
            "e3d18a"
        ]
    },
    {
        "id": "e40017f4c9835b6d5b484018",
        "tags": [
            "red",
            "yellow",
            "vintage"
        ],
        "colors": [
            "e40017",
            "f4c983",
            "5b6d5b",
            "484018"
        ]
    },
    {
        "id": "ffcb91ffefa194ebcd6ddccf",
        "tags": [
            "orange",
            "yellow",
            "teal",
            "light",
            "spring",
            "happy",
            "kids",
            "summer"
        ],
        "colors": [
            "ffcb91",
            "ffefa1",
            "94ebcd",
            "6ddccf"
        ]
    },
    {
        "id": "ff75a0fce38aeaffd095e1d3",
        "tags": [
            "pink",
            "yellow",
            "teal",
            "summer",
            "light",
            "rainbow",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "ff75a0",
            "fce38a",
            "eaffd0",
            "95e1d3"
        ]
    },
    {
        "id": "c5d7bd9fb8ad383e56fb743e",
        "tags": [
            "green",
            "navy",
            "orange",
            "winter",
            "nature",
            "fall",
            "vintage"
        ],
        "colors": [
            "c5d7bd",
            "9fb8ad",
            "383e56",
            "fb743e"
        ]
    },
    {
        "id": "a1cae2c2b092cfc5a5eae3c8",
        "tags": [
            "blue",
            "brown",
            "beige",
            "pastel",
            "light",
            "earth",
            "skin",
            "cream",
            "fall",
            "kids"
        ],
        "colors": [
            "a1cae2",
            "c2b092",
            "cfc5a5",
            "eae3c8"
        ]
    },
    {
        "id": "faf3e0eabf9fb689731e212d",
        "tags": [
            "beige",
            "peach",
            "brown",
            "navy",
            "skin",
            "coffee",
            "winter",
            "wedding",
            "gold"
        ],
        "colors": [
            "faf3e0",
            "eabf9f",
            "b68973",
            "1e212d"
        ]
    },
    {
        "id": "99bbadebd8b7c6a9a39a8194",
        "tags": [
            "teal",
            "beige",
            "purple",
            "pastel",
            "vintage",
            "kids",
            "cream"
        ],
        "colors": [
            "99bbad",
            "ebd8b7",
            "c6a9a3",
            "9a8194"
        ]
    },
    {
        "id": "91091eda723cc39e5cfdf1d6",
        "tags": [
            "maroon",
            "red",
            "orange",
            "brown",
            "beige",
            "warm",
            "food",
            "coffee",
            "sunset",
            "halloween",
            "fall"
        ],
        "colors": [
            "91091e",
            "da723c",
            "c39e5c",
            "fdf1d6"
        ]
    },
    {
        "id": "822659b34180e36baef8a1d1",
        "tags": [
            "purple",
            "pink",
            "space",
            "wedding",
            "happy"
        ],
        "colors": [
            "822659",
            "b34180",
            "e36bae",
            "f8a1d1"
        ]
    },
    {
        "id": "f4f9f9ccf2f4a4ebf3aaaaaa",
        "tags": [
            "white",
            "blue",
            "grey",
            "light",
            "cold",
            "winter",
            "vintage",
            "kids",
            "sky"
        ],
        "colors": [
            "f4f9f9",
            "ccf2f4",
            "a4ebf3",
            "aaaaaa"
        ]
    },
    {
        "id": "f4f9f9f1d1d0fbacccf875aa",
        "tags": [
            "white",
            "peach",
            "pink",
            "light",
            "skin",
            "kids",
            "spring",
            "wedding"
        ],
        "colors": [
            "f4f9f9",
            "f1d1d0",
            "fbaccc",
            "f875aa"
        ]
    },
    {
        "id": "e7e6e1f7f6e7f2a154314e52",
        "tags": [
            "grey",
            "beige",
            "orange",
            "navy",
            "gold",
            "cream",
            "winter",
            "fall"
        ],
        "colors": [
            "e7e6e1",
            "f7f6e7",
            "f2a154",
            "314e52"
        ]
    },
    {
        "id": "ffee93f5d782e978789b5151",
        "tags": [
            "yellow",
            "red",
            "warm",
            "happy",
            "food"
        ],
        "colors": [
            "ffee93",
            "f5d782",
            "e97878",
            "9b5151"
        ]
    },
    {
        "id": "d8c2925b5b5bb67171c19065",
        "tags": [
            "brown",
            "grey",
            "vintage",
            "earth",
            "food",
            "winter"
        ],
        "colors": [
            "d8c292",
            "5b5b5b",
            "b67171",
            "c19065"
        ]
    },
    {
        "id": "f6f6f6c7ffd898ded9161d6f",
        "tags": [
            "white",
            "grey",
            "mint",
            "teal",
            "blue",
            "navy",
            "neon",
            "light",
            "kids"
        ],
        "colors": [
            "f6f6f6",
            "c7ffd8",
            "98ded9",
            "161d6f"
        ]
    },
    {
        "id": "ff9292ffb4b4ffdcdcffe8e8",
        "tags": [
            "peach",
            "pink",
            "skin",
            "light",
            "cream",
            "spring",
            "kids"
        ],
        "colors": [
            "ff9292",
            "ffb4b4",
            "ffdcdc",
            "ffe8e8"
        ]
    },
    {
        "id": "fcd1d1ece2e1d3e0dcaee1e1",
        "tags": [
            "pink",
            "peach",
            "teal",
            "pastel",
            "light",
            "kids",
            "cream",
            "vintage",
            "sky"
        ],
        "colors": [
            "fcd1d1",
            "ece2e1",
            "d3e0dc",
            "aee1e1"
        ]
    },
    {
        "id": "845ec2ffc75ff9f871ff5e78",
        "tags": [
            "purple",
            "orange",
            "yellow",
            "neon",
            "rainbow",
            "happy",
            "summer"
        ],
        "colors": [
            "845ec2",
            "ffc75f",
            "f9f871",
            "ff5e78"
        ]
    },
    {
        "id": "94b5c0350b40ad6c80ee99a0",
        "tags": [
            "blue",
            "navy",
            "peach",
            "vintage",
            "space",
            "winter",
            "retro"
        ],
        "colors": [
            "94b5c0",
            "350b40",
            "ad6c80",
            "ee99a0"
        ]
    },
    {
        "id": "75cfb8bbdfc8f0e5d8ffc478",
        "tags": [
            "mint",
            "green",
            "beige",
            "orange",
            "summer",
            "light",
            "nature",
            "kids"
        ],
        "colors": [
            "75cfb8",
            "bbdfc8",
            "f0e5d8",
            "ffc478"
        ]
    },
    {
        "id": "f6f5f5d3e0ea1687a7276678",
        "tags": [
            "white",
            "grey",
            "blue",
            "cold",
            "winter",
            "wedding"
        ],
        "colors": [
            "f6f5f5",
            "d3e0ea",
            "1687a7",
            "276678"
        ]
    },
    {
        "id": "f8f1f1a3d2ca5eaaa8eb5e0b",
        "tags": [
            "white",
            "teal",
            "orange",
            "retro",
            "kids"
        ],
        "colors": [
            "f8f1f1",
            "a3d2ca",
            "5eaaa8",
            "eb5e0b"
        ]
    },
    {
        "id": "0a043c03506fa3ddcbffe3de",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "0a043c",
            "03506f",
            "a3ddcb",
            "ffe3de"
        ]
    },
    {
        "id": "62959cc19277e1bc91e3d0b9",
        "tags": [
            "teal",
            "brown",
            "beige",
            "vintage",
            "earth",
            "coffee",
            "skin"
        ],
        "colors": [
            "62959c",
            "c19277",
            "e1bc91",
            "e3d0b9"
        ]
    },
    {
        "id": "351f39726a95719fb0a0c1b8",
        "tags": [
            "purple",
            "blue",
            "retro",
            "night",
            "cold",
            "dark"
        ],
        "colors": [
            "351f39",
            "726a95",
            "719fb0",
            "a0c1b8"
        ]
    },
    {
        "id": "a6f0c6a98b984e3d530f1123",
        "tags": [
            "mint",
            "green",
            "purple",
            "black",
            "retro",
            "space"
        ],
        "colors": [
            "a6f0c6",
            "a98b98",
            "4e3d53",
            "0f1123"
        ]
    },
    {
        "id": "49332391684aeaac7fffdf91",
        "tags": [
            "brown",
            "peach",
            "yellow",
            "warm",
            "skin",
            "coffee",
            "summer",
            "sunset",
            "vintage"
        ],
        "colors": [
            "493323",
            "91684a",
            "eaac7f",
            "ffdf91"
        ]
    },
    {
        "id": "f7f7e8c7cfb79dad7f557174",
        "tags": [
            "sage",
            "teal",
            "pastel",
            "nature",
            "cold",
            "cream",
            "food"
        ],
        "colors": [
            "f7f7e8",
            "c7cfb7",
            "9dad7f",
            "557174"
        ]
    },
    {
        "id": "f4f5dbd9dab0487e9523689b",
        "tags": [
            "blue",
            "summer",
            "kids",
            "cream"
        ],
        "colors": [
            "f4f5db",
            "d9dab0",
            "487e95",
            "23689b"
        ]
    },
    {
        "id": "ec4646663f3f51c2d5bbf1fa",
        "tags": [
            "red",
            "brown",
            "blue",
            "wedding",
            "kids"
        ],
        "colors": [
            "ec4646",
            "663f3f",
            "51c2d5",
            "bbf1fa"
        ]
    },
    {
        "id": "ffe227eb596e4d375d121013",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "black",
            "sunset",
            "neon",
            "space"
        ],
        "colors": [
            "ffe227",
            "eb596e",
            "4d375d",
            "121013"
        ]
    },
    {
        "id": "2525256930c364dfdf80ffdb",
        "tags": [
            "black",
            "purple",
            "teal",
            "mint",
            "neon",
            "space"
        ],
        "colors": [
            "252525",
            "6930c3",
            "64dfdf",
            "80ffdb"
        ]
    },
    {
        "id": "f8f1f111698e19456b16c79a",
        "tags": [
            "white",
            "blue",
            "navy",
            "green",
            "winter",
            "kids",
            "retro"
        ],
        "colors": [
            "f8f1f1",
            "11698e",
            "19456b",
            "16c79a"
        ]
    },
    {
        "id": "f8dc81eff7e1a2d0c1214151",
        "tags": [
            "yellow",
            "teal",
            "navy",
            "happy",
            "summer"
        ],
        "colors": [
            "f8dc81",
            "eff7e1",
            "a2d0c1",
            "214151"
        ]
    },
    {
        "id": "bee5d3d6b0b18b5e833b5360",
        "tags": [
            "mint",
            "peach",
            "purple",
            "navy",
            "pastel",
            "vintage",
            "cream",
            "fall"
        ],
        "colors": [
            "bee5d3",
            "d6b0b1",
            "8b5e83",
            "3b5360"
        ]
    },
    {
        "id": "09015faf006955b3b1f6c065",
        "tags": [
            "navy",
            "maroon",
            "teal",
            "yellow",
            "kids",
            "happy",
            "space",
            "sunset"
        ],
        "colors": [
            "09015f",
            "af0069",
            "55b3b1",
            "f6c065"
        ]
    },
    {
        "id": "00af91007965f58634ffcc29",
        "tags": [
            "green",
            "teal",
            "orange",
            "yellow",
            "neon",
            "food",
            "happy"
        ],
        "colors": [
            "00af91",
            "007965",
            "f58634",
            "ffcc29"
        ]
    },
    {
        "id": "fff3e61a508b0d335dc1a1d3",
        "tags": [
            "beige",
            "blue",
            "navy",
            "purple",
            "wedding",
            "retro"
        ],
        "colors": [
            "fff3e6",
            "1a508b",
            "0d335d",
            "c1a1d3"
        ]
    },
    {
        "id": "312c5148426df0c38ef1aa9b",
        "tags": [
            "navy",
            "peach",
            "night"
        ],
        "colors": [
            "312c51",
            "48426d",
            "f0c38e",
            "f1aa9b"
        ]
    },
    {
        "id": "f88f01e278026a492b58391c",
        "tags": [
            "orange",
            "brown",
            "warm",
            "gold",
            "coffee",
            "kids",
            "skin",
            "fall"
        ],
        "colors": [
            "f88f01",
            "e27802",
            "6a492b",
            "58391c"
        ]
    },
    {
        "id": "fdffbcffeebbffdcb8ffc1b6",
        "tags": [
            "yellow",
            "peach",
            "light",
            "pastel",
            "summer",
            "kids",
            "cream",
            "skin"
        ],
        "colors": [
            "fdffbc",
            "ffeebb",
            "ffdcb8",
            "ffc1b6"
        ]
    },
    {
        "id": "184d4796bb7cd6efc7fad586",
        "tags": [
            "teal",
            "green",
            "orange",
            "spring",
            "nature",
            "kids",
            "vintage"
        ],
        "colors": [
            "184d47",
            "96bb7c",
            "d6efc7",
            "fad586"
        ]
    },
    {
        "id": "ff577fff884bffc764cdfffc",
        "tags": [
            "pink",
            "orange",
            "yellow",
            "blue",
            "light",
            "neon",
            "rainbow",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "ff577f",
            "ff884b",
            "ffc764",
            "cdfffc"
        ]
    },
    {
        "id": "2c061f374045d89216e1d89f",
        "tags": [
            "black",
            "orange",
            "warm",
            "vintage",
            "dark",
            "coffee",
            "earth",
            "night"
        ],
        "colors": [
            "2c061f",
            "374045",
            "d89216",
            "e1d89f"
        ]
    },
    {
        "id": "295939e9b0dfadeecfe8efeb",
        "tags": [
            "green",
            "pink",
            "mint",
            "retro",
            "kids",
            "vintage",
            "cream"
        ],
        "colors": [
            "295939",
            "e9b0df",
            "adeecf",
            "e8efeb"
        ]
    },
    {
        "id": "fde8cd43352000917cdfe0df",
        "tags": [
            "beige",
            "brown",
            "green",
            "grey",
            "earth",
            "wedding",
            "vintage"
        ],
        "colors": [
            "fde8cd",
            "433520",
            "00917c",
            "dfe0df"
        ]
    },
    {
        "id": "7c9473cfdac8e8eae6cdd0cb",
        "tags": [
            "sage",
            "grey",
            "pastel",
            "cream",
            "light",
            "winter",
            "cold"
        ],
        "colors": [
            "7c9473",
            "cfdac8",
            "e8eae6",
            "cdd0cb"
        ]
    },
    {
        "id": "ff7b54ffb26bffd56b939b62",
        "tags": [
            "peach",
            "orange",
            "yellow",
            "green",
            "sage",
            "warm",
            "food",
            "nature",
            "happy",
            "summer"
        ],
        "colors": [
            "ff7b54",
            "ffb26b",
            "ffd56b",
            "939b62"
        ]
    },
    {
        "id": "dddddd22283130475ef05454",
        "tags": [
            "grey",
            "navy",
            "red",
            "space",
            "cold",
            "dark"
        ],
        "colors": [
            "dddddd",
            "222831",
            "30475e",
            "f05454"
        ]
    },
    {
        "id": "e7e7de00889100587a0f3057",
        "tags": [
            "grey",
            "teal",
            "blue",
            "navy",
            "cold",
            "winter"
        ],
        "colors": [
            "e7e7de",
            "008891",
            "00587a",
            "0f3057"
        ]
    },
    {
        "id": "ef4f4fee9595ffcda374c7b8",
        "tags": [
            "red",
            "pink",
            "peach",
            "beige",
            "teal",
            "spring",
            "happy",
            "kids",
            "food",
            "rainbow"
        ],
        "colors": [
            "ef4f4f",
            "ee9595",
            "ffcda3",
            "74c7b8"
        ]
    },
    {
        "id": "e7d9ea11698e19456b16c79a",
        "tags": [
            "purple",
            "blue",
            "navy",
            "green",
            "winter",
            "cold",
            "space",
            "kids",
            "sea"
        ],
        "colors": [
            "e7d9ea",
            "11698e",
            "19456b",
            "16c79a"
        ]
    },
    {
        "id": "f5f4f4cae4dbcdac8100303f",
        "tags": [
            "white",
            "grey",
            "teal",
            "brown",
            "navy",
            "vintage",
            "wedding",
            "earth",
            "winter",
            "fall"
        ],
        "colors": [
            "f5f4f4",
            "cae4db",
            "cdac81",
            "00303f"
        ]
    },
    {
        "id": "6f9eafa9294fc7753df6d887",
        "tags": [
            "blue",
            "maroon",
            "brown",
            "beige",
            "retro",
            "kids"
        ],
        "colors": [
            "6f9eaf",
            "a9294f",
            "c7753d",
            "f6d887"
        ]
    },
    {
        "id": "111d5ec70039f37121c0e218",
        "tags": [
            "navy",
            "maroon",
            "orange",
            "green",
            "neon",
            "rainbow",
            "kids",
            "space"
        ],
        "colors": [
            "111d5e",
            "c70039",
            "f37121",
            "c0e218"
        ]
    },
    {
        "id": "a3ddcbe8e9a1e6b566e5707e",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "red",
            "pink",
            "pastel",
            "rainbow",
            "happy",
            "kids",
            "summer",
            "light"
        ],
        "colors": [
            "a3ddcb",
            "e8e9a1",
            "e6b566",
            "e5707e"
        ]
    },
    {
        "id": "fcf8e8d4e2d4ecb390df7861",
        "tags": [
            "beige",
            "teal",
            "peach",
            "vintage",
            "pastel",
            "wedding",
            "light",
            "cream"
        ],
        "colors": [
            "fcf8e8",
            "d4e2d4",
            "ecb390",
            "df7861"
        ]
    },
    {
        "id": "cc7351e08f62ded7b19dab86",
        "tags": [
            "brown",
            "orange",
            "sage",
            "pastel",
            "skin",
            "earth",
            "nature",
            "food",
            "kids",
            "fall",
            "vintage"
        ],
        "colors": [
            "cc7351",
            "e08f62",
            "ded7b1",
            "9dab86"
        ]
    },
    {
        "id": "f8f1f1a3d2ca5eaaa8db6400",
        "tags": [
            "grey",
            "teal",
            "orange",
            "retro"
        ],
        "colors": [
            "f8f1f1",
            "a3d2ca",
            "5eaaa8",
            "db6400"
        ]
    },
    {
        "id": "583d729f5f80ffba93ff8e71",
        "tags": [
            "purple",
            "peach",
            "sunset",
            "skin"
        ],
        "colors": [
            "583d72",
            "9f5f80",
            "ffba93",
            "ff8e71"
        ]
    },
    {
        "id": "c6ebc970af85f0e2d0aa8976",
        "tags": [
            "green",
            "beige",
            "brown",
            "pastel",
            "nature",
            "kids",
            "light"
        ],
        "colors": [
            "c6ebc9",
            "70af85",
            "f0e2d0",
            "aa8976"
        ]
    },
    {
        "id": "433d3c944e6ce9c49683a95c",
        "tags": [
            "grey",
            "purple",
            "beige",
            "green",
            "vintage"
        ],
        "colors": [
            "433d3c",
            "944e6c",
            "e9c496",
            "83a95c"
        ]
    },
    {
        "id": "cd5d7df6ecf0a7c5eb949cdf",
        "tags": [
            "red",
            "blue",
            "pastel",
            "kids",
            "light"
        ],
        "colors": [
            "cd5d7d",
            "f6ecf0",
            "a7c5eb",
            "949cdf"
        ]
    },
    {
        "id": "654062ffd66bff9d72f4f4f4",
        "tags": [
            "purple",
            "yellow",
            "orange",
            "peach",
            "grey",
            "happy"
        ],
        "colors": [
            "654062",
            "ffd66b",
            "ff9d72",
            "f4f4f4"
        ]
    },
    {
        "id": "fa957965406265d6ceffe9d6",
        "tags": [
            "orange",
            "peach",
            "purple",
            "teal",
            "beige",
            "retro",
            "happy"
        ],
        "colors": [
            "fa9579",
            "654062",
            "65d6ce",
            "ffe9d6"
        ]
    },
    {
        "id": "ffe5b9eff8ffc9cbffa6a9b6",
        "tags": [
            "yellow",
            "white",
            "grey",
            "light",
            "summer",
            "pastel",
            "kids",
            "vintage"
        ],
        "colors": [
            "ffe5b9",
            "eff8ff",
            "c9cbff",
            "a6a9b6"
        ]
    },
    {
        "id": "ffe6e6ffabe1a685e26155a6",
        "tags": [
            "peach",
            "pink",
            "purple",
            "pastel",
            "kids",
            "spring",
            "gradient"
        ],
        "colors": [
            "ffe6e6",
            "ffabe1",
            "a685e2",
            "6155a6"
        ]
    },
    {
        "id": "ff4646ff8585ffb396fff5c0",
        "tags": [
            "red",
            "orange",
            "yellow",
            "warm",
            "light",
            "sunset",
            "happy"
        ],
        "colors": [
            "ff4646",
            "ff8585",
            "ffb396",
            "fff5c0"
        ]
    },
    {
        "id": "d68060f1ae89dff3e386aba1",
        "tags": [
            "orange",
            "peach",
            "teal",
            "pastel",
            "summer",
            "nature",
            "earth",
            "fall",
            "kids",
            "food"
        ],
        "colors": [
            "d68060",
            "f1ae89",
            "dff3e3",
            "86aba1"
        ]
    },
    {
        "id": "f1f1f1fdb82721209c23120b",
        "tags": [
            "grey",
            "white",
            "yellow",
            "blue",
            "black",
            "neon",
            "space"
        ],
        "colors": [
            "f1f1f1",
            "fdb827",
            "21209c",
            "23120b"
        ]
    },
    {
        "id": "e6e6e6c5a880532e1c0f0f0f",
        "tags": [
            "grey",
            "brown",
            "black",
            "vintage",
            "earth",
            "coffee",
            "skin",
            "night",
            "gold"
        ],
        "colors": [
            "e6e6e6",
            "c5a880",
            "532e1c",
            "0f0f0f"
        ]
    },
    {
        "id": "fff3b2ffe0d8ff9b9341584b",
        "tags": [
            "yellow",
            "pink",
            "peach",
            "food"
        ],
        "colors": [
            "fff3b2",
            "ffe0d8",
            "ff9b93",
            "41584b"
        ]
    },
    {
        "id": "f3f2da4e8d7c045762ea97ad",
        "tags": [
            "green",
            "pink",
            "vintage",
            "nature",
            "food",
            "kids"
        ],
        "colors": [
            "f3f2da",
            "4e8d7c",
            "045762",
            "ea97ad"
        ]
    },
    {
        "id": "999b84d8ac9cefd9d1f4eeed",
        "tags": [
            "sage",
            "pink",
            "beige",
            "pastel",
            "light",
            "skin",
            "coffee",
            "cream",
            "nature",
            "winter",
            "wedding",
            "food",
            "gradient"
        ],
        "colors": [
            "999b84",
            "d8ac9c",
            "efd9d1",
            "f4eeed"
        ]
    },
    {
        "id": "fcf8ecd0e8f279a3b1456268",
        "tags": [
            "beige",
            "blue",
            "navy",
            "light",
            "winter",
            "cold",
            "sky"
        ],
        "colors": [
            "fcf8ec",
            "d0e8f2",
            "79a3b1",
            "456268"
        ]
    },
    {
        "id": "bedcfa98acf8b088f9da9ff9",
        "tags": [
            "blue",
            "purple",
            "happy",
            "light"
        ],
        "colors": [
            "bedcfa",
            "98acf8",
            "b088f9",
            "da9ff9"
        ]
    },
    {
        "id": "f9e0aefc8621c24914682c0e",
        "tags": [
            "yellow",
            "orange",
            "brown",
            "maroon",
            "warm",
            "skin",
            "gold",
            "coffee",
            "fall"
        ],
        "colors": [
            "f9e0ae",
            "fc8621",
            "c24914",
            "682c0e"
        ]
    },
    {
        "id": "153e900e49b554e346fffaa4",
        "tags": [
            "navy",
            "blue",
            "green",
            "yellow",
            "neon",
            "happy",
            "kids",
            "winter"
        ],
        "colors": [
            "153e90",
            "0e49b5",
            "54e346",
            "fffaa4"
        ]
    },
    {
        "id": "a076768259598ad7c1c6fced",
        "tags": [
            "brown",
            "teal",
            "vintage",
            "cream",
            "earth",
            "kids"
        ],
        "colors": [
            "a07676",
            "825959",
            "8ad7c1",
            "c6fced"
        ]
    },
    {
        "id": "0a043c03506fbbbbbbffe3d8",
        "tags": [
            "navy",
            "grey",
            "peach",
            "wedding",
            "vintage",
            "night",
            "dark"
        ],
        "colors": [
            "0a043c",
            "03506f",
            "bbbbbb",
            "ffe3d8"
        ]
    },
    {
        "id": "f8f7ded1c145d08752c75643",
        "tags": [
            "yellow",
            "orange",
            "red",
            "warm",
            "summer",
            "gold",
            "retro"
        ],
        "colors": [
            "f8f7de",
            "d1c145",
            "d08752",
            "c75643"
        ]
    },
    {
        "id": "61b15aadce74fff76affce89",
        "tags": [
            "green",
            "yellow",
            "orange",
            "summer",
            "light",
            "food",
            "nature",
            "happy"
        ],
        "colors": [
            "61b15a",
            "adce74",
            "fff76a",
            "ffce89"
        ]
    },
    {
        "id": "d35d6eefb08cf8d49d5aa469",
        "tags": [
            "red",
            "peach",
            "beige",
            "green",
            "retro",
            "pastel",
            "kids",
            "food",
            "summer"
        ],
        "colors": [
            "d35d6e",
            "efb08c",
            "f8d49d",
            "5aa469"
        ]
    },
    {
        "id": "f2d974c7956d965d62534e52",
        "tags": [
            "yellow",
            "brown",
            "maroon",
            "summer",
            "warm",
            "coffee",
            "gold",
            "fall"
        ],
        "colors": [
            "f2d974",
            "c7956d",
            "965d62",
            "534e52"
        ]
    },
    {
        "id": "222831393e46ffd369eeeeee",
        "tags": [
            "black",
            "yellow",
            "grey",
            "space",
            "night",
            "dark",
            "neon"
        ],
        "colors": [
            "222831",
            "393e46",
            "ffd369",
            "eeeeee"
        ]
    },
    {
        "id": "16697adb6400ffa62bf8f1f1",
        "tags": [
            "teal",
            "orange",
            "grey",
            "white",
            "gold",
            "vintage",
            "kids"
        ],
        "colors": [
            "16697a",
            "db6400",
            "ffa62b",
            "f8f1f1"
        ]
    },
    {
        "id": "bedbbb8db59692817a707070",
        "tags": [
            "sage",
            "green",
            "brown",
            "grey",
            "pastel",
            "vintage",
            "nature"
        ],
        "colors": [
            "bedbbb",
            "8db596",
            "92817a",
            "707070"
        ]
    },
    {
        "id": "59886bc05555ffc85cfff8c1",
        "tags": [
            "sage",
            "red",
            "orange",
            "yellow",
            "retro",
            "rainbow",
            "vintage",
            "kids"
        ],
        "colors": [
            "59886b",
            "c05555",
            "ffc85c",
            "fff8c1"
        ]
    },
    {
        "id": "1200789d0191fd3a69fecd1a",
        "tags": [
            "navy",
            "purple",
            "pink",
            "yellow",
            "neon",
            "space",
            "happy",
            "gradient"
        ],
        "colors": [
            "120078",
            "9d0191",
            "fd3a69",
            "fecd1a"
        ]
    },
    {
        "id": "ffa45bffda77fbf6f0aee6e6",
        "tags": [
            "orange",
            "yellow",
            "teal",
            "white",
            "light",
            "summer",
            "food",
            "kids",
            "happy",
            "gold"
        ],
        "colors": [
            "ffa45b",
            "ffda77",
            "fbf6f0",
            "aee6e6"
        ]
    },
    {
        "id": "bce6ebfdcfdffbbedffca3cc",
        "tags": [
            "blue",
            "pink",
            "kids",
            "light",
            "spring",
            "cream"
        ],
        "colors": [
            "bce6eb",
            "fdcfdf",
            "fbbedf",
            "fca3cc"
        ]
    },
    {
        "id": "ec5858fd8c04edf28593abd3",
        "tags": [
            "red",
            "orange",
            "yellow",
            "blue",
            "sunset",
            "rainbow",
            "kids",
            "happy",
            "summer"
        ],
        "colors": [
            "ec5858",
            "fd8c04",
            "edf285",
            "93abd3"
        ]
    },
    {
        "id": "f9f7cff2dcbbbbbbbbaaaaaa",
        "tags": [
            "yellow",
            "beige",
            "grey",
            "pastel",
            "light",
            "cream"
        ],
        "colors": [
            "f9f7cf",
            "f2dcbb",
            "bbbbbb",
            "aaaaaa"
        ]
    },
    {
        "id": "34626c839b97cfd3cec6b497",
        "tags": [
            "teal",
            "grey",
            "beige",
            "vintage",
            "winter",
            "earth",
            "pastel",
            "sea"
        ],
        "colors": [
            "34626c",
            "839b97",
            "cfd3ce",
            "c6b497"
        ]
    },
    {
        "id": "e8e8e8f0545430475e222831",
        "tags": [
            "grey",
            "red",
            "navy",
            "black",
            "retro",
            "space"
        ],
        "colors": [
            "e8e8e8",
            "f05454",
            "30475e",
            "222831"
        ]
    },
    {
        "id": "eeeded5c6e918f384ddd9866",
        "tags": [
            "grey",
            "blue",
            "navy",
            "maroon",
            "orange",
            "vintage"
        ],
        "colors": [
            "eeeded",
            "5c6e91",
            "8f384d",
            "dd9866"
        ]
    },
    {
        "id": "f2f4c0e4e978cad315d37815",
        "tags": [
            "yellow",
            "orange",
            "summer",
            "warm",
            "light",
            "food",
            "happy"
        ],
        "colors": [
            "f2f4c0",
            "e4e978",
            "cad315",
            "d37815"
        ]
    },
    {
        "id": "fff3e2ebcfc47068979088d4",
        "tags": [
            "beige",
            "peach",
            "navy",
            "skin",
            "cream",
            "wedding",
            "kids"
        ],
        "colors": [
            "fff3e2",
            "ebcfc4",
            "706897",
            "9088d4"
        ]
    },
    {
        "id": "556052af6b58cbbcb1f2efea",
        "tags": [
            "green",
            "orange",
            "brown",
            "grey",
            "beige",
            "vintage",
            "earth",
            "coffee",
            "winter"
        ],
        "colors": [
            "556052",
            "af6b58",
            "cbbcb1",
            "f2efea"
        ]
    },
    {
        "id": "ffdadadbf6e99ddfd331326f",
        "tags": [
            "pink",
            "teal",
            "navy",
            "wedding",
            "kids",
            "retro"
        ],
        "colors": [
            "ffdada",
            "dbf6e9",
            "9ddfd3",
            "31326f"
        ]
    },
    {
        "id": "fceef5f3bad6ea86b6e05297",
        "tags": [
            "pink",
            "kids",
            "happy"
        ],
        "colors": [
            "fceef5",
            "f3bad6",
            "ea86b6",
            "e05297"
        ]
    },
    {
        "id": "ea2c62ff9a8cfad5adadb36e",
        "tags": [
            "red",
            "peach",
            "beige",
            "green",
            "happy",
            "fall"
        ],
        "colors": [
            "ea2c62",
            "ff9a8c",
            "fad5ad",
            "adb36e"
        ]
    },
    {
        "id": "39311d7e7474c4b6b6ffdd93",
        "tags": [
            "black",
            "grey",
            "yellow",
            "night",
            "dark"
        ],
        "colors": [
            "39311d",
            "7e7474",
            "c4b6b6",
            "ffdd93"
        ]
    },
    {
        "id": "16a596898b8afae0dff6f5f1",
        "tags": [
            "teal",
            "grey",
            "pink",
            "white",
            "vintage"
        ],
        "colors": [
            "16a596",
            "898b8a",
            "fae0df",
            "f6f5f1"
        ]
    },
    {
        "id": "00000052057b892cdcbc6ff1",
        "tags": [
            "purple",
            "black",
            "dark",
            "neon",
            "night",
            "space",
            "cold"
        ],
        "colors": [
            "000000",
            "52057b",
            "892cdc",
            "bc6ff1"
        ]
    },
    {
        "id": "a20a0affa36cf6eec9799351",
        "tags": [
            "red",
            "maroon",
            "orange",
            "peach",
            "beige",
            "green",
            "christmas",
            "food",
            "happy"
        ],
        "colors": [
            "a20a0a",
            "ffa36c",
            "f6eec9",
            "799351"
        ]
    },
    {
        "id": "321f28734046a05344e79e4f",
        "tags": [
            "black",
            "brown",
            "orange",
            "warm",
            "halloween",
            "skin",
            "dark",
            "coffee",
            "night"
        ],
        "colors": [
            "321f28",
            "734046",
            "a05344",
            "e79e4f"
        ]
    },
    {
        "id": "9ad3bcf3eac2f5b461ec524b",
        "tags": [
            "teal",
            "beige",
            "orange",
            "red",
            "summer",
            "rainbow",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "9ad3bc",
            "f3eac2",
            "f5b461",
            "ec524b"
        ]
    },
    {
        "id": "aa3a3aa4b787f4f4f4f8e4b7",
        "tags": [
            "red",
            "green",
            "white",
            "beige",
            "christmas",
            "wedding",
            "vintage"
        ],
        "colors": [
            "aa3a3a",
            "a4b787",
            "f4f4f4",
            "f8e4b7"
        ]
    },
    {
        "id": "f4f4f2e8e8e8bbbfca495464",
        "tags": [
            "white",
            "grey",
            "navy",
            "cold",
            "winter",
            "cream"
        ],
        "colors": [
            "f4f4f2",
            "e8e8e8",
            "bbbfca",
            "495464"
        ]
    },
    {
        "id": "fcf1f1ffd5cdf9813a1a1c20",
        "tags": [
            "peach",
            "orange",
            "black",
            "skin",
            "warm",
            "kids"
        ],
        "colors": [
            "fcf1f1",
            "ffd5cd",
            "f9813a",
            "1a1c20"
        ]
    },
    {
        "id": "f4abc4595b83333456060930",
        "tags": [
            "pink",
            "navy",
            "black",
            "cold",
            "dark",
            "wedding",
            "night",
            "vintage"
        ],
        "colors": [
            "f4abc4",
            "595b83",
            "333456",
            "060930"
        ]
    },
    {
        "id": "214252f05454af2d2dce6262",
        "tags": [
            "navy",
            "red",
            "maroon",
            "retro",
            "space",
            "kids"
        ],
        "colors": [
            "214252",
            "f05454",
            "af2d2d",
            "ce6262"
        ]
    },
    {
        "id": "fcf876cee3978bcdcd3797a4",
        "tags": [
            "yellow",
            "green",
            "teal",
            "happy",
            "summer",
            "light",
            "neon"
        ],
        "colors": [
            "fcf876",
            "cee397",
            "8bcdcd",
            "3797a4"
        ]
    },
    {
        "id": "1c2b2d1f6f8b99a8b2e6d5b8",
        "tags": [
            "black",
            "blue",
            "beige",
            "cold",
            "winter",
            "night",
            "vintage",
            "gradient",
            "sea"
        ],
        "colors": [
            "1c2b2d",
            "1f6f8b",
            "99a8b2",
            "e6d5b8"
        ]
    },
    {
        "id": "92817abedbbb8db596707070",
        "tags": [
            "brown",
            "sage",
            "grey",
            "pastel",
            "earth",
            "winter",
            "food"
        ],
        "colors": [
            "92817a",
            "bedbbb",
            "8db596",
            "707070"
        ]
    },
    {
        "id": "ebebebf5a25dfa7f72389393",
        "tags": [
            "grey",
            "orange",
            "peach",
            "teal",
            "vintage",
            "kids",
            "retro"
        ],
        "colors": [
            "ebebeb",
            "f5a25d",
            "fa7f72",
            "389393"
        ]
    },
    {
        "id": "f1f6f914274e3948679ba4b4",
        "tags": [
            "white",
            "navy",
            "grey",
            "cold",
            "winter",
            "night",
            "wedding"
        ],
        "colors": [
            "f1f6f9",
            "14274e",
            "394867",
            "9ba4b4"
        ]
    },
    {
        "id": "f1d4d4e6739fcc0e74790c5a",
        "tags": [
            "peach",
            "pink",
            "purple",
            "warm",
            "kids"
        ],
        "colors": [
            "f1d4d4",
            "e6739f",
            "cc0e74",
            "790c5a"
        ]
    },
    {
        "id": "0000006a097dc060a1f1d4d4",
        "tags": [
            "black",
            "purple",
            "beige",
            "wedding",
            "night",
            "space",
            "dark",
            "gradient"
        ],
        "colors": [
            "000000",
            "6a097d",
            "c060a1",
            "f1d4d4"
        ]
    },
    {
        "id": "d2d3c90e918cf6830fbb2205",
        "tags": [
            "grey",
            "teal",
            "orange",
            "red",
            "maroon",
            "vintage",
            "kids"
        ],
        "colors": [
            "d2d3c9",
            "0e918c",
            "f6830f",
            "bb2205"
        ]
    },
    {
        "id": "28abb92d6187effad3a8dda8",
        "tags": [],
        "colors": [
            "28abb9",
            "2d6187",
            "effad3",
            "a8dda8"
        ]
    },
    {
        "id": "fff8cdffe05dff9642646464",
        "tags": [
            "yellow",
            "grey",
            "orange",
            "gold",
            "happy",
            "sunset"
        ],
        "colors": [
            "fff8cd",
            "ffe05d",
            "ff9642",
            "646464"
        ]
    },
    {
        "id": "01c5c4b8de6ff1e189f39233",
        "tags": [
            "teal",
            "green",
            "beige",
            "orange",
            "happy",
            "kids",
            "summer",
            "spring"
        ],
        "colors": [
            "01c5c4",
            "b8de6f",
            "f1e189",
            "f39233"
        ]
    },
    {
        "id": "968c83d6d2c4fff5eaf7dad9",
        "tags": [
            "brown",
            "grey",
            "pink",
            "light",
            "pastel",
            "coffee",
            "cream",
            "kids"
        ],
        "colors": [
            "968c83",
            "d6d2c4",
            "fff5ea",
            "f7dad9"
        ]
    },
    {
        "id": "f6f5f5ee6f571f3c88070d59",
        "tags": [
            "white",
            "orange",
            "blue",
            "navy",
            "space",
            "wedding",
            "kids"
        ],
        "colors": [
            "f6f5f5",
            "ee6f57",
            "1f3c88",
            "070d59"
        ]
    },
    {
        "id": "94b4a4d2f5e3e5c5b5f4d9c6",
        "tags": [
            "sage",
            "mint",
            "peach",
            "beige",
            "light",
            "nature",
            "happy",
            "vintage"
        ],
        "colors": [
            "94b4a4",
            "d2f5e3",
            "e5c5b5",
            "f4d9c6"
        ]
    },
    {
        "id": "794c74c56183fadcaab2deec",
        "tags": [
            "purple",
            "yellow",
            "blue",
            "sunset",
            "rainbow",
            "spring"
        ],
        "colors": [
            "794c74",
            "c56183",
            "fadcaa",
            "b2deec"
        ]
    },
    {
        "id": "eeeeee686d76373a4019d3da",
        "tags": [
            "grey",
            "black",
            "teal",
            "space"
        ],
        "colors": [
            "eeeeee",
            "686d76",
            "373a40",
            "19d3da"
        ]
    },
    {
        "id": "fcdadaffa5a55c969e3d7ea6",
        "tags": [
            "pink",
            "peach",
            "teal",
            "blue",
            "kids",
            "vintage"
        ],
        "colors": [
            "fcdada",
            "ffa5a5",
            "5c969e",
            "3d7ea6"
        ]
    },
    {
        "id": "f8efd4edc988d7385e132743",
        "tags": [
            "yellow",
            "beige",
            "red",
            "black",
            "retro",
            "space"
        ],
        "colors": [
            "f8efd4",
            "edc988",
            "d7385e",
            "132743"
        ]
    },
    {
        "id": "150485590995c62a8803c4a1",
        "tags": [
            "navy",
            "blue",
            "purple",
            "teal",
            "retro",
            "space",
            "kids",
            "dark"
        ],
        "colors": [
            "150485",
            "590995",
            "c62a88",
            "03c4a1"
        ]
    },
    {
        "id": "7579e79ab3f5a3d8f4b9fffc",
        "tags": [
            "blue",
            "teal",
            "light",
            "cold",
            "neon",
            "kids",
            "gradient",
            "sky"
        ],
        "colors": [
            "7579e7",
            "9ab3f5",
            "a3d8f4",
            "b9fffc"
        ]
    },
    {
        "id": "e8ffffa6f6f141aea9213e3b",
        "tags": [
            "teal",
            "neon",
            "cold",
            "winter"
        ],
        "colors": [
            "e8ffff",
            "a6f6f1",
            "41aea9",
            "213e3b"
        ]
    },
    {
        "id": "fff0f0ebd4d4835858463333",
        "tags": [
            "pink",
            "brown",
            "vintage",
            "wedding",
            "night",
            "earth",
            "cream"
        ],
        "colors": [
            "fff0f0",
            "ebd4d4",
            "835858",
            "463333"
        ]
    },
    {
        "id": "eeeeee32e0c40d7377212121",
        "tags": [
            "grey",
            "teal",
            "black",
            "neon",
            "space",
            "cold"
        ],
        "colors": [
            "eeeeee",
            "32e0c4",
            "0d7377",
            "212121"
        ]
    },
    {
        "id": "ccf6c8fafcc2f6d6adf9c0c0",
        "tags": [
            "green",
            "mint",
            "yellow",
            "beige",
            "orange",
            "peach",
            "pastel",
            "light",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "ccf6c8",
            "fafcc2",
            "f6d6ad",
            "f9c0c0"
        ]
    },
    {
        "id": "ffefa0ffd57efca652ac4b1c",
        "tags": [
            "yellow",
            "orange",
            "maroon",
            "gold",
            "warm",
            "happy",
            "summer"
        ],
        "colors": [
            "ffefa0",
            "ffd57e",
            "fca652",
            "ac4b1c"
        ]
    },
    {
        "id": "625261a6a6a4e8e8e889beb3",
        "tags": [
            "grey",
            "teal",
            "vintage",
            "winter"
        ],
        "colors": [
            "625261",
            "a6a6a4",
            "e8e8e8",
            "89beb3"
        ]
    },
    {
        "id": "ffd5cdefbbcfc3aed68675a9",
        "tags": [
            "peach",
            "pink",
            "purple",
            "skin",
            "pastel",
            "kids",
            "light"
        ],
        "colors": [
            "ffd5cd",
            "efbbcf",
            "c3aed6",
            "8675a9"
        ]
    },
    {
        "id": "726a95709fb0a0c1b8f4ebc1",
        "tags": [
            "purple",
            "teal",
            "yellow",
            "beige",
            "pastel",
            "retro",
            "gradient"
        ],
        "colors": [
            "726a95",
            "709fb0",
            "a0c1b8",
            "f4ebc1"
        ]
    },
    {
        "id": "f8efd4edc988de4463821752",
        "tags": [
            "beige",
            "red",
            "purple",
            "warm",
            "wedding",
            "kids",
            "retro"
        ],
        "colors": [
            "f8efd4",
            "edc988",
            "de4463",
            "821752"
        ]
    },
    {
        "id": "d9ecf2f56a79ff414d1aa6b7",
        "tags": [
            "blue",
            "red",
            "teal",
            "retro",
            "happy"
        ],
        "colors": [
            "d9ecf2",
            "f56a79",
            "ff414d",
            "1aa6b7"
        ]
    },
    {
        "id": "ff9a76ffeadb679b9b637373",
        "tags": [
            "orange",
            "beige",
            "teal",
            "retro",
            "kids",
            "fall"
        ],
        "colors": [
            "ff9a76",
            "ffeadb",
            "679b9b",
            "637373"
        ]
    },
    {
        "id": "f6f6f6ffe2e2ffc7c7aaaaaa",
        "tags": [
            "white",
            "grey",
            "peach",
            "pink",
            "light",
            "pastel",
            "kids",
            "cream"
        ],
        "colors": [
            "f6f6f6",
            "ffe2e2",
            "ffc7c7",
            "aaaaaa"
        ]
    },
    {
        "id": "ffcbcb70adb5407088132743",
        "tags": [
            "pink",
            "peach",
            "teal",
            "navy",
            "wedding",
            "retro"
        ],
        "colors": [
            "ffcbcb",
            "70adb5",
            "407088",
            "132743"
        ]
    },
    {
        "id": "931a25e97171ffcb8ef5efef",
        "tags": [
            "maroon",
            "red",
            "orange",
            "grey",
            "warm",
            "food",
            "happy",
            "gradient"
        ],
        "colors": [
            "931a25",
            "e97171",
            "ffcb8e",
            "f5efef"
        ]
    },
    {
        "id": "e5df88e8e8e8a37eba4c4c4c",
        "tags": [
            "yellow",
            "grey",
            "purple",
            "vintage"
        ],
        "colors": [
            "e5df88",
            "e8e8e8",
            "a37eba",
            "4c4c4c"
        ]
    },
    {
        "id": "ecf4f368b0ab006a71ff7e67",
        "tags": [
            "teal",
            "peach",
            "cold",
            "happy"
        ],
        "colors": [
            "ecf4f3",
            "68b0ab",
            "006a71",
            "ff7e67"
        ]
    },
    {
        "id": "d789d79d65c95d54a42a3d66",
        "tags": [
            "purple",
            "pink",
            "navy",
            "kids",
            "gradient"
        ],
        "colors": [
            "d789d7",
            "9d65c9",
            "5d54a4",
            "2a3d66"
        ]
    },
    {
        "id": "e7dec8cbaf877e8a9730475e",
        "tags": [
            "beige",
            "brown",
            "navy",
            "pastel",
            "warm",
            "gold",
            "coffee"
        ],
        "colors": [
            "e7dec8",
            "cbaf87",
            "7e8a97",
            "30475e"
        ]
    },
    {
        "id": "f4f4f4f0a500cf75001a1c20",
        "tags": [
            "white",
            "grey",
            "orange",
            "black",
            "gold"
        ],
        "colors": [
            "f4f4f4",
            "f0a500",
            "cf7500",
            "1a1c20"
        ]
    },
    {
        "id": "ffb0b0fe7171335d2d7ea04d",
        "tags": [
            "pink",
            "peach",
            "green",
            "spring",
            "happy",
            "kids",
            "nature"
        ],
        "colors": [
            "ffb0b0",
            "fe7171",
            "335d2d",
            "7ea04d"
        ]
    },
    {
        "id": "faf3dd64958f065c6fffbb91",
        "tags": [
            "beige",
            "teal",
            "orange",
            "vintage"
        ],
        "colors": [
            "faf3dd",
            "64958f",
            "065c6f",
            "ffbb91"
        ]
    },
    {
        "id": "28df9999f3bdd2f6c5f6f7d4",
        "tags": [
            "green",
            "mint",
            "beige",
            "neon",
            "light",
            "happy",
            "summer",
            "gradient"
        ],
        "colors": [
            "28df99",
            "99f3bd",
            "d2f6c5",
            "f6f7d4"
        ]
    },
    {
        "id": "1d2d50133b5c1e5f74fcdab7",
        "tags": [
            "blue",
            "navy",
            "beige",
            "dark",
            "night",
            "sea"
        ],
        "colors": [
            "1d2d50",
            "133b5c",
            "1e5f74",
            "fcdab7"
        ]
    },
    {
        "id": "2ec1ac3e978bd2e603eff48e",
        "tags": [
            "teal",
            "green",
            "neon",
            "summer",
            "nature",
            "happy"
        ],
        "colors": [
            "2ec1ac",
            "3e978b",
            "d2e603",
            "eff48e"
        ]
    },
    {
        "id": "e0ece4ff4b5c05667466bfbf",
        "tags": [
            "grey",
            "red",
            "teal",
            "space"
        ],
        "colors": [
            "e0ece4",
            "ff4b5c",
            "056674",
            "66bfbf"
        ]
    },
    {
        "id": "edcfa9e89f71d57149aa4a30",
        "tags": [
            "beige",
            "orange",
            "brown",
            "skin",
            "warm",
            "fall",
            "food",
            "cream"
        ],
        "colors": [
            "edcfa9",
            "e89f71",
            "d57149",
            "aa4a30"
        ]
    },
    {
        "id": "7d063331112cf2a07bfbdcc4",
        "tags": [
            "maroon",
            "black",
            "peach",
            "beige",
            "dark",
            "night",
            "vintage"
        ],
        "colors": [
            "7d0633",
            "31112c",
            "f2a07b",
            "fbdcc4"
        ]
    },
    {
        "id": "29000187431dc87941dbcbbd",
        "tags": [
            "brown",
            "orange",
            "gold",
            "warm",
            "dark",
            "coffee",
            "skin",
            "night",
            "gradient"
        ],
        "colors": [
            "290001",
            "87431d",
            "c87941",
            "dbcbbd"
        ]
    },
    {
        "id": "f6f6f6ffbb91ff8e6e515070",
        "tags": [
            "white",
            "grey",
            "orange",
            "navy",
            "kids"
        ],
        "colors": [
            "f6f6f6",
            "ffbb91",
            "ff8e6e",
            "515070"
        ]
    },
    {
        "id": "4e89ae43658bed6663ffa372",
        "tags": [
            "blue",
            "red",
            "peach",
            "orange",
            "retro"
        ],
        "colors": [
            "4e89ae",
            "43658b",
            "ed6663",
            "ffa372"
        ]
    },
    {
        "id": "f8bd7f00416df5f1dae3dfc8",
        "tags": [
            "orange",
            "navy",
            "beige",
            "summer",
            "wedding"
        ],
        "colors": [
            "f8bd7f",
            "00416d",
            "f5f1da",
            "e3dfc8"
        ]
    },
    {
        "id": "f1f3f8d6e0f08d93ab393b44",
        "tags": [
            "grey",
            "wedding",
            "winter",
            "cream"
        ],
        "colors": [
            "f1f3f8",
            "d6e0f0",
            "8d93ab",
            "393b44"
        ]
    },
    {
        "id": "ffc93c07689f40a8c4a2d5f2",
        "tags": [
            "yellow",
            "blue",
            "teal",
            "summer",
            "happy"
        ],
        "colors": [
            "ffc93c",
            "07689f",
            "40a8c4",
            "a2d5f2"
        ]
    },
    {
        "id": "f1f3deeb8f8fec0101cd0a0a",
        "tags": [
            "beige",
            "red",
            "peach",
            "kids"
        ],
        "colors": [
            "f1f3de",
            "eb8f8f",
            "ec0101",
            "cd0a0a"
        ]
    },
    {
        "id": "f6f5f514537400334eee6f57",
        "tags": [
            "white",
            "grey",
            "navy",
            "orange",
            "retro",
            "space"
        ],
        "colors": [
            "f6f5f5",
            "145374",
            "00334e",
            "ee6f57"
        ]
    },
    {
        "id": "206a5d81b214bfdcaef1f1e8",
        "tags": [
            "green",
            "summer",
            "nature",
            "happy",
            "food",
            "gradient"
        ],
        "colors": [
            "206a5d",
            "81b214",
            "bfdcae",
            "f1f1e8"
        ]
    },
    {
        "id": "1a1a2e16213e0f3460e94560",
        "tags": [
            "black",
            "navy",
            "red",
            "dark",
            "space",
            "night"
        ],
        "colors": [
            "1a1a2e",
            "16213e",
            "0f3460",
            "e94560"
        ]
    },
    {
        "id": "557571d49a89f7d1baf4f4f4",
        "tags": [
            "green",
            "peach",
            "white",
            "grey",
            "pastel",
            "vintage",
            "warm",
            "light",
            "earth",
            "food",
            "fall"
        ],
        "colors": [
            "557571",
            "d49a89",
            "f7d1ba",
            "f4f4f4"
        ]
    },
    {
        "id": "e8ded2a3d2ca5eaaa8056676",
        "tags": [
            "beige",
            "teal",
            "vintage",
            "pastel",
            "winter",
            "sea"
        ],
        "colors": [
            "e8ded2",
            "a3d2ca",
            "5eaaa8",
            "056676"
        ]
    },
    {
        "id": "2d4059ea5455decdc3e5e5e5",
        "tags": [
            "navy",
            "red",
            "beige",
            "grey",
            "vintage",
            "space"
        ],
        "colors": [
            "2d4059",
            "ea5455",
            "decdc3",
            "e5e5e5"
        ]
    },
    {
        "id": "ff7171ffaa716e6d6dececec",
        "tags": [
            "red",
            "peach",
            "orange",
            "grey"
        ],
        "colors": [
            "ff7171",
            "ffaa71",
            "6e6d6d",
            "ececec"
        ]
    },
    {
        "id": "fbecec91d18be11d74440047",
        "tags": [
            "peach",
            "green",
            "pink",
            "purple",
            "retro",
            "happy",
            "spring"
        ],
        "colors": [
            "fbecec",
            "91d18b",
            "e11d74",
            "440047"
        ]
    },
    {
        "id": "f6f4e6fddb3a52575d41444b",
        "tags": [
            "beige",
            "yellow",
            "grey"
        ],
        "colors": [
            "f6f4e6",
            "fddb3a",
            "52575d",
            "41444b"
        ]
    },
    {
        "id": "fabea7fbe2e59cada4767c77",
        "tags": [
            "orange",
            "peach",
            "pink",
            "green",
            "pastel",
            "vintage",
            "light",
            "food",
            "fall",
            "kids"
        ],
        "colors": [
            "fabea7",
            "fbe2e5",
            "9cada4",
            "767c77"
        ]
    },
    {
        "id": "e0ece4f7f2e7d8d3cd797a7e",
        "tags": [
            "grey",
            "beige",
            "vintage",
            "light",
            "pastel",
            "winter",
            "kids",
            "cream"
        ],
        "colors": [
            "e0ece4",
            "f7f2e7",
            "d8d3cd",
            "797a7e"
        ]
    },
    {
        "id": "776d8af3e6e3dbe3e5d3c09a",
        "tags": [
            "purple",
            "beige",
            "pastel",
            "vintage"
        ],
        "colors": [
            "776d8a",
            "f3e6e3",
            "dbe3e5",
            "d3c09a"
        ]
    },
    {
        "id": "68b0ab8fc0a9c8d5b9faf3dd",
        "tags": [
            "teal",
            "sage",
            "beige",
            "summer",
            "light",
            "kids",
            "gradient",
            "sea"
        ],
        "colors": [
            "68b0ab",
            "8fc0a9",
            "c8d5b9",
            "faf3dd"
        ]
    },
    {
        "id": "3829333b5249519872a4b494",
        "tags": [
            "black",
            "green",
            "night",
            "dark",
            "nature",
            "earth"
        ],
        "colors": [
            "382933",
            "3b5249",
            "519872",
            "a4b494"
        ]
    },
    {
        "id": "fadcac158467197163065446",
        "tags": [
            "beige",
            "green",
            "summer",
            "nature",
            "retro"
        ],
        "colors": [
            "fadcac",
            "158467",
            "197163",
            "065446"
        ]
    },
    {
        "id": "f7e7bdd9c6a5a35d6ac26565",
        "tags": [
            "beige",
            "red",
            "maroon",
            "warm",
            "vintage",
            "wedding",
            "skin",
            "coffee"
        ],
        "colors": [
            "f7e7bd",
            "d9c6a5",
            "a35d6a",
            "c26565"
        ]
    },
    {
        "id": "ffd571bbd19656556e3c2946",
        "tags": [
            "yellow",
            "green",
            "navy",
            "vintage",
            "summer"
        ],
        "colors": [
            "ffd571",
            "bbd196",
            "56556e",
            "3c2946"
        ]
    },
    {
        "id": "ddddddd9adad84a9ac89c9b8",
        "tags": [
            "grey",
            "peach",
            "teal",
            "pastel",
            "light"
        ],
        "colors": [
            "dddddd",
            "d9adad",
            "84a9ac",
            "89c9b8"
        ]
    },
    {
        "id": "d54062ffa36cebdc87799351",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "spring",
            "rainbow",
            "happy",
            "summer"
        ],
        "colors": [
            "d54062",
            "ffa36c",
            "ebdc87",
            "799351"
        ]
    },
    {
        "id": "cffffef9f7d9fce2ceffc1f3",
        "tags": [
            "blue",
            "teal",
            "yellow",
            "peach",
            "pink",
            "neon",
            "light",
            "spring",
            "happy",
            "kids"
        ],
        "colors": [
            "cffffe",
            "f9f7d9",
            "fce2ce",
            "ffc1f3"
        ]
    },
    {
        "id": "1b262c0f4c7500b7c2fdcb9e",
        "tags": [
            "black",
            "navy",
            "teal",
            "orange",
            "neon",
            "space"
        ],
        "colors": [
            "1b262c",
            "0f4c75",
            "00b7c2",
            "fdcb9e"
        ]
    },
    {
        "id": "b0cac7f7d6bf318fb5005086",
        "tags": [
            "teal",
            "peach",
            "beige",
            "blue",
            "navy",
            "vintage",
            "kids",
            "summer"
        ],
        "colors": [
            "b0cac7",
            "f7d6bf",
            "318fb5",
            "005086"
        ]
    },
    {
        "id": "810000e97171ffcb8ef5efef",
        "tags": [
            "maroon",
            "red",
            "peach",
            "orange",
            "warm",
            "food",
            "kids"
        ],
        "colors": [
            "810000",
            "e97171",
            "ffcb8e",
            "f5efef"
        ]
    },
    {
        "id": "00bcd4b2ebf2ff5722dd2c00",
        "tags": [
            "blue",
            "orange",
            "red",
            "summer",
            "happy",
            "kids"
        ],
        "colors": [
            "00bcd4",
            "b2ebf2",
            "ff5722",
            "dd2c00"
        ]
    },
    {
        "id": "411f1fcedebd86c4baf3f3f3",
        "tags": [
            "brown",
            "sage",
            "teal",
            "grey",
            "white",
            "vintage",
            "earth",
            "winter"
        ],
        "colors": [
            "411f1f",
            "cedebd",
            "86c4ba",
            "f3f3f3"
        ]
    },
    {
        "id": "4b5d67322f3d59405c87556f",
        "tags": [
            "teal",
            "purple",
            "dark",
            "night",
            "cold"
        ],
        "colors": [
            "4b5d67",
            "322f3d",
            "59405c",
            "87556f"
        ]
    },
    {
        "id": "eeeeee2228314f8a8bfbd46d",
        "tags": [
            "grey",
            "black",
            "teal",
            "yellow",
            "retro",
            "space"
        ],
        "colors": [
            "eeeeee",
            "222831",
            "4f8a8b",
            "fbd46d"
        ]
    },
    {
        "id": "f09ae9ffc1faffe78fffd36b",
        "tags": [
            "pink",
            "yellow",
            "spring",
            "happy",
            "light"
        ],
        "colors": [
            "f09ae9",
            "ffc1fa",
            "ffe78f",
            "ffd36b"
        ]
    },
    {
        "id": "cdb30c62760c535204523906",
        "tags": [
            "yellow",
            "green",
            "brown",
            "warm",
            "summer",
            "nature",
            "food"
        ],
        "colors": [
            "cdb30c",
            "62760c",
            "535204",
            "523906"
        ]
    },
    {
        "id": "848ccf93b5e1ffe4e4be5683",
        "tags": [
            "blue",
            "peach",
            "wedding",
            "kids"
        ],
        "colors": [
            "848ccf",
            "93b5e1",
            "ffe4e4",
            "be5683"
        ]
    },
    {
        "id": "838383ad9d9dd9adadfccbcb",
        "tags": [
            "grey",
            "peach",
            "vintage",
            "pastel",
            "skin",
            "cream",
            "light",
            "gradient"
        ],
        "colors": [
            "838383",
            "ad9d9d",
            "d9adad",
            "fccbcb"
        ]
    },
    {
        "id": "ebecf1206a5d1f40681b1c25",
        "tags": [
            "grey",
            "green",
            "navy",
            "black",
            "cold"
        ],
        "colors": [
            "ebecf1",
            "206a5d",
            "1f4068",
            "1b1c25"
        ]
    },
    {
        "id": "e3dfc8f5f1da96bb7ceebb4d",
        "tags": [
            "beige",
            "green",
            "yellow",
            "summer",
            "light",
            "happy",
            "cream"
        ],
        "colors": [
            "e3dfc8",
            "f5f1da",
            "96bb7c",
            "eebb4d"
        ]
    },
    {
        "id": "6f4a8e221f3b050505ebebeb",
        "tags": [
            "purple",
            "black",
            "grey",
            "space",
            "night"
        ],
        "colors": [
            "6f4a8e",
            "221f3b",
            "050505",
            "ebebeb"
        ]
    },
    {
        "id": "ffdbc5cf1b1b900d0d423144",
        "tags": [
            "peach",
            "red",
            "maroon"
        ],
        "colors": [
            "ffdbc5",
            "cf1b1b",
            "900d0d",
            "423144"
        ]
    },
    {
        "id": "006a71ffffddcbeaedd3de32",
        "tags": [
            "teal",
            "blue",
            "green",
            "summer",
            "happy",
            "nature"
        ],
        "colors": [
            "006a71",
            "ffffdd",
            "cbeaed",
            "d3de32"
        ]
    },
    {
        "id": "3b2e5a3949894ea0aefff48f",
        "tags": [
            "purple",
            "blue",
            "navy",
            "teal",
            "yellow"
        ],
        "colors": [
            "3b2e5a",
            "394989",
            "4ea0ae",
            "fff48f"
        ]
    },
    {
        "id": "24a19c6ebfb5ffc7c7ff5f40",
        "tags": [
            "teal",
            "pink",
            "peach",
            "orange",
            "retro",
            "kids"
        ],
        "colors": [
            "24a19c",
            "6ebfb5",
            "ffc7c7",
            "ff5f40"
        ]
    },
    {
        "id": "7fdbdaade498ede682febf63",
        "tags": [
            "blue",
            "green",
            "teal",
            "yellow",
            "orange",
            "summer",
            "light",
            "kids",
            "happy"
        ],
        "colors": [
            "7fdbda",
            "ade498",
            "ede682",
            "febf63"
        ]
    },
    {
        "id": "ffe0f7fe91cad3dbff251f44",
        "tags": [
            "pink",
            "navy",
            "wedding",
            "vintage"
        ],
        "colors": [
            "ffe0f7",
            "fe91ca",
            "d3dbff",
            "251f44"
        ]
    },
    {
        "id": "8fcfd1df5e88f6ab6cf6efa6",
        "tags": [
            "teal",
            "red",
            "orange",
            "yellow",
            "summer",
            "spring",
            "rainbow",
            "happy",
            "kids"
        ],
        "colors": [
            "8fcfd1",
            "df5e88",
            "f6ab6c",
            "f6efa6"
        ]
    },
    {
        "id": "ffdecfba79675e6f643f4441",
        "tags": [
            "beige",
            "peach",
            "brown",
            "green",
            "nature",
            "earth",
            "vintage",
            "warm"
        ],
        "colors": [
            "ffdecf",
            "ba7967",
            "5e6f64",
            "3f4441"
        ]
    },
    {
        "id": "e8505bf9d56ef3ecc214b1ab",
        "tags": [
            "red",
            "yellow",
            "teal",
            "rainbow",
            "happy",
            "spring"
        ],
        "colors": [
            "e8505b",
            "f9d56e",
            "f3ecc2",
            "14b1ab"
        ]
    },
    {
        "id": "5952381dd3bd2bb2bb87d4c5",
        "tags": [
            "brown",
            "teal",
            "winter"
        ],
        "colors": [
            "595238",
            "1dd3bd",
            "2bb2bb",
            "87d4c5"
        ]
    },
    {
        "id": "f0ece3dfd3c3c7b198596e79",
        "tags": [
            "beige",
            "brown",
            "navy",
            "vintage",
            "pastel",
            "cream",
            "coffee",
            "light"
        ],
        "colors": [
            "f0ece3",
            "dfd3c3",
            "c7b198",
            "596e79"
        ]
    },
    {
        "id": "e3dfc8f5f1da9bb67ceebb4d",
        "tags": [
            "beige",
            "green",
            "yellow",
            "cream",
            "pastel",
            "kids"
        ],
        "colors": [
            "e3dfc8",
            "f5f1da",
            "9bb67c",
            "eebb4d"
        ]
    },
    {
        "id": "eeecdaf08a5db83b5e6a2c70",
        "tags": [
            "beige",
            "orange",
            "maroon",
            "purple",
            "warm",
            "sunset"
        ],
        "colors": [
            "eeecda",
            "f08a5d",
            "b83b5e",
            "6a2c70"
        ]
    },
    {
        "id": "e4e3e384a9ac3b6978204051",
        "tags": [
            "grey",
            "teal",
            "navy",
            "cold"
        ],
        "colors": [
            "e4e3e3",
            "84a9ac",
            "3b6978",
            "204051"
        ]
    },
    {
        "id": "fa26a005dfd7a3f7bffff591",
        "tags": [
            "pink",
            "teal",
            "mint",
            "yellow",
            "neon",
            "light",
            "spring",
            "kids",
            "happy"
        ],
        "colors": [
            "fa26a0",
            "05dfd7",
            "a3f7bf",
            "fff591"
        ]
    },
    {
        "id": "ff9a76ffeadbf7c5a8679b9b",
        "tags": [
            "orange",
            "peach",
            "teal",
            "skin",
            "kids"
        ],
        "colors": [
            "ff9a76",
            "ffeadb",
            "f7c5a8",
            "679b9b"
        ]
    },
    {
        "id": "eeeeee393e4676ead7c4fb6d",
        "tags": [
            "grey",
            "black",
            "teal",
            "green",
            "neon",
            "space"
        ],
        "colors": [
            "eeeeee",
            "393e46",
            "76ead7",
            "c4fb6d"
        ]
    },
    {
        "id": "f1c5c5faf0afe5edb78bcdcd",
        "tags": [
            "pink",
            "peach",
            "yellow",
            "teal",
            "pastel",
            "light",
            "summer",
            "kids"
        ],
        "colors": [
            "f1c5c5",
            "faf0af",
            "e5edb7",
            "8bcdcd"
        ]
    },
    {
        "id": "383e56f69e7beedad1d4b5b0",
        "tags": [
            "navy",
            "orange",
            "peach",
            "skin",
            "pastel",
            "coffee",
            "earth",
            "fall",
            "warm",
            "vintage"
        ],
        "colors": [
            "383e56",
            "f69e7b",
            "eedad1",
            "d4b5b0"
        ]
    },
    {
        "id": "36363699d8d0b7efcdffbcbc",
        "tags": [
            "black",
            "teal",
            "mint",
            "pink"
        ],
        "colors": [
            "363636",
            "99d8d0",
            "b7efcd",
            "ffbcbc"
        ]
    },
    {
        "id": "b9ac92ffa931fecb89fbe6d4",
        "tags": [
            "beige",
            "brown",
            "orange",
            "warm",
            "light",
            "cream",
            "gold",
            "kids",
            "food"
        ],
        "colors": [
            "b9ac92",
            "ffa931",
            "fecb89",
            "fbe6d4"
        ]
    },
    {
        "id": "f6bed6e79cc21d1b38336d88",
        "tags": [
            "pink",
            "navy",
            "black",
            "blue",
            "wedding"
        ],
        "colors": [
            "f6bed6",
            "e79cc2",
            "1d1b38",
            "336d88"
        ]
    },
    {
        "id": "fa161612cad60fabbce4f9ff",
        "tags": [
            "red",
            "teal",
            "retro",
            "happy",
            "space"
        ],
        "colors": [
            "fa1616",
            "12cad6",
            "0fabbc",
            "e4f9ff"
        ]
    },
    {
        "id": "09253289c9b8c7e2b2e1ffc2",
        "tags": [
            "black",
            "teal",
            "green",
            "night"
        ],
        "colors": [
            "092532",
            "89c9b8",
            "c7e2b2",
            "e1ffc2"
        ]
    },
    {
        "id": "2f25194a3f35fa7d09ff4301",
        "tags": [
            "brown",
            "orange",
            "red",
            "night",
            "warm",
            "dark"
        ],
        "colors": [
            "2f2519",
            "4a3f35",
            "fa7d09",
            "ff4301"
        ]
    },
    {
        "id": "99b898feceabff847ce84a5f",
        "tags": [
            "sage",
            "peach",
            "orange",
            "red",
            "spring",
            "vintage",
            "nature",
            "food",
            "kids",
            "christmas"
        ],
        "colors": [
            "99b898",
            "feceab",
            "ff847c",
            "e84a5f"
        ]
    },
    {
        "id": "f4f6ffffcb74ea907a4f8a8b",
        "tags": [
            "white",
            "yellow",
            "orange",
            "summer",
            "vintage",
            "kids"
        ],
        "colors": [
            "f4f6ff",
            "ffcb74",
            "ea907a",
            "4f8a8b"
        ]
    },
    {
        "id": "f4f6fffbd46d4f8a8b07031a",
        "tags": [
            "white",
            "yellow",
            "teal",
            "black",
            "retro"
        ],
        "colors": [
            "f4f6ff",
            "fbd46d",
            "4f8a8b",
            "07031a"
        ]
    },
    {
        "id": "a2de963ca59d5a3d55e79c2a",
        "tags": [
            "green",
            "teal",
            "purple",
            "orange",
            "retro",
            "kids"
        ],
        "colors": [
            "a2de96",
            "3ca59d",
            "5a3d55",
            "e79c2a"
        ]
    },
    {
        "id": "111d5ec70039f37121ffbd69",
        "tags": [
            "navy",
            "red",
            "maroon",
            "orange",
            "beige",
            "sunset",
            "gradient"
        ],
        "colors": [
            "111d5e",
            "c70039",
            "f37121",
            "ffbd69"
        ]
    },
    {
        "id": "08697201a9b487dfd6fbfd8a",
        "tags": [
            "teal",
            "blue",
            "yellow",
            "summer",
            "happy",
            "sky"
        ],
        "colors": [
            "086972",
            "01a9b4",
            "87dfd6",
            "fbfd8a"
        ]
    },
    {
        "id": "184d4796bb7cd6efc7eebb4d",
        "tags": [
            "green",
            "orange",
            "spring",
            "nature",
            "kids"
        ],
        "colors": [
            "184d47",
            "96bb7c",
            "d6efc7",
            "eebb4d"
        ]
    },
    {
        "id": "e7305be2979cf7f5dd9bdeac",
        "tags": [
            "red",
            "green",
            "spring",
            "summer",
            "kids"
        ],
        "colors": [
            "e7305b",
            "e2979c",
            "f7f5dd",
            "9bdeac"
        ]
    },
    {
        "id": "ddf3f5a6dceff2aaaae36387",
        "tags": [
            "blue",
            "peach",
            "pastel",
            "wedding",
            "happy",
            "summer"
        ],
        "colors": [
            "ddf3f5",
            "a6dcef",
            "f2aaaa",
            "e36387"
        ]
    },
    {
        "id": "f7fbe1bac964438a5e436f8a",
        "tags": [
            "green",
            "navy",
            "nature"
        ],
        "colors": [
            "f7fbe1",
            "bac964",
            "438a5e",
            "436f8a"
        ]
    },
    {
        "id": "cff6cfcfe5cfe5cfe5f6def6",
        "tags": [
            "green",
            "purple",
            "pink",
            "light",
            "pastel",
            "spring",
            "kids",
            "vintage"
        ],
        "colors": [
            "cff6cf",
            "cfe5cf",
            "e5cfe5",
            "f6def6"
        ]
    },
    {
        "id": "f5f5f5e0dedeffa5b06a197d",
        "tags": [
            "grey",
            "white",
            "pink",
            "peach",
            "purple",
            "wedding"
        ],
        "colors": [
            "f5f5f5",
            "e0dede",
            "ffa5b0",
            "6a197d"
        ]
    },
    {
        "id": "e7dfd584a9ac3b6978204051",
        "tags": [
            "grey",
            "beige",
            "teal",
            "winter",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "e7dfd5",
            "84a9ac",
            "3b6978",
            "204051"
        ]
    },
    {
        "id": "b6eb7af7f7eefb781317706e",
        "tags": [
            "green",
            "white",
            "orange",
            "teal",
            "summer",
            "spring",
            "neon",
            "nature"
        ],
        "colors": [
            "b6eb7a",
            "f7f7ee",
            "fb7813",
            "17706e"
        ]
    },
    {
        "id": "ccafafffcac2fc9d9d900c3f",
        "tags": [
            "pink",
            "peach",
            "maroon",
            "skin",
            "warm",
            "cream"
        ],
        "colors": [
            "ccafaf",
            "ffcac2",
            "fc9d9d",
            "900c3f"
        ]
    },
    {
        "id": "654062ff9c71fbd46de8ead3",
        "tags": [
            "purple",
            "orange",
            "peach",
            "yellow",
            "warm",
            "sunset"
        ],
        "colors": [
            "654062",
            "ff9c71",
            "fbd46d",
            "e8ead3"
        ]
    },
    {
        "id": "eeeeee32e0c4393e46222831",
        "tags": [
            "grey",
            "teal",
            "black",
            "neon",
            "space"
        ],
        "colors": [
            "eeeeee",
            "32e0c4",
            "393e46",
            "222831"
        ]
    },
    {
        "id": "f4f6fff3c62312768110375c",
        "tags": [
            "white",
            "grey",
            "yellow",
            "teal",
            "navy"
        ],
        "colors": [
            "f4f6ff",
            "f3c623",
            "127681",
            "10375c"
        ]
    },
    {
        "id": "ea907afbc687f4f7c5aacdbe",
        "tags": [
            "red",
            "peach",
            "orange",
            "yellow",
            "teal",
            "pastel",
            "summer",
            "warm",
            "rainbow",
            "light",
            "spring"
        ],
        "colors": [
            "ea907a",
            "fbc687",
            "f4f7c5",
            "aacdbe"
        ]
    },
    {
        "id": "f4f4f4f0a500cf7500000000",
        "tags": [
            "white",
            "grey",
            "orange",
            "black",
            "skin",
            "gold",
            "coffee"
        ],
        "colors": [
            "f4f4f4",
            "f0a500",
            "cf7500",
            "000000"
        ]
    },
    {
        "id": "ffcb74b1b4934f8a8b07031a",
        "tags": [
            "yellow",
            "teal",
            "black",
            "summer",
            "night",
            "earth"
        ],
        "colors": [
            "ffcb74",
            "b1b493",
            "4f8a8b",
            "07031a"
        ]
    },
    {
        "id": "ff9595342b3880bdabbbf1c8",
        "tags": [
            "pink",
            "peach",
            "black",
            "teal",
            "green",
            "vintage"
        ],
        "colors": [
            "ff9595",
            "342b38",
            "80bdab",
            "bbf1c8"
        ]
    },
    {
        "id": "faeee7f542914cd3c20a97b0",
        "tags": [
            "beige",
            "pink",
            "teal",
            "retro",
            "neon",
            "kids"
        ],
        "colors": [
            "faeee7",
            "f54291",
            "4cd3c2",
            "0a97b0"
        ]
    },
    {
        "id": "efee9dd1eaa3dbc6ebabc2e8",
        "tags": [
            "yellow",
            "green",
            "purple",
            "blue",
            "light",
            "pastel",
            "nature",
            "happy"
        ],
        "colors": [
            "efee9d",
            "d1eaa3",
            "dbc6eb",
            "abc2e8"
        ]
    },
    {
        "id": "d92027ff9234ffcd3c35d0ba",
        "tags": [
            "red",
            "orange",
            "yellow",
            "teal",
            "rainbow",
            "kids"
        ],
        "colors": [
            "d92027",
            "ff9234",
            "ffcd3c",
            "35d0ba"
        ]
    },
    {
        "id": "0e9aa73da4abf6cd61fe8a71",
        "tags": [
            "teal",
            "yellow",
            "peach",
            "summer",
            "happy"
        ],
        "colors": [
            "0e9aa7",
            "3da4ab",
            "f6cd61",
            "fe8a71"
        ]
    },
    {
        "id": "1b6ca80a97b0ffd3e1fce8d5",
        "tags": [
            "blue",
            "teal",
            "pink",
            "beige",
            "wedding"
        ],
        "colors": [
            "1b6ca8",
            "0a97b0",
            "ffd3e1",
            "fce8d5"
        ]
    },
    {
        "id": "a8df65edf492efb960ee91bc",
        "tags": [
            "green",
            "yellow",
            "orange",
            "pink",
            "spring",
            "light",
            "happy"
        ],
        "colors": [
            "a8df65",
            "edf492",
            "efb960",
            "ee91bc"
        ]
    },
    {
        "id": "ffc4a3ff9a76f96d80bb596b",
        "tags": [
            "peach",
            "orange",
            "red",
            "maroon",
            "skin",
            "warm",
            "gradient"
        ],
        "colors": [
            "ffc4a3",
            "ff9a76",
            "f96d80",
            "bb596b"
        ]
    },
    {
        "id": "ffcbcbd291bcaacfcf679b9b",
        "tags": [
            "pink",
            "purple",
            "teal",
            "wedding",
            "pastel"
        ],
        "colors": [
            "ffcbcb",
            "d291bc",
            "aacfcf",
            "679b9b"
        ]
    },
    {
        "id": "303960ea9a96f8b24fe5e5e5",
        "tags": [
            "navy",
            "peach",
            "orange",
            "grey",
            "vintage",
            "space"
        ],
        "colors": [
            "303960",
            "ea9a96",
            "f8b24f",
            "e5e5e5"
        ]
    },
    {
        "id": "e8e4e1f9c49aec823a7c3c21",
        "tags": [
            "grey",
            "orange",
            "brown",
            "skin",
            "gold",
            "earth",
            "fall"
        ],
        "colors": [
            "e8e4e1",
            "f9c49a",
            "ec823a",
            "7c3c21"
        ]
    },
    {
        "id": "2fc4b212947fe71414f17808",
        "tags": [
            "teal",
            "red",
            "orange",
            "neon",
            "happy"
        ],
        "colors": [
            "2fc4b2",
            "12947f",
            "e71414",
            "f17808"
        ]
    },
    {
        "id": "fcf8763797a48ccbbee4e4e4",
        "tags": [
            "yellow",
            "teal",
            "grey",
            "summer",
            "happy"
        ],
        "colors": [
            "fcf876",
            "3797a4",
            "8ccbbe",
            "e4e4e4"
        ]
    },
    {
        "id": "5fdde5f4ea8ef37121d92027",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "red",
            "summer",
            "rainbow",
            "happy"
        ],
        "colors": [
            "5fdde5",
            "f4ea8e",
            "f37121",
            "d92027"
        ]
    },
    {
        "id": "79d70fd32626f5a31aedf4f2",
        "tags": [
            "green",
            "red",
            "orange",
            "white",
            "spring",
            "nature",
            "food",
            "kids"
        ],
        "colors": [
            "79d70f",
            "d32626",
            "f5a31a",
            "edf4f2"
        ]
    },
    {
        "id": "fee2b3ffa299ad6989562349",
        "tags": [
            "yellow",
            "peach",
            "purple",
            "skin",
            "warm",
            "sunset",
            "pastel",
            "coffee",
            "vintage",
            "gradient"
        ],
        "colors": [
            "fee2b3",
            "ffa299",
            "ad6989",
            "562349"
        ]
    },
    {
        "id": "45046a5c2a9db5076bf1ebbb",
        "tags": [
            "purple",
            "maroon",
            "beige",
            "space",
            "dark"
        ],
        "colors": [
            "45046a",
            "5c2a9d",
            "b5076b",
            "f1ebbb"
        ]
    },
    {
        "id": "bc658d82c4c3f9d89cf5a7a7",
        "tags": [
            "teal",
            "yellow",
            "peach",
            "pastel",
            "vintage",
            "rainbow",
            "kids",
            "light"
        ],
        "colors": [
            "bc658d",
            "82c4c3",
            "f9d89c",
            "f5a7a7"
        ]
    },
    {
        "id": "f7f7f7cceabb3f3f44fdcb9e",
        "tags": [
            "grey",
            "white",
            "green",
            "black",
            "orange",
            "peach",
            "earth",
            "retro"
        ],
        "colors": [
            "f7f7f7",
            "cceabb",
            "3f3f44",
            "fdcb9e"
        ]
    },
    {
        "id": "63b7afabf0e9d4f3efee8572",
        "tags": [
            "teal",
            "orange",
            "winter",
            "light"
        ],
        "colors": [
            "63b7af",
            "abf0e9",
            "d4f3ef",
            "ee8572"
        ]
    },
    {
        "id": "ffd8a6fc8210ff427f007892",
        "tags": [
            "beige",
            "orange",
            "pink",
            "teal",
            "kids"
        ],
        "colors": [
            "ffd8a6",
            "fc8210",
            "ff427f",
            "007892"
        ]
    },
    {
        "id": "9a1f40d9455f74d4c0def4f0",
        "tags": [
            "maroon",
            "red",
            "teal",
            "retro"
        ],
        "colors": [
            "9a1f40",
            "d9455f",
            "74d4c0",
            "def4f0"
        ]
    },
    {
        "id": "00005c6a097dc060a1ffdcb4",
        "tags": [
            "navy",
            "purple",
            "yellow",
            "wedding",
            "sunset",
            "gradient"
        ],
        "colors": [
            "00005c",
            "6a097d",
            "c060a1",
            "ffdcb4"
        ]
    },
    {
        "id": "ffd31dd63447f57b51f6eedf",
        "tags": [
            "yellow",
            "red",
            "orange",
            "beige",
            "warm",
            "gold",
            "happy",
            "food"
        ],
        "colors": [
            "ffd31d",
            "d63447",
            "f57b51",
            "f6eedf"
        ]
    },
    {
        "id": "eb6383fa9191ffe9c5b4f2e1",
        "tags": [
            "red",
            "peach",
            "yellow",
            "mint",
            "teal",
            "rainbow",
            "happy",
            "light",
            "pastel"
        ],
        "colors": [
            "eb6383",
            "fa9191",
            "ffe9c5",
            "b4f2e1"
        ]
    },
    {
        "id": "58b4aeffe277ffb367ffe2bc",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "beige",
            "summer",
            "light"
        ],
        "colors": [
            "58b4ae",
            "ffe277",
            "ffb367",
            "ffe2bc"
        ]
    },
    {
        "id": "ddddddfab7b7f5a8a8e19999",
        "tags": [
            "grey",
            "peach",
            "pastel",
            "skin",
            "cream",
            "kids"
        ],
        "colors": [
            "dddddd",
            "fab7b7",
            "f5a8a8",
            "e19999"
        ]
    },
    {
        "id": "ff52006f000000263b00a1ab",
        "tags": [
            "orange",
            "maroon",
            "navy",
            "teal",
            "neon",
            "space"
        ],
        "colors": [
            "ff5200",
            "6f0000",
            "00263b",
            "00a1ab"
        ]
    },
    {
        "id": "7d5a5af1d1d1f3e1e1faf2f2",
        "tags": [
            "brown",
            "peach",
            "pink",
            "skin",
            "pastel",
            "cream",
            "light",
            "wedding"
        ],
        "colors": [
            "7d5a5a",
            "f1d1d1",
            "f3e1e1",
            "faf2f2"
        ]
    },
    {
        "id": "f1e3cbf9b384ca5116581c0c",
        "tags": [
            "beige",
            "orange",
            "brown",
            "skin",
            "vintage",
            "gold",
            "warm",
            "coffee",
            "gradient"
        ],
        "colors": [
            "f1e3cb",
            "f9b384",
            "ca5116",
            "581c0c"
        ]
    },
    {
        "id": "1624471f40681b1b2fe43f5a",
        "tags": [
            "navy",
            "red",
            "black",
            "dark",
            "space",
            "night"
        ],
        "colors": [
            "162447",
            "1f4068",
            "1b1b2f",
            "e43f5a"
        ]
    },
    {
        "id": "f8f3ebc3edeafc7e2ff40552",
        "tags": [
            "beige",
            "teal",
            "orange",
            "red",
            "retro",
            "happy",
            "kids",
            "spring"
        ],
        "colors": [
            "f8f3eb",
            "c3edea",
            "fc7e2f",
            "f40552"
        ]
    },
    {
        "id": "f9f9f9ffe0acffacb76886c5",
        "tags": [
            "white",
            "yellow",
            "pink",
            "blue",
            "pastel",
            "light",
            "wedding",
            "spring",
            "kids"
        ],
        "colors": [
            "f9f9f9",
            "ffe0ac",
            "ffacb7",
            "6886c5"
        ]
    },
    {
        "id": "bb3b0edd7631708160d8c593",
        "tags": [
            "maroon",
            "red",
            "orange",
            "green",
            "warm",
            "vintage",
            "nature",
            "earth",
            "food"
        ],
        "colors": [
            "bb3b0e",
            "dd7631",
            "708160",
            "d8c593"
        ]
    },
    {
        "id": "4d3e3efff3cdffc38bff926b",
        "tags": [
            "black",
            "yellow",
            "orange",
            "peach",
            "gold",
            "warm",
            "coffee"
        ],
        "colors": [
            "4d3e3e",
            "fff3cd",
            "ffc38b",
            "ff926b"
        ]
    },
    {
        "id": "ffe8dffffffff0f0f0888888",
        "tags": [
            "peach",
            "white",
            "grey",
            "light",
            "skin",
            "cream"
        ],
        "colors": [
            "ffe8df",
            "ffffff",
            "f0f0f0",
            "888888"
        ]
    },
    {
        "id": "565d47b49c73eaac9df0daa4",
        "tags": [
            "brown",
            "pink",
            "beige",
            "spring",
            "vintage",
            "earth",
            "pastel",
            "nature",
            "fall"
        ],
        "colors": [
            "565d47",
            "b49c73",
            "eaac9d",
            "f0daa4"
        ]
    },
    {
        "id": "14285027496d00909edae1e7",
        "tags": [
            "navy",
            "teal",
            "grey",
            "cold",
            "winter",
            "night",
            "sea"
        ],
        "colors": [
            "142850",
            "27496d",
            "00909e",
            "dae1e7"
        ]
    },
    {
        "id": "f6f578f6d743649d6606623b",
        "tags": [
            "yellow",
            "green",
            "summer",
            "happy"
        ],
        "colors": [
            "f6f578",
            "f6d743",
            "649d66",
            "06623b"
        ]
    },
    {
        "id": "120136035aa640bad5fcbf1e",
        "tags": [
            "navy",
            "blue",
            "orange",
            "space"
        ],
        "colors": [
            "120136",
            "035aa6",
            "40bad5",
            "fcbf1e"
        ]
    },
    {
        "id": "7ebdb4f6d198f4a548862a5c",
        "tags": [
            "teal",
            "orange",
            "purple",
            "retro",
            "kids",
            "wedding"
        ],
        "colors": [
            "7ebdb4",
            "f6d198",
            "f4a548",
            "862a5c"
        ]
    },
    {
        "id": "f6acc8af8baf58415326191b",
        "tags": [
            "pink",
            "purple",
            "black",
            "night",
            "wedding"
        ],
        "colors": [
            "f6acc8",
            "af8baf",
            "584153",
            "26191b"
        ]
    },
    {
        "id": "22283130475ec1a57bececec",
        "tags": [
            "black",
            "navy",
            "brown",
            "grey",
            "winter",
            "night",
            "vintage"
        ],
        "colors": [
            "222831",
            "30475e",
            "c1a57b",
            "ececec"
        ]
    },
    {
        "id": "f7f7f743d8c995389e100303",
        "tags": [
            "white",
            "grey",
            "teal",
            "purple",
            "black",
            "neon"
        ],
        "colors": [
            "f7f7f7",
            "43d8c9",
            "95389e",
            "100303"
        ]
    },
    {
        "id": "2c003e512b58ffa372ea9085",
        "tags": [
            "purple",
            "orange",
            "peach"
        ],
        "colors": [
            "2c003e",
            "512b58",
            "ffa372",
            "ea9085"
        ]
    },
    {
        "id": "85a392f5b971fdd998ffecc7",
        "tags": [
            "sage",
            "orange",
            "yellow",
            "beige",
            "summer",
            "pastel",
            "light",
            "happy",
            "food"
        ],
        "colors": [
            "85a392",
            "f5b971",
            "fdd998",
            "ffecc7"
        ]
    },
    {
        "id": "22283130475ef2a365ececec",
        "tags": [
            "navy",
            "orange",
            "grey",
            "night"
        ],
        "colors": [
            "222831",
            "30475e",
            "f2a365",
            "ececec"
        ]
    },
    {
        "id": "0779e44cbbb977d8d8eff3c6",
        "tags": [
            "blue",
            "teal",
            "summer",
            "happy",
            "kids",
            "sky",
            "sea"
        ],
        "colors": [
            "0779e4",
            "4cbbb9",
            "77d8d8",
            "eff3c6"
        ]
    },
    {
        "id": "588da8ccafafe58a8ad8345f",
        "tags": [
            "blue",
            "peach",
            "red"
        ],
        "colors": [
            "588da8",
            "ccafaf",
            "e58a8a",
            "d8345f"
        ]
    },
    {
        "id": "dbdbdbf0a500cf7500000000",
        "tags": [
            "grey",
            "orange",
            "black",
            "vintage",
            "gold"
        ],
        "colors": [
            "dbdbdb",
            "f0a500",
            "cf7500",
            "000000"
        ]
    },
    {
        "id": "511845900c3fc70039ff5733",
        "tags": [
            "maroon",
            "red",
            "orange",
            "warm",
            "dark",
            "sunset"
        ],
        "colors": [
            "511845",
            "900c3f",
            "c70039",
            "ff5733"
        ]
    },
    {
        "id": "f4f4f48ec6c56983aa8566aa",
        "tags": [
            "grey",
            "teal",
            "purple",
            "cold"
        ],
        "colors": [
            "f4f4f4",
            "8ec6c5",
            "6983aa",
            "8566aa"
        ]
    },
    {
        "id": "202040543864ff6363ffbd69",
        "tags": [
            "black",
            "purple",
            "red",
            "orange",
            "dark",
            "space"
        ],
        "colors": [
            "202040",
            "543864",
            "ff6363",
            "ffbd69"
        ]
    },
    {
        "id": "efa8e4f8e1f4fff0f597e5ef",
        "tags": [],
        "colors": [
            "efa8e4",
            "f8e1f4",
            "fff0f5",
            "97e5ef"
        ]
    },
    {
        "id": "442727eae7d9d2c6b2937d14",
        "tags": [
            "brown",
            "beige",
            "grey",
            "earth",
            "coffee",
            "cream"
        ],
        "colors": [
            "442727",
            "eae7d9",
            "d2c6b2",
            "937d14"
        ]
    },
    {
        "id": "342eadea6227f2a51ab9ebcc",
        "tags": [
            "blue",
            "orange",
            "mint",
            "retro",
            "rainbow",
            "happy",
            "kids"
        ],
        "colors": [
            "342ead",
            "ea6227",
            "f2a51a",
            "b9ebcc"
        ]
    },
    {
        "id": "ffbcbc3636364cd3c2b7efcd",
        "tags": [
            "pink",
            "peach",
            "black",
            "teal",
            "mint",
            "vintage",
            "wedding"
        ],
        "colors": [
            "ffbcbc",
            "363636",
            "4cd3c2",
            "b7efcd"
        ]
    },
    {
        "id": "f4e04df2ed6fcee3978db1ab",
        "tags": [
            "yellow",
            "summer",
            "light",
            "food",
            "happy"
        ],
        "colors": [
            "f4e04d",
            "f2ed6f",
            "cee397",
            "8db1ab"
        ]
    },
    {
        "id": "eb4559f78259aeefecf8eeee",
        "tags": [
            "red",
            "orange",
            "teal",
            "grey",
            "retro",
            "kids"
        ],
        "colors": [
            "eb4559",
            "f78259",
            "aeefec",
            "f8eeee"
        ]
    },
    {
        "id": "522d5bd7385efb7b6be7d39f",
        "tags": [
            "purple",
            "red",
            "orange",
            "peach",
            "beige",
            "warm",
            "sunset"
        ],
        "colors": [
            "522d5b",
            "d7385e",
            "fb7b6b",
            "e7d39f"
        ]
    },
    {
        "id": "3630624d4c7d827397d8b9c3",
        "tags": [
            "navy",
            "dark",
            "night",
            "winter",
            "gradient",
            "sea"
        ],
        "colors": [
            "363062",
            "4d4c7d",
            "827397",
            "d8b9c3"
        ]
    },
    {
        "id": "faf4fff3c62384468510375c",
        "tags": [
            "white",
            "yellow",
            "purple",
            "navy"
        ],
        "colors": [
            "faf4ff",
            "f3c623",
            "844685",
            "10375c"
        ]
    },
    {
        "id": "ffb6b6fde2e2aacfcf679b9b",
        "tags": [
            "peach",
            "pink",
            "teal",
            "pastel",
            "light",
            "cream",
            "kids"
        ],
        "colors": [
            "ffb6b6",
            "fde2e2",
            "aacfcf",
            "679b9b"
        ]
    },
    {
        "id": "856c8bd4ebd0a4c5c6ffeb99",
        "tags": [
            "purple",
            "sage",
            "teal",
            "yellow",
            "pastel",
            "vintage",
            "happy"
        ],
        "colors": [
            "856c8b",
            "d4ebd0",
            "a4c5c6",
            "ffeb99"
        ]
    },
    {
        "id": "faf4f4ef962d9c55185a3f11",
        "tags": [
            "white",
            "orange",
            "brown",
            "skin",
            "gold",
            "coffee"
        ],
        "colors": [
            "faf4f4",
            "ef962d",
            "9c5518",
            "5a3f11"
        ]
    },
    {
        "id": "ffa41b00083900508200a8cc",
        "tags": [
            "orange",
            "navy",
            "blue",
            "summer",
            "space"
        ],
        "colors": [
            "ffa41b",
            "000839",
            "005082",
            "00a8cc"
        ]
    },
    {
        "id": "ffaaa5fcf8f3ffd3b6698474",
        "tags": [
            "peach",
            "white",
            "beige",
            "green",
            "vintage",
            "wedding",
            "pastel",
            "happy"
        ],
        "colors": [
            "ffaaa5",
            "fcf8f3",
            "ffd3b6",
            "698474"
        ]
    },
    {
        "id": "ffd31dfae7cbffb385ff7272",
        "tags": [
            "yellow",
            "beige",
            "peach",
            "orange",
            "red",
            "light",
            "summer",
            "kids",
            "warm"
        ],
        "colors": [
            "ffd31d",
            "fae7cb",
            "ffb385",
            "ff7272"
        ]
    },
    {
        "id": "00bdaa400082fe346ef1e7b6",
        "tags": [],
        "colors": [
            "00bdaa",
            "400082",
            "fe346e",
            "f1e7b6"
        ]
    },
    {
        "id": "2040513b697884a9accae8d5",
        "tags": [
            "navy",
            "teal",
            "mint",
            "cold",
            "winter",
            "night",
            "gradient",
            "sea"
        ],
        "colors": [
            "204051",
            "3b6978",
            "84a9ac",
            "cae8d5"
        ]
    },
    {
        "id": "de7119dee3e211697918b0b0",
        "tags": [],
        "colors": [
            "de7119",
            "dee3e2",
            "116979",
            "18b0b0"
        ]
    },
    {
        "id": "2b580c639a67d8ebb5d9bf77",
        "tags": [
            "green",
            "beige",
            "nature",
            "kids",
            "vintage"
        ],
        "colors": [
            "2b580c",
            "639a67",
            "d8ebb5",
            "d9bf77"
        ]
    },
    {
        "id": "f6d186fcf7bbcbe2b0f19292",
        "tags": [
            "orange",
            "yellow",
            "green",
            "red",
            "pastel",
            "light",
            "summer",
            "spring",
            "happy"
        ],
        "colors": [
            "f6d186",
            "fcf7bb",
            "cbe2b0",
            "f19292"
        ]
    },
    {
        "id": "084177687466cd8d7bfbc490",
        "tags": [
            "navy",
            "blue",
            "green",
            "brown",
            "peach",
            "vintage",
            "wedding"
        ],
        "colors": [
            "084177",
            "687466",
            "cd8d7b",
            "fbc490"
        ]
    },
    {
        "id": "f76a8cf8dc88f8fab8ccf0e1",
        "tags": [
            "pink",
            "yellow",
            "teal",
            "light",
            "spring",
            "happy",
            "kids"
        ],
        "colors": [
            "f76a8c",
            "f8dc88",
            "f8fab8",
            "ccf0e1"
        ]
    },
    {
        "id": "ffd1bdffb0cdffffffc2f0fc",
        "tags": [
            "peach",
            "pink",
            "white",
            "blue",
            "light",
            "kids"
        ],
        "colors": [
            "ffd1bd",
            "ffb0cd",
            "ffffff",
            "c2f0fc"
        ]
    },
    {
        "id": "d1f5d39dc6a77d5e2a231903",
        "tags": [
            "mint",
            "brown",
            "black",
            "vintage",
            "earth"
        ],
        "colors": [
            "d1f5d3",
            "9dc6a7",
            "7d5e2a",
            "231903"
        ]
    },
    {
        "id": "cff1effffffffbcffcbe79df",
        "tags": [
            "teal",
            "white",
            "pink",
            "purple",
            "light",
            "kids",
            "wedding"
        ],
        "colors": [
            "cff1ef",
            "ffffff",
            "fbcffc",
            "be79df"
        ]
    },
    {
        "id": "000000323232ff1e56ffac41",
        "tags": [
            "black",
            "grey",
            "red",
            "orange",
            "dark",
            "space"
        ],
        "colors": [
            "000000",
            "323232",
            "ff1e56",
            "ffac41"
        ]
    },
    {
        "id": "ecfbfcffebd9ffc8bd235952",
        "tags": [
            "peach",
            "teal",
            "skin",
            "light",
            "summer",
            "kids",
            "happy"
        ],
        "colors": [
            "ecfbfc",
            "ffebd9",
            "ffc8bd",
            "235952"
        ]
    },
    {
        "id": "2c003e512b58fe346ed2fafb",
        "tags": [
            "purple",
            "red",
            "wedding",
            "space"
        ],
        "colors": [
            "2c003e",
            "512b58",
            "fe346e",
            "d2fafb"
        ]
    },
    {
        "id": "f3d1f4f5fcc1bae5e598d6ea",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "light",
            "pastel",
            "rainbow",
            "happy",
            "kids"
        ],
        "colors": [
            "f3d1f4",
            "f5fcc1",
            "bae5e5",
            "98d6ea"
        ]
    },
    {
        "id": "4813807f78d2efb1ffffe2ff",
        "tags": [
            "purple",
            "pink",
            "wedding",
            "kids",
            "gradient"
        ],
        "colors": [
            "481380",
            "7f78d2",
            "efb1ff",
            "ffe2ff"
        ]
    },
    {
        "id": "1eb2a6d4f8e8ffa34df67575",
        "tags": [
            "teal",
            "orange",
            "peach",
            "red",
            "retro",
            "summer",
            "happy"
        ],
        "colors": [
            "1eb2a6",
            "d4f8e8",
            "ffa34d",
            "f67575"
        ]
    },
    {
        "id": "721b65b80d57f8615affd868",
        "tags": [
            "purple",
            "maroon",
            "red",
            "peach",
            "orange",
            "yellow",
            "warm",
            "sunset",
            "gradient"
        ],
        "colors": [
            "721b65",
            "b80d57",
            "f8615a",
            "ffd868"
        ]
    },
    {
        "id": "b590caa8d3daf5cab3f3ecb8",
        "tags": [
            "purple",
            "blue",
            "peach",
            "beige",
            "pastel",
            "light",
            "retro",
            "kids",
            "rainbow"
        ],
        "colors": [
            "b590ca",
            "a8d3da",
            "f5cab3",
            "f3ecb8"
        ]
    },
    {
        "id": "ffb2a7e6739fcc0e74790c5a",
        "tags": [
            "peach",
            "orange",
            "pink",
            "maroon",
            "purple",
            "warm"
        ],
        "colors": [
            "ffb2a7",
            "e6739f",
            "cc0e74",
            "790c5a"
        ]
    },
    {
        "id": "d63447f57b51f6eedfd1cebd",
        "tags": [
            "red",
            "orange",
            "beige",
            "wedding",
            "food",
            "warm",
            "retro"
        ],
        "colors": [
            "d63447",
            "f57b51",
            "f6eedf",
            "d1cebd"
        ]
    },
    {
        "id": "f4eeffdcd6f7a6b1e1424874",
        "tags": [
            "purple",
            "blue",
            "navy",
            "cold",
            "pastel",
            "cream"
        ],
        "colors": [
            "f4eeff",
            "dcd6f7",
            "a6b1e1",
            "424874"
        ]
    },
    {
        "id": "d7fffda1e6e3eca0b6fafba4",
        "tags": [
            "teal",
            "peach",
            "yellow",
            "summer",
            "spring",
            "light",
            "kids",
            "neon"
        ],
        "colors": [
            "d7fffd",
            "a1e6e3",
            "eca0b6",
            "fafba4"
        ]
    },
    {
        "id": "413c694a47a3ad62aaeab9c9",
        "tags": [
            "navy",
            "blue",
            "purple",
            "dark",
            "night"
        ],
        "colors": [
            "413c69",
            "4a47a3",
            "ad62aa",
            "eab9c9"
        ]
    },
    {
        "id": "edffea75daad2163537a4d1d",
        "tags": [
            "mint",
            "teal",
            "brown",
            "nature",
            "kids"
        ],
        "colors": [
            "edffea",
            "75daad",
            "216353",
            "7a4d1d"
        ]
    },
    {
        "id": "1b262c0f4c81ed6663ffa372",
        "tags": [
            "black",
            "navy",
            "blue",
            "peach",
            "orange",
            "space"
        ],
        "colors": [
            "1b262c",
            "0f4c81",
            "ed6663",
            "ffa372"
        ]
    },
    {
        "id": "4d089a323edddc2adee8f044",
        "tags": [
            "purple",
            "blue",
            "pink",
            "yellow",
            "neon",
            "happy"
        ],
        "colors": [
            "4d089a",
            "323edd",
            "dc2ade",
            "e8f044"
        ]
    },
    {
        "id": "f3558805dfd7a3f7bffff591",
        "tags": [
            "red",
            "teal",
            "mint",
            "yellow",
            "light",
            "neon",
            "happy",
            "rainbow"
        ],
        "colors": [
            "f35588",
            "05dfd7",
            "a3f7bf",
            "fff591"
        ]
    },
    {
        "id": "4f3961ea728cfc9d9df3d4d4",
        "tags": [
            "purple",
            "red",
            "orange",
            "peach",
            "skin",
            "kids"
        ],
        "colors": [
            "4f3961",
            "ea728c",
            "fc9d9d",
            "f3d4d4"
        ]
    },
    {
        "id": "f688bbe8f9e9baf1a19de3d0",
        "tags": [
            "pink",
            "green",
            "teal",
            "summer",
            "spring",
            "light",
            "happy"
        ],
        "colors": [
            "f688bb",
            "e8f9e9",
            "baf1a1",
            "9de3d0"
        ]
    },
    {
        "id": "6e5773d45079ea9085e9e1cc",
        "tags": [
            "red",
            "orange",
            "peach",
            "beige",
            "pastel",
            "wedding",
            "warm"
        ],
        "colors": [
            "6e5773",
            "d45079",
            "ea9085",
            "e9e1cc"
        ]
    },
    {
        "id": "beebe9f4dadaffb6b9f6eec7",
        "tags": [
            "teal",
            "peach",
            "pink",
            "beige",
            "light",
            "pastel",
            "skin",
            "kids",
            "cream"
        ],
        "colors": [
            "beebe9",
            "f4dada",
            "ffb6b9",
            "f6eec7"
        ]
    },
    {
        "id": "5522445961575b8c5acfd186",
        "tags": [
            "green",
            "vintage",
            "nature",
            "winter"
        ],
        "colors": [
            "552244",
            "596157",
            "5b8c5a",
            "cfd186"
        ]
    },
    {
        "id": "381460b21f66fe346effbd69",
        "tags": [
            "navy",
            "maroon",
            "red",
            "yellow",
            "neon",
            "sunset",
            "space"
        ],
        "colors": [
            "381460",
            "b21f66",
            "fe346e",
            "ffbd69"
        ]
    },
    {
        "id": "e7b2a5f1935cba6b5730475e",
        "tags": [
            "peach",
            "orange",
            "brown",
            "navy",
            "skin",
            "pastel",
            "warm",
            "vintage",
            "coffee",
            "halloween"
        ],
        "colors": [
            "e7b2a5",
            "f1935c",
            "ba6b57",
            "30475e"
        ]
    },
    {
        "id": "ffe75efeb72b899857527318",
        "tags": [
            "yellow",
            "orange",
            "green",
            "summer",
            "nature"
        ],
        "colors": [
            "ffe75e",
            "feb72b",
            "899857",
            "527318"
        ]
    },
    {
        "id": "beebe9fffdf9ffe3ed8ac6d1",
        "tags": [
            "teal",
            "white",
            "pink",
            "light",
            "kids",
            "sky"
        ],
        "colors": [
            "beebe9",
            "fffdf9",
            "ffe3ed",
            "8ac6d1"
        ]
    },
    {
        "id": "b7472aeb9788ffd5abfff2e5",
        "tags": [
            "red",
            "peach",
            "beige",
            "warm",
            "summer",
            "food",
            "skin"
        ],
        "colors": [
            "b7472a",
            "eb9788",
            "ffd5ab",
            "fff2e5"
        ]
    },
    {
        "id": "f1f3f479bac12a7886512b58",
        "tags": [
            "white",
            "grey",
            "teal",
            "purple",
            "cold",
            "winter",
            "wedding"
        ],
        "colors": [
            "f1f3f4",
            "79bac1",
            "2a7886",
            "512b58"
        ]
    },
    {
        "id": "fcf8e8ecdfc8ecb390df7861",
        "tags": [
            "beige",
            "peach",
            "orange",
            "skin",
            "light",
            "cream",
            "coffee",
            "kids",
            "pastel"
        ],
        "colors": [
            "fcf8e8",
            "ecdfc8",
            "ecb390",
            "df7861"
        ]
    },
    {
        "id": "65587ff18867e85f9950bda1",
        "tags": [
            "orange",
            "pink",
            "teal",
            "vintage",
            "kids"
        ],
        "colors": [
            "65587f",
            "f18867",
            "e85f99",
            "50bda1"
        ]
    },
    {
        "id": "f8b195f67280c06c846c567b",
        "tags": [
            "orange",
            "peach",
            "red",
            "pastel",
            "warm",
            "halloween"
        ],
        "colors": [
            "f8b195",
            "f67280",
            "c06c84",
            "6c567b"
        ]
    },
    {
        "id": "edededffa41bff51519818d6",
        "tags": [
            "grey",
            "orange",
            "red",
            "purple",
            "neon",
            "kids"
        ],
        "colors": [
            "ededed",
            "ffa41b",
            "ff5151",
            "9818d6"
        ]
    },
    {
        "id": "010a43ffc2c2ff9d9dff2e63",
        "tags": [
            "navy",
            "black",
            "pink",
            "peach",
            "red",
            "skin"
        ],
        "colors": [
            "010a43",
            "ffc2c2",
            "ff9d9d",
            "ff2e63"
        ]
    },
    {
        "id": "14285027496d0c7b9300a8cc",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter",
            "night",
            "dark",
            "sea"
        ],
        "colors": [
            "142850",
            "27496d",
            "0c7b93",
            "00a8cc"
        ]
    },
    {
        "id": "54123b84142dc0273929c7ac",
        "tags": [
            "maroon",
            "red",
            "teal",
            "dark",
            "wedding",
            "space",
            "retro"
        ],
        "colors": [
            "54123b",
            "84142d",
            "c02739",
            "29c7ac"
        ]
    },
    {
        "id": "ffd5e5ffffdda0ffe681f5ff",
        "tags": [
            "pink",
            "yellow",
            "teal",
            "blue",
            "pastel",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "ffd5e5",
            "ffffdd",
            "a0ffe6",
            "81f5ff"
        ]
    },
    {
        "id": "21243dff7c7cffd08288e1f2",
        "tags": [
            "black",
            "red",
            "orange",
            "blue",
            "retro",
            "space"
        ],
        "colors": [
            "21243d",
            "ff7c7c",
            "ffd082",
            "88e1f2"
        ]
    },
    {
        "id": "42240cc81912f64b3cfdba9a",
        "tags": [
            "brown",
            "maroon",
            "red",
            "peach",
            "orange",
            "warm"
        ],
        "colors": [
            "42240c",
            "c81912",
            "f64b3c",
            "fdba9a"
        ]
    },
    {
        "id": "5b8c85434e52b0a160ecce6d",
        "tags": [
            "teal",
            "yellow"
        ],
        "colors": [
            "5b8c85",
            "434e52",
            "b0a160",
            "ecce6d"
        ]
    },
    {
        "id": "ffc7c7ff80b09399ffa9fffd",
        "tags": [
            "pink",
            "peach",
            "blue",
            "teal",
            "kids"
        ],
        "colors": [
            "ffc7c7",
            "ff80b0",
            "9399ff",
            "a9fffd"
        ]
    },
    {
        "id": "ffae8fff677dcd66846f5a7e",
        "tags": [
            "orange",
            "peach",
            "red",
            "sunset",
            "warm",
            "kids"
        ],
        "colors": [
            "ffae8f",
            "ff677d",
            "cd6684",
            "6f5a7e"
        ]
    },
    {
        "id": "eab0d9f1c6def7e8f0feb377",
        "tags": [
            "pink",
            "orange",
            "pastel",
            "light",
            "kids"
        ],
        "colors": [
            "eab0d9",
            "f1c6de",
            "f7e8f0",
            "feb377"
        ]
    },
    {
        "id": "61d4b3fdd365fb8d62fd2eb3",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "peach",
            "pink",
            "vintage",
            "rainbow",
            "happy"
        ],
        "colors": [
            "61d4b3",
            "fdd365",
            "fb8d62",
            "fd2eb3"
        ]
    },
    {
        "id": "fce2dbf1c6d3e4a3d4c295d8",
        "tags": [
            "beige",
            "pink",
            "purple",
            "skin",
            "light",
            "pastel"
        ],
        "colors": [
            "fce2db",
            "f1c6d3",
            "e4a3d4",
            "c295d8"
        ]
    },
    {
        "id": "f1fcfc40e0d072b5b7633a82",
        "tags": [
            "teal",
            "purple",
            "winter",
            "cold"
        ],
        "colors": [
            "f1fcfc",
            "40e0d0",
            "72b5b7",
            "633a82"
        ]
    },
    {
        "id": "deddfadab8f3ea7ad7ce0f3d",
        "tags": [
            "purple",
            "pink",
            "red",
            "wedding"
        ],
        "colors": [
            "deddfa",
            "dab8f3",
            "ea7ad7",
            "ce0f3d"
        ]
    },
    {
        "id": "ffbabaffeadbf7c5a8678a74",
        "tags": [
            "peach",
            "pink",
            "beige",
            "green",
            "skin",
            "vintage",
            "pastel",
            "kids"
        ],
        "colors": [
            "ffbaba",
            "ffeadb",
            "f7c5a8",
            "678a74"
        ]
    },
    {
        "id": "05dfd7ec7373d8b5b5ffe196",
        "tags": [
            "teal",
            "red",
            "yellow",
            "retro",
            "kids"
        ],
        "colors": [
            "05dfd7",
            "ec7373",
            "d8b5b5",
            "ffe196"
        ]
    },
    {
        "id": "333333ffffffe1f4f3706c61",
        "tags": [
            "black",
            "white",
            "grey",
            "wedding",
            "space"
        ],
        "colors": [
            "333333",
            "ffffff",
            "e1f4f3",
            "706c61"
        ]
    },
    {
        "id": "e1f2fbf1f9f9f3dfe3e9b2bc",
        "tags": [
            "blue",
            "peach",
            "light",
            "pastel",
            "cream"
        ],
        "colors": [
            "e1f2fb",
            "f1f9f9",
            "f3dfe3",
            "e9b2bc"
        ]
    },
    {
        "id": "eef9bfa7e9af75b79e6a8caf",
        "tags": [
            "green",
            "blue",
            "light",
            "pastel",
            "nature",
            "gradient"
        ],
        "colors": [
            "eef9bf",
            "a7e9af",
            "75b79e",
            "6a8caf"
        ]
    },
    {
        "id": "f6e5f5fbf4f9f6e7e6b9cced",
        "tags": [
            "pink",
            "beige",
            "blue",
            "skin",
            "light",
            "pastel",
            "kids",
            "cream"
        ],
        "colors": [
            "f6e5f5",
            "fbf4f9",
            "f6e7e6",
            "b9cced"
        ]
    },
    {
        "id": "fd5e53f9fcfbb0eacd21bf73",
        "tags": [
            "red",
            "white",
            "green",
            "nature",
            "food",
            "christmas"
        ],
        "colors": [
            "fd5e53",
            "f9fcfb",
            "b0eacd",
            "21bf73"
        ]
    },
    {
        "id": "192965f0efefbbcffffaafff",
        "tags": [
            "navy",
            "grey",
            "blue",
            "pink",
            "vintage",
            "retro"
        ],
        "colors": [
            "192965",
            "f0efef",
            "bbcfff",
            "faafff"
        ]
    },
    {
        "id": "6e5773d45d79ea9085e9e2d0",
        "tags": [
            "maroon",
            "red",
            "orange",
            "beige",
            "pastel",
            "coffee"
        ],
        "colors": [
            "6e5773",
            "d45d79",
            "ea9085",
            "e9e2d0"
        ]
    },
    {
        "id": "effcefccedd294d3ac655c56",
        "tags": [
            "green",
            "cold",
            "nature",
            "earth"
        ],
        "colors": [
            "effcef",
            "ccedd2",
            "94d3ac",
            "655c56"
        ]
    },
    {
        "id": "c9485be89da2f5c3bc96d1c7",
        "tags": [
            "maroon",
            "red",
            "peach",
            "pink",
            "teal",
            "skin",
            "vintage"
        ],
        "colors": [
            "c9485b",
            "e89da2",
            "f5c3bc",
            "96d1c7"
        ]
    },
    {
        "id": "ee857235495e34747463b7af",
        "tags": [
            "orange",
            "navy",
            "teal",
            "halloween"
        ],
        "colors": [
            "ee8572",
            "35495e",
            "347474",
            "63b7af"
        ]
    },
    {
        "id": "8cba51deff8bfbceb5ff5d6c",
        "tags": [
            "green",
            "peach",
            "red",
            "summer",
            "retro",
            "neon",
            "nature",
            "happy",
            "food"
        ],
        "colors": [
            "8cba51",
            "deff8b",
            "fbceb5",
            "ff5d6c"
        ]
    },
    {
        "id": "f6eec7f7d695ee8972d15a7c",
        "tags": [
            "yellow",
            "beige",
            "orange",
            "maroon",
            "warm",
            "sunset",
            "gold",
            "happy"
        ],
        "colors": [
            "f6eec7",
            "f7d695",
            "ee8972",
            "d15a7c"
        ]
    },
    {
        "id": "be8abfea9abbfea5adf8c3af",
        "tags": [
            "purple",
            "pink",
            "peach",
            "sunset",
            "light",
            "pastel",
            "wedding",
            "warm",
            "gradient",
            "sky"
        ],
        "colors": [
            "be8abf",
            "ea9abb",
            "fea5ad",
            "f8c3af"
        ]
    },
    {
        "id": "4d46465b56567fcd91f5eaea",
        "tags": [
            "black",
            "green",
            "grey",
            "retro",
            "night",
            "winter"
        ],
        "colors": [
            "4d4646",
            "5b5656",
            "7fcd91",
            "f5eaea"
        ]
    },
    {
        "id": "af460ffe8761fed39ff6eec9",
        "tags": [
            "maroon",
            "orange",
            "peach",
            "beige",
            "skin",
            "gold",
            "warm",
            "food",
            "kids",
            "fall"
        ],
        "colors": [
            "af460f",
            "fe8761",
            "fed39f",
            "f6eec9"
        ]
    },
    {
        "id": "f6f4e6ede59ad5c455fddb3a",
        "tags": [
            "beige",
            "yellow",
            "light",
            "summer",
            "cream",
            "happy"
        ],
        "colors": [
            "f6f4e6",
            "ede59a",
            "d5c455",
            "fddb3a"
        ]
    },
    {
        "id": "edf7fa5f6cafffb677ff8364",
        "tags": [
            "blue",
            "navy",
            "orange",
            "peach",
            "summer",
            "happy"
        ],
        "colors": [
            "edf7fa",
            "5f6caf",
            "ffb677",
            "ff8364"
        ]
    },
    {
        "id": "f0134dff6f5ef5f0e340bfc1",
        "tags": [
            "red",
            "orange",
            "beige",
            "teal",
            "retro",
            "kids",
            "neon"
        ],
        "colors": [
            "f0134d",
            "ff6f5e",
            "f5f0e3",
            "40bfc1"
        ]
    },
    {
        "id": "ffb99aff6464db3056851d41",
        "tags": [
            "peach",
            "orange",
            "red",
            "maroon",
            "warm",
            "wedding",
            "kids"
        ],
        "colors": [
            "ffb99a",
            "ff6464",
            "db3056",
            "851d41"
        ]
    },
    {
        "id": "ffb6b9fae3d9bbded68ac6d1",
        "tags": [
            "pink",
            "beige",
            "blue",
            "light",
            "pastel",
            "spring"
        ],
        "colors": [
            "ffb6b9",
            "fae3d9",
            "bbded6",
            "8ac6d1"
        ]
    },
    {
        "id": "e32249f17362dddc92d8c962",
        "tags": [
            "red",
            "peach",
            "yellow",
            "warm",
            "spring"
        ],
        "colors": [
            "e32249",
            "f17362",
            "dddc92",
            "d8c962"
        ]
    },
    {
        "id": "1b262c0f4c753282b8bbe1fa",
        "tags": [
            "black",
            "navy",
            "blue",
            "winter",
            "cold",
            "dark",
            "night",
            "gradient",
            "sea"
        ],
        "colors": [
            "1b262c",
            "0f4c75",
            "3282b8",
            "bbe1fa"
        ]
    },
    {
        "id": "ffba5ac0ffb352de972c7873",
        "tags": [
            "orange",
            "green",
            "summer",
            "neon",
            "nature"
        ],
        "colors": [
            "ffba5a",
            "c0ffb3",
            "52de97",
            "2c7873"
        ]
    },
    {
        "id": "7fa998f1f1b0df85439d2503",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "maroon",
            "warm",
            "vintage",
            "fall",
            "christmas"
        ],
        "colors": [
            "7fa998",
            "f1f1b0",
            "df8543",
            "9d2503"
        ]
    },
    {
        "id": "ffcc00ff6666cc006666cccc",
        "tags": [
            "yellow",
            "peach",
            "maroon",
            "teal",
            "rainbow",
            "kids"
        ],
        "colors": [
            "ffcc00",
            "ff6666",
            "cc0066",
            "66cccc"
        ]
    },
    {
        "id": "be9fe1c9b6e4e1ccecf1f1f6",
        "tags": [
            "purple",
            "grey",
            "light",
            "pastel",
            "cream"
        ],
        "colors": [
            "be9fe1",
            "c9b6e4",
            "e1ccec",
            "f1f1f6"
        ]
    },
    {
        "id": "f0e3ffd89cf6916dd53e206d",
        "tags": [
            "purple",
            "wedding",
            "gradient"
        ],
        "colors": [
            "f0e3ff",
            "d89cf6",
            "916dd5",
            "3e206d"
        ]
    },
    {
        "id": "fa163f12cad60fabbce4f9ff",
        "tags": [
            "red",
            "teal",
            "neon",
            "kids"
        ],
        "colors": [
            "fa163f",
            "12cad6",
            "0fabbc",
            "e4f9ff"
        ]
    },
    {
        "id": "f8b400faf5e42c786c004445",
        "tags": [
            "orange",
            "beige",
            "green",
            "nature",
            "vintage"
        ],
        "colors": [
            "f8b400",
            "faf5e4",
            "2c786c",
            "004445"
        ]
    },
    {
        "id": "fe9801f4eec7ccda46697c37",
        "tags": [],
        "colors": [
            "fe9801",
            "f4eec7",
            "ccda46",
            "697c37"
        ]
    },
    {
        "id": "9dab86e6a157eb8242c9753d",
        "tags": [
            "sage",
            "orange",
            "brown",
            "pastel",
            "summer",
            "earth",
            "fall"
        ],
        "colors": [
            "9dab86",
            "e6a157",
            "eb8242",
            "c9753d"
        ]
    },
    {
        "id": "5d5b6a758184cfb495f5cdaa",
        "tags": [
            "grey",
            "beige",
            "skin",
            "pastel",
            "night"
        ],
        "colors": [
            "5d5b6a",
            "758184",
            "cfb495",
            "f5cdaa"
        ]
    },
    {
        "id": "f6e1e1ff9d76eb4d55333366",
        "tags": [
            "orange",
            "peach",
            "red",
            "navy",
            "warm"
        ],
        "colors": [
            "f6e1e1",
            "ff9d76",
            "eb4d55",
            "333366"
        ]
    },
    {
        "id": "f0cf85e7f0c3a4d4ae32afa9",
        "tags": [
            "yellow",
            "green",
            "teal",
            "summer",
            "pastel",
            "happy"
        ],
        "colors": [
            "f0cf85",
            "e7f0c3",
            "a4d4ae",
            "32afa9"
        ]
    },
    {
        "id": "effffb50d8904f98ca272727",
        "tags": [
            "white",
            "green",
            "blue",
            "black",
            "light",
            "cold",
            "winter"
        ],
        "colors": [
            "effffb",
            "50d890",
            "4f98ca",
            "272727"
        ]
    },
    {
        "id": "ff896be8d4b4ebe6e6f3f3f3",
        "tags": [
            "orange",
            "beige",
            "grey",
            "skin",
            "light",
            "cream",
            "warm"
        ],
        "colors": [
            "ff896b",
            "e8d4b4",
            "ebe6e6",
            "f3f3f3"
        ]
    },
    {
        "id": "698474889e81bac7a7e5e4cc",
        "tags": [
            "sage",
            "beige",
            "pastel",
            "nature",
            "earth"
        ],
        "colors": [
            "698474",
            "889e81",
            "bac7a7",
            "e5e4cc"
        ]
    },
    {
        "id": "23044490303ded8240d2ebe9",
        "tags": [
            "navy",
            "maroon",
            "orange",
            "teal",
            "winter",
            "halloween",
            "space"
        ],
        "colors": [
            "230444",
            "90303d",
            "ed8240",
            "d2ebe9"
        ]
    },
    {
        "id": "550a464a69bb617be39aceff",
        "tags": [
            "maroon",
            "blue",
            "winter",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "550a46",
            "4a69bb",
            "617be3",
            "9aceff"
        ]
    },
    {
        "id": "015668263f44ffd369fff1cf",
        "tags": [
            "teal",
            "yellow",
            "space"
        ],
        "colors": [
            "015668",
            "263f44",
            "ffd369",
            "fff1cf"
        ]
    },
    {
        "id": "01838302a8a842e6a4f5dea3",
        "tags": [
            "teal",
            "mint",
            "green",
            "beige",
            "neon",
            "happy"
        ],
        "colors": [
            "018383",
            "02a8a8",
            "42e6a4",
            "f5dea3"
        ]
    },
    {
        "id": "fffffff9f6f7ffe8d6ff971d",
        "tags": [
            "white",
            "grey",
            "beige",
            "orange",
            "christmas",
            "light",
            "skin",
            "cream"
        ],
        "colors": [
            "ffffff",
            "f9f6f7",
            "ffe8d6",
            "ff971d"
        ]
    },
    {
        "id": "f67280c06c846c5b7b35477d",
        "tags": [
            "red",
            "navy",
            "night",
            "wedding"
        ],
        "colors": [
            "f67280",
            "c06c84",
            "6c5b7b",
            "35477d"
        ]
    },
    {
        "id": "413c694a47a3ad62aaf4b0c7",
        "tags": [
            "navy",
            "blue",
            "purple",
            "pink",
            "space"
        ],
        "colors": [
            "413c69",
            "4a47a3",
            "ad62aa",
            "f4b0c7"
        ]
    },
    {
        "id": "4641596c7b958bbabbc7f0db",
        "tags": [
            "black",
            "teal",
            "mint",
            "winter",
            "night",
            "gradient",
            "sea"
        ],
        "colors": [
            "464159",
            "6c7b95",
            "8bbabb",
            "c7f0db"
        ]
    },
    {
        "id": "d3f4ffb2dffbe7a4e4ffc55c",
        "tags": [
            "blue",
            "purple",
            "orange",
            "light",
            "summer",
            "kids",
            "spring"
        ],
        "colors": [
            "d3f4ff",
            "b2dffb",
            "e7a4e4",
            "ffc55c"
        ]
    },
    {
        "id": "fbdff0f6c3e5a278b5381460",
        "tags": [
            "pink",
            "purple",
            "wedding"
        ],
        "colors": [
            "fbdff0",
            "f6c3e5",
            "a278b5",
            "381460"
        ]
    },
    {
        "id": "f65c78ffd271fff3afc3f584",
        "tags": [
            "red",
            "orange",
            "yellow",
            "green",
            "light",
            "summer",
            "neon",
            "kids",
            "spring",
            "rainbow"
        ],
        "colors": [
            "f65c78",
            "ffd271",
            "fff3af",
            "c3f584"
        ]
    },
    {
        "id": "111d5eb21f66fe346effbd69",
        "tags": [
            "navy",
            "maroon",
            "red",
            "beige",
            "space",
            "sunset"
        ],
        "colors": [
            "111d5e",
            "b21f66",
            "fe346e",
            "ffbd69"
        ]
    },
    {
        "id": "f4f4f4ff73153a3535232020",
        "tags": [
            "grey",
            "orange",
            "black",
            "retro",
            "fall"
        ],
        "colors": [
            "f4f4f4",
            "ff7315",
            "3a3535",
            "232020"
        ]
    },
    {
        "id": "4000827e0cf5cd4dccf7beff",
        "tags": [
            "purple",
            "pink",
            "space",
            "gradient"
        ],
        "colors": [
            "400082",
            "7e0cf5",
            "cd4dcc",
            "f7beff"
        ]
    },
    {
        "id": "46185f297ca0bbbbbbe9ea77",
        "tags": [
            "purple",
            "teal",
            "grey",
            "yellow",
            "retro"
        ],
        "colors": [
            "46185f",
            "297ca0",
            "bbbbbb",
            "e9ea77"
        ]
    },
    {
        "id": "d77fa1e6b2c6fef6fbd6e5fa",
        "tags": [
            "red",
            "peach",
            "white",
            "skin",
            "pastel",
            "light",
            "kids"
        ],
        "colors": [
            "d77fa1",
            "e6b2c6",
            "fef6fb",
            "d6e5fa"
        ]
    },
    {
        "id": "f8b195f67280c06c846c5b7b",
        "tags": [
            "orange",
            "red",
            "warm",
            "pastel"
        ],
        "colors": [
            "f8b195",
            "f67280",
            "c06c84",
            "6c5b7b"
        ]
    },
    {
        "id": "15196532407b51558546b5d1",
        "tags": [
            "navy",
            "blue",
            "dark",
            "cold",
            "winter",
            "night",
            "sky",
            "sea"
        ],
        "colors": [
            "151965",
            "32407b",
            "515585",
            "46b5d1"
        ]
    },
    {
        "id": "fbe3b9fab6960c94632d334a",
        "tags": [
            "beige",
            "peach",
            "green",
            "black",
            "skin",
            "summer",
            "nature",
            "food"
        ],
        "colors": [
            "fbe3b9",
            "fab696",
            "0c9463",
            "2d334a"
        ]
    },
    {
        "id": "561f558b2f97cf56a1fcb2bf",
        "tags": [],
        "colors": [
            "561f55",
            "8b2f97",
            "cf56a1",
            "fcb2bf"
        ]
    },
    {
        "id": "ffa259fe6845fa425291bd3a",
        "tags": [
            "orange",
            "red",
            "green",
            "christmas",
            "kids",
            "happy"
        ],
        "colors": [
            "ffa259",
            "fe6845",
            "fa4252",
            "91bd3a"
        ]
    },
    {
        "id": "2d132c801336c72c41ee4540",
        "tags": [
            "black",
            "maroon",
            "red",
            "dark",
            "night",
            "halloween"
        ],
        "colors": [
            "2d132c",
            "801336",
            "c72c41",
            "ee4540"
        ]
    },
    {
        "id": "dff6f046b3e64d80e42e279d",
        "tags": [
            "blue",
            "navy",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "dff6f0",
            "46b3e6",
            "4d80e4",
            "2e279d"
        ]
    },
    {
        "id": "0044452c78736fb98fffd800",
        "tags": [
            "green",
            "yellow",
            "nature",
            "happy"
        ],
        "colors": [
            "004445",
            "2c7873",
            "6fb98f",
            "ffd800"
        ]
    },
    {
        "id": "fa697ce13a9d9b45e4fcc169",
        "tags": [
            "red",
            "purple",
            "yellow",
            "kids",
            "neon"
        ],
        "colors": [
            "fa697c",
            "e13a9d",
            "9b45e4",
            "fcc169"
        ]
    },
    {
        "id": "272343ffffffe3f6f5bae8e8",
        "tags": [
            "black",
            "white",
            "teal",
            "winter",
            "cold",
            "wedding",
            "vintage"
        ],
        "colors": [
            "272343",
            "ffffff",
            "e3f6f5",
            "bae8e8"
        ]
    },
    {
        "id": "222831393e4629a19ca3f7bf",
        "tags": [
            "black",
            "grey",
            "teal"
        ],
        "colors": [
            "222831",
            "393e46",
            "29a19c",
            "a3f7bf"
        ]
    },
    {
        "id": "e5dfdf6ba8a93573761d4d4f",
        "tags": [
            "grey",
            "teal",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "e5dfdf",
            "6ba8a9",
            "357376",
            "1d4d4f"
        ]
    },
    {
        "id": "621055b52b65ed6663ffa372",
        "tags": [
            "purple",
            "orange",
            "peach",
            "warm",
            "sunset"
        ],
        "colors": [
            "621055",
            "b52b65",
            "ed6663",
            "ffa372"
        ]
    },
    {
        "id": "51eaeaffdbc5ff9d76ef4339",
        "tags": [
            "teal",
            "orange",
            "red",
            "skin",
            "neon",
            "happy"
        ],
        "colors": [
            "51eaea",
            "ffdbc5",
            "ff9d76",
            "ef4339"
        ]
    },
    {
        "id": "36b5b09dd8c8f09595fcf5b0",
        "tags": [
            "teal",
            "peach",
            "yellow",
            "light",
            "spring"
        ],
        "colors": [
            "36b5b0",
            "9dd8c8",
            "f09595",
            "fcf5b0"
        ]
    },
    {
        "id": "9d0b0bda2d2deb8242f6da63",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "sunset",
            "kids",
            "halloween"
        ],
        "colors": [
            "9d0b0b",
            "da2d2d",
            "eb8242",
            "f6da63"
        ]
    },
    {
        "id": "f4efd3ccccccc2b0c99656a1",
        "tags": [
            "beige",
            "grey",
            "purple",
            "pastel",
            "cream"
        ],
        "colors": [
            "f4efd3",
            "cccccc",
            "c2b0c9",
            "9656a1"
        ]
    },
    {
        "id": "594a4ee78fb3ffc0ad6fc1a5",
        "tags": [
            "pink",
            "peach",
            "green",
            "vintage",
            "kids"
        ],
        "colors": [
            "594a4e",
            "e78fb3",
            "ffc0ad",
            "6fc1a5"
        ]
    },
    {
        "id": "ff8ba7ffc6c7faeee7c3f0ca",
        "tags": [
            "pink",
            "peach",
            "beige",
            "green",
            "light",
            "summer",
            "happy",
            "spring",
            "food"
        ],
        "colors": [
            "ff8ba7",
            "ffc6c7",
            "faeee7",
            "c3f0ca"
        ]
    },
    {
        "id": "10316b000000e25822ececeb",
        "tags": [
            "navy",
            "black",
            "orange",
            "grey",
            "retro",
            "space"
        ],
        "colors": [
            "10316b",
            "000000",
            "e25822",
            "ececeb"
        ]
    },
    {
        "id": "a35638e08f62d7c79e9dab86",
        "tags": [
            "brown",
            "beige",
            "green",
            "fall",
            "summer",
            "warm",
            "earth"
        ],
        "colors": [
            "a35638",
            "e08f62",
            "d7c79e",
            "9dab86"
        ]
    },
    {
        "id": "ffac8efd77923f4d7155ae95",
        "tags": [
            "orange",
            "peach",
            "pink",
            "navy",
            "green",
            "retro",
            "kids"
        ],
        "colors": [
            "ffac8e",
            "fd7792",
            "3f4d71",
            "55ae95"
        ]
    },
    {
        "id": "1b2a4946588100909ec9d1d3",
        "tags": [
            "navy",
            "blue",
            "teal",
            "grey",
            "cold",
            "winter",
            "night",
            "sea"
        ],
        "colors": [
            "1b2a49",
            "465881",
            "00909e",
            "c9d1d3"
        ]
    },
    {
        "id": "3fc5f042dee16decb9eef5b2",
        "tags": [
            "blue",
            "mint",
            "yellow",
            "light",
            "neon",
            "summer",
            "happy",
            "sky"
        ],
        "colors": [
            "3fc5f0",
            "42dee1",
            "6decb9",
            "eef5b2"
        ]
    },
    {
        "id": "003f5c472b62bc4873fb5b5a",
        "tags": [
            "purple",
            "peach",
            "maroon",
            "halloween",
            "dark"
        ],
        "colors": [
            "003f5c",
            "472b62",
            "bc4873",
            "fb5b5a"
        ]
    },
    {
        "id": "9be3debeebe9fffdf9ffe3ed",
        "tags": [
            "teal",
            "white",
            "pink",
            "light",
            "pastel",
            "kids",
            "spring",
            "cream"
        ],
        "colors": [
            "9be3de",
            "beebe9",
            "fffdf9",
            "ffe3ed"
        ]
    },
    {
        "id": "11013300918e4dd599ffdc34",
        "tags": [
            "black",
            "teal",
            "mint",
            "yellow",
            "space"
        ],
        "colors": [
            "110133",
            "00918e",
            "4dd599",
            "ffdc34"
        ]
    },
    {
        "id": "bd574efa877fffad87dedef0",
        "tags": [
            "red",
            "peach",
            "grey",
            "skin",
            "pastel",
            "gold",
            "kids",
            "fall",
            "warm"
        ],
        "colors": [
            "bd574e",
            "fa877f",
            "ffad87",
            "dedef0"
        ]
    },
    {
        "id": "f45905c70d3a512c6245969b",
        "tags": [
            "orange",
            "maroon",
            "red",
            "teal",
            "halloween",
            "kids"
        ],
        "colors": [
            "f45905",
            "c70d3a",
            "512c62",
            "45969b"
        ]
    },
    {
        "id": "eafbea6f9a8d1f6650ea5e5e",
        "tags": [
            "green",
            "red",
            "food",
            "vintage"
        ],
        "colors": [
            "eafbea",
            "6f9a8d",
            "1f6650",
            "ea5e5e"
        ]
    },
    {
        "id": "010038293a80537ec5f39422",
        "tags": [
            "navy",
            "blue",
            "orange",
            "night",
            "dark"
        ],
        "colors": [
            "010038",
            "293a80",
            "537ec5",
            "f39422"
        ]
    },
    {
        "id": "fff4e4f88020d1274b3d0e1e",
        "tags": [
            "beige",
            "orange",
            "red",
            "warm",
            "gradient"
        ],
        "colors": [
            "fff4e4",
            "f88020",
            "d1274b",
            "3d0e1e"
        ]
    },
    {
        "id": "f35588ffbbb471a95a007944",
        "tags": [
            "pink",
            "peach",
            "green",
            "nature",
            "summer"
        ],
        "colors": [
            "f35588",
            "ffbbb4",
            "71a95a",
            "007944"
        ]
    },
    {
        "id": "39375b745c97d597cef5b0cb",
        "tags": [
            "purple",
            "peach",
            "pastel",
            "night",
            "wedding"
        ],
        "colors": [
            "39375b",
            "745c97",
            "d597ce",
            "f5b0cb"
        ]
    },
    {
        "id": "f8f8f8f1d6abe3b04b2b2b28",
        "tags": [
            "grey",
            "yellow",
            "black",
            "gold",
            "vintage"
        ],
        "colors": [
            "f8f8f8",
            "f1d6ab",
            "e3b04b",
            "2b2b28"
        ]
    },
    {
        "id": "380e7f6915cfd62196e497cd",
        "tags": [
            "purple",
            "pink",
            "space",
            "kids"
        ],
        "colors": [
            "380e7f",
            "6915cf",
            "d62196",
            "e497cd"
        ]
    },
    {
        "id": "dcffcc9fdfcdbaabdad79abc",
        "tags": [
            "green",
            "mint",
            "teal",
            "purple",
            "light",
            "summer",
            "pastel",
            "spring",
            "happy"
        ],
        "colors": [
            "dcffcc",
            "9fdfcd",
            "baabda",
            "d79abc"
        ]
    },
    {
        "id": "8f4426de6b35f9b28264ccda",
        "tags": [
            "brown",
            "orange",
            "blue",
            "warm",
            "skin",
            "coffee",
            "kids"
        ],
        "colors": [
            "8f4426",
            "de6b35",
            "f9b282",
            "64ccda"
        ]
    },
    {
        "id": "851de0aa26dac355f5f1fa3c",
        "tags": [
            "purple",
            "yellow",
            "neon",
            "space",
            "happy"
        ],
        "colors": [
            "851de0",
            "aa26da",
            "c355f5",
            "f1fa3c"
        ]
    },
    {
        "id": "ffe7d1f6c89f4b8e8d396362",
        "tags": [
            "beige",
            "teal",
            "skin",
            "earth"
        ],
        "colors": [
            "ffe7d1",
            "f6c89f",
            "4b8e8d",
            "396362"
        ]
    },
    {
        "id": "0c093cdf42d1eea5f6fad6d6",
        "tags": [
            "black",
            "purple",
            "pink",
            "beige",
            "wedding"
        ],
        "colors": [
            "0c093c",
            "df42d1",
            "eea5f6",
            "fad6d6"
        ]
    },
    {
        "id": "e5d8bf94aa2ae47312d55252",
        "tags": [
            "beige",
            "green",
            "orange",
            "red",
            "summer",
            "vintage",
            "nature",
            "food",
            "fall",
            "kids"
        ],
        "colors": [
            "e5d8bf",
            "94aa2a",
            "e47312",
            "d55252"
        ]
    },
    {
        "id": "c2e8cef2eee5f6ad7bbe7575",
        "tags": [
            "mint",
            "grey",
            "green",
            "orange",
            "maroon",
            "pastel",
            "summer",
            "cream",
            "vintage",
            "kids"
        ],
        "colors": [
            "c2e8ce",
            "f2eee5",
            "f6ad7b",
            "be7575"
        ]
    },
    {
        "id": "09005757007ec400c6ffa069",
        "tags": [
            "navy",
            "purple",
            "peach",
            "night",
            "dark",
            "halloween"
        ],
        "colors": [
            "090057",
            "57007e",
            "c400c6",
            "ffa069"
        ]
    },
    {
        "id": "5eb7b796d1c7fc7978ffafb0",
        "tags": [
            "teal",
            "red",
            "peach",
            "vintage",
            "kids"
        ],
        "colors": [
            "5eb7b7",
            "96d1c7",
            "fc7978",
            "ffafb0"
        ]
    },
    {
        "id": "dfddc7f58b54a34a28211717",
        "tags": [
            "beige",
            "orange",
            "brown",
            "black",
            "fall",
            "halloween"
        ],
        "colors": [
            "dfddc7",
            "f58b54",
            "a34a28",
            "211717"
        ]
    },
    {
        "id": "6807f99852f9c299fcffd739",
        "tags": [
            "purple",
            "yellow",
            "happy",
            "neon"
        ],
        "colors": [
            "6807f9",
            "9852f9",
            "c299fc",
            "ffd739"
        ]
    },
    {
        "id": "29346200818aec9b3bf7be16",
        "tags": [
            "navy",
            "orange",
            "yellow",
            "retro",
            "kids"
        ],
        "colors": [
            "293462",
            "00818a",
            "ec9b3b",
            "f7be16"
        ]
    },
    {
        "id": "efe9cceadea6f6cd90deb881",
        "tags": [
            "beige",
            "yellow",
            "light",
            "pastel",
            "summer",
            "skin",
            "cream",
            "happy"
        ],
        "colors": [
            "efe9cc",
            "eadea6",
            "f6cd90",
            "deb881"
        ]
    },
    {
        "id": "003f5c58508dbc5090ff6361",
        "tags": [
            "navy",
            "purple",
            "red",
            "space"
        ],
        "colors": [
            "003f5c",
            "58508d",
            "bc5090",
            "ff6361"
        ]
    },
    {
        "id": "ffd369e26241940a375b0909",
        "tags": [
            "yellow",
            "orange",
            "maroon",
            "warm",
            "sunset"
        ],
        "colors": [
            "ffd369",
            "e26241",
            "940a37",
            "5b0909"
        ]
    },
    {
        "id": "f54291ff78aeffa0d2fff8cd",
        "tags": [
            "pink",
            "yellow",
            "light",
            "happy"
        ],
        "colors": [
            "f54291",
            "ff78ae",
            "ffa0d2",
            "fff8cd"
        ]
    },
    {
        "id": "f1d4d4ddb6c6ac8daf484c7f",
        "tags": [
            "skin",
            "pink",
            "purple",
            "navy",
            "pastel",
            "winter",
            "cream",
            "gradient"
        ],
        "colors": [
            "f1d4d4",
            "ddb6c6",
            "ac8daf",
            "484c7f"
        ]
    },
    {
        "id": "ecfcffb2fcff5edfff3e64ff",
        "tags": [
            "blue",
            "neon",
            "cold",
            "happy",
            "sky"
        ],
        "colors": [
            "ecfcff",
            "b2fcff",
            "5edfff",
            "3e64ff"
        ]
    },
    {
        "id": "fff1e9ffd5d5fc7fb245454d",
        "tags": [
            "peach",
            "pink",
            "black",
            "wedding",
            "skin",
            "kids"
        ],
        "colors": [
            "fff1e9",
            "ffd5d5",
            "fc7fb2",
            "45454d"
        ]
    },
    {
        "id": "3c42455f6769719192dfcdc3",
        "tags": [
            "black",
            "grey",
            "teal",
            "beige",
            "cold",
            "winter",
            "earth",
            "vintage"
        ],
        "colors": [
            "3c4245",
            "5f6769",
            "719192",
            "dfcdc3"
        ]
    },
    {
        "id": "7c0a02b22222e25822f1bc31",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "sunset",
            "food",
            "gradient"
        ],
        "colors": [
            "7c0a02",
            "b22222",
            "e25822",
            "f1bc31"
        ]
    },
    {
        "id": "e6f8f9b1e8ededb5f5e86ed0",
        "tags": [
            "blue",
            "pink",
            "purple",
            "light",
            "happy"
        ],
        "colors": [
            "e6f8f9",
            "b1e8ed",
            "edb5f5",
            "e86ed0"
        ]
    },
    {
        "id": "443737272121ff0000ff4d00",
        "tags": [
            "brown",
            "black",
            "red",
            "orange",
            "dark",
            "warm",
            "halloween",
            "neon",
            "space"
        ],
        "colors": [
            "443737",
            "272121",
            "ff0000",
            "ff4d00"
        ]
    },
    {
        "id": "5d14512f416d14868c94ceca",
        "tags": [
            "purple",
            "navy",
            "teal",
            "cold",
            "night",
            "winter"
        ],
        "colors": [
            "5d1451",
            "2f416d",
            "14868c",
            "94ceca"
        ]
    },
    {
        "id": "ffe7addb75c5a05f966a1051",
        "tags": [
            "yellow",
            "purple",
            "maroon"
        ],
        "colors": [
            "ffe7ad",
            "db75c5",
            "a05f96",
            "6a1051"
        ]
    },
    {
        "id": "2a1a5ef45905fb9224fbe555",
        "tags": [
            "navy",
            "orange",
            "yellow",
            "sunset",
            "gold"
        ],
        "colors": [
            "2a1a5e",
            "f45905",
            "fb9224",
            "fbe555"
        ]
    },
    {
        "id": "f9d5bbf66767d356563c3d47",
        "tags": [
            "beige",
            "peach",
            "red",
            "black",
            "warm",
            "kids"
        ],
        "colors": [
            "f9d5bb",
            "f66767",
            "d35656",
            "3c3d47"
        ]
    },
    {
        "id": "4709381a3e595c94bdf2d6eb",
        "tags": [
            "blue",
            "pink",
            "cold",
            "wedding",
            "night"
        ],
        "colors": [
            "470938",
            "1a3e59",
            "5c94bd",
            "f2d6eb"
        ]
    },
    {
        "id": "5026a78d448bcc6a87eccd8f",
        "tags": [
            "purple",
            "peach",
            "beige",
            "sunset",
            "rainbow",
            "gradient"
        ],
        "colors": [
            "5026a7",
            "8d448b",
            "cc6a87",
            "eccd8f"
        ]
    },
    {
        "id": "2337146b591defcfb6fdeced",
        "tags": [
            "green",
            "brown",
            "beige",
            "skin",
            "nature",
            "vintage",
            "food"
        ],
        "colors": [
            "233714",
            "6b591d",
            "efcfb6",
            "fdeced"
        ]
    },
    {
        "id": "6d0c747f78d2d2d0fefdecff",
        "tags": [
            "purple",
            "blue",
            "pink",
            "wedding",
            "gradient"
        ],
        "colors": [
            "6d0c74",
            "7f78d2",
            "d2d0fe",
            "fdecff"
        ]
    },
    {
        "id": "42b88334747435495eff7e67",
        "tags": [
            "green",
            "navy",
            "orange",
            "nature",
            "kids"
        ],
        "colors": [
            "42b883",
            "347474",
            "35495e",
            "ff7e67"
        ]
    },
    {
        "id": "ffdfdffbc1bc315b96233567",
        "tags": [
            "pink",
            "peach",
            "blue",
            "navy",
            "skin",
            "kids"
        ],
        "colors": [
            "ffdfdf",
            "fbc1bc",
            "315b96",
            "233567"
        ]
    },
    {
        "id": "512c963c6f9cdd6892f9c6ba",
        "tags": [
            "purple",
            "blue",
            "pink",
            "beige",
            "peach",
            "vintage",
            "happy",
            "retro"
        ],
        "colors": [
            "512c96",
            "3c6f9c",
            "dd6892",
            "f9c6ba"
        ]
    },
    {
        "id": "445c3cfda77fc9d99efae8c8",
        "tags": [
            "green",
            "orange",
            "peach",
            "beige",
            "summer",
            "pastel",
            "earth",
            "nature",
            "happy"
        ],
        "colors": [
            "445c3c",
            "fda77f",
            "c9d99e",
            "fae8c8"
        ]
    },
    {
        "id": "ffbbccffccccffddccffeecc",
        "tags": [
            "pink",
            "peach",
            "beige",
            "light",
            "skin",
            "pastel",
            "happy",
            "gradient"
        ],
        "colors": [
            "ffbbcc",
            "ffcccc",
            "ffddcc",
            "ffeecc"
        ]
    },
    {
        "id": "1a2849505bdab063c5ffaac3",
        "tags": [
            "navy",
            "blue",
            "purple",
            "pink",
            "cold",
            "space"
        ],
        "colors": [
            "1a2849",
            "505bda",
            "b063c5",
            "ffaac3"
        ]
    },
    {
        "id": "43ab92f75f00c93838512c62",
        "tags": [
            "teal",
            "orange",
            "red",
            "maroon",
            "retro",
            "kids"
        ],
        "colors": [
            "43ab92",
            "f75f00",
            "c93838",
            "512c62"
        ]
    },
    {
        "id": "f9f9f9f6ecbfcaaddec886e5",
        "tags": [
            "white",
            "yellow",
            "purple",
            "light",
            "pastel",
            "happy"
        ],
        "colors": [
            "f9f9f9",
            "f6ecbf",
            "caadde",
            "c886e5"
        ]
    },
    {
        "id": "504658f0decbffb5b5ce2e6c",
        "tags": [
            "grey",
            "beige",
            "peach",
            "maroon",
            "skin",
            "halloween"
        ],
        "colors": [
            "504658",
            "f0decb",
            "ffb5b5",
            "ce2e6c"
        ]
    },
    {
        "id": "394a6d3c9d9b52de97c0ffb3",
        "tags": [
            "navy",
            "teal",
            "green",
            "mint",
            "cold"
        ],
        "colors": [
            "394a6d",
            "3c9d9b",
            "52de97",
            "c0ffb3"
        ]
    },
    {
        "id": "23374d1089ffe5e5e5eeeeee",
        "tags": [
            "navy",
            "blue",
            "grey",
            "cold",
            "retro"
        ],
        "colors": [
            "23374d",
            "1089ff",
            "e5e5e5",
            "eeeeee"
        ]
    },
    {
        "id": "3b064d8105d8ed0ceffe59d7",
        "tags": [],
        "colors": [
            "3b064d",
            "8105d8",
            "ed0cef",
            "fe59d7"
        ]
    },
    {
        "id": "bbeaa6e3c878ed9a73e688a1",
        "tags": [
            "green",
            "orange",
            "pink",
            "pastel",
            "summer",
            "warm",
            "kids",
            "spring",
            "food"
        ],
        "colors": [
            "bbeaa6",
            "e3c878",
            "ed9a73",
            "e688a1"
        ]
    },
    {
        "id": "f7e8f6f1c6e7e5b0eabd83ce",
        "tags": [
            "pink",
            "purple",
            "pastel",
            "wedding",
            "cream",
            "gradient"
        ],
        "colors": [
            "f7e8f6",
            "f1c6e7",
            "e5b0ea",
            "bd83ce"
        ]
    },
    {
        "id": "d9eeec64b2cd3c70a4da9833",
        "tags": [
            "blue",
            "orange",
            "summer",
            "sea"
        ],
        "colors": [
            "d9eeec",
            "64b2cd",
            "3c70a4",
            "da9833"
        ]
    },
    {
        "id": "b2e4d5f2a6a6b18ea6e7f3ee",
        "tags": [
            "teal",
            "peach",
            "pastel",
            "light",
            "kids"
        ],
        "colors": [
            "b2e4d5",
            "f2a6a6",
            "b18ea6",
            "e7f3ee"
        ]
    },
    {
        "id": "f6f07801d28e434982730068",
        "tags": [
            "yellow",
            "green",
            "mint",
            "navy",
            "purple",
            "summer",
            "retro"
        ],
        "colors": [
            "f6f078",
            "01d28e",
            "434982",
            "730068"
        ]
    },
    {
        "id": "fcf9eabadfdbf8a978ffc5a1",
        "tags": [
            "beige",
            "teal",
            "orange",
            "light",
            "pastel",
            "summer",
            "cream",
            "happy"
        ],
        "colors": [
            "fcf9ea",
            "badfdb",
            "f8a978",
            "ffc5a1"
        ]
    },
    {
        "id": "202040202060602080b030b0",
        "tags": [
            "black",
            "navy",
            "purple",
            "dark",
            "night",
            "halloween"
        ],
        "colors": [
            "202040",
            "202060",
            "602080",
            "b030b0"
        ]
    },
    {
        "id": "4baea0b6e6bdf1f0cff0c9c9",
        "tags": [
            "teal",
            "mint",
            "beige",
            "peach",
            "pastel",
            "light",
            "nature",
            "happy"
        ],
        "colors": [
            "4baea0",
            "b6e6bd",
            "f1f0cf",
            "f0c9c9"
        ]
    },
    {
        "id": "c70d3aed510723033802383c",
        "tags": [
            "red",
            "orange",
            "black",
            "green",
            "dark",
            "space",
            "halloween"
        ],
        "colors": [
            "c70d3a",
            "ed5107",
            "230338",
            "02383c"
        ]
    },
    {
        "id": "ddf796f3fe7e979797757575",
        "tags": [
            "green",
            "yellow",
            "grey",
            "retro"
        ],
        "colors": [
            "ddf796",
            "f3fe7e",
            "979797",
            "757575"
        ]
    },
    {
        "id": "47e4bbec9b3be8647c000000",
        "tags": [
            "teal",
            "orange",
            "pink",
            "black",
            "retro",
            "kids"
        ],
        "colors": [
            "47e4bb",
            "ec9b3b",
            "e8647c",
            "000000"
        ]
    },
    {
        "id": "ecf4f3d1eecc76dbd157a99a",
        "tags": [
            "grey",
            "green",
            "teal",
            "cold"
        ],
        "colors": [
            "ecf4f3",
            "d1eecc",
            "76dbd1",
            "57a99a"
        ]
    },
    {
        "id": "e4f2f099d8d070416d170a19",
        "tags": [
            "teal",
            "purple",
            "black",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "e4f2f0",
            "99d8d0",
            "70416d",
            "170a19"
        ]
    },
    {
        "id": "fb0091fb8691fb9e91fbda91",
        "tags": [
            "pink",
            "peach",
            "orange",
            "yellow",
            "skin",
            "kids",
            "warm"
        ],
        "colors": [
            "fb0091",
            "fb8691",
            "fb9e91",
            "fbda91"
        ]
    },
    {
        "id": "f7f7f75d5d5da0c334e5d429",
        "tags": [
            "white",
            "grey",
            "green",
            "yellow",
            "retro",
            "happy"
        ],
        "colors": [
            "f7f7f7",
            "5d5d5d",
            "a0c334",
            "e5d429"
        ]
    },
    {
        "id": "d2fafb51dacf41aaa82c003e",
        "tags": [
            "blue",
            "teal",
            "black",
            "cold"
        ],
        "colors": [
            "d2fafb",
            "51dacf",
            "41aaa8",
            "2c003e"
        ]
    },
    {
        "id": "91b029e6a400eaebd8ffffea",
        "tags": [
            "green",
            "orange",
            "beige",
            "summer",
            "nature"
        ],
        "colors": [
            "91b029",
            "e6a400",
            "eaebd8",
            "ffffea"
        ]
    },
    {
        "id": "fa5477ef4b4bf2e3c97ecfc0",
        "tags": [
            "red",
            "beige",
            "teal",
            "happy"
        ],
        "colors": [
            "fa5477",
            "ef4b4b",
            "f2e3c9",
            "7ecfc0"
        ]
    },
    {
        "id": "d2fafb6bc5d2105e62b5525c",
        "tags": [
            "blue",
            "maroon",
            "winter",
            "cold",
            "wedding"
        ],
        "colors": [
            "d2fafb",
            "6bc5d2",
            "105e62",
            "b5525c"
        ]
    },
    {
        "id": "000272341677a32f80ff6363",
        "tags": [
            "navy",
            "red",
            "dark",
            "neon",
            "night",
            "space"
        ],
        "colors": [
            "000272",
            "341677",
            "a32f80",
            "ff6363"
        ]
    },
    {
        "id": "f77754584b42537d91a4d1c8",
        "tags": [
            "orange",
            "brown",
            "teal",
            "vintage"
        ],
        "colors": [
            "f77754",
            "584b42",
            "537d91",
            "a4d1c8"
        ]
    },
    {
        "id": "1fab89ff8080ffba92c6f1d6",
        "tags": [
            "teal",
            "green",
            "red",
            "peach",
            "mint",
            "kids"
        ],
        "colors": [
            "1fab89",
            "ff8080",
            "ffba92",
            "c6f1d6"
        ]
    },
    {
        "id": "010a43f3d3d3eda593ff3f98",
        "tags": [
            "navy",
            "peach",
            "pink",
            "skin",
            "wedding"
        ],
        "colors": [
            "010a43",
            "f3d3d3",
            "eda593",
            "ff3f98"
        ]
    },
    {
        "id": "b7e77840dab2be6283ed7575",
        "tags": [
            "green",
            "teal",
            "maroon",
            "red",
            "vintage",
            "spring",
            "kids"
        ],
        "colors": [
            "b7e778",
            "40dab2",
            "be6283",
            "ed7575"
        ]
    },
    {
        "id": "45454dff4893ffd5d5fff1e9",
        "tags": [
            "grey",
            "pink",
            "peach"
        ],
        "colors": [
            "45454d",
            "ff4893",
            "ffd5d5",
            "fff1e9"
        ]
    },
    {
        "id": "ebefd032dbc649beb7ff502f",
        "tags": [
            "beige",
            "teal",
            "orange",
            "vintage",
            "summer",
            "happy"
        ],
        "colors": [
            "ebefd0",
            "32dbc6",
            "49beb7",
            "ff502f"
        ]
    },
    {
        "id": "f6f6f6eae9e9d4d7dd420000",
        "tags": [
            "grey",
            "maroon",
            "wedding"
        ],
        "colors": [
            "f6f6f6",
            "eae9e9",
            "d4d7dd",
            "420000"
        ]
    },
    {
        "id": "01024e5438648b4367ff6464",
        "tags": [
            "navy",
            "maroon",
            "red",
            "dark",
            "night",
            "halloween",
            "gradient"
        ],
        "colors": [
            "01024e",
            "543864",
            "8b4367",
            "ff6464"
        ]
    },
    {
        "id": "f0dd92ffffc5d6e4aa83b582",
        "tags": [
            "beige",
            "yellow",
            "green",
            "summer",
            "pastel",
            "earth",
            "light",
            "nature",
            "happy"
        ],
        "colors": [
            "f0dd92",
            "ffffc5",
            "d6e4aa",
            "83b582"
        ]
    },
    {
        "id": "eb7070fec771e6e56c64e291",
        "tags": [
            "red",
            "orange",
            "green",
            "summer",
            "rainbow",
            "kids"
        ],
        "colors": [
            "eb7070",
            "fec771",
            "e6e56c",
            "64e291"
        ]
    },
    {
        "id": "f0d78cfcfafa64c4ed4f81c7",
        "tags": [
            "yellow",
            "white",
            "blue",
            "summer"
        ],
        "colors": [
            "f0d78c",
            "fcfafa",
            "64c4ed",
            "4f81c7"
        ]
    },
    {
        "id": "160f30241663a72693eae7af",
        "tags": [
            "black",
            "navy",
            "blue",
            "purple",
            "dark",
            "space"
        ],
        "colors": [
            "160f30",
            "241663",
            "a72693",
            "eae7af"
        ]
    },
    {
        "id": "c5f0a435b0ab226b80f34573",
        "tags": [
            "green",
            "teal",
            "red",
            "happy"
        ],
        "colors": [
            "c5f0a4",
            "35b0ab",
            "226b80",
            "f34573"
        ]
    },
    {
        "id": "b6ffeafce2aeffb3b3ffdcf7",
        "tags": [
            "mint",
            "peach",
            "pink",
            "light",
            "pastel",
            "skin",
            "neon"
        ],
        "colors": [
            "b6ffea",
            "fce2ae",
            "ffb3b3",
            "ffdcf7"
        ]
    },
    {
        "id": "3a1f5dc83660e15249f6d365",
        "tags": [
            "red",
            "orange",
            "yellow",
            "sunset"
        ],
        "colors": [
            "3a1f5d",
            "c83660",
            "e15249",
            "f6d365"
        ]
    },
    {
        "id": "207561589167a0cc78da4302",
        "tags": [
            "green",
            "orange",
            "nature"
        ],
        "colors": [
            "207561",
            "589167",
            "a0cc78",
            "da4302"
        ]
    },
    {
        "id": "61f2f5ffffffe0e0e0723881",
        "tags": [
            "blue",
            "white",
            "grey",
            "purple",
            "neon",
            "light"
        ],
        "colors": [
            "61f2f5",
            "ffffff",
            "e0e0e0",
            "723881"
        ]
    },
    {
        "id": "6e2142943855e16363ffd692",
        "tags": [
            "maroon",
            "peach",
            "yellow",
            "warm",
            "skin",
            "sunset",
            "wedding",
            "fall",
            "gradient"
        ],
        "colors": [
            "6e2142",
            "943855",
            "e16363",
            "ffd692"
        ]
    },
    {
        "id": "ffcbcbffb5b5407088132743",
        "tags": [
            "pink",
            "peach",
            "blue",
            "navy",
            "vintage"
        ],
        "colors": [
            "ffcbcb",
            "ffb5b5",
            "407088",
            "132743"
        ]
    },
    {
        "id": "fcf9eabadfdb49beb7ff8a5c",
        "tags": [
            "beige",
            "teal",
            "orange",
            "summer",
            "light",
            "kids"
        ],
        "colors": [
            "fcf9ea",
            "badfdb",
            "49beb7",
            "ff8a5c"
        ]
    },
    {
        "id": "200f213820395a3d5cf638dc",
        "tags": [
            "black",
            "purple",
            "dark",
            "night"
        ],
        "colors": [
            "200f21",
            "382039",
            "5a3d5c",
            "f638dc"
        ]
    },
    {
        "id": "9cf196eceba7ebce95edaaaa",
        "tags": [
            "green",
            "yellow",
            "peach",
            "pastel",
            "spring",
            "happy"
        ],
        "colors": [
            "9cf196",
            "eceba7",
            "ebce95",
            "edaaaa"
        ]
    },
    {
        "id": "042f4bfff6dafbc99ded1250",
        "tags": [],
        "colors": [
            "042f4b",
            "fff6da",
            "fbc99d",
            "ed1250"
        ]
    },
    {
        "id": "ebfffbff585861234e032535",
        "tags": [
            "red",
            "black",
            "retro"
        ],
        "colors": [
            "ebfffb",
            "ff5858",
            "61234e",
            "032535"
        ]
    },
    {
        "id": "7ecfc0f2e3c9ec8f6aef4b4b",
        "tags": [
            "teal",
            "beige",
            "orange",
            "red",
            "pastel",
            "happy"
        ],
        "colors": [
            "7ecfc0",
            "f2e3c9",
            "ec8f6a",
            "ef4b4b"
        ]
    },
    {
        "id": "f9e090ff935cdc5353a72461",
        "tags": [
            "yellow",
            "orange",
            "maroon",
            "warm",
            "gold",
            "kids",
            "gradient"
        ],
        "colors": [
            "f9e090",
            "ff935c",
            "dc5353",
            "a72461"
        ]
    },
    {
        "id": "c7f0db8bbabb6c7b95464159",
        "tags": [
            "teal",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "c7f0db",
            "8bbabb",
            "6c7b95",
            "464159"
        ]
    },
    {
        "id": "faf5efd7d1c999b19c672f2f",
        "tags": [
            "beige",
            "grey",
            "green",
            "maroon",
            "winter",
            "earth",
            "nature"
        ],
        "colors": [
            "faf5ef",
            "d7d1c9",
            "99b19c",
            "672f2f"
        ]
    },
    {
        "id": "ffb997f67e7d843b620b032d",
        "tags": [
            "orange",
            "peach",
            "purple",
            "black",
            "warm",
            "gold"
        ],
        "colors": [
            "ffb997",
            "f67e7d",
            "843b62",
            "0b032d"
        ]
    },
    {
        "id": "29346221658300818af7be16",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "cold",
            "kids",
            "sea"
        ],
        "colors": [
            "293462",
            "216583",
            "00818a",
            "f7be16"
        ]
    },
    {
        "id": "696464e9e5ddd04925992e24",
        "tags": [
            "grey",
            "beige",
            "orange",
            "maroon",
            "vintage",
            "fall"
        ],
        "colors": [
            "696464",
            "e9e5dd",
            "d04925",
            "992e24"
        ]
    },
    {
        "id": "00706500a79df5c181ffeecf",
        "tags": [
            "teal",
            "yellow",
            "beige",
            "summer",
            "happy"
        ],
        "colors": [
            "007065",
            "00a79d",
            "f5c181",
            "ffeecf"
        ]
    },
    {
        "id": "cf455cffdd67ff8a5c444444",
        "tags": [
            "red",
            "yellow",
            "orange",
            "black",
            "warm"
        ],
        "colors": [
            "cf455c",
            "ffdd67",
            "ff8a5c",
            "444444"
        ]
    },
    {
        "id": "f6edcff0dab1daf1f9a4d7e1",
        "tags": [
            "beige",
            "blue",
            "pastel",
            "light",
            "summer"
        ],
        "colors": [
            "f6edcf",
            "f0dab1",
            "daf1f9",
            "a4d7e1"
        ]
    },
    {
        "id": "ff8080ffba92e0f5b9c6f1d6",
        "tags": [
            "red",
            "orange",
            "green",
            "mint",
            "teal",
            "pastel",
            "light",
            "summer",
            "rainbow",
            "kids"
        ],
        "colors": [
            "ff8080",
            "ffba92",
            "e0f5b9",
            "c6f1d6"
        ]
    },
    {
        "id": "f9f6f2f1d6aba0855b38470b",
        "tags": [
            "white",
            "beige",
            "brown",
            "skin",
            "earth",
            "cream",
            "coffee",
            "gradient"
        ],
        "colors": [
            "f9f6f2",
            "f1d6ab",
            "a0855b",
            "38470b"
        ]
    },
    {
        "id": "eaeaeaa1dd7000bdaa8559a5",
        "tags": [
            "grey",
            "green",
            "teal",
            "purple",
            "retro",
            "kids"
        ],
        "colors": [
            "eaeaea",
            "a1dd70",
            "00bdaa",
            "8559a5"
        ]
    },
    {
        "id": "44000d83142cad1d45f9d276",
        "tags": [
            "maroon",
            "yellow",
            "dark",
            "warm",
            "night"
        ],
        "colors": [
            "44000d",
            "83142c",
            "ad1d45",
            "f9d276"
        ]
    },
    {
        "id": "08ffc8fff7f7dadada204969",
        "tags": [
            "mint",
            "white",
            "grey",
            "navy",
            "cold",
            "neon"
        ],
        "colors": [
            "08ffc8",
            "fff7f7",
            "dadada",
            "204969"
        ]
    },
    {
        "id": "252525ff0000af0404414141",
        "tags": [
            "black",
            "red",
            "maroon",
            "grey",
            "neon",
            "dark",
            "halloween"
        ],
        "colors": [
            "252525",
            "ff0000",
            "af0404",
            "414141"
        ]
    },
    {
        "id": "fffcc1fdeaabcba1d2ab72c0",
        "tags": [
            "yellow",
            "purple",
            "summer",
            "happy",
            "light"
        ],
        "colors": [
            "fffcc1",
            "fdeaab",
            "cba1d2",
            "ab72c0"
        ]
    },
    {
        "id": "2d3561c05c7ef3826fffb961",
        "tags": [
            "navy",
            "orange",
            "warm",
            "sunset",
            "retro"
        ],
        "colors": [
            "2d3561",
            "c05c7e",
            "f3826f",
            "ffb961"
        ]
    },
    {
        "id": "f4f6f6ff9c91cd3f3e1c2938",
        "tags": [
            "grey",
            "white",
            "peach",
            "orange",
            "maroon",
            "navy",
            "skin",
            "wedding"
        ],
        "colors": [
            "f4f6f6",
            "ff9c91",
            "cd3f3e",
            "1c2938"
        ]
    },
    {
        "id": "f5b5fc96f7d2f0f696fcb1b1",
        "tags": [
            "purple",
            "mint",
            "yellow",
            "peach",
            "neon",
            "pastel",
            "retro",
            "summer",
            "rainbow",
            "happy",
            "kids"
        ],
        "colors": [
            "f5b5fc",
            "96f7d2",
            "f0f696",
            "fcb1b1"
        ]
    },
    {
        "id": "f8f8f850b6bb45969bf96d15",
        "tags": [
            "white",
            "teal",
            "orange",
            "retro"
        ],
        "colors": [
            "f8f8f8",
            "50b6bb",
            "45969b",
            "f96d15"
        ]
    },
    {
        "id": "bb1542eb5f5dfabc74239f95",
        "tags": [
            "red",
            "orange",
            "teal",
            "rainbow",
            "kids"
        ],
        "colors": [
            "bb1542",
            "eb5f5d",
            "fabc74",
            "239f95"
        ]
    },
    {
        "id": "fff1acf9bcddd5a4cfb689b0",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "pastel",
            "spring",
            "light"
        ],
        "colors": [
            "fff1ac",
            "f9bcdd",
            "d5a4cf",
            "b689b0"
        ]
    },
    {
        "id": "ffdfd3fec8d8d291bc957dad",
        "tags": [
            "beige",
            "peach",
            "pink",
            "purple",
            "pastel",
            "vintage",
            "warm",
            "skin",
            "light",
            "cream",
            "gradient"
        ],
        "colors": [
            "ffdfd3",
            "fec8d8",
            "d291bc",
            "957dad"
        ]
    },
    {
        "id": "540e33de356afdc8b76e9086",
        "tags": [
            "maroon",
            "red",
            "beige",
            "vintage",
            "halloween",
            "christmas"
        ],
        "colors": [
            "540e33",
            "de356a",
            "fdc8b7",
            "6e9086"
        ]
    },
    {
        "id": "f38effff00c8ffcecefff0f0",
        "tags": [
            "purple",
            "pink",
            "beige",
            "neon",
            "light",
            "kids"
        ],
        "colors": [
            "f38eff",
            "ff00c8",
            "ffcece",
            "fff0f0"
        ]
    },
    {
        "id": "f9f3ec63aabced383360204b",
        "tags": [
            "beige",
            "teal",
            "red",
            "maroon",
            "vintage",
            "wedding"
        ],
        "colors": [
            "f9f3ec",
            "63aabc",
            "ed3833",
            "60204b"
        ]
    },
    {
        "id": "d3f6f3f9fce1fee9b2fbd1b7",
        "tags": [
            "blue",
            "yellow",
            "peach",
            "light",
            "pastel",
            "summer",
            "kids",
            "spring"
        ],
        "colors": [
            "d3f6f3",
            "f9fce1",
            "fee9b2",
            "fbd1b7"
        ]
    },
    {
        "id": "293462216583f76262fff1c1",
        "tags": [
            "navy",
            "teal",
            "red",
            "retro",
            "space"
        ],
        "colors": [
            "293462",
            "216583",
            "f76262",
            "fff1c1"
        ]
    },
    {
        "id": "f4ff61a8ff3e32ff6a27aa80",
        "tags": [
            "yellow",
            "green",
            "neon",
            "light",
            "summer",
            "happy"
        ],
        "colors": [
            "f4ff61",
            "a8ff3e",
            "32ff6a",
            "27aa80"
        ]
    },
    {
        "id": "60a9a6caf2d7f5fec0fddede",
        "tags": [
            "teal",
            "mint",
            "yellow",
            "pink",
            "light",
            "summer",
            "pastel",
            "happy",
            "spring",
            "nature"
        ],
        "colors": [
            "60a9a6",
            "caf2d7",
            "f5fec0",
            "fddede"
        ]
    },
    {
        "id": "f7e8e8f2a2e4f090d9ea7dc7",
        "tags": [
            "beige",
            "pink",
            "skin",
            "kids"
        ],
        "colors": [
            "f7e8e8",
            "f2a2e4",
            "f090d9",
            "ea7dc7"
        ]
    },
    {
        "id": "e42c64614ad32d248a121b74",
        "tags": [
            "red",
            "maroon",
            "navy",
            "space"
        ],
        "colors": [
            "e42c64",
            "614ad3",
            "2d248a",
            "121b74"
        ]
    },
    {
        "id": "aeeff0f1f0d1f0e3c4daa592",
        "tags": [
            "blue",
            "beige",
            "brown",
            "pastel",
            "light",
            "summer"
        ],
        "colors": [
            "aeeff0",
            "f1f0d1",
            "f0e3c4",
            "daa592"
        ]
    },
    {
        "id": "ca5fa6f36886fa8282ffaf65",
        "tags": [
            "purple",
            "red",
            "peach",
            "orange",
            "warm",
            "wedding",
            "kids",
            "gradient"
        ],
        "colors": [
            "ca5fa6",
            "f36886",
            "fa8282",
            "ffaf65"
        ]
    },
    {
        "id": "fdef96f7b71dafa9392b580c",
        "tags": [
            "yellow",
            "orange",
            "green",
            "summer",
            "warm",
            "nature"
        ],
        "colors": [
            "fdef96",
            "f7b71d",
            "afa939",
            "2b580c"
        ]
    },
    {
        "id": "f2f6f5c8dad393b5b363707e",
        "tags": [
            "grey",
            "teal",
            "vintage",
            "gradient"
        ],
        "colors": [
            "f2f6f5",
            "c8dad3",
            "93b5b3",
            "63707e"
        ]
    },
    {
        "id": "fac0e1caa5f159d4e839bdc8",
        "tags": [
            "pink",
            "purple",
            "teal",
            "happy"
        ],
        "colors": [
            "fac0e1",
            "caa5f1",
            "59d4e8",
            "39bdc8"
        ]
    },
    {
        "id": "dff0ea95adbe574f7d4f3a65",
        "tags": [
            "teal",
            "navy",
            "cold",
            "winter",
            "wedding",
            "sea"
        ],
        "colors": [
            "dff0ea",
            "95adbe",
            "574f7d",
            "4f3a65"
        ]
    },
    {
        "id": "01005952437bff7a8afcf594",
        "tags": [
            "navy",
            "peach",
            "yellow",
            "space"
        ],
        "colors": [
            "010059",
            "52437b",
            "ff7a8a",
            "fcf594"
        ]
    },
    {
        "id": "fafdcbaee7e828c3d4248ea9",
        "tags": [
            "yellow",
            "blue",
            "teal",
            "summer",
            "happy"
        ],
        "colors": [
            "fafdcb",
            "aee7e8",
            "28c3d4",
            "248ea9"
        ]
    },
    {
        "id": "17223b2638596b778dff6768",
        "tags": [
            "navy",
            "red",
            "dark",
            "night"
        ],
        "colors": [
            "17223b",
            "263859",
            "6b778d",
            "ff6768"
        ]
    },
    {
        "id": "f6ef9823eae61b7fbd112f91",
        "tags": [
            "yellow",
            "teal",
            "blue",
            "navy",
            "summer",
            "happy"
        ],
        "colors": [
            "f6ef98",
            "23eae6",
            "1b7fbd",
            "112f91"
        ]
    },
    {
        "id": "525252414141313131ca3e47",
        "tags": [
            "grey",
            "maroon",
            "dark",
            "night",
            "halloween"
        ],
        "colors": [
            "525252",
            "414141",
            "313131",
            "ca3e47"
        ]
    },
    {
        "id": "f4f4f4eadca6e2c275c36a2d",
        "tags": [
            "beige",
            "white",
            "grey",
            "orange",
            "brown",
            "skin",
            "pastel",
            "gold",
            "earth",
            "coffee"
        ],
        "colors": [
            "f4f4f4",
            "eadca6",
            "e2c275",
            "c36a2d"
        ]
    },
    {
        "id": "090088930077e4007cffbd39",
        "tags": [
            "navy",
            "blue",
            "red",
            "yellow",
            "neon",
            "sunset"
        ],
        "colors": [
            "090088",
            "930077",
            "e4007c",
            "ffbd39"
        ]
    },
    {
        "id": "f2f4d1b2d3be89a3b25e6073",
        "tags": [
            "yellow",
            "green",
            "blue",
            "grey",
            "earth",
            "pastel",
            "gradient"
        ],
        "colors": [
            "f2f4d1",
            "b2d3be",
            "89a3b2",
            "5e6073"
        ]
    },
    {
        "id": "f5f687fcfdd8e2bebeb96b9f",
        "tags": [
            "yellow",
            "peach",
            "purple",
            "happy",
            "kids"
        ],
        "colors": [
            "f5f687",
            "fcfdd8",
            "e2bebe",
            "b96b9f"
        ]
    },
    {
        "id": "f2f4f61ee3cf6b48ff0d3f67",
        "tags": [
            "grey",
            "teal",
            "purple",
            "navy",
            "neon",
            "space"
        ],
        "colors": [
            "f2f4f6",
            "1ee3cf",
            "6b48ff",
            "0d3f67"
        ]
    },
    {
        "id": "ff487eff9776ffd5beffedff",
        "tags": [
            "red",
            "pink",
            "peach",
            "orange",
            "skin",
            "spring",
            "kids",
            "gradient"
        ],
        "colors": [
            "ff487e",
            "ff9776",
            "ffd5be",
            "ffedff"
        ]
    },
    {
        "id": "c1f6e7ffcbcbbb71714e3440",
        "tags": [
            "mint",
            "peach",
            "brown",
            "skin",
            "vintage"
        ],
        "colors": [
            "c1f6e7",
            "ffcbcb",
            "bb7171",
            "4e3440"
        ]
    },
    {
        "id": "fff78f22b9ca0c99c1f30cd4",
        "tags": [
            "yellow",
            "teal",
            "purple",
            "retro",
            "kids"
        ],
        "colors": [
            "fff78f",
            "22b9ca",
            "0c99c1",
            "f30cd4"
        ]
    },
    {
        "id": "ffc6beffa1c5a773c3854777",
        "tags": [
            "peach",
            "pink",
            "purple",
            "warm",
            "vintage"
        ],
        "colors": [
            "ffc6be",
            "ffa1c5",
            "a773c3",
            "854777"
        ]
    },
    {
        "id": "f1f4df10eaf00028ff24009c",
        "tags": [
            "beige",
            "teal",
            "blue",
            "navy",
            "cold",
            "neon",
            "winter"
        ],
        "colors": [
            "f1f4df",
            "10eaf0",
            "0028ff",
            "24009c"
        ]
    },
    {
        "id": "e6f0b6b8e9c06384b3684949",
        "tags": [
            "mint",
            "blue",
            "brown",
            "earth"
        ],
        "colors": [
            "e6f0b6",
            "b8e9c0",
            "6384b3",
            "684949"
        ]
    },
    {
        "id": "064acb366ed8f3a953f2f3f3",
        "tags": [
            "blue",
            "orange",
            "grey",
            "white",
            "summer",
            "kids"
        ],
        "colors": [
            "064acb",
            "366ed8",
            "f3a953",
            "f2f3f3"
        ]
    },
    {
        "id": "293462a64942fe5f55fff1c1",
        "tags": [
            "navy",
            "maroon",
            "red",
            "beige",
            "sunset"
        ],
        "colors": [
            "293462",
            "a64942",
            "fe5f55",
            "fff1c1"
        ]
    },
    {
        "id": "8a00d4d527b7ff82c3ffc46b",
        "tags": [
            "purple",
            "pink",
            "orange",
            "kids",
            "neon"
        ],
        "colors": [
            "8a00d4",
            "d527b7",
            "ff82c3",
            "ffc46b"
        ]
    },
    {
        "id": "553c8b9ea9f0ccc1ffffeafe",
        "tags": [
            "purple",
            "blue",
            "wedding",
            "pastel",
            "cold",
            "gradient",
            "sky"
        ],
        "colors": [
            "553c8b",
            "9ea9f0",
            "ccc1ff",
            "ffeafe"
        ]
    },
    {
        "id": "f6f6f6bdf2d57ad9f55d13e7",
        "tags": [
            "grey",
            "white",
            "mint",
            "green",
            "teal",
            "purple",
            "retro",
            "winter"
        ],
        "colors": [
            "f6f6f6",
            "bdf2d5",
            "7ad9f5",
            "5d13e7"
        ]
    },
    {
        "id": "454d6600997558b368d9d872",
        "tags": [
            "navy",
            "green",
            "nature"
        ],
        "colors": [
            "454d66",
            "009975",
            "58b368",
            "d9d872"
        ]
    },
    {
        "id": "fcf9ecb0f4e667eaca12d3cf",
        "tags": [
            "beige",
            "mint",
            "teal",
            "light",
            "summer",
            "spring"
        ],
        "colors": [
            "fcf9ec",
            "b0f4e6",
            "67eaca",
            "12d3cf"
        ]
    },
    {
        "id": "5bd1d7348498004d61ff502f",
        "tags": [
            "teal",
            "blue",
            "red"
        ],
        "colors": [
            "5bd1d7",
            "348498",
            "004d61",
            "ff502f"
        ]
    },
    {
        "id": "b0deffffc5a1ffd19afff8a6",
        "tags": [
            "blue",
            "peach",
            "orange",
            "yellow",
            "skin",
            "light",
            "pastel",
            "kids"
        ],
        "colors": [
            "b0deff",
            "ffc5a1",
            "ffd19a",
            "fff8a6"
        ]
    },
    {
        "id": "fab95b71a0a5665c84212121",
        "tags": [
            "orange",
            "teal",
            "purple",
            "black",
            "vintage"
        ],
        "colors": [
            "fab95b",
            "71a0a5",
            "665c84",
            "212121"
        ]
    },
    {
        "id": "f7ff5694fc134be3ac032d3c",
        "tags": [
            "yellow",
            "green",
            "teal",
            "black",
            "light",
            "neon",
            "summer",
            "happy"
        ],
        "colors": [
            "f7ff56",
            "94fc13",
            "4be3ac",
            "032d3c"
        ]
    },
    {
        "id": "004a2f002f35ff6337ffa323",
        "tags": [
            "green",
            "navy",
            "peach",
            "orange",
            "food"
        ],
        "colors": [
            "004a2f",
            "002f35",
            "ff6337",
            "ffa323"
        ]
    },
    {
        "id": "eeeeeedededeff4949c10000",
        "tags": [],
        "colors": [
            "eeeeee",
            "dedede",
            "ff4949",
            "c10000"
        ]
    },
    {
        "id": "8adfdc3138487353728f758e",
        "tags": [
            "teal",
            "black",
            "purple",
            "vintage",
            "night"
        ],
        "colors": [
            "8adfdc",
            "313848",
            "735372",
            "8f758e"
        ]
    },
    {
        "id": "22eacab31e6fee5a5aff9e74",
        "tags": [
            "teal",
            "mint",
            "maroon",
            "orange",
            "retro",
            "neon",
            "happy"
        ],
        "colors": [
            "22eaca",
            "b31e6f",
            "ee5a5a",
            "ff9e74"
        ]
    },
    {
        "id": "d2f3e0feb9c8f6a7baf5fbf1",
        "tags": [
            "mint",
            "green",
            "pink",
            "light",
            "pastel",
            "cream",
            "kids",
            "spring"
        ],
        "colors": [
            "d2f3e0",
            "feb9c8",
            "f6a7ba",
            "f5fbf1"
        ]
    },
    {
        "id": "e41749f5587bff8a5cfff591",
        "tags": [
            "red",
            "pink",
            "orange",
            "yellow",
            "neon",
            "warm"
        ],
        "colors": [
            "e41749",
            "f5587b",
            "ff8a5c",
            "fff591"
        ]
    },
    {
        "id": "beeef76fc2d0373a6dff8246",
        "tags": [
            "blue",
            "navy",
            "orange",
            "kids"
        ],
        "colors": [
            "beeef7",
            "6fc2d0",
            "373a6d",
            "ff8246"
        ]
    },
    {
        "id": "b206b0e41749f5587bff8a5c",
        "tags": [
            "purple",
            "red",
            "pink",
            "orange",
            "warm"
        ],
        "colors": [
            "b206b0",
            "e41749",
            "f5587b",
            "ff8a5c"
        ]
    },
    {
        "id": "33313b4592afe3c4a8f6f5f5",
        "tags": [
            "black",
            "blue",
            "beige",
            "white",
            "grey",
            "vintage"
        ],
        "colors": [
            "33313b",
            "4592af",
            "e3c4a8",
            "f6f5f5"
        ]
    },
    {
        "id": "f3c1c6f0f69fb0e0a8d8eff0",
        "tags": [
            "pink",
            "yellow",
            "green",
            "blue",
            "light",
            "spring",
            "pastel",
            "rainbow",
            "happy"
        ],
        "colors": [
            "f3c1c6",
            "f0f69f",
            "b0e0a8",
            "d8eff0"
        ]
    },
    {
        "id": "bfcd7eee77778e2e6a311054",
        "tags": [
            "green",
            "orange",
            "maroon",
            "navy",
            "vintage"
        ],
        "colors": [
            "bfcd7e",
            "ee7777",
            "8e2e6a",
            "311054"
        ]
    },
    {
        "id": "211717a34a28f58b54dfddc7",
        "tags": [
            "black",
            "brown",
            "orange",
            "beige",
            "skin",
            "warm",
            "gold",
            "coffee",
            "earth"
        ],
        "colors": [
            "211717",
            "a34a28",
            "f58b54",
            "dfddc7"
        ]
    },
    {
        "id": "ffeaa5226b8040a798ffebd3",
        "tags": [
            "yellow",
            "teal",
            "peach",
            "retro",
            "happy"
        ],
        "colors": [
            "ffeaa5",
            "226b80",
            "40a798",
            "ffebd3"
        ]
    },
    {
        "id": "fff3a3ff7bb0ff3e6d7572f4",
        "tags": [
            "yellow",
            "pink",
            "red",
            "spring",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "fff3a3",
            "ff7bb0",
            "ff3e6d",
            "7572f4"
        ]
    },
    {
        "id": "6c5ce77b88fffdcb6efff3b1",
        "tags": [
            "blue",
            "yellow",
            "summer",
            "happy"
        ],
        "colors": [
            "6c5ce7",
            "7b88ff",
            "fdcb6e",
            "fff3b1"
        ]
    },
    {
        "id": "103c4202576c05a19cffe837",
        "tags": [
            "navy",
            "teal",
            "yellow"
        ],
        "colors": [
            "103c42",
            "02576c",
            "05a19c",
            "ffe837"
        ]
    },
    {
        "id": "e6d3855c7658681313d25959",
        "tags": [
            "yellow",
            "beige",
            "green",
            "maroon",
            "red",
            "food",
            "earth",
            "vintage"
        ],
        "colors": [
            "e6d385",
            "5c7658",
            "681313",
            "d25959"
        ]
    },
    {
        "id": "866ec78f71ff82acffb7fbff",
        "tags": [
            "purple",
            "blue",
            "cold",
            "kids",
            "sky"
        ],
        "colors": [
            "866ec7",
            "8f71ff",
            "82acff",
            "b7fbff"
        ]
    },
    {
        "id": "7fa99bf6e79cf79c1d9c2c2c",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "maroon",
            "vintage"
        ],
        "colors": [
            "7fa99b",
            "f6e79c",
            "f79c1d",
            "9c2c2c"
        ]
    },
    {
        "id": "010059107595fdbfb3fcf594",
        "tags": [
            "navy",
            "teal",
            "peach",
            "yellow",
            "wedding"
        ],
        "colors": [
            "010059",
            "107595",
            "fdbfb3",
            "fcf594"
        ]
    },
    {
        "id": "ab93c9d698b9eda1abffbea3",
        "tags": [
            "purple",
            "peach",
            "pastel",
            "skin",
            "kids",
            "light",
            "gradient"
        ],
        "colors": [
            "ab93c9",
            "d698b9",
            "eda1ab",
            "ffbea3"
        ]
    },
    {
        "id": "560d0d76a21ec6cf65f3ff93",
        "tags": [
            "maroon",
            "brown",
            "green",
            "vintage"
        ],
        "colors": [
            "560d0d",
            "76a21e",
            "c6cf65",
            "f3ff93"
        ]
    },
    {
        "id": "7189bfdf7599ffc78572d6c9",
        "tags": [
            "blue",
            "pink",
            "orange",
            "teal",
            "pastel",
            "vintage",
            "kids",
            "rainbow"
        ],
        "colors": [
            "7189bf",
            "df7599",
            "ffc785",
            "72d6c9"
        ]
    },
    {
        "id": "ebefd032dbc649beb7085f63",
        "tags": [
            "beige",
            "teal",
            "cold"
        ],
        "colors": [
            "ebefd0",
            "32dbc6",
            "49beb7",
            "085f63"
        ]
    },
    {
        "id": "ff0b55d61d4e323232ffdee6",
        "tags": [
            "red",
            "black",
            "pink"
        ],
        "colors": [
            "ff0b55",
            "d61d4e",
            "323232",
            "ffdee6"
        ]
    },
    {
        "id": "222831393e46d65a31eeeeee",
        "tags": [
            "black",
            "grey",
            "orange",
            "white",
            "dark",
            "halloween",
            "night"
        ],
        "colors": [
            "222831",
            "393e46",
            "d65a31",
            "eeeeee"
        ]
    },
    {
        "id": "f5e1daf1f1f149beb7085f63",
        "tags": [
            "peach",
            "grey",
            "white",
            "teal",
            "retro"
        ],
        "colors": [
            "f5e1da",
            "f1f1f1",
            "49beb7",
            "085f63"
        ]
    },
    {
        "id": "e8e8e85588a314537400334e",
        "tags": [
            "grey",
            "blue",
            "navy",
            "cold",
            "winter",
            "night"
        ],
        "colors": [
            "e8e8e8",
            "5588a3",
            "145374",
            "00334e"
        ]
    },
    {
        "id": "a9eec2fad284f38181705772",
        "tags": [
            "mint",
            "green",
            "orange",
            "peach",
            "vintage",
            "summer",
            "happy"
        ],
        "colors": [
            "a9eec2",
            "fad284",
            "f38181",
            "705772"
        ]
    },
    {
        "id": "7f4782aa5c9fe2598bfdd043",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "kids"
        ],
        "colors": [
            "7f4782",
            "aa5c9f",
            "e2598b",
            "fdd043"
        ]
    },
    {
        "id": "616f39ffd98effb677ff8364",
        "tags": [
            "green",
            "orange",
            "peach",
            "summer",
            "skin",
            "pastel",
            "earth",
            "gold"
        ],
        "colors": [
            "616f39",
            "ffd98e",
            "ffb677",
            "ff8364"
        ]
    },
    {
        "id": "0c084c09638600b7a8f0eec8",
        "tags": [
            "navy",
            "blue",
            "teal",
            "beige",
            "cold",
            "winter",
            "space",
            "gradient",
            "sea"
        ],
        "colors": [
            "0c084c",
            "096386",
            "00b7a8",
            "f0eec8"
        ]
    },
    {
        "id": "eaf5ffa9c6de247e6ce4c666",
        "tags": [
            "blue",
            "green",
            "yellow",
            "kids"
        ],
        "colors": [
            "eaf5ff",
            "a9c6de",
            "247e6c",
            "e4c666"
        ]
    },
    {
        "id": "fffde8f7e0a3f09c674c8492",
        "tags": [
            "yellow",
            "beige",
            "orange",
            "skin",
            "summer",
            "gold"
        ],
        "colors": [
            "fffde8",
            "f7e0a3",
            "f09c67",
            "4c8492"
        ]
    },
    {
        "id": "f2eee0c8e6f55ca0d35e0a0a",
        "tags": [
            "beige",
            "blue",
            "maroon",
            "vintage",
            "wedding"
        ],
        "colors": [
            "f2eee0",
            "c8e6f5",
            "5ca0d3",
            "5e0a0a"
        ]
    },
    {
        "id": "f1e4e415cda8099a979764c7",
        "tags": [
            "grey",
            "green",
            "purple",
            "vintage"
        ],
        "colors": [
            "f1e4e4",
            "15cda8",
            "099a97",
            "9764c7"
        ]
    },
    {
        "id": "085f6349beb7facf5aff5959",
        "tags": [
            "teal",
            "yellow",
            "red",
            "retro",
            "kids",
            "rainbow"
        ],
        "colors": [
            "085f63",
            "49beb7",
            "facf5a",
            "ff5959"
        ]
    },
    {
        "id": "305f72f1d1b5f0b7a4f18c8e",
        "tags": [
            "navy",
            "peach",
            "skin",
            "pastel",
            "warm"
        ],
        "colors": [
            "305f72",
            "f1d1b5",
            "f0b7a4",
            "f18c8e"
        ]
    },
    {
        "id": "fff5ebf6e0b3dbcc8f4e4e4e",
        "tags": [
            "beige",
            "yellow",
            "black",
            "skin",
            "cream"
        ],
        "colors": [
            "fff5eb",
            "f6e0b3",
            "dbcc8f",
            "4e4e4e"
        ]
    },
    {
        "id": "d7f7f575cac32a6171f34573",
        "tags": [
            "teal",
            "navy",
            "red",
            "cold"
        ],
        "colors": [
            "d7f7f5",
            "75cac3",
            "2a6171",
            "f34573"
        ]
    },
    {
        "id": "ececec9fd3c7385170142d4c",
        "tags": [],
        "colors": [
            "ececec",
            "9fd3c7",
            "385170",
            "142d4c"
        ]
    },
    {
        "id": "fffbbeeec1eabe97dca374d5",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "pastel",
            "light",
            "happy"
        ],
        "colors": [
            "fffbbe",
            "eec1ea",
            "be97dc",
            "a374d5"
        ]
    },
    {
        "id": "eaeaea00bdaa257aa6621e81",
        "tags": [
            "grey",
            "teal",
            "blue",
            "purple",
            "retro"
        ],
        "colors": [
            "eaeaea",
            "00bdaa",
            "257aa6",
            "621e81"
        ]
    },
    {
        "id": "444444f3006700d1cdeaeaea",
        "tags": [
            "grey",
            "red",
            "teal",
            "neon"
        ],
        "colors": [
            "444444",
            "f30067",
            "00d1cd",
            "eaeaea"
        ]
    },
    {
        "id": "c5fad9aceacff77feedb66e4",
        "tags": [
            "mint",
            "green",
            "pink",
            "purple",
            "kids",
            "neon"
        ],
        "colors": [
            "c5fad9",
            "aceacf",
            "f77fee",
            "db66e4"
        ]
    },
    {
        "id": "fffeecaeddcde4508f556fb5",
        "tags": [
            "yellow",
            "green",
            "red",
            "blue",
            "pastel",
            "spring",
            "rainbow",
            "happy"
        ],
        "colors": [
            "fffeec",
            "aeddcd",
            "e4508f",
            "556fb5"
        ]
    },
    {
        "id": "00028c21aa9301676bffc3e7",
        "tags": [
            "blue",
            "navy",
            "green",
            "pink",
            "vintage",
            "kids"
        ],
        "colors": [
            "00028c",
            "21aa93",
            "01676b",
            "ffc3e7"
        ]
    },
    {
        "id": "5a39216b8c427bc67bffffb5",
        "tags": [
            "brown",
            "green",
            "yellow",
            "nature"
        ],
        "colors": [
            "5a3921",
            "6b8c42",
            "7bc67b",
            "ffffb5"
        ]
    },
    {
        "id": "ffc15e8158fc692db734314f",
        "tags": [
            "orange",
            "purple",
            "retro"
        ],
        "colors": [
            "ffc15e",
            "8158fc",
            "692db7",
            "34314f"
        ]
    },
    {
        "id": "480032df0054ff8b6affd6c2",
        "tags": [
            "maroon",
            "red",
            "orange",
            "peach",
            "warm",
            "halloween",
            "gradient"
        ],
        "colors": [
            "480032",
            "df0054",
            "ff8b6a",
            "ffd6c2"
        ]
    },
    {
        "id": "302387ff379600faacfffdaf",
        "tags": [
            "navy",
            "blue",
            "pink",
            "mint",
            "yellow",
            "neon",
            "retro",
            "rainbow",
            "happy"
        ],
        "colors": [
            "302387",
            "ff3796",
            "00faac",
            "fffdaf"
        ]
    },
    {
        "id": "ff62a5ffe5ae6b76ffdee0d9",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "grey",
            "retro",
            "kids"
        ],
        "colors": [
            "ff62a5",
            "ffe5ae",
            "6b76ff",
            "dee0d9"
        ]
    },
    {
        "id": "f5c7f7c54fa78d309b3426a4",
        "tags": [
            "pink",
            "purple",
            "navy"
        ],
        "colors": [
            "f5c7f7",
            "c54fa7",
            "8d309b",
            "3426a4"
        ]
    },
    {
        "id": "f9fd5085ef4700bd56207dff",
        "tags": [
            "yellow",
            "green",
            "blue",
            "neon",
            "light",
            "summer",
            "happy"
        ],
        "colors": [
            "f9fd50",
            "85ef47",
            "00bd56",
            "207dff"
        ]
    },
    {
        "id": "1836611c4b82dd6b4ddae1e7",
        "tags": [
            "navy",
            "blue",
            "orange",
            "grey",
            "night"
        ],
        "colors": [
            "183661",
            "1c4b82",
            "dd6b4d",
            "dae1e7"
        ]
    },
    {
        "id": "7fe7ccdfe38eefca8cf17e7e",
        "tags": [
            "teal",
            "yellow",
            "red",
            "peach",
            "pastel",
            "rainbow",
            "kids"
        ],
        "colors": [
            "7fe7cc",
            "dfe38e",
            "efca8c",
            "f17e7e"
        ]
    },
    {
        "id": "e7eaf6a2a8d338598b113f67",
        "tags": [
            "navy",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "e7eaf6",
            "a2a8d3",
            "38598b",
            "113f67"
        ]
    },
    {
        "id": "11144c3a9679fabc60e16262",
        "tags": [
            "navy",
            "green",
            "yellow",
            "red",
            "retro",
            "rainbow"
        ],
        "colors": [
            "11144c",
            "3a9679",
            "fabc60",
            "e16262"
        ]
    },
    {
        "id": "e3c4a84592af226089000000",
        "tags": [
            "beige",
            "blue",
            "navy",
            "black",
            "night",
            "winter"
        ],
        "colors": [
            "e3c4a8",
            "4592af",
            "226089",
            "000000"
        ]
    },
    {
        "id": "f6f5f5e9e4e63bb4c1048998",
        "tags": [
            "white",
            "grey",
            "teal"
        ],
        "colors": [
            "f6f5f5",
            "e9e4e6",
            "3bb4c1",
            "048998"
        ]
    },
    {
        "id": "dadddff69314c40b13621295",
        "tags": [
            "grey",
            "orange",
            "red",
            "purple",
            "retro"
        ],
        "colors": [
            "dadddf",
            "f69314",
            "c40b13",
            "621295"
        ]
    },
    {
        "id": "ffd7e8f2c0ffbf9fee866ec7",
        "tags": [
            "pink",
            "purple",
            "kids",
            "gradient"
        ],
        "colors": [
            "ffd7e8",
            "f2c0ff",
            "bf9fee",
            "866ec7"
        ]
    },
    {
        "id": "f8b739f3dcade44985bd245f",
        "tags": [
            "yellow",
            "beige",
            "pink"
        ],
        "colors": [
            "f8b739",
            "f3dcad",
            "e44985",
            "bd245f"
        ]
    },
    {
        "id": "f3f9fb87c0cd226597113f67",
        "tags": [
            "white",
            "blue",
            "navy",
            "cold",
            "winter"
        ],
        "colors": [
            "f3f9fb",
            "87c0cd",
            "226597",
            "113f67"
        ]
    },
    {
        "id": "1d1919ffce760075f60900c3",
        "tags": [
            "black",
            "yellow",
            "blue",
            "navy",
            "space"
        ],
        "colors": [
            "1d1919",
            "ffce76",
            "0075f6",
            "0900c3"
        ]
    },
    {
        "id": "eeeeeed8cbbbbb8fa9560764",
        "tags": [
            "grey",
            "beige",
            "purple",
            "pastel",
            "cream",
            "gradient"
        ],
        "colors": [
            "eeeeee",
            "d8cbbb",
            "bb8fa9",
            "560764"
        ]
    },
    {
        "id": "cdffebffaaaac7004c8f1537",
        "tags": [
            "mint",
            "peach",
            "red",
            "maroon",
            "happy"
        ],
        "colors": [
            "cdffeb",
            "ffaaaa",
            "c7004c",
            "8f1537"
        ]
    },
    {
        "id": "494ca28186d5c6cbefe3e7f1",
        "tags": [
            "blue",
            "grey",
            "cold",
            "winter",
            "sky"
        ],
        "colors": [
            "494ca2",
            "8186d5",
            "c6cbef",
            "e3e7f1"
        ]
    },
    {
        "id": "ff5d9e8f71ff82acff8bffff",
        "tags": [
            "pink",
            "purple",
            "blue",
            "teal",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "ff5d9e",
            "8f71ff",
            "82acff",
            "8bffff"
        ]
    },
    {
        "id": "33313b62374e007880fdc57b",
        "tags": [
            "black",
            "teal",
            "yellow",
            "vintage",
            "dark",
            "night"
        ],
        "colors": [
            "33313b",
            "62374e",
            "007880",
            "fdc57b"
        ]
    },
    {
        "id": "fcd3071c1259ee4266d5daeb",
        "tags": [
            "yellow",
            "navy",
            "red",
            "grey",
            "retro",
            "space"
        ],
        "colors": [
            "fcd307",
            "1c1259",
            "ee4266",
            "d5daeb"
        ]
    },
    {
        "id": "dbe9b7fdfdf6f4dadab8b2a6",
        "tags": [
            "green",
            "white",
            "pink",
            "sage",
            "light",
            "pastel",
            "spring",
            "wedding",
            "earth",
            "food"
        ],
        "colors": [
            "dbe9b7",
            "fdfdf6",
            "f4dada",
            "b8b2a6"
        ]
    },
    {
        "id": "b7fbfffff6beffe0a3ffa1ac",
        "tags": [
            "blue",
            "yellow",
            "pink",
            "summer",
            "light",
            "spring",
            "rainbow",
            "kids"
        ],
        "colors": [
            "b7fbff",
            "fff6be",
            "ffe0a3",
            "ffa1ac"
        ]
    },
    {
        "id": "421b9ba06ee1cbbcf6cef9e2",
        "tags": [
            "purple",
            "mint",
            "retro",
            "wedding"
        ],
        "colors": [
            "421b9b",
            "a06ee1",
            "cbbcf6",
            "cef9e2"
        ]
    },
    {
        "id": "022c43053f5e115173ffd700",
        "tags": [
            "navy",
            "yellow",
            "dark",
            "night",
            "space",
            "sea"
        ],
        "colors": [
            "022c43",
            "053f5e",
            "115173",
            "ffd700"
        ]
    },
    {
        "id": "faf562f36a7bb824a4aaaaaa",
        "tags": [],
        "colors": [
            "faf562",
            "f36a7b",
            "b824a4",
            "aaaaaa"
        ]
    },
    {
        "id": "352961774181e6b2c6f6e5e5",
        "tags": [
            "navy",
            "purple",
            "pink",
            "beige",
            "night",
            "gradient"
        ],
        "colors": [
            "352961",
            "774181",
            "e6b2c6",
            "f6e5e5"
        ]
    },
    {
        "id": "f8f1f1d2c8c8a3816a0a065d",
        "tags": [
            "beige",
            "grey",
            "brown",
            "navy",
            "winter",
            "skin",
            "cream"
        ],
        "colors": [
            "f8f1f1",
            "d2c8c8",
            "a3816a",
            "0a065d"
        ]
    },
    {
        "id": "1b1919616f39a7d129f8eeb4",
        "tags": [
            "black",
            "green",
            "beige",
            "nature",
            "gradient"
        ],
        "colors": [
            "1b1919",
            "616f39",
            "a7d129",
            "f8eeb4"
        ]
    },
    {
        "id": "ffe6ebdefcfccbf1f5a6e3e9",
        "tags": [
            "pink",
            "blue",
            "light",
            "pastel",
            "cream",
            "kids"
        ],
        "colors": [
            "ffe6eb",
            "defcfc",
            "cbf1f5",
            "a6e3e9"
        ]
    },
    {
        "id": "070d591f3c885893d4f7b633",
        "tags": [
            "navy",
            "blue",
            "orange",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "070d59",
            "1f3c88",
            "5893d4",
            "f7b633"
        ]
    },
    {
        "id": "f857b5f781bcfdffdcc5ecbe",
        "tags": [
            "pink",
            "yellow",
            "green",
            "spring",
            "happy"
        ],
        "colors": [
            "f857b5",
            "f781bc",
            "fdffdc",
            "c5ecbe"
        ]
    },
    {
        "id": "6f07654c0045bd512fffb228",
        "tags": [
            "purple",
            "orange",
            "space"
        ],
        "colors": [
            "6f0765",
            "4c0045",
            "bd512f",
            "ffb228"
        ]
    },
    {
        "id": "eeeeeeacc6aa71a0a577628c",
        "tags": [
            "grey",
            "sage",
            "teal",
            "purple",
            "pastel",
            "vintage"
        ],
        "colors": [
            "eeeeee",
            "acc6aa",
            "71a0a5",
            "77628c"
        ]
    },
    {
        "id": "5d3a3a905858b5e0baf7ffbd",
        "tags": [
            "maroon",
            "brown",
            "green",
            "yellow",
            "earth",
            "nature"
        ],
        "colors": [
            "5d3a3a",
            "905858",
            "b5e0ba",
            "f7ffbd"
        ]
    },
    {
        "id": "99235cdf4d19a43737572121",
        "tags": [
            "purple",
            "red",
            "orange",
            "maroon",
            "warm"
        ],
        "colors": [
            "99235c",
            "df4d19",
            "a43737",
            "572121"
        ]
    },
    {
        "id": "b4e9e232dbc6309286ebefd0",
        "tags": [
            "teal",
            "beige"
        ],
        "colors": [
            "b4e9e2",
            "32dbc6",
            "309286",
            "ebefd0"
        ]
    },
    {
        "id": "a1dd70fdfff0e8ecd6a23131",
        "tags": [
            "green",
            "white",
            "beige",
            "red",
            "maroon",
            "spring",
            "food"
        ],
        "colors": [
            "a1dd70",
            "fdfff0",
            "e8ecd6",
            "a23131"
        ]
    },
    {
        "id": "00a8b5774898de4383f3ae4b",
        "tags": [
            "teal",
            "purple",
            "orange",
            "pink",
            "retro",
            "kids"
        ],
        "colors": [
            "00a8b5",
            "774898",
            "de4383",
            "f3ae4b"
        ]
    },
    {
        "id": "6d3580cc4165e4734fffe26f",
        "tags": [
            "purple",
            "red",
            "orange",
            "yellow",
            "sunset",
            "warm",
            "rainbow",
            "gradient"
        ],
        "colors": [
            "6d3580",
            "cc4165",
            "e4734f",
            "ffe26f"
        ]
    },
    {
        "id": "01010169779bacdbdff0ece2",
        "tags": [
            "black",
            "blue",
            "beige",
            "winter",
            "cold",
            "gradient",
            "sea"
        ],
        "colors": [
            "010101",
            "69779b",
            "acdbdf",
            "f0ece2"
        ]
    },
    {
        "id": "51eaeafffde1ff9d76fb3569",
        "tags": [
            "blue",
            "teal",
            "beige",
            "orange",
            "red",
            "summer",
            "light",
            "spring",
            "neon",
            "rainbow",
            "happy"
        ],
        "colors": [
            "51eaea",
            "fffde1",
            "ff9d76",
            "fb3569"
        ]
    },
    {
        "id": "f68787f8a978f1eb9aa4f6a5",
        "tags": [
            "red",
            "peach",
            "orange",
            "yellow",
            "green",
            "light",
            "neon",
            "spring",
            "happy"
        ],
        "colors": [
            "f68787",
            "f8a978",
            "f1eb9a",
            "a4f6a5"
        ]
    },
    {
        "id": "d9d9d9e88a1acf3030141414",
        "tags": [],
        "colors": [
            "d9d9d9",
            "e88a1a",
            "cf3030",
            "141414"
        ]
    },
    {
        "id": "10316b0b8457eac100dee1ec",
        "tags": [
            "blue",
            "navy",
            "green",
            "yellow",
            "grey",
            "vintage"
        ],
        "colors": [
            "10316b",
            "0b8457",
            "eac100",
            "dee1ec"
        ]
    },
    {
        "id": "5e0606831212970690ffa400",
        "tags": [
            "maroon",
            "red",
            "purple",
            "orange",
            "warm"
        ],
        "colors": [
            "5e0606",
            "831212",
            "970690",
            "ffa400"
        ]
    },
    {
        "id": "ffceceffc1c8ffe3b08ed6ff",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "pastel",
            "light",
            "skin",
            "kids"
        ],
        "colors": [
            "ffcece",
            "ffc1c8",
            "ffe3b0",
            "8ed6ff"
        ]
    },
    {
        "id": "2331424f9da6facf5aff5959",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "red"
        ],
        "colors": [
            "233142",
            "4f9da6",
            "facf5a",
            "ff5959"
        ]
    },
    {
        "id": "f3f8ffdeecffc6cfffe8d3ff",
        "tags": [
            "blue",
            "white",
            "pastel",
            "wedding",
            "light",
            "sky"
        ],
        "colors": [
            "f3f8ff",
            "deecff",
            "c6cfff",
            "e8d3ff"
        ]
    },
    {
        "id": "ffa9009d822101444101252a",
        "tags": [
            "orange",
            "teal",
            "black"
        ],
        "colors": [
            "ffa900",
            "9d8221",
            "014441",
            "01252a"
        ]
    },
    {
        "id": "df0e62fac70b12768121174a",
        "tags": [
            "red",
            "yellow",
            "teal",
            "navy",
            "retro",
            "rainbow"
        ],
        "colors": [
            "df0e62",
            "fac70b",
            "127681",
            "21174a"
        ]
    },
    {
        "id": "e8e2dbfab95bf168211a3263",
        "tags": [
            "grey",
            "orange",
            "navy",
            "fall",
            "gold",
            "skin"
        ],
        "colors": [
            "e8e2db",
            "fab95b",
            "f16821",
            "1a3263"
        ]
    },
    {
        "id": "1c819e005542ffbe00dfdfdf",
        "tags": [
            "blue",
            "teal",
            "yellow",
            "grey"
        ],
        "colors": [
            "1c819e",
            "005542",
            "ffbe00",
            "dfdfdf"
        ]
    },
    {
        "id": "ffd3def6b8d15dc0a63f8f8d",
        "tags": [
            "pink",
            "teal",
            "spring",
            "kids"
        ],
        "colors": [
            "ffd3de",
            "f6b8d1",
            "5dc0a6",
            "3f8f8d"
        ]
    },
    {
        "id": "6927ff837dffbf81ffffd581",
        "tags": [
            "purple",
            "blue",
            "yellow",
            "neon",
            "happy"
        ],
        "colors": [
            "6927ff",
            "837dff",
            "bf81ff",
            "ffd581"
        ]
    },
    {
        "id": "f777540187900a516d2b2726",
        "tags": [
            "orange",
            "teal",
            "navy",
            "black",
            "vintage"
        ],
        "colors": [
            "f77754",
            "018790",
            "0a516d",
            "2b2726"
        ]
    },
    {
        "id": "3c415e738598dfe2e21cb3c8",
        "tags": [
            "navy",
            "grey",
            "blue",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "3c415e",
            "738598",
            "dfe2e2",
            "1cb3c8"
        ]
    },
    {
        "id": "f9989ffccb8ffaf096c5f8c8",
        "tags": [
            "red",
            "orange",
            "yellow",
            "mint",
            "light",
            "spring",
            "summer",
            "rainbow",
            "happy"
        ],
        "colors": [
            "f9989f",
            "fccb8f",
            "faf096",
            "c5f8c8"
        ]
    },
    {
        "id": "fcf9edffba5aff7657665c84",
        "tags": [
            "beige",
            "orange",
            "skin",
            "warm",
            "gold"
        ],
        "colors": [
            "fcf9ed",
            "ffba5a",
            "ff7657",
            "665c84"
        ]
    },
    {
        "id": "f5f5f530e3ca2f89fc40514e",
        "tags": [
            "grey",
            "white",
            "teal",
            "blue",
            "cold",
            "retro",
            "neon"
        ],
        "colors": [
            "f5f5f5",
            "30e3ca",
            "2f89fc",
            "40514e"
        ]
    },
    {
        "id": "283148913535bbbbbbe9eec9",
        "tags": [
            "navy",
            "maroon",
            "grey",
            "fall",
            "vintage",
            "night",
            "halloween",
            "earth"
        ],
        "colors": [
            "283148",
            "913535",
            "bbbbbb",
            "e9eec9"
        ]
    },
    {
        "id": "fff4e3ffcdabffa45c5d5d5a",
        "tags": [
            "beige",
            "orange",
            "peach",
            "warm",
            "fall",
            "skin",
            "coffee"
        ],
        "colors": [
            "fff4e3",
            "ffcdab",
            "ffa45c",
            "5d5d5a"
        ]
    },
    {
        "id": "0746840ea5c6a0edf7f2efb6",
        "tags": [
            "navy",
            "blue",
            "beige",
            "happy",
            "sea"
        ],
        "colors": [
            "074684",
            "0ea5c6",
            "a0edf7",
            "f2efb6"
        ]
    },
    {
        "id": "eef2f5ea168e6125701eafed",
        "tags": [
            "grey",
            "white",
            "pink",
            "purple",
            "blue",
            "retro",
            "neon",
            "space",
            "kids"
        ],
        "colors": [
            "eef2f5",
            "ea168e",
            "612570",
            "1eafed"
        ]
    },
    {
        "id": "feffdbffc60bff8b00444444",
        "tags": [
            "yellow",
            "orange",
            "black",
            "summer",
            "fall",
            "warm",
            "gold"
        ],
        "colors": [
            "feffdb",
            "ffc60b",
            "ff8b00",
            "444444"
        ]
    },
    {
        "id": "00204a005792448ef6fdb44b",
        "tags": [
            "navy",
            "blue",
            "orange",
            "winter",
            "cold",
            "night"
        ],
        "colors": [
            "00204a",
            "005792",
            "448ef6",
            "fdb44b"
        ]
    },
    {
        "id": "900c3fc70039ff5733ffc300",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "gold",
            "sunset",
            "gradient"
        ],
        "colors": [
            "900c3f",
            "c70039",
            "ff5733",
            "ffc300"
        ]
    },
    {
        "id": "f4f9f4a7d7c574b49b5c8d89",
        "tags": [
            "white",
            "sage",
            "green",
            "nature",
            "food",
            "kids"
        ],
        "colors": [
            "f4f9f4",
            "a7d7c5",
            "74b49b",
            "5c8d89"
        ]
    },
    {
        "id": "33313b3c4f65834c69e6f5ff",
        "tags": [],
        "colors": [
            "33313b",
            "3c4f65",
            "834c69",
            "e6f5ff"
        ]
    },
    {
        "id": "fffafaffe0e0ffc0d0efdfbf",
        "tags": [
            "white",
            "pink",
            "peach",
            "beige",
            "pastel",
            "light",
            "spring",
            "skin",
            "kids",
            "cream",
            "vintage"
        ],
        "colors": [
            "fffafa",
            "ffe0e0",
            "ffc0d0",
            "efdfbf"
        ]
    },
    {
        "id": "a2eae241aaa8105e62b5525c",
        "tags": [
            "teal",
            "maroon",
            "cold",
            "winter"
        ],
        "colors": [
            "a2eae2",
            "41aaa8",
            "105e62",
            "b5525c"
        ]
    },
    {
        "id": "d34848ff8162ffcd60fffa67",
        "tags": [
            "red",
            "peach",
            "yellow",
            "warm",
            "neon",
            "happy"
        ],
        "colors": [
            "d34848",
            "ff8162",
            "ffcd60",
            "fffa67"
        ]
    },
    {
        "id": "ffcccccaabd89873b9714288",
        "tags": [
            "pink",
            "peach",
            "purple",
            "pastel",
            "wedding"
        ],
        "colors": [
            "ffcccc",
            "caabd8",
            "9873b9",
            "714288"
        ]
    },
    {
        "id": "0c005abc2525ff0000eaeaea",
        "tags": [
            "navy",
            "red",
            "grey",
            "neon",
            "space"
        ],
        "colors": [
            "0c005a",
            "bc2525",
            "ff0000",
            "eaeaea"
        ]
    },
    {
        "id": "cdffeb009f9d07456f0f0a3c",
        "tags": [],
        "colors": [
            "cdffeb",
            "009f9d",
            "07456f",
            "0f0a3c"
        ]
    },
    {
        "id": "ffefe0fed9cac5c5c57d7d7d",
        "tags": [
            "beige",
            "peach",
            "grey",
            "skin",
            "cream",
            "vintage",
            "pastel"
        ],
        "colors": [
            "ffefe0",
            "fed9ca",
            "c5c5c5",
            "7d7d7d"
        ]
    },
    {
        "id": "c82121dee1ecbecbff0d0cb5",
        "tags": [
            "red",
            "blue",
            "retro"
        ],
        "colors": [
            "c82121",
            "dee1ec",
            "becbff",
            "0d0cb5"
        ]
    },
    {
        "id": "ff8484d84c735c3b6f35234b",
        "tags": [
            "peach",
            "purple",
            "night"
        ],
        "colors": [
            "ff8484",
            "d84c73",
            "5c3b6f",
            "35234b"
        ]
    },
    {
        "id": "f4f3f3dfdfdfbfd8d5b1bed5",
        "tags": [
            "grey",
            "teal",
            "blue",
            "pastel",
            "light",
            "cream"
        ],
        "colors": [
            "f4f3f3",
            "dfdfdf",
            "bfd8d5",
            "b1bed5"
        ]
    },
    {
        "id": "3a0088930077e61c5dffe98a",
        "tags": [
            "navy",
            "purple",
            "red",
            "yellow",
            "sunset",
            "rainbow",
            "neon",
            "kids",
            "gradient"
        ],
        "colors": [
            "3a0088",
            "930077",
            "e61c5d",
            "ffe98a"
        ]
    },
    {
        "id": "ef6c577ed3b2b9e6d3f2f2f2",
        "tags": [
            "peach",
            "green",
            "grey",
            "pastel",
            "food",
            "happy"
        ],
        "colors": [
            "ef6c57",
            "7ed3b2",
            "b9e6d3",
            "f2f2f2"
        ]
    },
    {
        "id": "4e21619bbfabebf0c2774e26",
        "tags": [
            "purple",
            "sage",
            "beige",
            "brown",
            "vintage"
        ],
        "colors": [
            "4e2161",
            "9bbfab",
            "ebf0c2",
            "774e26"
        ]
    },
    {
        "id": "cd4545f16821f3a333fffe9a",
        "tags": [
            "red",
            "orange",
            "yellow",
            "warm",
            "halloween",
            "summer",
            "gold"
        ],
        "colors": [
            "cd4545",
            "f16821",
            "f3a333",
            "fffe9a"
        ]
    },
    {
        "id": "eeeeeecde8f6d195f90033c7",
        "tags": [
            "grey",
            "blue",
            "purple",
            "wedding"
        ],
        "colors": [
            "eeeeee",
            "cde8f6",
            "d195f9",
            "0033c7"
        ]
    },
    {
        "id": "f59aa3f5e4c334a7b25b2e35",
        "tags": [
            "pink",
            "peach",
            "beige",
            "teal",
            "brown",
            "vintage",
            "rainbow"
        ],
        "colors": [
            "f59aa3",
            "f5e4c3",
            "34a7b2",
            "5b2e35"
        ]
    },
    {
        "id": "222831393e46b55400eeeeee",
        "tags": [
            "black",
            "grey",
            "brown",
            "dark",
            "winter",
            "night"
        ],
        "colors": [
            "222831",
            "393e46",
            "b55400",
            "eeeeee"
        ]
    },
    {
        "id": "fafafae3e3e3ee6f57cb3737",
        "tags": [
            "white",
            "grey",
            "orange",
            "red",
            "retro"
        ],
        "colors": [
            "fafafa",
            "e3e3e3",
            "ee6f57",
            "cb3737"
        ]
    },
    {
        "id": "d1d1d1c8e8edf7fdb1ded473",
        "tags": [
            "grey",
            "blue",
            "yellow",
            "light",
            "pastel",
            "kids"
        ],
        "colors": [
            "d1d1d1",
            "c8e8ed",
            "f7fdb1",
            "ded473"
        ]
    },
    {
        "id": "fe9191e4406fca23749c297f",
        "tags": [
            "peach",
            "red",
            "purple",
            "warm",
            "wedding",
            "kids",
            "gradient"
        ],
        "colors": [
            "fe9191",
            "e4406f",
            "ca2374",
            "9c297f"
        ]
    },
    {
        "id": "6e3b3bac3f21be6a15f3cf7a",
        "tags": [
            "brown",
            "maroon",
            "beige",
            "warm",
            "gold",
            "skin",
            "earth",
            "food",
            "vintage",
            "coffee",
            "sunset",
            "fall"
        ],
        "colors": [
            "6e3b3b",
            "ac3f21",
            "be6a15",
            "f3cf7a"
        ]
    },
    {
        "id": "6effbfdcaee8ffc5e6fcf2db",
        "tags": [
            "green",
            "purple",
            "pink",
            "beige",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "6effbf",
            "dcaee8",
            "ffc5e6",
            "fcf2db"
        ]
    },
    {
        "id": "d6f8b8acdeaa8fbbaf6b7b8e",
        "tags": [
            "green",
            "navy",
            "pastel",
            "cold",
            "nature",
            "gradient"
        ],
        "colors": [
            "d6f8b8",
            "acdeaa",
            "8fbbaf",
            "6b7b8e"
        ]
    },
    {
        "id": "e6dedd8f1d141b120ff89d13",
        "tags": [
            "grey",
            "red",
            "maroon",
            "black",
            "orange",
            "warm",
            "halloween",
            "fall",
            "vintage",
            "night"
        ],
        "colors": [
            "e6dedd",
            "8f1d14",
            "1b120f",
            "f89d13"
        ]
    },
    {
        "id": "ebfffb7efaff13abc43161a3",
        "tags": [
            "blue",
            "navy",
            "cold",
            "winter",
            "neon"
        ],
        "colors": [
            "ebfffb",
            "7efaff",
            "13abc4",
            "3161a3"
        ]
    },
    {
        "id": "5c4d4d915b4aa96851f2f1e7",
        "tags": [
            "grey",
            "brown",
            "beige",
            "warm",
            "vintage",
            "skin",
            "coffee",
            "earth"
        ],
        "colors": [
            "5c4d4d",
            "915b4a",
            "a96851",
            "f2f1e7"
        ]
    },
    {
        "id": "fa86bea275e39aebedfffcab",
        "tags": [
            "pink",
            "purple",
            "teal",
            "yellow",
            "light",
            "neon",
            "rainbow",
            "kids"
        ],
        "colors": [
            "fa86be",
            "a275e3",
            "9aebed",
            "fffcab"
        ]
    },
    {
        "id": "c9f658dbff3d55968f8acbbb",
        "tags": [
            "green",
            "teal",
            "light",
            "neon",
            "nature"
        ],
        "colors": [
            "c9f658",
            "dbff3d",
            "55968f",
            "8acbbb"
        ]
    },
    {
        "id": "ffaaaae37070c7004c8f1537",
        "tags": [
            "peach",
            "red",
            "maroon",
            "warm",
            "skin"
        ],
        "colors": [
            "ffaaaa",
            "e37070",
            "c7004c",
            "8f1537"
        ]
    },
    {
        "id": "69779b9692afacdbdfd7eaea",
        "tags": [
            "navy",
            "blue",
            "teal",
            "pastel",
            "cold",
            "winter",
            "sky"
        ],
        "colors": [
            "69779b",
            "9692af",
            "acdbdf",
            "d7eaea"
        ]
    },
    {
        "id": "ffedc6cdeeaa96dae46d70c6",
        "tags": [
            "yellow",
            "beige",
            "green",
            "blue",
            "summer",
            "happy",
            "light",
            "gradient"
        ],
        "colors": [
            "ffedc6",
            "cdeeaa",
            "96dae4",
            "6d70c6"
        ]
    },
    {
        "id": "f185b3d5248490007f3d0043",
        "tags": [
            "pink",
            "purple",
            "black",
            "wedding",
            "space"
        ],
        "colors": [
            "f185b3",
            "d52484",
            "90007f",
            "3d0043"
        ]
    },
    {
        "id": "1b335fff6bd6ffb0feffecd3",
        "tags": [
            "navy",
            "pink",
            "beige",
            "happy"
        ],
        "colors": [
            "1b335f",
            "ff6bd6",
            "ffb0fe",
            "ffecd3"
        ]
    },
    {
        "id": "fbfad3c6e377729d3936622b",
        "tags": [
            "beige",
            "green",
            "nature",
            "happy",
            "food"
        ],
        "colors": [
            "fbfad3",
            "c6e377",
            "729d39",
            "36622b"
        ]
    },
    {
        "id": "e8e2dbfab95bf5564e1a3263",
        "tags": [
            "grey",
            "orange",
            "red",
            "navy",
            "warm",
            "fall",
            "gold"
        ],
        "colors": [
            "e8e2db",
            "fab95b",
            "f5564e",
            "1a3263"
        ]
    },
    {
        "id": "f9f8eb76b39d05004efd5f00",
        "tags": [
            "beige",
            "white",
            "teal",
            "navy",
            "orange",
            "retro",
            "vintage",
            "space"
        ],
        "colors": [
            "f9f8eb",
            "76b39d",
            "05004e",
            "fd5f00"
        ]
    },
    {
        "id": "5d50c6f85e9ff18facfacd49",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "kids"
        ],
        "colors": [
            "5d50c6",
            "f85e9f",
            "f18fac",
            "facd49"
        ]
    },
    {
        "id": "f05a28f7931efff0bcfefcdb",
        "tags": [
            "orange",
            "yellow",
            "beige",
            "warm",
            "summer",
            "fall",
            "gold",
            "skin",
            "happy"
        ],
        "colors": [
            "f05a28",
            "f7931e",
            "fff0bc",
            "fefcdb"
        ]
    },
    {
        "id": "f3f9fb474f8551e3d4f3ecd3",
        "tags": [
            "white",
            "navy",
            "teal",
            "beige",
            "cold",
            "retro"
        ],
        "colors": [
            "f3f9fb",
            "474f85",
            "51e3d4",
            "f3ecd3"
        ]
    },
    {
        "id": "3e3838ae7c7c6cbbb3efe784",
        "tags": [
            "brown",
            "teal",
            "yellow",
            "retro",
            "vintage",
            "kids",
            "earth"
        ],
        "colors": [
            "3e3838",
            "ae7c7c",
            "6cbbb3",
            "efe784"
        ]
    },
    {
        "id": "ffb4ac679186264e70ffebd3",
        "tags": [
            "pink",
            "peach",
            "green",
            "navy",
            "beige",
            "vintage",
            "wedding",
            "pastel"
        ],
        "colors": [
            "ffb4ac",
            "679186",
            "264e70",
            "ffebd3"
        ]
    },
    {
        "id": "a8026fdb2d43e76838fbd5af",
        "tags": [
            "purple",
            "red",
            "orange",
            "beige",
            "sunset",
            "warm",
            "gradient"
        ],
        "colors": [
            "a8026f",
            "db2d43",
            "e76838",
            "fbd5af"
        ]
    },
    {
        "id": "fcf8f3aedadddb996c6e7da2",
        "tags": [
            "white",
            "blue",
            "brown",
            "vintage",
            "pastel",
            "earth",
            "winter",
            "light"
        ],
        "colors": [
            "fcf8f3",
            "aedadd",
            "db996c",
            "6e7da2"
        ]
    },
    {
        "id": "b5edbaf06f32a44444594129",
        "tags": [
            "green",
            "mint",
            "orange",
            "maroon",
            "brown",
            "kids",
            "food"
        ],
        "colors": [
            "b5edba",
            "f06f32",
            "a44444",
            "594129"
        ]
    },
    {
        "id": "ffeed0f79f24f12d2d7c064d",
        "tags": [
            "beige",
            "orange",
            "red",
            "sunset",
            "warm",
            "summer",
            "gold"
        ],
        "colors": [
            "ffeed0",
            "f79f24",
            "f12d2d",
            "7c064d"
        ]
    },
    {
        "id": "d7f7f575cac32a6171f3d516",
        "tags": [
            "teal",
            "yellow",
            "happy",
            "summer"
        ],
        "colors": [
            "d7f7f5",
            "75cac3",
            "2a6171",
            "f3d516"
        ]
    },
    {
        "id": "070d591f3c885893d4ceddef",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter",
            "night",
            "sea"
        ],
        "colors": [
            "070d59",
            "1f3c88",
            "5893d4",
            "ceddef"
        ]
    },
    {
        "id": "fafafae0bb20841818000000",
        "tags": [
            "white",
            "yellow",
            "maroon",
            "black",
            "fall",
            "halloween",
            "gold",
            "vintage"
        ],
        "colors": [
            "fafafa",
            "e0bb20",
            "841818",
            "000000"
        ]
    },
    {
        "id": "20716a23a393ffc0c2f7e9e3",
        "tags": [
            "teal",
            "pink",
            "peach",
            "kids"
        ],
        "colors": [
            "20716a",
            "23a393",
            "ffc0c2",
            "f7e9e3"
        ]
    },
    {
        "id": "db2d4387e5dac7f2e3f7aa00",
        "tags": [
            "red",
            "teal",
            "orange",
            "retro",
            "happy",
            "kids"
        ],
        "colors": [
            "db2d43",
            "87e5da",
            "c7f2e3",
            "f7aa00"
        ]
    },
    {
        "id": "58785070907878b0a0f8d0b0",
        "tags": [
            "green",
            "sage",
            "teal",
            "peach",
            "pastel",
            "food",
            "nature"
        ],
        "colors": [
            "587850",
            "709078",
            "78b0a0",
            "f8d0b0"
        ]
    },
    {
        "id": "ff8f56ff5959984a5960424c",
        "tags": [
            "orange",
            "red",
            "maroon",
            "warm"
        ],
        "colors": [
            "ff8f56",
            "ff5959",
            "984a59",
            "60424c"
        ]
    },
    {
        "id": "f2f4fbd22780f8b5005e227f",
        "tags": [
            "white",
            "yellow",
            "purple",
            "retro",
            "neon",
            "happy"
        ],
        "colors": [
            "f2f4fb",
            "d22780",
            "f8b500",
            "5e227f"
        ]
    },
    {
        "id": "ebebe32b2b284a4a48c19898",
        "tags": [
            "grey",
            "black",
            "vintage",
            "night"
        ],
        "colors": [
            "ebebe3",
            "2b2b28",
            "4a4a48",
            "c19898"
        ]
    },
    {
        "id": "feffdfffe79affa952ef5a5a",
        "tags": [
            "yellow",
            "orange",
            "red",
            "warm",
            "light",
            "spring",
            "gold",
            "happy"
        ],
        "colors": [
            "feffdf",
            "ffe79a",
            "ffa952",
            "ef5a5a"
        ]
    },
    {
        "id": "ebf0f698ccd3364e68132238",
        "tags": [
            "grey",
            "blue",
            "navy",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "ebf0f6",
            "98ccd3",
            "364e68",
            "132238"
        ]
    },
    {
        "id": "fdf1dba6cb12e0054384253e",
        "tags": [
            "beige",
            "green",
            "red",
            "maroon",
            "summer",
            "neon",
            "food"
        ],
        "colors": [
            "fdf1db",
            "a6cb12",
            "e00543",
            "84253e"
        ]
    },
    {
        "id": "1d5464207e82298f9bd8d860",
        "tags": [
            "navy",
            "teal",
            "yellow"
        ],
        "colors": [
            "1d5464",
            "207e82",
            "298f9b",
            "d8d860"
        ]
    },
    {
        "id": "c1224ff16f6f94d2e6fff78f",
        "tags": [
            "red",
            "peach",
            "blue",
            "yellow",
            "rainbow",
            "kids"
        ],
        "colors": [
            "c1224f",
            "f16f6f",
            "94d2e6",
            "fff78f"
        ]
    },
    {
        "id": "f3f6c8ea9c1b5f685a362207",
        "tags": [
            "yellow",
            "orange",
            "grey",
            "fall",
            "warm",
            "halloween",
            "vintage"
        ],
        "colors": [
            "f3f6c8",
            "ea9c1b",
            "5f685a",
            "362207"
        ]
    },
    {
        "id": "0b032d843b62f67e7dffb997",
        "tags": [
            "black",
            "purple",
            "peach",
            "orange",
            "halloween",
            "night"
        ],
        "colors": [
            "0b032d",
            "843b62",
            "f67e7d",
            "ffb997"
        ]
    },
    {
        "id": "ece49384a1be5c7893535962",
        "tags": [
            "yellow",
            "blue",
            "grey",
            "pastel",
            "wedding"
        ],
        "colors": [
            "ece493",
            "84a1be",
            "5c7893",
            "535962"
        ]
    },
    {
        "id": "f3f0d1e29c68c85108a20e0e",
        "tags": [
            "beige",
            "orange",
            "maroon",
            "red",
            "fall",
            "skin",
            "gold",
            "coffee",
            "warm",
            "gradient"
        ],
        "colors": [
            "f3f0d1",
            "e29c68",
            "c85108",
            "a20e0e"
        ]
    },
    {
        "id": "260c1af05d23c5d86df7f7f2",
        "tags": [
            "black",
            "orange",
            "green",
            "white",
            "fall",
            "halloween"
        ],
        "colors": [
            "260c1a",
            "f05d23",
            "c5d86d",
            "f7f7f2"
        ]
    },
    {
        "id": "faf9f9add2c95ea3a3488b8f",
        "tags": [
            "white",
            "grey",
            "teal",
            "cold",
            "light"
        ],
        "colors": [
            "faf9f9",
            "add2c9",
            "5ea3a3",
            "488b8f"
        ]
    },
    {
        "id": "eaec9643c0aca93199fa0559",
        "tags": [
            "yellow",
            "teal",
            "purple",
            "red",
            "neon",
            "happy",
            "rainbow"
        ],
        "colors": [
            "eaec96",
            "43c0ac",
            "a93199",
            "fa0559"
        ]
    },
    {
        "id": "f9ececf0d9dac8d9ebecf2f9",
        "tags": [
            "peach",
            "blue",
            "pastel",
            "skin",
            "cream",
            "light",
            "kids"
        ],
        "colors": [
            "f9ecec",
            "f0d9da",
            "c8d9eb",
            "ecf2f9"
        ]
    },
    {
        "id": "071e3d1f4287278ea521e6c1",
        "tags": [
            "black",
            "navy",
            "blue",
            "teal",
            "dark",
            "winter",
            "space",
            "sea"
        ],
        "colors": [
            "071e3d",
            "1f4287",
            "278ea5",
            "21e6c1"
        ]
    },
    {
        "id": "edfffa8bd5cbc56868974949",
        "tags": [
            "teal",
            "brown",
            "peach",
            "maroon",
            "winter"
        ],
        "colors": [
            "edfffa",
            "8bd5cb",
            "c56868",
            "974949"
        ]
    },
    {
        "id": "6b76ffa5aeffc8e4fefeffe0",
        "tags": [
            "blue",
            "yellow",
            "summer",
            "light",
            "happy",
            "gradient"
        ],
        "colors": [
            "6b76ff",
            "a5aeff",
            "c8e4fe",
            "feffe0"
        ]
    },
    {
        "id": "fbeed7ffba5aff7657665c84",
        "tags": [
            "beige",
            "orange",
            "gold",
            "vintage"
        ],
        "colors": [
            "fbeed7",
            "ffba5a",
            "ff7657",
            "665c84"
        ]
    },
    {
        "id": "1d23235c848edecdc3e0e0ec",
        "tags": [
            "black",
            "teal",
            "beige",
            "grey",
            "winter",
            "night",
            "vintage"
        ],
        "colors": [
            "1d2323",
            "5c848e",
            "decdc3",
            "e0e0ec"
        ]
    },
    {
        "id": "f9f8eba7d7c574b49b5c8d89",
        "tags": [
            "beige",
            "teal",
            "pastel",
            "summer",
            "light",
            "wedding",
            "nature",
            "earth"
        ],
        "colors": [
            "f9f8eb",
            "a7d7c5",
            "74b49b",
            "5c8d89"
        ]
    },
    {
        "id": "05004eff0000fb7777ffcccc",
        "tags": [
            "navy",
            "red",
            "pink",
            "halloween",
            "space"
        ],
        "colors": [
            "05004e",
            "ff0000",
            "fb7777",
            "ffcccc"
        ]
    },
    {
        "id": "612147509aaf7dd8c7f5ffc3",
        "tags": [
            "maroon",
            "teal",
            "yellow"
        ],
        "colors": [
            "612147",
            "509aaf",
            "7dd8c7",
            "f5ffc3"
        ]
    },
    {
        "id": "fcf5eefbe8e7f7dddeffc4d0",
        "tags": [
            "beige",
            "white",
            "pink",
            "pastel",
            "cream",
            "skin",
            "light"
        ],
        "colors": [
            "fcf5ee",
            "fbe8e7",
            "f7ddde",
            "ffc4d0"
        ]
    },
    {
        "id": "45b7b87063812c3848f7de1c",
        "tags": [
            "teal",
            "grey",
            "black",
            "yellow",
            "retro"
        ],
        "colors": [
            "45b7b8",
            "706381",
            "2c3848",
            "f7de1c"
        ]
    },
    {
        "id": "ffffd2e4e4e48293ff503bff",
        "tags": [
            "yellow",
            "grey",
            "blue",
            "summer",
            "light",
            "happy"
        ],
        "colors": [
            "ffffd2",
            "e4e4e4",
            "8293ff",
            "503bff"
        ]
    },
    {
        "id": "fdf0f69515557711441e0411",
        "tags": [
            "pink",
            "maroon",
            "black",
            "wedding"
        ],
        "colors": [
            "fdf0f6",
            "951555",
            "771144",
            "1e0411"
        ]
    },
    {
        "id": "d1f6c145b7b78b4c8cf57665",
        "tags": [
            "green",
            "teal",
            "purple",
            "orange",
            "retro",
            "happy"
        ],
        "colors": [
            "d1f6c1",
            "45b7b7",
            "8b4c8c",
            "f57665"
        ]
    },
    {
        "id": "ff9234ffcd3cfefed535d0ba",
        "tags": [
            "orange",
            "yellow",
            "teal",
            "light",
            "kids",
            "summer",
            "gold"
        ],
        "colors": [
            "ff9234",
            "ffcd3c",
            "fefed5",
            "35d0ba"
        ]
    },
    {
        "id": "adccc7144c52053220d34c26",
        "tags": [
            "teal",
            "orange",
            "winter",
            "cold",
            "night"
        ],
        "colors": [
            "adccc7",
            "144c52",
            "053220",
            "d34c26"
        ]
    },
    {
        "id": "64638f9795cfaba9e9cbc9ff",
        "tags": [
            "purple",
            "cold",
            "winter"
        ],
        "colors": [
            "64638f",
            "9795cf",
            "aba9e9",
            "cbc9ff"
        ]
    },
    {
        "id": "fbf9fafd0054a800382b2024",
        "tags": [
            "white",
            "red",
            "maroon",
            "black"
        ],
        "colors": [
            "fbf9fa",
            "fd0054",
            "a80038",
            "2b2024"
        ]
    },
    {
        "id": "37364063686e7e97a6b6f7c1",
        "tags": [
            "black",
            "grey",
            "green",
            "mint",
            "space"
        ],
        "colors": [
            "373640",
            "63686e",
            "7e97a6",
            "b6f7c1"
        ]
    },
    {
        "id": "f2f4b2cce4900c907d0d627a",
        "tags": [
            "yellow",
            "green",
            "teal",
            "blue",
            "summer"
        ],
        "colors": [
            "f2f4b2",
            "cce490",
            "0c907d",
            "0d627a"
        ]
    },
    {
        "id": "f9f9f9bcbab89d8f8f625757",
        "tags": [
            "white",
            "grey",
            "brown",
            "coffee",
            "vintage",
            "pastel"
        ],
        "colors": [
            "f9f9f9",
            "bcbab8",
            "9d8f8f",
            "625757"
        ]
    },
    {
        "id": "a26ea1f18a9bffb480ffff9d",
        "tags": [
            "purple",
            "peach",
            "orange",
            "yellow",
            "sunset",
            "rainbow",
            "light",
            "happy",
            "gradient",
            "sky"
        ],
        "colors": [
            "a26ea1",
            "f18a9b",
            "ffb480",
            "ffff9d"
        ]
    },
    {
        "id": "fff0f8ffc2e9cca2e1543e5c",
        "tags": [
            "pink",
            "purple",
            "wedding",
            "kids"
        ],
        "colors": [
            "fff0f8",
            "ffc2e9",
            "cca2e1",
            "543e5c"
        ]
    },
    {
        "id": "373331605a5680ac7be8eaa1",
        "tags": [
            "black",
            "grey",
            "green",
            "night",
            "earth"
        ],
        "colors": [
            "373331",
            "605a56",
            "80ac7b",
            "e8eaa1"
        ]
    },
    {
        "id": "7acfdff47645f9ad8dfde3d9",
        "tags": [
            "blue",
            "orange",
            "peach",
            "summer",
            "kids"
        ],
        "colors": [
            "7acfdf",
            "f47645",
            "f9ad8d",
            "fde3d9"
        ]
    },
    {
        "id": "deecfcb9ceeb87a8d0c3b4d2",
        "tags": [
            "blue",
            "winter",
            "pastel"
        ],
        "colors": [
            "deecfc",
            "b9ceeb",
            "87a8d0",
            "c3b4d2"
        ]
    },
    {
        "id": "f2f7ff0b409c10316bffe867",
        "tags": [
            "white",
            "blue",
            "navy",
            "yellow",
            "winter",
            "cold"
        ],
        "colors": [
            "f2f7ff",
            "0b409c",
            "10316b",
            "ffe867"
        ]
    },
    {
        "id": "c7f2e39ed9c5eeddd2b73535",
        "tags": [],
        "colors": [
            "c7f2e3",
            "9ed9c5",
            "eeddd2",
            "b73535"
        ]
    },
    {
        "id": "9fe8fa26baee73d2f3fff4e0",
        "tags": [
            "blue",
            "beige",
            "summer",
            "light"
        ],
        "colors": [
            "9fe8fa",
            "26baee",
            "73d2f3",
            "fff4e0"
        ]
    },
    {
        "id": "f7f7f7eeeeee393e46929aab",
        "tags": [
            "white",
            "grey",
            "black",
            "cream"
        ],
        "colors": [
            "f7f7f7",
            "eeeeee",
            "393e46",
            "929aab"
        ]
    },
    {
        "id": "a8026fdb2d43e76838fbf9af",
        "tags": [
            "purple",
            "red",
            "orange",
            "yellow",
            "sunset",
            "warm"
        ],
        "colors": [
            "a8026f",
            "db2d43",
            "e76838",
            "fbf9af"
        ]
    },
    {
        "id": "b8ffd0ecffc1ffe6ccdfbaf7",
        "tags": [
            "mint",
            "yellow",
            "peach",
            "purple",
            "light",
            "spring",
            "neon",
            "pastel",
            "kids"
        ],
        "colors": [
            "b8ffd0",
            "ecffc1",
            "ffe6cc",
            "dfbaf7"
        ]
    },
    {
        "id": "f8b500ece8d900adb5393e46",
        "tags": [
            "orange",
            "beige",
            "teal",
            "black",
            "retro"
        ],
        "colors": [
            "f8b500",
            "ece8d9",
            "00adb5",
            "393e46"
        ]
    },
    {
        "id": "00579253cde2d1f4faedf9fc",
        "tags": [
            "navy",
            "blue",
            "cold",
            "winter",
            "sky"
        ],
        "colors": [
            "005792",
            "53cde2",
            "d1f4fa",
            "edf9fc"
        ]
    },
    {
        "id": "1fe5bd41a7b35e227fd22780",
        "tags": [
            "teal",
            "purple",
            "space"
        ],
        "colors": [
            "1fe5bd",
            "41a7b3",
            "5e227f",
            "d22780"
        ]
    },
    {
        "id": "f2f4fbff9280ff240045315d",
        "tags": [
            "white",
            "grey",
            "orange",
            "red"
        ],
        "colors": [
            "f2f4fb",
            "ff9280",
            "ff2400",
            "45315d"
        ]
    },
    {
        "id": "033fff4a9ff55ff4eec2fcf6",
        "tags": [
            "blue",
            "teal",
            "cold",
            "winter",
            "neon",
            "happy"
        ],
        "colors": [
            "033fff",
            "4a9ff5",
            "5ff4ee",
            "c2fcf6"
        ]
    },
    {
        "id": "ccf0c3bca3ca7c47894a0e5c",
        "tags": [
            "green",
            "purple",
            "retro",
            "vintage"
        ],
        "colors": [
            "ccf0c3",
            "bca3ca",
            "7c4789",
            "4a0e5c"
        ]
    },
    {
        "id": "0000003e432e616f39a7d129",
        "tags": [
            "black",
            "green",
            "dark",
            "winter",
            "night"
        ],
        "colors": [
            "000000",
            "3e432e",
            "616f39",
            "a7d129"
        ]
    },
    {
        "id": "73dbc4faf7e6ff008bfff8a1",
        "tags": [
            "teal",
            "beige",
            "pink",
            "yellow",
            "spring",
            "neon",
            "happy"
        ],
        "colors": [
            "73dbc4",
            "faf7e6",
            "ff008b",
            "fff8a1"
        ]
    },
    {
        "id": "2d39999a1ba0f08181ebbb91",
        "tags": [
            "navy",
            "purple",
            "peach",
            "vintage"
        ],
        "colors": [
            "2d3999",
            "9a1ba0",
            "f08181",
            "ebbb91"
        ]
    },
    {
        "id": "f5efe3e6e7e5f7d3baa6aa9c",
        "tags": [
            "beige",
            "grey",
            "peach",
            "pastel",
            "skin",
            "earth",
            "coffee",
            "food",
            "vintage"
        ],
        "colors": [
            "f5efe3",
            "e6e7e5",
            "f7d3ba",
            "a6aa9c"
        ]
    },
    {
        "id": "dfe2feb1cbfa8e98f57874f2",
        "tags": [
            "blue",
            "cold",
            "winter"
        ],
        "colors": [
            "dfe2fe",
            "b1cbfa",
            "8e98f5",
            "7874f2"
        ]
    },
    {
        "id": "ff1f5affd615f9ff211e2a78",
        "tags": [
            "red",
            "yellow",
            "navy",
            "light",
            "neon",
            "kids"
        ],
        "colors": [
            "ff1f5a",
            "ffd615",
            "f9ff21",
            "1e2a78"
        ]
    },
    {
        "id": "d1f4fa005792ffe6ebffcdcd",
        "tags": [
            "blue",
            "navy",
            "peach",
            "kids"
        ],
        "colors": [
            "d1f4fa",
            "005792",
            "ffe6eb",
            "ffcdcd"
        ]
    },
    {
        "id": "ddf51612e2a33891680f117a",
        "tags": [
            "yellow",
            "teal",
            "navy",
            "nature"
        ],
        "colors": [
            "ddf516",
            "12e2a3",
            "389168",
            "0f117a"
        ]
    },
    {
        "id": "343434e6b31efcfaf1cacaca",
        "tags": [
            "black",
            "orange",
            "white",
            "grey",
            "gold",
            "vintage"
        ],
        "colors": [
            "343434",
            "e6b31e",
            "fcfaf1",
            "cacaca"
        ]
    },
    {
        "id": "0000ff6a5acdadd8e6e6e6fa",
        "tags": [
            "blue",
            "purple",
            "teal",
            "cold"
        ],
        "colors": [
            "0000ff",
            "6a5acd",
            "add8e6",
            "e6e6fa"
        ]
    },
    {
        "id": "cb9b42b1d1c5f2f3eedbd7cb",
        "tags": [
            "brown",
            "teal",
            "grey",
            "pastel",
            "earth",
            "cream"
        ],
        "colors": [
            "cb9b42",
            "b1d1c5",
            "f2f3ee",
            "dbd7cb"
        ]
    },
    {
        "id": "ff8000d3560e851e52521168",
        "tags": [
            "orange",
            "maroon",
            "purple",
            "warm"
        ],
        "colors": [
            "ff8000",
            "d3560e",
            "851e52",
            "521168"
        ]
    },
    {
        "id": "dcb5ffd9f2ffa5bdfd77529e",
        "tags": [
            "pink",
            "blue",
            "purple",
            "kids"
        ],
        "colors": [
            "dcb5ff",
            "d9f2ff",
            "a5bdfd",
            "77529e"
        ]
    },
    {
        "id": "f7f4e3d2e1c8fee4a6f9c4aa",
        "tags": [
            "beige",
            "sage",
            "yellow",
            "peach",
            "pastel",
            "summer",
            "light",
            "kids",
            "cream"
        ],
        "colors": [
            "f7f4e3",
            "d2e1c8",
            "fee4a6",
            "f9c4aa"
        ]
    },
    {
        "id": "12e6c8a287f4414141000000",
        "tags": [
            "teal",
            "purple",
            "grey",
            "black",
            "space"
        ],
        "colors": [
            "12e6c8",
            "a287f4",
            "414141",
            "000000"
        ]
    },
    {
        "id": "bae5d5d7acd4eec2c2f2f2b0",
        "tags": [
            "teal",
            "purple",
            "peach",
            "yellow",
            "pastel",
            "retro",
            "kids",
            "light"
        ],
        "colors": [
            "bae5d5",
            "d7acd4",
            "eec2c2",
            "f2f2b0"
        ]
    },
    {
        "id": "573697933f99e88c5dfadbac",
        "tags": [
            "purple",
            "orange",
            "beige",
            "wedding"
        ],
        "colors": [
            "573697",
            "933f99",
            "e88c5d",
            "fadbac"
        ]
    },
    {
        "id": "f1fff1c4f0c5be37376a0000",
        "tags": [
            "green",
            "red",
            "maroon"
        ],
        "colors": [
            "f1fff1",
            "c4f0c5",
            "be3737",
            "6a0000"
        ]
    },
    {
        "id": "a3f3ebf1ffabfbd341fb9a40",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "gold",
            "summer",
            "light",
            "happy",
            "neon"
        ],
        "colors": [
            "a3f3eb",
            "f1ffab",
            "fbd341",
            "fb9a40"
        ]
    },
    {
        "id": "2c28283b2c8521989785cfcb",
        "tags": [
            "black",
            "purple",
            "teal",
            "dark",
            "winter",
            "night",
            "space",
            "sea"
        ],
        "colors": [
            "2c2828",
            "3b2c85",
            "219897",
            "85cfcb"
        ]
    },
    {
        "id": "faf6e9ece8d9fffdf6494949",
        "tags": [
            "beige",
            "white",
            "grey",
            "pastel",
            "wedding",
            "skin",
            "cream"
        ],
        "colors": [
            "faf6e9",
            "ece8d9",
            "fffdf6",
            "494949"
        ]
    },
    {
        "id": "5f18548b104e1abb9cf7f7f7",
        "tags": [
            "maroon",
            "teal",
            "white"
        ],
        "colors": [
            "5f1854",
            "8b104e",
            "1abb9c",
            "f7f7f7"
        ]
    },
    {
        "id": "20716a23a393f4a9c7fff78c",
        "tags": [
            "green",
            "pink",
            "yellow",
            "wedding",
            "happy"
        ],
        "colors": [
            "20716a",
            "23a393",
            "f4a9c7",
            "fff78c"
        ]
    },
    {
        "id": "6bd5e1ffd98effb677ff8364",
        "tags": [
            "blue",
            "orange",
            "peach",
            "summer",
            "kids"
        ],
        "colors": [
            "6bd5e1",
            "ffd98e",
            "ffb677",
            "ff8364"
        ]
    },
    {
        "id": "612c83509aaf7dd8c7f5ffc3",
        "tags": [
            "purple",
            "teal",
            "yellow"
        ],
        "colors": [
            "612c83",
            "509aaf",
            "7dd8c7",
            "f5ffc3"
        ]
    },
    {
        "id": "c3f1fff87d42db395100136c",
        "tags": [
            "blue",
            "orange",
            "red",
            "navy",
            "kids"
        ],
        "colors": [
            "c3f1ff",
            "f87d42",
            "db3951",
            "00136c"
        ]
    },
    {
        "id": "f0ece2dfd3c3c7b198596e79",
        "tags": [
            "beige",
            "brown",
            "pastel",
            "vintage",
            "skin",
            "coffee",
            "earth",
            "fall"
        ],
        "colors": [
            "f0ece2",
            "dfd3c3",
            "c7b198",
            "596e79"
        ]
    },
    {
        "id": "fb929effdfdffff6f6aedefc",
        "tags": [
            "peach",
            "pink",
            "white",
            "blue",
            "kids"
        ],
        "colors": [
            "fb929e",
            "ffdfdf",
            "fff6f6",
            "aedefc"
        ]
    },
    {
        "id": "f5e965ff9668db456fa74faf",
        "tags": [
            "yellow",
            "orange",
            "red",
            "purple",
            "sunset",
            "neon"
        ],
        "colors": [
            "f5e965",
            "ff9668",
            "db456f",
            "a74faf"
        ]
    },
    {
        "id": "dbf1f2cd5555882042efedbb",
        "tags": [
            "blue",
            "red",
            "maroon",
            "beige",
            "vintage",
            "wedding"
        ],
        "colors": [
            "dbf1f2",
            "cd5555",
            "882042",
            "efedbb"
        ]
    },
    {
        "id": "d3d5fd929aab474a560b0b0d",
        "tags": [
            "purple",
            "grey",
            "black",
            "winter",
            "cold",
            "night"
        ],
        "colors": [
            "d3d5fd",
            "929aab",
            "474a56",
            "0b0b0d"
        ]
    },
    {
        "id": "35013fb643cdff5da299ddcc",
        "tags": [
            "purple",
            "pink",
            "teal",
            "wedding",
            "retro",
            "neon",
            "space"
        ],
        "colors": [
            "35013f",
            "b643cd",
            "ff5da2",
            "99ddcc"
        ]
    },
    {
        "id": "eeeeee7971ea393e46222831",
        "tags": [
            "grey",
            "black",
            "wedding"
        ],
        "colors": [
            "eeeeee",
            "7971ea",
            "393e46",
            "222831"
        ]
    },
    {
        "id": "a1c45afff9e0f1c550ea4c4c",
        "tags": [
            "green",
            "beige",
            "yellow",
            "red",
            "summer",
            "food",
            "kids"
        ],
        "colors": [
            "a1c45a",
            "fff9e0",
            "f1c550",
            "ea4c4c"
        ]
    },
    {
        "id": "481380742dd2efb1ffffe2ff",
        "tags": [
            "purple",
            "pink",
            "cold",
            "gradient"
        ],
        "colors": [
            "481380",
            "742dd2",
            "efb1ff",
            "ffe2ff"
        ]
    },
    {
        "id": "00a8b5774898e62a76fbb901",
        "tags": [
            "teal",
            "purple",
            "pink",
            "yellow",
            "retro",
            "rainbow",
            "kids"
        ],
        "colors": [
            "00a8b5",
            "774898",
            "e62a76",
            "fbb901"
        ]
    },
    {
        "id": "fdfdc4ffe8cfffdedeccffec",
        "tags": [
            "yellow",
            "peach",
            "pink",
            "teal",
            "light",
            "pastel",
            "summer",
            "cream"
        ],
        "colors": [
            "fdfdc4",
            "ffe8cf",
            "ffdede",
            "ccffec"
        ]
    },
    {
        "id": "ecf4f376dbd157a99a555151",
        "tags": [
            "grey",
            "teal"
        ],
        "colors": [
            "ecf4f3",
            "76dbd1",
            "57a99a",
            "555151"
        ]
    },
    {
        "id": "f0f2ebb5592af090278cbeaa",
        "tags": [
            "grey",
            "white",
            "brown",
            "orange",
            "teal",
            "fall",
            "gold"
        ],
        "colors": [
            "f0f2eb",
            "b5592a",
            "f09027",
            "8cbeaa"
        ]
    },
    {
        "id": "f30e5cf6f3a7f6c523228c7b",
        "tags": [
            "red",
            "yellow",
            "teal",
            "spring",
            "happy"
        ],
        "colors": [
            "f30e5c",
            "f6f3a7",
            "f6c523",
            "228c7b"
        ]
    },
    {
        "id": "b6e1e09cd3d3e8630a2b4353",
        "tags": [
            "blue",
            "orange",
            "navy"
        ],
        "colors": [
            "b6e1e0",
            "9cd3d3",
            "e8630a",
            "2b4353"
        ]
    },
    {
        "id": "3634345c575762929aefecec",
        "tags": [
            "black",
            "grey",
            "teal",
            "winter",
            "space",
            "night"
        ],
        "colors": [
            "363434",
            "5c5757",
            "62929a",
            "efecec"
        ]
    },
    {
        "id": "e9e2d0ea90856e57734f323b",
        "tags": [
            "beige",
            "peach",
            "purple",
            "vintage",
            "wedding"
        ],
        "colors": [
            "e9e2d0",
            "ea9085",
            "6e5773",
            "4f323b"
        ]
    },
    {
        "id": "a3a7e4bae2bef0f1b3c5e5e3",
        "tags": [
            "purple",
            "green",
            "yellow",
            "blue",
            "summer",
            "light",
            "kids"
        ],
        "colors": [
            "a3a7e4",
            "bae2be",
            "f0f1b3",
            "c5e5e3"
        ]
    },
    {
        "id": "ff5959ffad5a4f9da61a0841",
        "tags": [
            "red",
            "orange",
            "teal",
            "navy",
            "retro",
            "rainbow"
        ],
        "colors": [
            "ff5959",
            "ffad5a",
            "4f9da6",
            "1a0841"
        ]
    },
    {
        "id": "89f8cef5fac7dec8edcc99f9",
        "tags": [
            "mint",
            "yellow",
            "purple",
            "light",
            "neon",
            "happy",
            "spring"
        ],
        "colors": [
            "89f8ce",
            "f5fac7",
            "dec8ed",
            "cc99f9"
        ]
    },
    {
        "id": "7b3c3cdb5f29f0f0e468bde1",
        "tags": [
            "maroon",
            "brown",
            "orange",
            "white",
            "blue",
            "retro"
        ],
        "colors": [
            "7b3c3c",
            "db5f29",
            "f0f0e4",
            "68bde1"
        ]
    },
    {
        "id": "e0ffcdfdffcdffebbbffcab0",
        "tags": [
            "green",
            "yellow",
            "peach",
            "pastel",
            "light",
            "summer",
            "nature",
            "happy"
        ],
        "colors": [
            "e0ffcd",
            "fdffcd",
            "ffebbb",
            "ffcab0"
        ]
    },
    {
        "id": "1829522b35957045afe14594",
        "tags": [
            "navy",
            "blue",
            "purple",
            "dark",
            "space"
        ],
        "colors": [
            "182952",
            "2b3595",
            "7045af",
            "e14594"
        ]
    },
    {
        "id": "f7f7f7393e465c636ef8b500",
        "tags": [
            "white",
            "grey",
            "yellow",
            "vintage"
        ],
        "colors": [
            "f7f7f7",
            "393e46",
            "5c636e",
            "f8b500"
        ]
    },
    {
        "id": "ffd96af34949ff9090ffb6b9",
        "tags": [
            "yellow",
            "red",
            "peach",
            "pink",
            "warm",
            "summer",
            "happy"
        ],
        "colors": [
            "ffd96a",
            "f34949",
            "ff9090",
            "ffb6b9"
        ]
    },
    {
        "id": "155e6376b39df9f8ebeae7e7",
        "tags": [
            "teal",
            "green",
            "beige",
            "grey",
            "nature"
        ],
        "colors": [
            "155e63",
            "76b39d",
            "f9f8eb",
            "eae7e7"
        ]
    },
    {
        "id": "ff9900ca431d8b104e520556",
        "tags": [
            "orange",
            "maroon",
            "purple",
            "warm",
            "sunset",
            "gradient"
        ],
        "colors": [
            "ff9900",
            "ca431d",
            "8b104e",
            "520556"
        ]
    },
    {
        "id": "f9499efff0dbbbbbbb5e5e5e",
        "tags": [
            "pink",
            "beige",
            "grey",
            "wedding"
        ],
        "colors": [
            "f9499e",
            "fff0db",
            "bbbbbb",
            "5e5e5e"
        ]
    },
    {
        "id": "f7aa0023578440a8c4bcdbdf",
        "tags": [
            "orange",
            "navy",
            "blue",
            "vintage"
        ],
        "colors": [
            "f7aa00",
            "235784",
            "40a8c4",
            "bcdbdf"
        ]
    },
    {
        "id": "f7f7f73b09445f18541abb9c",
        "tags": [
            "white",
            "grey",
            "purple",
            "teal",
            "wedding",
            "retro"
        ],
        "colors": [
            "f7f7f7",
            "3b0944",
            "5f1854",
            "1abb9c"
        ]
    },
    {
        "id": "f5f4e8c50d66f07810eec60a",
        "tags": [
            "beige",
            "red",
            "orange",
            "yellow",
            "gold",
            "happy"
        ],
        "colors": [
            "f5f4e8",
            "c50d66",
            "f07810",
            "eec60a"
        ]
    },
    {
        "id": "fef9d9ce7d0093590000541a",
        "tags": [
            "yellow",
            "beige",
            "brown",
            "green",
            "vintage",
            "skin",
            "earth",
            "gold"
        ],
        "colors": [
            "fef9d9",
            "ce7d00",
            "935900",
            "00541a"
        ]
    },
    {
        "id": "fad3cfa696c82470a0060608",
        "tags": [
            "peach",
            "pink",
            "purple",
            "blue",
            "black",
            "wedding",
            "retro"
        ],
        "colors": [
            "fad3cf",
            "a696c8",
            "2470a0",
            "060608"
        ]
    },
    {
        "id": "f2f2f2ebd5d5ea8a8a685454",
        "tags": [
            "white",
            "grey",
            "pink",
            "peach",
            "brown",
            "pastel",
            "skin",
            "cream"
        ],
        "colors": [
            "f2f2f2",
            "ebd5d5",
            "ea8a8a",
            "685454"
        ]
    },
    {
        "id": "ff64737578825cc1b36ef7c8",
        "tags": [
            "red",
            "grey",
            "teal"
        ],
        "colors": [
            "ff6473",
            "757882",
            "5cc1b3",
            "6ef7c8"
        ]
    },
    {
        "id": "fff6da84f2d6fc6b3f262525",
        "tags": [
            "beige",
            "yellow",
            "teal",
            "orange",
            "black",
            "retro",
            "neon"
        ],
        "colors": [
            "fff6da",
            "84f2d6",
            "fc6b3f",
            "262525"
        ]
    },
    {
        "id": "87e5da92a4c0f4adade58cdb",
        "tags": [
            "teal",
            "pink",
            "peach",
            "purple",
            "vintage",
            "kids"
        ],
        "colors": [
            "87e5da",
            "92a4c0",
            "f4adad",
            "e58cdb"
        ]
    },
    {
        "id": "ffffe387e0ff53c7f01d97c1",
        "tags": [
            "yellow",
            "blue",
            "summer",
            "happy"
        ],
        "colors": [
            "ffffe3",
            "87e0ff",
            "53c7f0",
            "1d97c1"
        ]
    },
    {
        "id": "13334c005792f6f6e9fd5f00",
        "tags": [
            "navy",
            "blue",
            "white",
            "orange",
            "wedding"
        ],
        "colors": [
            "13334c",
            "005792",
            "f6f6e9",
            "fd5f00"
        ]
    },
    {
        "id": "e01171ab0e8659057b0f0766",
        "tags": [
            "red",
            "purple",
            "navy",
            "space",
            "gradient"
        ],
        "colors": [
            "e01171",
            "ab0e86",
            "59057b",
            "0f0766"
        ]
    },
    {
        "id": "d5eefff7ca44a2792f5c3c10",
        "tags": [
            "blue",
            "yellow",
            "brown",
            "gold",
            "summer"
        ],
        "colors": [
            "d5eeff",
            "f7ca44",
            "a2792f",
            "5c3c10"
        ]
    },
    {
        "id": "de5b7beccfd1f0e3c498ded3",
        "tags": [
            "red",
            "pink",
            "beige",
            "teal",
            "pastel",
            "kids",
            "cream"
        ],
        "colors": [
            "de5b7b",
            "eccfd1",
            "f0e3c4",
            "98ded3"
        ]
    },
    {
        "id": "1b37644ab8b8fafccbefa35c",
        "tags": [
            "navy",
            "teal",
            "yellow",
            "orange",
            "kids"
        ],
        "colors": [
            "1b3764",
            "4ab8b8",
            "fafccb",
            "efa35c"
        ]
    },
    {
        "id": "0e0220e4047548e0e4d7fbf6",
        "tags": [
            "black",
            "pink",
            "teal",
            "retro",
            "wedding",
            "space"
        ],
        "colors": [
            "0e0220",
            "e40475",
            "48e0e4",
            "d7fbf6"
        ]
    },
    {
        "id": "2e99b0fcd77fff2e4c1e1548",
        "tags": [
            "blue",
            "yellow",
            "red",
            "navy",
            "rainbow"
        ],
        "colors": [
            "2e99b0",
            "fcd77f",
            "ff2e4c",
            "1e1548"
        ]
    },
    {
        "id": "dd0a35e4d1d31687a7014955",
        "tags": [
            "red",
            "blue"
        ],
        "colors": [
            "dd0a35",
            "e4d1d3",
            "1687a7",
            "014955"
        ]
    },
    {
        "id": "d0efb5eb78782f3e75f3e595",
        "tags": [
            "green",
            "red",
            "navy",
            "yellow",
            "vintage"
        ],
        "colors": [
            "d0efb5",
            "eb7878",
            "2f3e75",
            "f3e595"
        ]
    },
    {
        "id": "0e31506dc9c8ffc0c2f7e9e3",
        "tags": [
            "navy",
            "teal",
            "pink",
            "peach",
            "kids"
        ],
        "colors": [
            "0e3150",
            "6dc9c8",
            "ffc0c2",
            "f7e9e3"
        ]
    },
    {
        "id": "fff6f6ffe5aba1c45affcdb5",
        "tags": [
            "white",
            "yellow",
            "green",
            "peach",
            "nature",
            "food"
        ],
        "colors": [
            "fff6f6",
            "ffe5ab",
            "a1c45a",
            "ffcdb5"
        ]
    },
    {
        "id": "233142455d7af95959facf5a",
        "tags": [
            "black",
            "navy",
            "red",
            "yellow",
            "halloween",
            "space"
        ],
        "colors": [
            "233142",
            "455d7a",
            "f95959",
            "facf5a"
        ]
    },
    {
        "id": "d1478cff7a5cf7f9ff53d397",
        "tags": [
            "purple",
            "orange",
            "white",
            "green",
            "happy"
        ],
        "colors": [
            "d1478c",
            "ff7a5c",
            "f7f9ff",
            "53d397"
        ]
    },
    {
        "id": "ff9393ff6767ff34340c317a",
        "tags": [
            "pink",
            "red",
            "navy"
        ],
        "colors": [
            "ff9393",
            "ff6767",
            "ff3434",
            "0c317a"
        ]
    },
    {
        "id": "edf0c74e95252e5a1cff5c00",
        "tags": [
            "green",
            "orange",
            "christmas",
            "nature"
        ],
        "colors": [
            "edf0c7",
            "4e9525",
            "2e5a1c",
            "ff5c00"
        ]
    },
    {
        "id": "ffd3adffa96a00558515005d",
        "tags": [
            "orange",
            "blue",
            "navy"
        ],
        "colors": [
            "ffd3ad",
            "ffa96a",
            "005585",
            "15005d"
        ]
    },
    {
        "id": "35d0baf8c43ac93d1b04322e",
        "tags": [
            "teal",
            "yellow",
            "orange",
            "black",
            "retro",
            "neon"
        ],
        "colors": [
            "35d0ba",
            "f8c43a",
            "c93d1b",
            "04322e"
        ]
    },
    {
        "id": "feb0625751513f3b3be7b3b3",
        "tags": [
            "orange",
            "grey",
            "pink",
            "vintage"
        ],
        "colors": [
            "feb062",
            "575151",
            "3f3b3b",
            "e7b3b3"
        ]
    },
    {
        "id": "efff9d2aa9d21874c32931b3",
        "tags": [
            "yellow",
            "blue",
            "navy",
            "summer"
        ],
        "colors": [
            "efff9d",
            "2aa9d2",
            "1874c3",
            "2931b3"
        ]
    },
    {
        "id": "232931f73859f1d18aededed",
        "tags": [
            "black",
            "red",
            "yellow",
            "beige",
            "grey",
            "space"
        ],
        "colors": [
            "232931",
            "f73859",
            "f1d18a",
            "ededed"
        ]
    },
    {
        "id": "0058741c819ee6e6d4ffbe00",
        "tags": [
            "blue",
            "beige",
            "yellow",
            "retro"
        ],
        "colors": [
            "005874",
            "1c819e",
            "e6e6d4",
            "ffbe00"
        ]
    },
    {
        "id": "fbd68563aebb7a5d7e312b30",
        "tags": [
            "yellow",
            "teal",
            "purple",
            "black",
            "wedding",
            "vintage"
        ],
        "colors": [
            "fbd685",
            "63aebb",
            "7a5d7e",
            "312b30"
        ]
    },
    {
        "id": "7c203af85959ff9f68feff89",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "sunset",
            "neon"
        ],
        "colors": [
            "7c203a",
            "f85959",
            "ff9f68",
            "feff89"
        ]
    },
    {
        "id": "f5f5c67da87b32676527253d",
        "tags": [
            "yellow",
            "green",
            "teal",
            "black",
            "nature"
        ],
        "colors": [
            "f5f5c6",
            "7da87b",
            "326765",
            "27253d"
        ]
    },
    {
        "id": "99e1e5f3e8cbf2c6b4fbafaf",
        "tags": [
            "blue",
            "beige",
            "peach",
            "pastel",
            "summer",
            "kids",
            "rainbow"
        ],
        "colors": [
            "99e1e5",
            "f3e8cb",
            "f2c6b4",
            "fbafaf"
        ]
    },
    {
        "id": "f5b17b4e709d89a4c7cdd5e0",
        "tags": [
            "orange",
            "blue",
            "grey",
            "pastel"
        ],
        "colors": [
            "f5b17b",
            "4e709d",
            "89a4c7",
            "cdd5e0"
        ]
    },
    {
        "id": "db3b61ef3f613a3a59555574",
        "tags": [
            "red"
        ],
        "colors": [
            "db3b61",
            "ef3f61",
            "3a3a59",
            "555574"
        ]
    },
    {
        "id": "f5eee6f3d7cae6a4b4c86b85",
        "tags": [
            "beige",
            "pink",
            "pastel",
            "skin",
            "cream"
        ],
        "colors": [
            "f5eee6",
            "f3d7ca",
            "e6a4b4",
            "c86b85"
        ]
    },
    {
        "id": "2d095c20366bdd7777eae3e3",
        "tags": [
            "navy",
            "peach",
            "grey",
            "night"
        ],
        "colors": [
            "2d095c",
            "20366b",
            "dd7777",
            "eae3e3"
        ]
    },
    {
        "id": "aa530edf8931f5c16cf3eded",
        "tags": [
            "brown",
            "orange",
            "grey",
            "fall",
            "gold",
            "skin"
        ],
        "colors": [
            "aa530e",
            "df8931",
            "f5c16c",
            "f3eded"
        ]
    },
    {
        "id": "860f44bb3939ea5f2deec89f",
        "tags": [
            "maroon",
            "red",
            "orange",
            "beige",
            "warm",
            "halloween",
            "gradient"
        ],
        "colors": [
            "860f44",
            "bb3939",
            "ea5f2d",
            "eec89f"
        ]
    },
    {
        "id": "17bebb2e282acd5334edb88b",
        "tags": [
            "teal",
            "black",
            "orange"
        ],
        "colors": [
            "17bebb",
            "2e282a",
            "cd5334",
            "edb88b"
        ]
    },
    {
        "id": "ffeaa5fe5f55c7efcfeef5db",
        "tags": [
            "yellow",
            "red",
            "green",
            "summer",
            "spring",
            "happy"
        ],
        "colors": [
            "ffeaa5",
            "fe5f55",
            "c7efcf",
            "eef5db"
        ]
    },
    {
        "id": "35477d6c5b7bc06c84f67280",
        "tags": [
            "navy",
            "red",
            "night",
            "gradient"
        ],
        "colors": [
            "35477d",
            "6c5b7b",
            "c06c84",
            "f67280"
        ]
    },
    {
        "id": "eda1c1fab2acbee4d2d7f8f7",
        "tags": [
            "pink",
            "peach",
            "green",
            "blue",
            "pastel",
            "spring"
        ],
        "colors": [
            "eda1c1",
            "fab2ac",
            "bee4d2",
            "d7f8f7"
        ]
    },
    {
        "id": "1a2c5b3e4e887971eab8dff0",
        "tags": [],
        "colors": [
            "1a2c5b",
            "3e4e88",
            "7971ea",
            "b8dff0"
        ]
    },
    {
        "id": "fffdb7aef4a479b8d1e36488",
        "tags": [
            "yellow",
            "green",
            "blue",
            "red",
            "rainbow",
            "kids"
        ],
        "colors": [
            "fffdb7",
            "aef4a4",
            "79b8d1",
            "e36488"
        ]
    },
    {
        "id": "2b007b2f89fce7e6fcdd7c1b",
        "tags": [
            "navy",
            "blue",
            "orange",
            "wedding"
        ],
        "colors": [
            "2b007b",
            "2f89fc",
            "e7e6fc",
            "dd7c1b"
        ]
    },
    {
        "id": "eaa81bc955017d0000012c0b",
        "tags": [
            "orange",
            "maroon",
            "warm",
            "fall",
            "gold",
            "skin"
        ],
        "colors": [
            "eaa81b",
            "c95501",
            "7d0000",
            "012c0b"
        ]
    },
    {
        "id": "2d4059ffb400f6f6f6ea5455",
        "tags": [
            "navy",
            "orange",
            "white",
            "red",
            "retro"
        ],
        "colors": [
            "2d4059",
            "ffb400",
            "f6f6f6",
            "ea5455"
        ]
    },
    {
        "id": "f9fa9bff7777ceecf0f0f3f3",
        "tags": [
            "yellow",
            "red",
            "blue",
            "grey",
            "spring",
            "light",
            "kids"
        ],
        "colors": [
            "f9fa9b",
            "ff7777",
            "ceecf0",
            "f0f3f3"
        ]
    },
    {
        "id": "5e8b6f436e4ffa8f4df87829",
        "tags": [
            "green",
            "orange"
        ],
        "colors": [
            "5e8b6f",
            "436e4f",
            "fa8f4d",
            "f87829"
        ]
    },
    {
        "id": "fee9d7f9bf8fe2434b34222e",
        "tags": [
            "beige",
            "orange",
            "red",
            "black",
            "warm",
            "fall",
            "halloween",
            "skin"
        ],
        "colors": [
            "fee9d7",
            "f9bf8f",
            "e2434b",
            "34222e"
        ]
    },
    {
        "id": "5352384bbb8b6ddabec9ffc7",
        "tags": [
            "brown",
            "green",
            "teal",
            "earth"
        ],
        "colors": [
            "535238",
            "4bbb8b",
            "6ddabe",
            "c9ffc7"
        ]
    },
    {
        "id": "424153fdadc7ea4c88993399",
        "tags": [
            "black",
            "pink",
            "purple"
        ],
        "colors": [
            "424153",
            "fdadc7",
            "ea4c88",
            "993399"
        ]
    },
    {
        "id": "1b3c59456173a6ed8ef2f2f0",
        "tags": [
            "navy",
            "green",
            "grey"
        ],
        "colors": [
            "1b3c59",
            "456173",
            "a6ed8e",
            "f2f2f0"
        ]
    },
    {
        "id": "ffffc1ffd2a5d38cad8a79af",
        "tags": [],
        "colors": [
            "ffffc1",
            "ffd2a5",
            "d38cad",
            "8a79af"
        ]
    },
    {
        "id": "0d7e8313293dffaf87eef0f2",
        "tags": [
            "teal",
            "black",
            "orange",
            "grey",
            "retro"
        ],
        "colors": [
            "0d7e83",
            "13293d",
            "ffaf87",
            "eef0f2"
        ]
    },
    {
        "id": "fd5f0000204a005792d9faff",
        "tags": [
            "orange",
            "navy",
            "blue",
            "space",
            "retro"
        ],
        "colors": [
            "fd5f00",
            "00204a",
            "005792",
            "d9faff"
        ]
    },
    {
        "id": "f7626221658365c0bacffdf8",
        "tags": [
            "red",
            "navy",
            "teal",
            "kids"
        ],
        "colors": [
            "f76262",
            "216583",
            "65c0ba",
            "cffdf8"
        ]
    },
    {
        "id": "ff75173e39392c2727f6f4f4",
        "tags": [
            "orange",
            "grey",
            "black",
            "white"
        ],
        "colors": [
            "ff7517",
            "3e3939",
            "2c2727",
            "f6f4f4"
        ]
    },
    {
        "id": "f9f8edc4e3cb6a9c78fff1bc",
        "tags": [
            "beige",
            "green",
            "yellow",
            "nature",
            "light"
        ],
        "colors": [
            "f9f8ed",
            "c4e3cb",
            "6a9c78",
            "fff1bc"
        ]
    },
    {
        "id": "480032df0054ff8b6affd2bb",
        "tags": [
            "maroon",
            "red",
            "orange",
            "peach",
            "halloween",
            "gradient"
        ],
        "colors": [
            "480032",
            "df0054",
            "ff8b6a",
            "ffd2bb"
        ]
    },
    {
        "id": "ffa258fff7c2a02a634b125c",
        "tags": [],
        "colors": [
            "ffa258",
            "fff7c2",
            "a02a63",
            "4b125c"
        ]
    },
    {
        "id": "00354500454a3c6562ed6363",
        "tags": [
            "navy",
            "teal",
            "red",
            "dark",
            "sea"
        ],
        "colors": [
            "003545",
            "00454a",
            "3c6562",
            "ed6363"
        ]
    },
    {
        "id": "90aeffcefc8660efb8f9f7f7",
        "tags": [
            "blue",
            "green",
            "mint",
            "white",
            "light",
            "kids",
            "happy",
            "summer"
        ],
        "colors": [
            "90aeff",
            "cefc86",
            "60efb8",
            "f9f7f7"
        ]
    },
    {
        "id": "6900ff9951ffffd700faf7ff",
        "tags": [
            "purple",
            "yellow",
            "white",
            "wedding",
            "light"
        ],
        "colors": [
            "6900ff",
            "9951ff",
            "ffd700",
            "faf7ff"
        ]
    },
    {
        "id": "203541374955f62a66ffd933",
        "tags": [
            "black",
            "red",
            "yellow",
            "space"
        ],
        "colors": [
            "203541",
            "374955",
            "f62a66",
            "ffd933"
        ]
    },
    {
        "id": "f4f9f4c4e3cb8aae92616161",
        "tags": [
            "white",
            "sage",
            "grey",
            "earth"
        ],
        "colors": [
            "f4f9f4",
            "c4e3cb",
            "8aae92",
            "616161"
        ]
    },
    {
        "id": "333366ff5f5ff9e75ef0f0f0",
        "tags": [
            "navy",
            "red",
            "yellow",
            "grey"
        ],
        "colors": [
            "333366",
            "ff5f5f",
            "f9e75e",
            "f0f0f0"
        ]
    },
    {
        "id": "fbffa874dac620c1bd33354a",
        "tags": [
            "yellow",
            "teal",
            "black"
        ],
        "colors": [
            "fbffa8",
            "74dac6",
            "20c1bd",
            "33354a"
        ]
    },
    {
        "id": "092a35658525cfee91f8eeb4",
        "tags": [
            "black",
            "green",
            "beige",
            "yellow",
            "nature"
        ],
        "colors": [
            "092a35",
            "658525",
            "cfee91",
            "f8eeb4"
        ]
    },
    {
        "id": "92e6e6fff9afd65d7a524c84",
        "tags": [
            "blue",
            "yellow",
            "red",
            "navy",
            "rainbow"
        ],
        "colors": [
            "92e6e6",
            "fff9af",
            "d65d7a",
            "524c84"
        ]
    },
    {
        "id": "bad7dfffe2e2f6f6f699ddcc",
        "tags": [
            "blue",
            "pink",
            "white",
            "green",
            "pastel",
            "wedding",
            "spring",
            "cream",
            "kids"
        ],
        "colors": [
            "bad7df",
            "ffe2e2",
            "f6f6f6",
            "99ddcc"
        ]
    },
    {
        "id": "283149404b6900818adbedf3",
        "tags": [
            "navy",
            "black",
            "teal",
            "dark",
            "winter",
            "night",
            "sea"
        ],
        "colors": [
            "283149",
            "404b69",
            "00818a",
            "dbedf3"
        ]
    },
    {
        "id": "fff9e0f1c550ff6600ce2525",
        "tags": [
            "yellow",
            "orange",
            "red",
            "warm",
            "fall",
            "gold"
        ],
        "colors": [
            "fff9e0",
            "f1c550",
            "ff6600",
            "ce2525"
        ]
    },
    {
        "id": "32364360647093defff7f7f7",
        "tags": [
            "black",
            "grey",
            "blue",
            "white",
            "cold",
            "winter"
        ],
        "colors": [
            "323643",
            "606470",
            "93deff",
            "f7f7f7"
        ]
    },
    {
        "id": "5ba19bfceaeaf5d9d9fbead1",
        "tags": [
            "teal",
            "pink",
            "beige",
            "wedding",
            "pastel",
            "kids"
        ],
        "colors": [
            "5ba19b",
            "fceaea",
            "f5d9d9",
            "fbead1"
        ]
    },
    {
        "id": "404b69283149f73859f3ecc8",
        "tags": [
            "navy",
            "red",
            "beige"
        ],
        "colors": [
            "404b69",
            "283149",
            "f73859",
            "f3ecc8"
        ]
    },
    {
        "id": "eeeeeeff7100be3030222222",
        "tags": [
            "grey",
            "orange",
            "maroon",
            "black",
            "fall"
        ],
        "colors": [
            "eeeeee",
            "ff7100",
            "be3030",
            "222222"
        ]
    },
    {
        "id": "eaafafa2738c645c84427996",
        "tags": [
            "peach",
            "wedding",
            "vintage",
            "pastel"
        ],
        "colors": [
            "eaafaf",
            "a2738c",
            "645c84",
            "427996"
        ]
    },
    {
        "id": "e9faddb8e4c93f546842291c",
        "tags": [
            "green",
            "navy",
            "brown",
            "earth"
        ],
        "colors": [
            "e9fadd",
            "b8e4c9",
            "3f5468",
            "42291c"
        ]
    },
    {
        "id": "a8e6cffdffabffd3b6ffaaa5",
        "tags": [
            "teal",
            "yellow",
            "peach",
            "pastel",
            "spring",
            "light",
            "kids"
        ],
        "colors": [
            "a8e6cf",
            "fdffab",
            "ffd3b6",
            "ffaaa5"
        ]
    },
    {
        "id": "e7759affa35fba78cd755da3",
        "tags": [
            "pink",
            "orange",
            "purple",
            "kids"
        ],
        "colors": [
            "e7759a",
            "ffa35f",
            "ba78cd",
            "755da3"
        ]
    },
    {
        "id": "062743113a5dc4ffddf9f9f9",
        "tags": [
            "navy",
            "mint",
            "white",
            "cold",
            "space"
        ],
        "colors": [
            "062743",
            "113a5d",
            "c4ffdd",
            "f9f9f9"
        ]
    },
    {
        "id": "ef7b7bfcf3cac4eada919190",
        "tags": [
            "red",
            "peach",
            "yellow",
            "beige",
            "teal",
            "grey",
            "pastel"
        ],
        "colors": [
            "ef7b7b",
            "fcf3ca",
            "c4eada",
            "919190"
        ]
    },
    {
        "id": "feffdfdde0ab97cba9668ba4",
        "tags": [
            "yellow",
            "green",
            "teal",
            "blue",
            "wedding"
        ],
        "colors": [
            "feffdf",
            "dde0ab",
            "97cba9",
            "668ba4"
        ]
    },
    {
        "id": "062743113a5dff7a8af9f9f9",
        "tags": [
            "navy",
            "pink",
            "white",
            "space"
        ],
        "colors": [
            "062743",
            "113a5d",
            "ff7a8a",
            "f9f9f9"
        ]
    },
    {
        "id": "fce8aa97de9508c299571179",
        "tags": [
            "yellow",
            "green",
            "purple",
            "spring"
        ],
        "colors": [
            "fce8aa",
            "97de95",
            "08c299",
            "571179"
        ]
    },
    {
        "id": "0833580f4471fc3c3cf6f6f6",
        "tags": [
            "navy",
            "red",
            "white",
            "winter"
        ],
        "colors": [
            "083358",
            "0f4471",
            "fc3c3c",
            "f6f6f6"
        ]
    },
    {
        "id": "f2f2f0ff5e3a2c365d272e4f",
        "tags": [
            "grey",
            "white",
            "orange",
            "navy",
            "halloween"
        ],
        "colors": [
            "f2f2f0",
            "ff5e3a",
            "2c365d",
            "272e4f"
        ]
    },
    {
        "id": "feeb974fb783409d9b034561",
        "tags": [
            "yellow",
            "green",
            "teal",
            "blue",
            "navy",
            "kids"
        ],
        "colors": [
            "feeb97",
            "4fb783",
            "409d9b",
            "034561"
        ]
    },
    {
        "id": "f8b195f67280c06c84355c7d",
        "tags": [
            "orange",
            "red",
            "blue",
            "wedding",
            "fall",
            "warm",
            "vintage"
        ],
        "colors": [
            "f8b195",
            "f67280",
            "c06c84",
            "355c7d"
        ]
    },
    {
        "id": "0900890060ca91cefffcdc74",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "cold"
        ],
        "colors": [
            "090089",
            "0060ca",
            "91ceff",
            "fcdc74"
        ]
    },
    {
        "id": "294a660b3846ffbbbbfcd2c2",
        "tags": [],
        "colors": [
            "294a66",
            "0b3846",
            "ffbbbb",
            "fcd2c2"
        ]
    },
    {
        "id": "240041900048ff4057ff8260",
        "tags": [
            "navy",
            "maroon",
            "red",
            "orange",
            "halloween",
            "space"
        ],
        "colors": [
            "240041",
            "900048",
            "ff4057",
            "ff8260"
        ]
    },
    {
        "id": "eff0f474dbef0074e4264e86",
        "tags": [
            "grey",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "eff0f4",
            "74dbef",
            "0074e4",
            "264e86"
        ]
    },
    {
        "id": "f8d5f058d5d341a4c33f4b83",
        "tags": [
            "pink",
            "teal",
            "blue",
            "kids"
        ],
        "colors": [
            "f8d5f0",
            "58d5d3",
            "41a4c3",
            "3f4b83"
        ]
    },
    {
        "id": "fff1bc7dc3836a9c78446e5c",
        "tags": [
            "yellow",
            "green",
            "nature",
            "happy",
            "food"
        ],
        "colors": [
            "fff1bc",
            "7dc383",
            "6a9c78",
            "446e5c"
        ]
    },
    {
        "id": "002bdc2f4bff00a6e7ffe37f",
        "tags": [
            "blue",
            "yellow",
            "kids"
        ],
        "colors": [
            "002bdc",
            "2f4bff",
            "00a6e7",
            "ffe37f"
        ]
    },
    {
        "id": "232931393e464ecca3eeeeee",
        "tags": [
            "black",
            "grey",
            "teal",
            "dark",
            "space"
        ],
        "colors": [
            "232931",
            "393e46",
            "4ecca3",
            "eeeeee"
        ]
    },
    {
        "id": "f6ec66fadc6df97272f65454",
        "tags": [
            "yellow",
            "peach",
            "red",
            "happy"
        ],
        "colors": [
            "f6ec66",
            "fadc6d",
            "f97272",
            "f65454"
        ]
    },
    {
        "id": "70228396207176b39dfdb44b",
        "tags": [
            "purple",
            "maroon",
            "green",
            "orange",
            "retro"
        ],
        "colors": [
            "702283",
            "962071",
            "76b39d",
            "fdb44b"
        ]
    },
    {
        "id": "faffb8c5f0a435b0ab226b80",
        "tags": [
            "yellow",
            "green",
            "teal",
            "light"
        ],
        "colors": [
            "faffb8",
            "c5f0a4",
            "35b0ab",
            "226b80"
        ]
    },
    {
        "id": "f8b595f67280c06c846c5b7c",
        "tags": [
            "orange",
            "red",
            "pastel",
            "halloween",
            "skin",
            "warm"
        ],
        "colors": [
            "f8b595",
            "f67280",
            "c06c84",
            "6c5b7c"
        ]
    },
    {
        "id": "448ef675c2f665daf7ffe981",
        "tags": [
            "blue",
            "yellow",
            "light",
            "happy",
            "summer"
        ],
        "colors": [
            "448ef6",
            "75c2f6",
            "65daf7",
            "ffe981"
        ]
    },
    {
        "id": "e4eddb307672144d531a3c40",
        "tags": [
            "teal",
            "winter",
            "nature"
        ],
        "colors": [
            "e4eddb",
            "307672",
            "144d53",
            "1a3c40"
        ]
    },
    {
        "id": "ff4d4dff8364fdb87dffe8d5",
        "tags": [
            "red",
            "orange",
            "peach",
            "warm",
            "gold",
            "happy"
        ],
        "colors": [
            "ff4d4d",
            "ff8364",
            "fdb87d",
            "ffe8d5"
        ]
    },
    {
        "id": "fafaf600fff000d1ff3d6cb9",
        "tags": [
            "white",
            "teal",
            "blue",
            "light",
            "cold",
            "neon"
        ],
        "colors": [
            "fafaf6",
            "00fff0",
            "00d1ff",
            "3d6cb9"
        ]
    },
    {
        "id": "1c1124684656de774eb7e1b5",
        "tags": [
            "black",
            "orange",
            "green",
            "vintage",
            "halloween",
            "fall",
            "night"
        ],
        "colors": [
            "1c1124",
            "684656",
            "de774e",
            "b7e1b5"
        ]
    },
    {
        "id": "1c1124693e5274b49ba7d7c5",
        "tags": [
            "black",
            "green",
            "vintage",
            "night"
        ],
        "colors": [
            "1c1124",
            "693e52",
            "74b49b",
            "a7d7c5"
        ]
    },
    {
        "id": "8ea6b4e7eff3ff8f56984a59",
        "tags": [
            "grey",
            "white",
            "orange",
            "maroon",
            "fall",
            "winter"
        ],
        "colors": [
            "8ea6b4",
            "e7eff3",
            "ff8f56",
            "984a59"
        ]
    },
    {
        "id": "45eba521aba51d566e163a5f",
        "tags": [
            "green",
            "teal",
            "blue",
            "navy",
            "cold",
            "sea"
        ],
        "colors": [
            "45eba5",
            "21aba5",
            "1d566e",
            "163a5f"
        ]
    },
    {
        "id": "011f3f0960bd429ffdfef2bf",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "cold"
        ],
        "colors": [
            "011f3f",
            "0960bd",
            "429ffd",
            "fef2bf"
        ]
    },
    {
        "id": "ff6107e9290fc40018292725",
        "tags": [
            "orange",
            "red",
            "maroon",
            "black",
            "warm"
        ],
        "colors": [
            "ff6107",
            "e9290f",
            "c40018",
            "292725"
        ]
    },
    {
        "id": "f7f7f7ff570c606470323643",
        "tags": [
            "white",
            "orange",
            "grey"
        ],
        "colors": [
            "f7f7f7",
            "ff570c",
            "606470",
            "323643"
        ]
    },
    {
        "id": "84b9effbe4c9ff5d5d952e4b",
        "tags": [
            "blue",
            "beige",
            "red",
            "maroon",
            "spring",
            "kids"
        ],
        "colors": [
            "84b9ef",
            "fbe4c9",
            "ff5d5d",
            "952e4b"
        ]
    },
    {
        "id": "78fee04bc2c53b9a9cfef4a9",
        "tags": [
            "teal",
            "yellow",
            "neon",
            "light",
            "happy"
        ],
        "colors": [
            "78fee0",
            "4bc2c5",
            "3b9a9c",
            "fef4a9"
        ]
    },
    {
        "id": "ecf0f133cccc2980b92c3e50",
        "tags": [
            "grey",
            "teal",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "ecf0f1",
            "33cccc",
            "2980b9",
            "2c3e50"
        ]
    },
    {
        "id": "edfeadd9f489bdcf88d95858",
        "tags": [
            "yellow",
            "green",
            "red",
            "christmas",
            "food",
            "spring",
            "nature"
        ],
        "colors": [
            "edfead",
            "d9f489",
            "bdcf88",
            "d95858"
        ]
    },
    {
        "id": "ff6138ffff9dbeeb9f79bd8f",
        "tags": [
            "red",
            "yellow",
            "green",
            "summer",
            "spring",
            "light",
            "happy"
        ],
        "colors": [
            "ff6138",
            "ffff9d",
            "beeb9f",
            "79bd8f"
        ]
    },
    {
        "id": "394a517fa99bfbf2d5fdc57b",
        "tags": [
            "teal",
            "beige",
            "orange",
            "earth",
            "sea"
        ],
        "colors": [
            "394a51",
            "7fa99b",
            "fbf2d5",
            "fdc57b"
        ]
    },
    {
        "id": "283149404b69f73859dbedf3",
        "tags": [
            "navy",
            "red",
            "space"
        ],
        "colors": [
            "283149",
            "404b69",
            "f73859",
            "dbedf3"
        ]
    },
    {
        "id": "fbfae1cef0b964a36fffe121",
        "tags": [
            "beige",
            "green",
            "yellow",
            "light",
            "summer"
        ],
        "colors": [
            "fbfae1",
            "cef0b9",
            "64a36f",
            "ffe121"
        ]
    },
    {
        "id": "f56a47b32c50681a1e0a0944",
        "tags": [
            "orange",
            "red",
            "maroon",
            "brown",
            "navy",
            "warm",
            "halloween"
        ],
        "colors": [
            "f56a47",
            "b32c50",
            "681a1e",
            "0a0944"
        ]
    },
    {
        "id": "f8f9fcc00000de3c3cf7b32d",
        "tags": [
            "white",
            "maroon",
            "red",
            "orange",
            "warm"
        ],
        "colors": [
            "f8f9fc",
            "c00000",
            "de3c3c",
            "f7b32d"
        ]
    },
    {
        "id": "ffe6ebffcdcd6a65d81d2786",
        "tags": [
            "pink",
            "peach",
            "navy",
            "wedding",
            "skin",
            "kids"
        ],
        "colors": [
            "ffe6eb",
            "ffcdcd",
            "6a65d8",
            "1d2786"
        ]
    },
    {
        "id": "28544bacbd86ffd6a0ffa06f",
        "tags": [
            "green",
            "sage",
            "orange",
            "fall",
            "nature"
        ],
        "colors": [
            "28544b",
            "acbd86",
            "ffd6a0",
            "ffa06f"
        ]
    },
    {
        "id": "6c567bc06c84f67280f8b195",
        "tags": [
            "purple",
            "red",
            "peach",
            "warm",
            "coffee",
            "gradient"
        ],
        "colors": [
            "6c567b",
            "c06c84",
            "f67280",
            "f8b195"
        ]
    },
    {
        "id": "fffb9797ffcf2fe1d638c6bd",
        "tags": [
            "yellow",
            "teal",
            "summer",
            "spring",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "fffb97",
            "97ffcf",
            "2fe1d6",
            "38c6bd"
        ]
    },
    {
        "id": "e7f5f2f9c7cf12776f0f4137",
        "tags": [
            "teal",
            "pink",
            "wedding"
        ],
        "colors": [
            "e7f5f2",
            "f9c7cf",
            "12776f",
            "0f4137"
        ]
    },
    {
        "id": "375a7f4d7cae6a99cbfcfa70",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "winter",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "375a7f",
            "4d7cae",
            "6a99cb",
            "fcfa70"
        ]
    },
    {
        "id": "360982b72a67ff9797fde8cb",
        "tags": [
            "navy",
            "maroon",
            "peach",
            "beige",
            "sunset",
            "wedding",
            "gradient"
        ],
        "colors": [
            "360982",
            "b72a67",
            "ff9797",
            "fde8cb"
        ]
    },
    {
        "id": "3232328559a56db193f4e5c2",
        "tags": [
            "black",
            "purple",
            "green",
            "beige",
            "retro"
        ],
        "colors": [
            "323232",
            "8559a5",
            "6db193",
            "f4e5c2"
        ]
    },
    {
        "id": "e9528023b1a5ffdd7ef3f3f3",
        "tags": [
            "pink",
            "teal",
            "yellow",
            "grey",
            "summer",
            "kids"
        ],
        "colors": [
            "e95280",
            "23b1a5",
            "ffdd7e",
            "f3f3f3"
        ]
    },
    {
        "id": "22559cf27370fa9856ede862",
        "tags": [
            "blue",
            "red",
            "orange",
            "yellow",
            "sunset",
            "rainbow",
            "happy"
        ],
        "colors": [
            "22559c",
            "f27370",
            "fa9856",
            "ede862"
        ]
    },
    {
        "id": "abedd846cdcf0081c648466d",
        "tags": [
            "teal",
            "blue",
            "navy",
            "cold",
            "sea"
        ],
        "colors": [
            "abedd8",
            "46cdcf",
            "0081c6",
            "48466d"
        ]
    },
    {
        "id": "fae3e3b7b7b71370833d0240",
        "tags": [
            "pink",
            "grey",
            "teal",
            "maroon",
            "wedding",
            "vintage"
        ],
        "colors": [
            "fae3e3",
            "b7b7b7",
            "137083",
            "3d0240"
        ]
    },
    {
        "id": "11cbd7c6f1e7f0fff3fa4659",
        "tags": [
            "teal",
            "white",
            "red",
            "light",
            "cold",
            "kids"
        ],
        "colors": [
            "11cbd7",
            "c6f1e7",
            "f0fff3",
            "fa4659"
        ]
    },
    {
        "id": "fda403e8751ac513508a1253",
        "tags": [
            "orange",
            "maroon",
            "halloween",
            "fall",
            "warm",
            "gold"
        ],
        "colors": [
            "fda403",
            "e8751a",
            "c51350",
            "8a1253"
        ]
    },
    {
        "id": "a7efe97fdfd4fbe1b6fbac91",
        "tags": [
            "teal",
            "beige",
            "orange",
            "summer",
            "happy"
        ],
        "colors": [
            "a7efe9",
            "7fdfd4",
            "fbe1b6",
            "fbac91"
        ]
    },
    {
        "id": "032a332559654c6f7bf1d18a",
        "tags": [
            "black",
            "teal",
            "yellow",
            "night"
        ],
        "colors": [
            "032a33",
            "255965",
            "4c6f7b",
            "f1d18a"
        ]
    },
    {
        "id": "faa9e0f8b3ebeaa3fcfce4b0",
        "tags": [
            "pink",
            "purple",
            "beige",
            "pastel",
            "spring",
            "kids"
        ],
        "colors": [
            "faa9e0",
            "f8b3eb",
            "eaa3fc",
            "fce4b0"
        ]
    },
    {
        "id": "fbf0f0dfd3d3b8b0b07c7575",
        "tags": [
            "pink",
            "grey",
            "skin",
            "cream",
            "coffee",
            "gradient"
        ],
        "colors": [
            "fbf0f0",
            "dfd3d3",
            "b8b0b0",
            "7c7575"
        ]
    },
    {
        "id": "ff6d244e413b857671e2ded3",
        "tags": [
            "orange",
            "brown",
            "grey",
            "fall",
            "skin",
            "coffee",
            "vintage"
        ],
        "colors": [
            "ff6d24",
            "4e413b",
            "857671",
            "e2ded3"
        ]
    },
    {
        "id": "f4eec0aed09e61b2927e6752",
        "tags": [
            "beige",
            "yellow",
            "green",
            "teal",
            "brown",
            "earth",
            "nature"
        ],
        "colors": [
            "f4eec0",
            "aed09e",
            "61b292",
            "7e6752"
        ]
    },
    {
        "id": "c7f3fffdc7ffffdcf5f2f4c3",
        "tags": [
            "blue",
            "pink",
            "yellow",
            "light",
            "spring",
            "happy"
        ],
        "colors": [
            "c7f3ff",
            "fdc7ff",
            "ffdcf5",
            "f2f4c3"
        ]
    },
    {
        "id": "f6efb435c2bd2796cb3379e4",
        "tags": [
            "yellow",
            "beige",
            "teal",
            "blue",
            "happy"
        ],
        "colors": [
            "f6efb4",
            "35c2bd",
            "2796cb",
            "3379e4"
        ]
    },
    {
        "id": "00204a00579200bbf0fdb44b",
        "tags": [
            "navy",
            "blue",
            "orange",
            "cold"
        ],
        "colors": [
            "00204a",
            "005792",
            "00bbf0",
            "fdb44b"
        ]
    },
    {
        "id": "f12b6bff467efd94b4f6c7c7",
        "tags": [
            "red",
            "pink",
            "peach",
            "spring"
        ],
        "colors": [
            "f12b6b",
            "ff467e",
            "fd94b4",
            "f6c7c7"
        ]
    },
    {
        "id": "f6ffcdbcffa86ba0834f323b",
        "tags": [
            "yellow",
            "green",
            "nature"
        ],
        "colors": [
            "f6ffcd",
            "bcffa8",
            "6ba083",
            "4f323b"
        ]
    },
    {
        "id": "00204a00579200bbf0d9faff",
        "tags": [
            "navy",
            "blue",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "00204a",
            "005792",
            "00bbf0",
            "d9faff"
        ]
    },
    {
        "id": "fcfcfc83ffe6ff5f5f2c2c2c",
        "tags": [
            "white",
            "teal",
            "red",
            "black",
            "neon"
        ],
        "colors": [
            "fcfcfc",
            "83ffe6",
            "ff5f5f",
            "2c2c2c"
        ]
    },
    {
        "id": "ececebf9a82807617d2e383f",
        "tags": [
            "grey",
            "orange",
            "navy",
            "retro"
        ],
        "colors": [
            "ececeb",
            "f9a828",
            "07617d",
            "2e383f"
        ]
    },
    {
        "id": "ff6464ff8264ffaa64fff5a5",
        "tags": [
            "red",
            "orange",
            "peach",
            "yellow",
            "summer",
            "warm",
            "sunset"
        ],
        "colors": [
            "ff6464",
            "ff8264",
            "ffaa64",
            "fff5a5"
        ]
    },
    {
        "id": "f9f8eb76b39d155263f0b917",
        "tags": [
            "beige",
            "teal",
            "navy",
            "yellow"
        ],
        "colors": [
            "f9f8eb",
            "76b39d",
            "155263",
            "f0b917"
        ]
    },
    {
        "id": "fffcefd2ebcdff7f5b393939",
        "tags": [
            "white",
            "sage",
            "orange",
            "black",
            "vintage"
        ],
        "colors": [
            "fffcef",
            "d2ebcd",
            "ff7f5b",
            "393939"
        ]
    },
    {
        "id": "6b0848a40a3cec610affc300",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "halloween",
            "sunset",
            "gradient"
        ],
        "colors": [
            "6b0848",
            "a40a3c",
            "ec610a",
            "ffc300"
        ]
    },
    {
        "id": "0278ae51adcfa5ecd7e8ffc1",
        "tags": [
            "blue",
            "teal",
            "mint",
            "winter",
            "cold",
            "sky",
            "sea"
        ],
        "colors": [
            "0278ae",
            "51adcf",
            "a5ecd7",
            "e8ffc1"
        ]
    },
    {
        "id": "70d4b4ffebb7bbbbbbaaaaaa",
        "tags": [
            "teal",
            "yellow",
            "grey"
        ],
        "colors": [
            "70d4b4",
            "ffebb7",
            "bbbbbb",
            "aaaaaa"
        ]
    },
    {
        "id": "ec7700d65f00c04d00efefef",
        "tags": [
            "orange",
            "grey",
            "gold"
        ],
        "colors": [
            "ec7700",
            "d65f00",
            "c04d00",
            "efefef"
        ]
    },
    {
        "id": "3a0088930077e61c5dffbd39",
        "tags": [
            "navy",
            "maroon",
            "red",
            "yellow",
            "rainbow",
            "gradient"
        ],
        "colors": [
            "3a0088",
            "930077",
            "e61c5d",
            "ffbd39"
        ]
    },
    {
        "id": "194769f6f6e9d7eef2f2855e",
        "tags": [
            "navy",
            "orange",
            "retro"
        ],
        "colors": [
            "194769",
            "f6f6e9",
            "d7eef2",
            "f2855e"
        ]
    },
    {
        "id": "0e957704deadf1efb9fbfae1",
        "tags": [
            "green",
            "yellow",
            "spring",
            "happy"
        ],
        "colors": [
            "0e9577",
            "04dead",
            "f1efb9",
            "fbfae1"
        ]
    },
    {
        "id": "970747fef4e81989ac283e56",
        "tags": [
            "maroon",
            "beige",
            "blue",
            "navy",
            "retro"
        ],
        "colors": [
            "970747",
            "fef4e8",
            "1989ac",
            "283e56"
        ]
    },
    {
        "id": "fdfdebf9ce0000818a09194f",
        "tags": [
            "yellow",
            "teal",
            "navy"
        ],
        "colors": [
            "fdfdeb",
            "f9ce00",
            "00818a",
            "09194f"
        ]
    },
    {
        "id": "0f305700587a008891e7e7de",
        "tags": [
            "navy",
            "teal",
            "grey",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "0f3057",
            "00587a",
            "008891",
            "e7e7de"
        ]
    },
    {
        "id": "9f609cea8f79e4d183f8f1e5",
        "tags": [
            "purple",
            "orange",
            "peach",
            "yellow",
            "beige",
            "pastel",
            "wedding",
            "gradient"
        ],
        "colors": [
            "9f609c",
            "ea8f79",
            "e4d183",
            "f8f1e5"
        ]
    },
    {
        "id": "283149404b69da0463dbedf3",
        "tags": [
            "grey",
            "red",
            "space"
        ],
        "colors": [
            "283149",
            "404b69",
            "da0463",
            "dbedf3"
        ]
    },
    {
        "id": "f4e8c1a0c1b8726a95351f39",
        "tags": [
            "yellow",
            "teal",
            "purple",
            "black",
            "retro",
            "vintage",
            "gradient"
        ],
        "colors": [
            "f4e8c1",
            "a0c1b8",
            "726a95",
            "351f39"
        ]
    },
    {
        "id": "ffb6b9fae3d9bbded661c0bf",
        "tags": [
            "peach",
            "teal",
            "pastel",
            "wedding",
            "kids",
            "light"
        ],
        "colors": [
            "ffb6b9",
            "fae3d9",
            "bbded6",
            "61c0bf"
        ]
    },
    {
        "id": "ecfafb81cbc84aa6b5d6c481",
        "tags": [
            "teal",
            "wedding",
            "summer"
        ],
        "colors": [
            "ecfafb",
            "81cbc8",
            "4aa6b5",
            "d6c481"
        ]
    },
    {
        "id": "5628b4d80e70e7455ff7b236",
        "tags": [
            "purple",
            "red",
            "yellow",
            "neon",
            "sunset"
        ],
        "colors": [
            "5628b4",
            "d80e70",
            "e7455f",
            "f7b236"
        ]
    },
    {
        "id": "f4f4f465eeb7ff5722474744",
        "tags": [
            "grey",
            "mint",
            "orange",
            "black",
            "neon"
        ],
        "colors": [
            "f4f4f4",
            "65eeb7",
            "ff5722",
            "474744"
        ]
    },
    {
        "id": "232855215b635fcc9caaffc7",
        "tags": [
            "navy",
            "teal",
            "green",
            "mint",
            "space",
            "sea"
        ],
        "colors": [
            "232855",
            "215b63",
            "5fcc9c",
            "aaffc7"
        ]
    },
    {
        "id": "4a772fffdd00fa9e05a7095c",
        "tags": [
            "green",
            "yellow",
            "orange",
            "maroon",
            "purple",
            "kids"
        ],
        "colors": [
            "4a772f",
            "ffdd00",
            "fa9e05",
            "a7095c"
        ]
    },
    {
        "id": "ffa3ac00043c005d6c00c9b1",
        "tags": [
            "pink",
            "black",
            "teal",
            "wedding"
        ],
        "colors": [
            "ffa3ac",
            "00043c",
            "005d6c",
            "00c9b1"
        ]
    },
    {
        "id": "26596122706676a665ffdd5c",
        "tags": [
            "teal",
            "green",
            "yellow",
            "nature"
        ],
        "colors": [
            "265961",
            "227066",
            "76a665",
            "ffdd5c"
        ]
    },
    {
        "id": "17139cdd3e3effe5e1f2f2f2",
        "tags": [
            "blue",
            "red",
            "grey",
            "white",
            "retro"
        ],
        "colors": [
            "17139c",
            "dd3e3e",
            "ffe5e1",
            "f2f2f2"
        ]
    },
    {
        "id": "ff7777fff195fcffbff5e9ff",
        "tags": [
            "red",
            "yellow",
            "pink",
            "light",
            "summer",
            "spring",
            "happy"
        ],
        "colors": [
            "ff7777",
            "fff195",
            "fcffbf",
            "f5e9ff"
        ]
    },
    {
        "id": "ebebebfec1005280783e615b",
        "tags": [
            "grey",
            "yellow",
            "teal"
        ],
        "colors": [
            "ebebeb",
            "fec100",
            "528078",
            "3e615b"
        ]
    },
    {
        "id": "33364484577cc65f63f6e1b8",
        "tags": [
            "black",
            "purple",
            "red",
            "beige",
            "vintage"
        ],
        "colors": [
            "333644",
            "84577c",
            "c65f63",
            "f6e1b8"
        ]
    },
    {
        "id": "fdfdfde1eb71ecab69e36161",
        "tags": [
            "white",
            "yellow",
            "orange",
            "red",
            "summer",
            "gold"
        ],
        "colors": [
            "fdfdfd",
            "e1eb71",
            "ecab69",
            "e36161"
        ]
    },
    {
        "id": "f2d1a8ebebeb669b7c557669",
        "tags": [
            "orange",
            "grey",
            "green",
            "earth"
        ],
        "colors": [
            "f2d1a8",
            "ebebeb",
            "669b7c",
            "557669"
        ]
    },
    {
        "id": "8e1d41dbbf0dffcd19ffefb4",
        "tags": [
            "maroon",
            "yellow"
        ],
        "colors": [
            "8e1d41",
            "dbbf0d",
            "ffcd19",
            "ffefb4"
        ]
    },
    {
        "id": "111f4df2f4f7e43a19020205",
        "tags": [
            "navy",
            "white",
            "orange",
            "black",
            "retro",
            "space"
        ],
        "colors": [
            "111f4d",
            "f2f4f7",
            "e43a19",
            "020205"
        ]
    },
    {
        "id": "fcf9f4ffc97cea7659c1c1c1",
        "tags": [
            "white",
            "beige",
            "orange",
            "grey",
            "fall",
            "skin",
            "gold",
            "coffee"
        ],
        "colors": [
            "fcf9f4",
            "ffc97c",
            "ea7659",
            "c1c1c1"
        ]
    },
    {
        "id": "5f4444af3264ff63b5ffbbbb",
        "tags": [
            "brown",
            "maroon",
            "pink",
            "peach"
        ],
        "colors": [
            "5f4444",
            "af3264",
            "ff63b5",
            "ffbbbb"
        ]
    },
    {
        "id": "bc5148fef8e67bcecc3090a1",
        "tags": [
            "red",
            "beige",
            "blue",
            "kids"
        ],
        "colors": [
            "bc5148",
            "fef8e6",
            "7bcecc",
            "3090a1"
        ]
    },
    {
        "id": "e7e6e1f7f6e7c1c0b9537791",
        "tags": [
            "grey",
            "navy",
            "retro",
            "cream"
        ],
        "colors": [
            "e7e6e1",
            "f7f6e7",
            "c1c0b9",
            "537791"
        ]
    },
    {
        "id": "faf4d0c14545ea4c4c703b3b",
        "tags": [
            "beige",
            "maroon",
            "red",
            "brown",
            "warm"
        ],
        "colors": [
            "faf4d0",
            "c14545",
            "ea4c4c",
            "703b3b"
        ]
    },
    {
        "id": "ecfeff00b7c21284944ef037",
        "tags": [
            "blue",
            "teal",
            "green",
            "light",
            "neon"
        ],
        "colors": [
            "ecfeff",
            "00b7c2",
            "128494",
            "4ef037"
        ]
    },
    {
        "id": "d0ef84f4d143fda831de561c",
        "tags": [
            "green",
            "yellow",
            "orange",
            "fall",
            "gold",
            "nature",
            "kids",
            "food"
        ],
        "colors": [
            "d0ef84",
            "f4d143",
            "fda831",
            "de561c"
        ]
    },
    {
        "id": "fffbccfd2e2ecf1b1b900d0d",
        "tags": [
            "yellow",
            "red",
            "maroon",
            "warm"
        ],
        "colors": [
            "fffbcc",
            "fd2e2e",
            "cf1b1b",
            "900d0d"
        ]
    },
    {
        "id": "248888e6e6e6e7475ef0d879",
        "tags": [
            "teal",
            "grey",
            "red",
            "yellow",
            "kids"
        ],
        "colors": [
            "248888",
            "e6e6e6",
            "e7475e",
            "f0d879"
        ]
    },
    {
        "id": "e1ffcfcfcbf1bab5f64d3664",
        "tags": [
            "green",
            "purple",
            "retro",
            "wedding",
            "light"
        ],
        "colors": [
            "e1ffcf",
            "cfcbf1",
            "bab5f6",
            "4d3664"
        ]
    },
    {
        "id": "08085ea2ef44fff07ae8fcf6",
        "tags": [
            "navy",
            "green",
            "yellow",
            "neon",
            "kids"
        ],
        "colors": [
            "08085e",
            "a2ef44",
            "fff07a",
            "e8fcf6"
        ]
    },
    {
        "id": "f6c667b30753280f34bff4ed",
        "tags": [
            "yellow",
            "maroon",
            "black",
            "teal",
            "retro"
        ],
        "colors": [
            "f6c667",
            "b30753",
            "280f34",
            "bff4ed"
        ]
    },
    {
        "id": "ffdd9358dada1ca2bb005e7c",
        "tags": [
            "beige",
            "blue",
            "summer"
        ],
        "colors": [
            "ffdd93",
            "58dada",
            "1ca2bb",
            "005e7c"
        ]
    },
    {
        "id": "fffde1fef778fba7467f7f7f",
        "tags": [
            "yellow",
            "orange",
            "grey",
            "gold"
        ],
        "colors": [
            "fffde1",
            "fef778",
            "fba746",
            "7f7f7f"
        ]
    },
    {
        "id": "3932324d45458d6262ed8d8d",
        "tags": [
            "black",
            "grey",
            "peach",
            "dark",
            "skin",
            "night",
            "halloween",
            "gradient"
        ],
        "colors": [
            "393232",
            "4d4545",
            "8d6262",
            "ed8d8d"
        ]
    },
    {
        "id": "a9eca2f5ffcbffe3b0f5c8bd",
        "tags": [
            "green",
            "yellow",
            "peach",
            "orange",
            "pastel",
            "summer",
            "light",
            "cream",
            "happy"
        ],
        "colors": [
            "a9eca2",
            "f5ffcb",
            "ffe3b0",
            "f5c8bd"
        ]
    },
    {
        "id": "36626a588d9c73b1c1f1d18a",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "winter",
            "wedding",
            "sea"
        ],
        "colors": [
            "36626a",
            "588d9c",
            "73b1c1",
            "f1d18a"
        ]
    },
    {
        "id": "21157224bddff4f4f4fffdbb",
        "tags": [
            "navy",
            "blue",
            "grey",
            "yellow",
            "wedding"
        ],
        "colors": [
            "211572",
            "24bddf",
            "f4f4f4",
            "fffdbb"
        ]
    },
    {
        "id": "f7f2c1f0ca6d48ba95403321",
        "tags": [
            "beige",
            "yellow",
            "teal",
            "brown"
        ],
        "colors": [
            "f7f2c1",
            "f0ca6d",
            "48ba95",
            "403321"
        ]
    },
    {
        "id": "282d4f23103aa0204cff6c00",
        "tags": [
            "navy",
            "maroon",
            "orange",
            "dark",
            "halloween",
            "night"
        ],
        "colors": [
            "282d4f",
            "23103a",
            "a0204c",
            "ff6c00"
        ]
    },
    {
        "id": "ffc7c7ffe2e2f6f6f68785a2",
        "tags": [
            "pink",
            "peach",
            "white",
            "retro",
            "wedding",
            "skin",
            "cream"
        ],
        "colors": [
            "ffc7c7",
            "ffe2e2",
            "f6f6f6",
            "8785a2"
        ]
    },
    {
        "id": "f2e8c6f5841abb002903002c",
        "tags": [
            "beige",
            "yellow",
            "orange",
            "red",
            "maroon",
            "black",
            "halloween",
            "fall",
            "gold"
        ],
        "colors": [
            "f2e8c6",
            "f5841a",
            "bb0029",
            "03002c"
        ]
    },
    {
        "id": "096c470b8457eac100f8f1d0",
        "tags": [
            "green",
            "yellow",
            "beige",
            "nature"
        ],
        "colors": [
            "096c47",
            "0b8457",
            "eac100",
            "f8f1d0"
        ]
    },
    {
        "id": "21157248c0d3dededeffe578",
        "tags": [
            "navy",
            "blue",
            "grey",
            "yellow",
            "retro",
            "wedding"
        ],
        "colors": [
            "211572",
            "48c0d3",
            "dedede",
            "ffe578"
        ]
    },
    {
        "id": "3e333ffc4442f0e19ef2f2f2",
        "tags": [
            "black",
            "red",
            "yellow",
            "grey"
        ],
        "colors": [
            "3e333f",
            "fc4442",
            "f0e19e",
            "f2f2f2"
        ]
    },
    {
        "id": "c6de412d6e7e153b44071c21",
        "tags": [
            "green",
            "teal",
            "navy",
            "black",
            "dark"
        ],
        "colors": [
            "c6de41",
            "2d6e7e",
            "153b44",
            "071c21"
        ]
    },
    {
        "id": "f6490d0002491dced8faf9f0",
        "tags": [
            "orange",
            "navy",
            "blue",
            "white",
            "retro",
            "kids"
        ],
        "colors": [
            "f6490d",
            "000249",
            "1dced8",
            "faf9f0"
        ]
    },
    {
        "id": "071a5208697217b978a7ff83",
        "tags": [
            "navy",
            "teal",
            "green",
            "neon",
            "space"
        ],
        "colors": [
            "071a52",
            "086972",
            "17b978",
            "a7ff83"
        ]
    },
    {
        "id": "363636dc2f2fff894cf8f8f8",
        "tags": [
            "black",
            "grey",
            "red",
            "orange",
            "white"
        ],
        "colors": [
            "363636",
            "dc2f2f",
            "ff894c",
            "f8f8f8"
        ]
    },
    {
        "id": "fcf9f9f1f864bceb3c7cbd1e",
        "tags": [
            "white",
            "yellow",
            "green",
            "summer",
            "light",
            "spring",
            "neon",
            "happy"
        ],
        "colors": [
            "fcf9f9",
            "f1f864",
            "bceb3c",
            "7cbd1e"
        ]
    },
    {
        "id": "00000086003ce41f7bff8ba0",
        "tags": [
            "black",
            "maroon",
            "pink",
            "dark",
            "space"
        ],
        "colors": [
            "000000",
            "86003c",
            "e41f7b",
            "ff8ba0"
        ]
    },
    {
        "id": "e0fcffbde4f4404969ff7f50",
        "tags": [
            "blue",
            "navy",
            "orange",
            "winter"
        ],
        "colors": [
            "e0fcff",
            "bde4f4",
            "404969",
            "ff7f50"
        ]
    },
    {
        "id": "a1d9ffca82f8ed93cbf2bbbb",
        "tags": [
            "blue",
            "purple",
            "pink",
            "peach",
            "wedding",
            "kids"
        ],
        "colors": [
            "a1d9ff",
            "ca82f8",
            "ed93cb",
            "f2bbbb"
        ]
    },
    {
        "id": "7344884926459febebfafcdb",
        "tags": [
            "purple",
            "blue",
            "yellow",
            "retro"
        ],
        "colors": [
            "734488",
            "492645",
            "9febeb",
            "fafcdb"
        ]
    },
    {
        "id": "ff895dd5eeff78bbe61b435d",
        "tags": [
            "orange",
            "blue",
            "navy",
            "kids"
        ],
        "colors": [
            "ff895d",
            "d5eeff",
            "78bbe6",
            "1b435d"
        ]
    },
    {
        "id": "1ffffffffde1ff9d76ff4273",
        "tags": [
            "teal",
            "beige",
            "orange",
            "red",
            "summer",
            "spring",
            "light",
            "neon"
        ],
        "colors": [
            "1fffff",
            "fffde1",
            "ff9d76",
            "ff4273"
        ]
    },
    {
        "id": "212125239d60a3de83f7f39a",
        "tags": [
            "black",
            "green",
            "yellow",
            "nature"
        ],
        "colors": [
            "212125",
            "239d60",
            "a3de83",
            "f7f39a"
        ]
    },
    {
        "id": "fafafaffe9e3c4c1e07c73e6",
        "tags": [
            "white",
            "peach",
            "purple",
            "vintage",
            "wedding"
        ],
        "colors": [
            "fafafa",
            "ffe9e3",
            "c4c1e0",
            "7c73e6"
        ]
    },
    {
        "id": "624464d02e77fed6befffee6",
        "tags": [
            "purple",
            "wedding",
            "peach"
        ],
        "colors": [
            "624464",
            "d02e77",
            "fed6be",
            "fffee6"
        ]
    },
    {
        "id": "fbfbfbb9e1dcf38181756c83",
        "tags": [
            "white",
            "teal",
            "red",
            "vintage",
            "retro"
        ],
        "colors": [
            "fbfbfb",
            "b9e1dc",
            "f38181",
            "756c83"
        ]
    },
    {
        "id": "3f52e3f6f6f6efe891f12d2d",
        "tags": [
            "blue",
            "white",
            "yellow",
            "red",
            "summer",
            "rainbow",
            "kids"
        ],
        "colors": [
            "3f52e3",
            "f6f6f6",
            "efe891",
            "f12d2d"
        ]
    },
    {
        "id": "323232295f4e6db193f4e5c2",
        "tags": [
            "black",
            "green",
            "beige",
            "earth"
        ],
        "colors": [
            "323232",
            "295f4e",
            "6db193",
            "f4e5c2"
        ]
    },
    {
        "id": "fbfbfbfff1c178b7bb808b97",
        "tags": [
            "white",
            "yellow",
            "teal",
            "grey",
            "pastel",
            "light"
        ],
        "colors": [
            "fbfbfb",
            "fff1c1",
            "78b7bb",
            "808b97"
        ]
    },
    {
        "id": "dffcb5b7f5deadd1fc9870fc",
        "tags": [
            "green",
            "mint",
            "blue",
            "purple",
            "kids"
        ],
        "colors": [
            "dffcb5",
            "b7f5de",
            "add1fc",
            "9870fc"
        ]
    },
    {
        "id": "161d6e1160aa9bb4dae9d2b3",
        "tags": [
            "navy",
            "blue",
            "beige",
            "winter",
            "sea"
        ],
        "colors": [
            "161d6e",
            "1160aa",
            "9bb4da",
            "e9d2b3"
        ]
    },
    {
        "id": "33425b87dfd638817af9f8eb",
        "tags": [
            "navy",
            "teal",
            "white",
            "wedding"
        ],
        "colors": [
            "33425b",
            "87dfd6",
            "38817a",
            "f9f8eb"
        ]
    },
    {
        "id": "feff89ff9f68f85959ac005d",
        "tags": [
            "yellow",
            "orange",
            "red",
            "maroon",
            "sunset",
            "gold",
            "warm"
        ],
        "colors": [
            "feff89",
            "ff9f68",
            "f85959",
            "ac005d"
        ]
    },
    {
        "id": "0881a3fffdfbfde9dfffd6a4",
        "tags": [
            "blue",
            "white",
            "pink",
            "yellow",
            "kids"
        ],
        "colors": [
            "0881a3",
            "fffdfb",
            "fde9df",
            "ffd6a4"
        ]
    },
    {
        "id": "f67280c06c846c5b7b355c7d",
        "tags": [
            "red",
            "navy",
            "sunset"
        ],
        "colors": [
            "f67280",
            "c06c84",
            "6c5b7b",
            "355c7d"
        ]
    },
    {
        "id": "fff5dbe1addcc238b5810075",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "wedding"
        ],
        "colors": [
            "fff5db",
            "e1addc",
            "c238b5",
            "810075"
        ]
    },
    {
        "id": "1b3c680074e400b8c0e9ffb2",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "gradient"
        ],
        "colors": [
            "1b3c68",
            "0074e4",
            "00b8c0",
            "e9ffb2"
        ]
    },
    {
        "id": "393e465c636ef96d00f2f2f2",
        "tags": [
            "grey",
            "orange",
            "white"
        ],
        "colors": [
            "393e46",
            "5c636e",
            "f96d00",
            "f2f2f2"
        ]
    },
    {
        "id": "d1f386eda045df654acc376d",
        "tags": [
            "green",
            "orange",
            "purple",
            "fall"
        ],
        "colors": [
            "d1f386",
            "eda045",
            "df654a",
            "cc376d"
        ]
    },
    {
        "id": "34374c2c2e3eee2b47f6f6f6",
        "tags": [
            "black",
            "red",
            "grey",
            "white",
            "space"
        ],
        "colors": [
            "34374c",
            "2c2e3e",
            "ee2b47",
            "f6f6f6"
        ]
    },
    {
        "id": "f5e1daf1f1f140a798476269",
        "tags": [
            "peach",
            "grey",
            "teal",
            "wedding",
            "skin",
            "nature"
        ],
        "colors": [
            "f5e1da",
            "f1f1f1",
            "40a798",
            "476269"
        ]
    },
    {
        "id": "37474f607d8b90a4aef7b633",
        "tags": [
            "grey",
            "orange",
            "night"
        ],
        "colors": [
            "37474f",
            "607d8b",
            "90a4ae",
            "f7b633"
        ]
    },
    {
        "id": "ffbdd4ffe5b9ffc77fff5c5c",
        "tags": [
            "pink",
            "beige",
            "orange",
            "red",
            "skin",
            "kids"
        ],
        "colors": [
            "ffbdd4",
            "ffe5b9",
            "ffc77f",
            "ff5c5c"
        ]
    },
    {
        "id": "f759403342523648573dc7be",
        "tags": [
            "peach",
            "navy",
            "teal",
            "retro",
            "space"
        ],
        "colors": [
            "f75940",
            "334252",
            "364857",
            "3dc7be"
        ]
    },
    {
        "id": "dddddd113c4a265a5c3f7b70",
        "tags": [
            "grey",
            "teal",
            "green",
            "cold",
            "night"
        ],
        "colors": [
            "dddddd",
            "113c4a",
            "265a5c",
            "3f7b70"
        ]
    },
    {
        "id": "ececec3e3e3eee046cfcac0c",
        "tags": [
            "grey",
            "black",
            "pink",
            "orange"
        ],
        "colors": [
            "ececec",
            "3e3e3e",
            "ee046c",
            "fcac0c"
        ]
    },
    {
        "id": "f54d42ff8356ffcd00f5f5f5",
        "tags": [
            "red",
            "orange",
            "yellow",
            "grey",
            "white",
            "gold"
        ],
        "colors": [
            "f54d42",
            "ff8356",
            "ffcd00",
            "f5f5f5"
        ]
    },
    {
        "id": "b0dedbe3f3f7fc6e5e583131",
        "tags": [
            "teal",
            "red",
            "brown",
            "kids"
        ],
        "colors": [
            "b0dedb",
            "e3f3f7",
            "fc6e5e",
            "583131"
        ]
    },
    {
        "id": "fbf7f7f1e9e3ee712bdc4712",
        "tags": [
            "white",
            "grey",
            "orange",
            "fall",
            "gold"
        ],
        "colors": [
            "fbf7f7",
            "f1e9e3",
            "ee712b",
            "dc4712"
        ]
    },
    {
        "id": "f3ecc878c2c33f66990d1b4c",
        "tags": [
            "beige",
            "teal",
            "blue",
            "navy",
            "winter",
            "gradient"
        ],
        "colors": [
            "f3ecc8",
            "78c2c3",
            "3f6699",
            "0d1b4c"
        ]
    },
    {
        "id": "cbf078f8f398f1b963e46161",
        "tags": [
            "green",
            "yellow",
            "orange",
            "red",
            "spring",
            "food",
            "happy"
        ],
        "colors": [
            "cbf078",
            "f8f398",
            "f1b963",
            "e46161"
        ]
    },
    {
        "id": "f9f9f9ded5c4ef7e56305973",
        "tags": [
            "white",
            "grey",
            "beige",
            "orange",
            "navy",
            "vintage",
            "retro"
        ],
        "colors": [
            "f9f9f9",
            "ded5c4",
            "ef7e56",
            "305973"
        ]
    },
    {
        "id": "8e3343ec9454f1f08ac6cd78",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "green",
            "fall",
            "halloween",
            "food"
        ],
        "colors": [
            "8e3343",
            "ec9454",
            "f1f08a",
            "c6cd78"
        ]
    },
    {
        "id": "fcfcfc0fc9e73186b24756ca",
        "tags": [
            "white",
            "blue"
        ],
        "colors": [
            "fcfcfc",
            "0fc9e7",
            "3186b2",
            "4756ca"
        ]
    },
    {
        "id": "e9007f7cdfffd5fffbfcffc8",
        "tags": [
            "pink",
            "blue",
            "yellow",
            "light",
            "neon",
            "spring",
            "happy"
        ],
        "colors": [
            "e9007f",
            "7cdfff",
            "d5fffb",
            "fcffc8"
        ]
    },
    {
        "id": "fafcd6259f6c1e6b7f140303",
        "tags": [
            "yellow",
            "green",
            "blue",
            "navy",
            "black"
        ],
        "colors": [
            "fafcd6",
            "259f6c",
            "1e6b7f",
            "140303"
        ]
    },
    {
        "id": "3e4377fd367ef1f2f3ff9900",
        "tags": [
            "navy",
            "pink",
            "grey",
            "white",
            "orange",
            "wedding"
        ],
        "colors": [
            "3e4377",
            "fd367e",
            "f1f2f3",
            "ff9900"
        ]
    },
    {
        "id": "f9fbfca0dbdb56a7a7fcea90",
        "tags": [
            "white",
            "teal",
            "yellow",
            "spring",
            "light"
        ],
        "colors": [
            "f9fbfc",
            "a0dbdb",
            "56a7a7",
            "fcea90"
        ]
    },
    {
        "id": "00345902809002c39afce38a",
        "tags": [
            "navy",
            "teal",
            "green",
            "yellow",
            "gradient"
        ],
        "colors": [
            "003459",
            "028090",
            "02c39a",
            "fce38a"
        ]
    },
    {
        "id": "d5f7ff494b67ff006cecebff",
        "tags": [
            "blue",
            "grey",
            "red"
        ],
        "colors": [
            "d5f7ff",
            "494b67",
            "ff006c",
            "ecebff"
        ]
    },
    {
        "id": "00649f01aac100dbe797ecc5",
        "tags": [
            "blue",
            "teal",
            "mint",
            "cold",
            "sea"
        ],
        "colors": [
            "00649f",
            "01aac1",
            "00dbe7",
            "97ecc5"
        ]
    },
    {
        "id": "f0f0f043dde6364f6bfc5185",
        "tags": [
            "grey",
            "blue",
            "navy",
            "pink",
            "space"
        ],
        "colors": [
            "f0f0f0",
            "43dde6",
            "364f6b",
            "fc5185"
        ]
    },
    {
        "id": "085f6349beb7fccf4def255f",
        "tags": [
            "teal",
            "yellow",
            "red",
            "spring",
            "kids"
        ],
        "colors": [
            "085f63",
            "49beb7",
            "fccf4d",
            "ef255f"
        ]
    },
    {
        "id": "4a2c2cd3504affdc76fefea4",
        "tags": [
            "brown",
            "maroon",
            "red",
            "yellow",
            "gold"
        ],
        "colors": [
            "4a2c2c",
            "d3504a",
            "ffdc76",
            "fefea4"
        ]
    },
    {
        "id": "a13939e75151fcc88ac2c57f",
        "tags": [
            "red",
            "orange",
            "green",
            "christmas",
            "fall",
            "food"
        ],
        "colors": [
            "a13939",
            "e75151",
            "fcc88a",
            "c2c57f"
        ]
    },
    {
        "id": "f1f4f65ac8d8597fca2552ac",
        "tags": [
            "grey",
            "teal",
            "blue",
            "cold"
        ],
        "colors": [
            "f1f4f6",
            "5ac8d8",
            "597fca",
            "2552ac"
        ]
    },
    {
        "id": "f5fac8aee8e68bcfcc539092",
        "tags": [
            "yellow",
            "teal",
            "pastel",
            "sky"
        ],
        "colors": [
            "f5fac8",
            "aee8e6",
            "8bcfcc",
            "539092"
        ]
    },
    {
        "id": "9b5d73b0757cc38b8bfff1c5",
        "tags": [
            "brown",
            "yellow",
            "skin"
        ],
        "colors": [
            "9b5d73",
            "b0757c",
            "c38b8b",
            "fff1c5"
        ]
    },
    {
        "id": "66bfbfeaf6f6fcfefef76b8a",
        "tags": [
            "teal",
            "grey",
            "white",
            "pink",
            "kids"
        ],
        "colors": [
            "66bfbf",
            "eaf6f6",
            "fcfefe",
            "f76b8a"
        ]
    },
    {
        "id": "f8eeb4cfee91658525092a35",
        "tags": [
            "yellow",
            "beige",
            "green",
            "black",
            "nature"
        ],
        "colors": [
            "f8eeb4",
            "cfee91",
            "658525",
            "092a35"
        ]
    },
    {
        "id": "f5f5f501ecd54586ff32424a",
        "tags": [
            "grey",
            "teal",
            "blue",
            "black",
            "cold"
        ],
        "colors": [
            "f5f5f5",
            "01ecd5",
            "4586ff",
            "32424a"
        ]
    },
    {
        "id": "283e561989ace8f1f5ffde25",
        "tags": [
            "navy",
            "blue",
            "yellow"
        ],
        "colors": [
            "283e56",
            "1989ac",
            "e8f1f5",
            "ffde25"
        ]
    },
    {
        "id": "f7f7f84eeaf6c82586291f71",
        "tags": [
            "white",
            "grey",
            "blue",
            "purple",
            "navy",
            "neon",
            "space"
        ],
        "colors": [
            "f7f7f8",
            "4eeaf6",
            "c82586",
            "291f71"
        ]
    },
    {
        "id": "155263ff6f3cff9a3cffc93c",
        "tags": [
            "navy",
            "orange",
            "yellow",
            "warm",
            "gold",
            "sunset"
        ],
        "colors": [
            "155263",
            "ff6f3c",
            "ff9a3c",
            "ffc93c"
        ]
    },
    {
        "id": "f5eeeeea21a2af05aa171313",
        "tags": [
            "grey",
            "pink",
            "purple",
            "black"
        ],
        "colors": [
            "f5eeee",
            "ea21a2",
            "af05aa",
            "171313"
        ]
    },
    {
        "id": "f60c86f9f6d8a5bfdd2e89ba",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "wedding",
            "spring"
        ],
        "colors": [
            "f60c86",
            "f9f6d8",
            "a5bfdd",
            "2e89ba"
        ]
    },
    {
        "id": "657dc4838ed9ece8e5f59292",
        "tags": [
            "blue",
            "peach",
            "kids"
        ],
        "colors": [
            "657dc4",
            "838ed9",
            "ece8e5",
            "f59292"
        ]
    },
    {
        "id": "682666cf0a2ce73e51ffce00",
        "tags": [
            "purple",
            "maroon",
            "red",
            "yellow",
            "sunset"
        ],
        "colors": [
            "682666",
            "cf0a2c",
            "e73e51",
            "ffce00"
        ]
    },
    {
        "id": "393939849561eed690ecefd8",
        "tags": [
            "green",
            "yellow",
            "beige",
            "earth",
            "nature",
            "gradient"
        ],
        "colors": [
            "393939",
            "849561",
            "eed690",
            "ecefd8"
        ]
    },
    {
        "id": "d4a5a5ffecdaf9ffeaa6d0e4",
        "tags": [
            "peach",
            "beige",
            "blue",
            "pastel",
            "vintage",
            "summer",
            "skin",
            "light",
            "happy"
        ],
        "colors": [
            "d4a5a5",
            "ffecda",
            "f9ffea",
            "a6d0e4"
        ]
    },
    {
        "id": "97124bdc4444f5a855f4e557",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "halloween"
        ],
        "colors": [
            "97124b",
            "dc4444",
            "f5a855",
            "f4e557"
        ]
    },
    {
        "id": "143a526e828acde3ebe3eff3",
        "tags": [
            "navy",
            "grey",
            "wedding",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "143a52",
            "6e828a",
            "cde3eb",
            "e3eff3"
        ]
    },
    {
        "id": "432160ff7a5a50e3c2fcf4d9",
        "tags": [
            "purple",
            "orange",
            "teal",
            "beige",
            "neon",
            "happy"
        ],
        "colors": [
            "432160",
            "ff7a5a",
            "50e3c2",
            "fcf4d9"
        ]
    },
    {
        "id": "a1eafbfdfdfdffcef3cabbe9",
        "tags": [
            "blue",
            "white",
            "pink",
            "purple",
            "light",
            "wedding",
            "spring",
            "kids",
            "sky"
        ],
        "colors": [
            "a1eafb",
            "fdfdfd",
            "ffcef3",
            "cabbe9"
        ]
    },
    {
        "id": "fff4c9c7e78b81ae64709053",
        "tags": [
            "yellow",
            "green",
            "nature",
            "happy",
            "food",
            "summer"
        ],
        "colors": [
            "fff4c9",
            "c7e78b",
            "81ae64",
            "709053"
        ]
    },
    {
        "id": "ffe0371dcd9f088c6f23033c",
        "tags": [
            "yellow",
            "teal",
            "black"
        ],
        "colors": [
            "ffe037",
            "1dcd9f",
            "088c6f",
            "23033c"
        ]
    },
    {
        "id": "ff395e8fecc86f6f6f4a4a4a",
        "tags": [
            "red",
            "mint",
            "grey"
        ],
        "colors": [
            "ff395e",
            "8fecc8",
            "6f6f6f",
            "4a4a4a"
        ]
    },
    {
        "id": "0002490f4392ff5151ff8b8b",
        "tags": [
            "navy",
            "blue",
            "red",
            "wedding",
            "halloween",
            "space"
        ],
        "colors": [
            "000249",
            "0f4392",
            "ff5151",
            "ff8b8b"
        ]
    },
    {
        "id": "f6f6f6d6e4f01e56a0163172",
        "tags": [],
        "colors": [
            "f6f6f6",
            "d6e4f0",
            "1e56a0",
            "163172"
        ]
    },
    {
        "id": "ff007bff5757ff8585ffebeb",
        "tags": [
            "pink",
            "red",
            "orange",
            "spring",
            "skin",
            "kids"
        ],
        "colors": [
            "ff007b",
            "ff5757",
            "ff8585",
            "ffebeb"
        ]
    },
    {
        "id": "f5f5f5ecececfacc2e27b1be",
        "tags": [
            "white",
            "grey",
            "yellow",
            "teal"
        ],
        "colors": [
            "f5f5f5",
            "ececec",
            "facc2e",
            "27b1be"
        ]
    },
    {
        "id": "d5def58594e46643b5430f58",
        "tags": [
            "blue",
            "purple",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "d5def5",
            "8594e4",
            "6643b5",
            "430f58"
        ]
    },
    {
        "id": "bff4ed280f34b30753f6c667",
        "tags": [
            "blue",
            "black",
            "maroon",
            "yellow",
            "retro"
        ],
        "colors": [
            "bff4ed",
            "280f34",
            "b30753",
            "f6c667"
        ]
    },
    {
        "id": "1fad9fcd3131ab1212f6c667",
        "tags": [
            "teal",
            "red",
            "maroon",
            "beige"
        ],
        "colors": [
            "1fad9f",
            "cd3131",
            "ab1212",
            "f6c667"
        ]
    },
    {
        "id": "fc00a3b30c7b780662e3f6f5",
        "tags": [
            "pink",
            "purple"
        ],
        "colors": [
            "fc00a3",
            "b30c7b",
            "780662",
            "e3f6f5"
        ]
    },
    {
        "id": "461b936a3cbc8253d7f78f1e",
        "tags": [
            "purple",
            "orange",
            "halloween"
        ],
        "colors": [
            "461b93",
            "6a3cbc",
            "8253d7",
            "f78f1e"
        ]
    },
    {
        "id": "ff008e124e960d8abcdaeaf6",
        "tags": [
            "pink",
            "navy",
            "blue"
        ],
        "colors": [
            "ff008e",
            "124e96",
            "0d8abc",
            "daeaf6"
        ]
    },
    {
        "id": "ffdaa96fa3a95f72b260366f",
        "tags": [
            "beige",
            "teal",
            "blue",
            "purple",
            "retro"
        ],
        "colors": [
            "ffdaa9",
            "6fa3a9",
            "5f72b2",
            "60366f"
        ]
    },
    {
        "id": "71397c91519dc582d5ffdf5a",
        "tags": [
            "purple",
            "yellow"
        ],
        "colors": [
            "71397c",
            "91519d",
            "c582d5",
            "ffdf5a"
        ]
    },
    {
        "id": "ffffc1ffd2a5ffa8b8d988bc",
        "tags": [
            "yellow",
            "orange",
            "pink",
            "purple",
            "light",
            "warm",
            "happy"
        ],
        "colors": [
            "ffffc1",
            "ffd2a5",
            "ffa8b8",
            "d988bc"
        ]
    },
    {
        "id": "626eef09a8fa41c5d3fffa9d",
        "tags": [
            "blue",
            "teal",
            "yellow",
            "light",
            "happy"
        ],
        "colors": [
            "626eef",
            "09a8fa",
            "41c5d3",
            "fffa9d"
        ]
    },
    {
        "id": "581845900c3fc70039ff5733",
        "tags": [
            "maroon",
            "red",
            "orange",
            "warm",
            "dark",
            "halloween"
        ],
        "colors": [
            "581845",
            "900c3f",
            "c70039",
            "ff5733"
        ]
    },
    {
        "id": "4a333398d083bcfcc9f2feca",
        "tags": [
            "brown",
            "green",
            "mint",
            "yellow",
            "nature",
            "summer"
        ],
        "colors": [
            "4a3333",
            "98d083",
            "bcfcc9",
            "f2feca"
        ]
    },
    {
        "id": "e3d9ca95a792596c68403f48",
        "tags": [
            "beige",
            "green",
            "earth",
            "vintage",
            "food"
        ],
        "colors": [
            "e3d9ca",
            "95a792",
            "596c68",
            "403f48"
        ]
    },
    {
        "id": "c84361e78775abcdcbebe59b",
        "tags": [
            "red",
            "peach",
            "orange",
            "blue",
            "yellow",
            "summer",
            "rainbow",
            "pastel",
            "kids"
        ],
        "colors": [
            "c84361",
            "e78775",
            "abcdcb",
            "ebe59b"
        ]
    },
    {
        "id": "6a0000935656c4f0c5f1fff1",
        "tags": [
            "maroon",
            "brown",
            "green",
            "white",
            "nature"
        ],
        "colors": [
            "6a0000",
            "935656",
            "c4f0c5",
            "f1fff1"
        ]
    },
    {
        "id": "7d156db94e8ad87ca1ffd7f1",
        "tags": [
            "purple",
            "pink",
            "wedding",
            "gradient"
        ],
        "colors": [
            "7d156d",
            "b94e8a",
            "d87ca1",
            "ffd7f1"
        ]
    },
    {
        "id": "363333272121e16428f6e9e9",
        "tags": [
            "grey",
            "black",
            "orange",
            "dark",
            "halloween",
            "night"
        ],
        "colors": [
            "363333",
            "272121",
            "e16428",
            "f6e9e9"
        ]
    },
    {
        "id": "feffeaa3de832eb872ff5d6e",
        "tags": [
            "yellow",
            "green",
            "red",
            "spring",
            "nature"
        ],
        "colors": [
            "feffea",
            "a3de83",
            "2eb872",
            "ff5d6e"
        ]
    },
    {
        "id": "f5feffbde4f4404969dc552c",
        "tags": [
            "white",
            "blue",
            "navy",
            "orange",
            "winter"
        ],
        "colors": [
            "f5feff",
            "bde4f4",
            "404969",
            "dc552c"
        ]
    },
    {
        "id": "f03861fef2f2f5d97ee8b844",
        "tags": [
            "red",
            "pink",
            "yellow",
            "spring",
            "kids"
        ],
        "colors": [
            "f03861",
            "fef2f2",
            "f5d97e",
            "e8b844"
        ]
    },
    {
        "id": "39065a6a05729a0f98ea0599",
        "tags": [
            "purple",
            "pink",
            "dark",
            "space"
        ],
        "colors": [
            "39065a",
            "6a0572",
            "9a0f98",
            "ea0599"
        ]
    },
    {
        "id": "27296d5e63b6a393ebf5c7f7",
        "tags": [
            "navy",
            "purple",
            "pink",
            "cold",
            "space",
            "gradient"
        ],
        "colors": [
            "27296d",
            "5e63b6",
            "a393eb",
            "f5c7f7"
        ]
    },
    {
        "id": "ffbc2c86b86b4d4d4dececec",
        "tags": [
            "yellow",
            "green",
            "grey"
        ],
        "colors": [
            "ffbc2c",
            "86b86b",
            "4d4d4d",
            "ececec"
        ]
    },
    {
        "id": "f7f7f7f5b553854836000000",
        "tags": [
            "white",
            "grey",
            "orange",
            "brown",
            "black",
            "fall",
            "skin",
            "gold"
        ],
        "colors": [
            "f7f7f7",
            "f5b553",
            "854836",
            "000000"
        ]
    },
    {
        "id": "dff4f3dde7f2b9bbdf878ecd",
        "tags": [
            "teal",
            "blue",
            "purple",
            "winter",
            "cold",
            "pastel",
            "sky"
        ],
        "colors": [
            "dff4f3",
            "dde7f2",
            "b9bbdf",
            "878ecd"
        ]
    },
    {
        "id": "dce8baf3d179f09872f46060",
        "tags": [
            "sage",
            "yellow",
            "orange",
            "peach",
            "red",
            "pastel",
            "fall",
            "happy"
        ],
        "colors": [
            "dce8ba",
            "f3d179",
            "f09872",
            "f46060"
        ]
    },
    {
        "id": "f1e290f677c19b3284690074",
        "tags": [
            "yellow",
            "pink",
            "purple"
        ],
        "colors": [
            "f1e290",
            "f677c1",
            "9b3284",
            "690074"
        ]
    },
    {
        "id": "f2f9f1388e3c8bc34addeedf",
        "tags": [
            "white",
            "green",
            "nature"
        ],
        "colors": [
            "f2f9f1",
            "388e3c",
            "8bc34a",
            "ddeedf"
        ]
    },
    {
        "id": "6c5070df6a6af6f6e3c2dbc1",
        "tags": [
            "purple",
            "red",
            "green",
            "vintage",
            "pastel"
        ],
        "colors": [
            "6c5070",
            "df6a6a",
            "f6f6e3",
            "c2dbc1"
        ]
    },
    {
        "id": "0e2431fc3a52f9b248e8d5b7",
        "tags": [
            "black",
            "red",
            "orange",
            "beige",
            "warm",
            "halloween",
            "space"
        ],
        "colors": [
            "0e2431",
            "fc3a52",
            "f9b248",
            "e8d5b7"
        ]
    },
    {
        "id": "f8ed86a5e9db2ca4bf415b90",
        "tags": [
            "yellow",
            "teal",
            "blue",
            "navy"
        ],
        "colors": [
            "f8ed86",
            "a5e9db",
            "2ca4bf",
            "415b90"
        ]
    },
    {
        "id": "e9e2d0ea9085d45d796e5773",
        "tags": [
            "beige",
            "peach",
            "red",
            "fall",
            "skin",
            "coffee",
            "pastel"
        ],
        "colors": [
            "e9e2d0",
            "ea9085",
            "d45d79",
            "6e5773"
        ]
    },
    {
        "id": "ffed8fa7d46f3597683c3352",
        "tags": [
            "yellow",
            "green"
        ],
        "colors": [
            "ffed8f",
            "a7d46f",
            "359768",
            "3c3352"
        ]
    },
    {
        "id": "c4aff0fffeec64d7d65782bb",
        "tags": [
            "purple",
            "yellow",
            "teal",
            "blue",
            "wedding",
            "kids"
        ],
        "colors": [
            "c4aff0",
            "fffeec",
            "64d7d6",
            "5782bb"
        ]
    },
    {
        "id": "ffe495ffc97b44558fe6f7f7",
        "tags": [
            "yellow",
            "orange",
            "navy",
            "blue"
        ],
        "colors": [
            "ffe495",
            "ffc97b",
            "44558f",
            "e6f7f7"
        ]
    },
    {
        "id": "dd105e46466e8787a3bdbdd7",
        "tags": [
            "red",
            "navy",
            "grey",
            "dark"
        ],
        "colors": [
            "dd105e",
            "46466e",
            "8787a3",
            "bdbdd7"
        ]
    },
    {
        "id": "feff9a6fe8c885fedeb7abfb",
        "tags": [
            "yellow",
            "teal",
            "mint",
            "purple",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "feff9a",
            "6fe8c8",
            "85fede",
            "b7abfb"
        ]
    },
    {
        "id": "ca498c8b2f8ab08fbbf6d5d5",
        "tags": [
            "purple",
            "pink",
            "peach",
            "happy"
        ],
        "colors": [
            "ca498c",
            "8b2f8a",
            "b08fbb",
            "f6d5d5"
        ]
    },
    {
        "id": "ffe3b7840404cb0101ffaf00",
        "tags": [
            "beige",
            "maroon",
            "red",
            "orange",
            "warm"
        ],
        "colors": [
            "ffe3b7",
            "840404",
            "cb0101",
            "ffaf00"
        ]
    },
    {
        "id": "ffdd83e3f8ff28cc9ea6ed8e",
        "tags": [
            "yellow",
            "green",
            "summer",
            "spring"
        ],
        "colors": [
            "ffdd83",
            "e3f8ff",
            "28cc9e",
            "a6ed8e"
        ]
    },
    {
        "id": "fcefeefccde2fc5c9cc5e3f6",
        "tags": [
            "pink",
            "blue",
            "retro",
            "wedding",
            "kids"
        ],
        "colors": [
            "fcefee",
            "fccde2",
            "fc5c9c",
            "c5e3f6"
        ]
    },
    {
        "id": "588c73f2e394f2ae72d96459",
        "tags": [
            "sage",
            "yellow",
            "orange",
            "red",
            "christmas"
        ],
        "colors": [
            "588c73",
            "f2e394",
            "f2ae72",
            "d96459"
        ]
    },
    {
        "id": "3b09445f1854a12559f1bbd5",
        "tags": [
            "purple",
            "maroon",
            "pink",
            "dark",
            "night"
        ],
        "colors": [
            "3b0944",
            "5f1854",
            "a12559",
            "f1bbd5"
        ]
    },
    {
        "id": "ffed78feffeaaddce4586b8f",
        "tags": [
            "yellow",
            "white",
            "blue",
            "navy",
            "summer"
        ],
        "colors": [
            "ffed78",
            "feffea",
            "addce4",
            "586b8f"
        ]
    },
    {
        "id": "f2fcfcbdf1f68fbaf30245a3",
        "tags": [
            "white",
            "teal",
            "blue",
            "navy",
            "cold",
            "winter",
            "sky"
        ],
        "colors": [
            "f2fcfc",
            "bdf1f6",
            "8fbaf3",
            "0245a3"
        ]
    },
    {
        "id": "f7f09bff5200971549470031",
        "tags": [
            "yellow",
            "orange",
            "maroon",
            "sunset",
            "warm"
        ],
        "colors": [
            "f7f09b",
            "ff5200",
            "971549",
            "470031"
        ]
    },
    {
        "id": "e2eff165799b555273e23e57",
        "tags": [
            "blue",
            "red",
            "retro",
            "cold"
        ],
        "colors": [
            "e2eff1",
            "65799b",
            "555273",
            "e23e57"
        ]
    },
    {
        "id": "222831393e46f96d00f2f2f2",
        "tags": [
            "black",
            "grey",
            "orange",
            "white",
            "fall"
        ],
        "colors": [
            "222831",
            "393e46",
            "f96d00",
            "f2f2f2"
        ]
    },
    {
        "id": "22eaaab31e6fee5a5affb174",
        "tags": [
            "green",
            "mint",
            "maroon",
            "purple",
            "peach",
            "orange",
            "vintage",
            "spring",
            "happy"
        ],
        "colors": [
            "22eaaa",
            "b31e6f",
            "ee5a5a",
            "ffb174"
        ]
    },
    {
        "id": "f1f6f59ef4e612cc946088bb",
        "tags": [
            "grey",
            "teal",
            "green",
            "blue"
        ],
        "colors": [
            "f1f6f5",
            "9ef4e6",
            "12cc94",
            "6088bb"
        ]
    },
    {
        "id": "c02727f4806dffffd3f3f2b4",
        "tags": [
            "red",
            "maroon",
            "peach",
            "yellow"
        ],
        "colors": [
            "c02727",
            "f4806d",
            "ffffd3",
            "f3f2b4"
        ]
    },
    {
        "id": "e9e9e5d4d6c89a9b9452524e",
        "tags": [
            "grey",
            "pastel",
            "winter",
            "cream"
        ],
        "colors": [
            "e9e9e5",
            "d4d6c8",
            "9a9b94",
            "52524e"
        ]
    },
    {
        "id": "324e7b86a6df5068a9f8f8f8",
        "tags": [
            "navy",
            "blue",
            "white",
            "cold",
            "winter"
        ],
        "colors": [
            "324e7b",
            "86a6df",
            "5068a9",
            "f8f8f8"
        ]
    },
    {
        "id": "434343a64452f7c873f8f8f8",
        "tags": [
            "grey",
            "red",
            "maroon",
            "yellow",
            "white",
            "fall"
        ],
        "colors": [
            "434343",
            "a64452",
            "f7c873",
            "f8f8f8"
        ]
    },
    {
        "id": "ef6c35161c2e2bb3c0faf7f2",
        "tags": [
            "orange",
            "black",
            "teal",
            "white",
            "space",
            "retro"
        ],
        "colors": [
            "ef6c35",
            "161c2e",
            "2bb3c0",
            "faf7f2"
        ]
    },
    {
        "id": "9ffbfba100ffdb97ffffb6ff",
        "tags": [
            "blue",
            "purple",
            "pink",
            "light",
            "cold",
            "neon"
        ],
        "colors": [
            "9ffbfb",
            "a100ff",
            "db97ff",
            "ffb6ff"
        ]
    },
    {
        "id": "0000001a8b9db2d430fff5f5",
        "tags": [
            "black",
            "teal",
            "green",
            "white"
        ],
        "colors": [
            "000000",
            "1a8b9d",
            "b2d430",
            "fff5f5"
        ]
    },
    {
        "id": "4e1e1ee63870fbe6a258e481",
        "tags": [
            "brown",
            "maroon",
            "pink",
            "yellow",
            "green",
            "kids"
        ],
        "colors": [
            "4e1e1e",
            "e63870",
            "fbe6a2",
            "58e481"
        ]
    },
    {
        "id": "ffeed0f79f24e200497c064d",
        "tags": [
            "beige",
            "orange",
            "red",
            "maroon",
            "purple",
            "warm"
        ],
        "colors": [
            "ffeed0",
            "f79f24",
            "e20049",
            "7c064d"
        ]
    },
    {
        "id": "f0bebe5ea3a63a718cffffdf",
        "tags": [
            "pink",
            "teal",
            "yellow",
            "kids"
        ],
        "colors": [
            "f0bebe",
            "5ea3a6",
            "3a718c",
            "ffffdf"
        ]
    },
    {
        "id": "19215ef7e6b5fa67ab80185f",
        "tags": [
            "navy",
            "yellow",
            "beige",
            "pink",
            "purple",
            "retro",
            "wedding"
        ],
        "colors": [
            "19215e",
            "f7e6b5",
            "fa67ab",
            "80185f"
        ]
    },
    {
        "id": "23314236506ca5def1ebf7fd",
        "tags": [
            "navy",
            "blue",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "233142",
            "36506c",
            "a5def1",
            "ebf7fd"
        ]
    },
    {
        "id": "303481d6e6f2f5f5f5fff200",
        "tags": [
            "navy",
            "blue",
            "grey",
            "white",
            "yellow",
            "light",
            "happy"
        ],
        "colors": [
            "303481",
            "d6e6f2",
            "f5f5f5",
            "fff200"
        ]
    },
    {
        "id": "e5f9bda0e4187fb414525050",
        "tags": [
            "green",
            "light",
            "grey",
            "nature"
        ],
        "colors": [
            "e5f9bd",
            "a0e418",
            "7fb414",
            "525050"
        ]
    },
    {
        "id": "f9c4ac626f92474168272637",
        "tags": [
            "peach",
            "navy",
            "black",
            "vintage",
            "night"
        ],
        "colors": [
            "f9c4ac",
            "626f92",
            "474168",
            "272637"
        ]
    },
    {
        "id": "070739521477c327abe1e099",
        "tags": [
            "black",
            "purple",
            "yellow",
            "dark"
        ],
        "colors": [
            "070739",
            "521477",
            "c327ab",
            "e1e099"
        ]
    },
    {
        "id": "a9eee6fefaecf38181625772",
        "tags": [
            "teal",
            "beige",
            "peach",
            "vintage",
            "happy"
        ],
        "colors": [
            "a9eee6",
            "fefaec",
            "f38181",
            "625772"
        ]
    },
    {
        "id": "e3e8f8c0c5cd3e588f203562",
        "tags": [
            "blue",
            "grey",
            "navy",
            "wedding",
            "cold"
        ],
        "colors": [
            "e3e8f8",
            "c0c5cd",
            "3e588f",
            "203562"
        ]
    },
    {
        "id": "464545fb5660f98e90f0f3b0",
        "tags": [
            "grey",
            "red",
            "pink",
            "yellow"
        ],
        "colors": [
            "464545",
            "fb5660",
            "f98e90",
            "f0f3b0"
        ]
    },
    {
        "id": "0b526903051e978d58eae1e1",
        "tags": [
            "navy",
            "black",
            "brown",
            "grey",
            "dark",
            "night",
            "sea"
        ],
        "colors": [
            "0b5269",
            "03051e",
            "978d58",
            "eae1e1"
        ]
    },
    {
        "id": "8e9fe66acafc6ce6dddbf094",
        "tags": [
            "blue",
            "purple",
            "teal",
            "green",
            "light"
        ],
        "colors": [
            "8e9fe6",
            "6acafc",
            "6ce6dd",
            "dbf094"
        ]
    },
    {
        "id": "2d5c7ffff1a8ff8f56984a59",
        "tags": [
            "blue",
            "navy",
            "yellow",
            "orange",
            "maroon",
            "sunset"
        ],
        "colors": [
            "2d5c7f",
            "fff1a8",
            "ff8f56",
            "984a59"
        ]
    },
    {
        "id": "feceabff847ceb4a5f2a363b",
        "tags": [
            "peach",
            "orange",
            "red",
            "black",
            "fall",
            "warm"
        ],
        "colors": [
            "feceab",
            "ff847c",
            "eb4a5f",
            "2a363b"
        ]
    },
    {
        "id": "fffbe0fce38a2994b2444f5a",
        "tags": [
            "yellow",
            "blue",
            "navy"
        ],
        "colors": [
            "fffbe0",
            "fce38a",
            "2994b2",
            "444f5a"
        ]
    },
    {
        "id": "fdfce0f0eeb1dad773b1ad25",
        "tags": [
            "yellow",
            "green",
            "cream",
            "nature",
            "food"
        ],
        "colors": [
            "fdfce0",
            "f0eeb1",
            "dad773",
            "b1ad25"
        ]
    },
    {
        "id": "3c1b1fb21e4be2bf81f6e1b5",
        "tags": [
            "brown",
            "maroon",
            "red",
            "yellow",
            "beige",
            "warm",
            "vintage"
        ],
        "colors": [
            "3c1b1f",
            "b21e4b",
            "e2bf81",
            "f6e1b5"
        ]
    },
    {
        "id": "314a5252686aacbdc5ffded5",
        "tags": [
            "navy",
            "teal",
            "peach",
            "winter",
            "night",
            "sea"
        ],
        "colors": [
            "314a52",
            "52686a",
            "acbdc5",
            "ffded5"
        ]
    },
    {
        "id": "f8f8f8c246c691157e65195e",
        "tags": [
            "white",
            "purple"
        ],
        "colors": [
            "f8f8f8",
            "c246c6",
            "91157e",
            "65195e"
        ]
    },
    {
        "id": "062121181810e4dcadeeeeee",
        "tags": [
            "black",
            "beige",
            "grey",
            "night"
        ],
        "colors": [
            "062121",
            "181810",
            "e4dcad",
            "eeeeee"
        ]
    },
    {
        "id": "e1f5f26bc5d25a5d9d390050",
        "tags": [
            "teal",
            "blue",
            "purple",
            "winter",
            "cold"
        ],
        "colors": [
            "e1f5f2",
            "6bc5d2",
            "5a5d9d",
            "390050"
        ]
    },
    {
        "id": "18587afc624dfca7a7ffd6d6",
        "tags": [
            "navy",
            "orange",
            "peach",
            "pink"
        ],
        "colors": [
            "18587a",
            "fc624d",
            "fca7a7",
            "ffd6d6"
        ]
    },
    {
        "id": "3434348e8b82e9dcbef3f3f3",
        "tags": [
            "black",
            "grey",
            "beige",
            "white",
            "coffee"
        ],
        "colors": [
            "343434",
            "8e8b82",
            "e9dcbe",
            "f3f3f3"
        ]
    },
    {
        "id": "f7f39aa3de8338817a346473",
        "tags": [
            "yellow",
            "green",
            "teal"
        ],
        "colors": [
            "f7f39a",
            "a3de83",
            "38817a",
            "346473"
        ]
    },
    {
        "id": "970747fef4e813445a446878",
        "tags": [
            "maroon",
            "red",
            "beige",
            "navy",
            "wedding",
            "retro"
        ],
        "colors": [
            "970747",
            "fef4e8",
            "13445a",
            "446878"
        ]
    },
    {
        "id": "331621cc085ede7d48eeca98",
        "tags": [
            "black",
            "pink",
            "orange",
            "halloween",
            "warm"
        ],
        "colors": [
            "331621",
            "cc085e",
            "de7d48",
            "eeca98"
        ]
    },
    {
        "id": "f8fcfbc9fdd779d1c36892d5",
        "tags": [
            "white",
            "mint",
            "teal",
            "blue",
            "light",
            "cold",
            "happy",
            "sky"
        ],
        "colors": [
            "f8fcfb",
            "c9fdd7",
            "79d1c3",
            "6892d5"
        ]
    },
    {
        "id": "f2f7ff0b409c10316bfdbe34",
        "tags": [
            "white",
            "blue",
            "navy",
            "yellow"
        ],
        "colors": [
            "f2f7ff",
            "0b409c",
            "10316b",
            "fdbe34"
        ]
    },
    {
        "id": "ac0c0ca7d82ef5f883fbfadf",
        "tags": [
            "red",
            "maroon",
            "green",
            "yellow",
            "christmas",
            "spring",
            "food",
            "happy"
        ],
        "colors": [
            "ac0c0c",
            "a7d82e",
            "f5f883",
            "fbfadf"
        ]
    },
    {
        "id": "f8f5e4f973000e304710828c",
        "tags": [
            "beige",
            "orange",
            "navy",
            "teal",
            "retro"
        ],
        "colors": [
            "f8f5e4",
            "f97300",
            "0e3047",
            "10828c"
        ]
    },
    {
        "id": "dbdbeb7577cd080957ff6d02",
        "tags": [
            "purple",
            "navy",
            "orange",
            "cold"
        ],
        "colors": [
            "dbdbeb",
            "7577cd",
            "080957",
            "ff6d02"
        ]
    },
    {
        "id": "1684a709a599f6ec72f6f6f6",
        "tags": [
            "blue",
            "green",
            "yellow",
            "white",
            "kids"
        ],
        "colors": [
            "1684a7",
            "09a599",
            "f6ec72",
            "f6f6f6"
        ]
    },
    {
        "id": "6a759b21273db9d4f1f1f6f8",
        "tags": [
            "navy",
            "black",
            "blue",
            "grey",
            "cold",
            "winter"
        ],
        "colors": [
            "6a759b",
            "21273d",
            "b9d4f1",
            "f1f6f8"
        ]
    },
    {
        "id": "2e3b3e50666bf9b8befd6378",
        "tags": [
            "grey",
            "pink",
            "vintage"
        ],
        "colors": [
            "2e3b3e",
            "50666b",
            "f9b8be",
            "fd6378"
        ]
    },
    {
        "id": "dcedc2ffd3b5ffaaa6ff8c94",
        "tags": [
            "sage",
            "peach",
            "red",
            "vintage",
            "pastel",
            "food"
        ],
        "colors": [
            "dcedc2",
            "ffd3b5",
            "ffaaa6",
            "ff8c94"
        ]
    },
    {
        "id": "f1e58a4c537471647cd0f0f7",
        "tags": [
            "yellow",
            "navy",
            "grey",
            "blue",
            "vintage"
        ],
        "colors": [
            "f1e58a",
            "4c5374",
            "71647c",
            "d0f0f7"
        ]
    },
    {
        "id": "222222045757044343e4e4e4",
        "tags": [
            "black",
            "teal",
            "grey",
            "dark",
            "night"
        ],
        "colors": [
            "222222",
            "045757",
            "044343",
            "e4e4e4"
        ]
    },
    {
        "id": "3f3038fdf6fafdaed8f361af",
        "tags": [
            "black",
            "white",
            "pink",
            "wedding"
        ],
        "colors": [
            "3f3038",
            "fdf6fa",
            "fdaed8",
            "f361af"
        ]
    },
    {
        "id": "466551368c727ecba1e7eed2",
        "tags": [
            "green"
        ],
        "colors": [
            "466551",
            "368c72",
            "7ecba1",
            "e7eed2"
        ]
    },
    {
        "id": "f1684e85c8ddd3e0e2e9f6f5",
        "tags": [
            "orange",
            "blue",
            "grey",
            "kids"
        ],
        "colors": [
            "f1684e",
            "85c8dd",
            "d3e0e2",
            "e9f6f5"
        ]
    },
    {
        "id": "e8f79a49d2923b445b383746",
        "tags": [
            "yellow",
            "green",
            "black"
        ],
        "colors": [
            "e8f79a",
            "49d292",
            "3b445b",
            "383746"
        ]
    },
    {
        "id": "f9f9f9efe94b9f1861631357",
        "tags": [
            "white",
            "yellow",
            "maroon",
            "purple"
        ],
        "colors": [
            "f9f9f9",
            "efe94b",
            "9f1861",
            "631357"
        ]
    },
    {
        "id": "f48fb1f06292ad1457880e4f",
        "tags": [
            "pink",
            "purple",
            "red",
            "maroon",
            "gradient"
        ],
        "colors": [
            "f48fb1",
            "f06292",
            "ad1457",
            "880e4f"
        ]
    },
    {
        "id": "fcf4d98ed2c900aaa0d55b3e",
        "tags": [
            "beige",
            "teal",
            "orange",
            "kids"
        ],
        "colors": [
            "fcf4d9",
            "8ed2c9",
            "00aaa0",
            "d55b3e"
        ]
    },
    {
        "id": "560764bb8fa9d8cbbbeeeeee",
        "tags": [
            "purple",
            "beige",
            "grey",
            "wedding",
            "gradient"
        ],
        "colors": [
            "560764",
            "bb8fa9",
            "d8cbbb",
            "eeeeee"
        ]
    },
    {
        "id": "fc345c49beb7afffdfeafff7",
        "tags": [
            "red",
            "teal",
            "mint",
            "white",
            "spring",
            "light"
        ],
        "colors": [
            "fc345c",
            "49beb7",
            "afffdf",
            "eafff7"
        ]
    },
    {
        "id": "1b4b36538f6aaebd77e0e7f1",
        "tags": [
            "green",
            "grey",
            "nature"
        ],
        "colors": [
            "1b4b36",
            "538f6a",
            "aebd77",
            "e0e7f1"
        ]
    },
    {
        "id": "2a363bcf4647f5d061f8f6f6",
        "tags": [
            "black",
            "red",
            "yellow",
            "white"
        ],
        "colors": [
            "2a363b",
            "cf4647",
            "f5d061",
            "f8f6f6"
        ]
    },
    {
        "id": "33425b3498dbfcc29aecf0f1",
        "tags": [
            "navy",
            "blue",
            "orange",
            "grey"
        ],
        "colors": [
            "33425b",
            "3498db",
            "fcc29a",
            "ecf0f1"
        ]
    },
    {
        "id": "1d3e53254b62476d7c77abb7",
        "tags": [
            "navy",
            "dark",
            "winter",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "1d3e53",
            "254b62",
            "476d7c",
            "77abb7"
        ]
    },
    {
        "id": "fbfbfbb1d056e0ff59ffa33e",
        "tags": [
            "white",
            "green",
            "orange",
            "light",
            "happy"
        ],
        "colors": [
            "fbfbfb",
            "b1d056",
            "e0ff59",
            "ffa33e"
        ]
    },
    {
        "id": "22213d4e318824babceaef9b",
        "tags": [
            "black",
            "purple",
            "teal",
            "yellow",
            "space"
        ],
        "colors": [
            "22213d",
            "4e3188",
            "24babc",
            "eaef9b"
        ]
    },
    {
        "id": "f4e1e1f98903c627274c3232",
        "tags": [
            "pink",
            "orange",
            "red",
            "brown",
            "fall"
        ],
        "colors": [
            "f4e1e1",
            "f98903",
            "c62727",
            "4c3232"
        ]
    },
    {
        "id": "1c1124693e52badf96f7ffcd",
        "tags": [
            "black",
            "green",
            "nature"
        ],
        "colors": [
            "1c1124",
            "693e52",
            "badf96",
            "f7ffcd"
        ]
    },
    {
        "id": "7eb19f0c8282ef9037edddbd",
        "tags": [
            "teal",
            "orange",
            "beige"
        ],
        "colors": [
            "7eb19f",
            "0c8282",
            "ef9037",
            "edddbd"
        ]
    },
    {
        "id": "3038412e4750f6c90ef7f7f7",
        "tags": [
            "black",
            "yellow",
            "white",
            "night"
        ],
        "colors": [
            "303841",
            "2e4750",
            "f6c90e",
            "f7f7f7"
        ]
    },
    {
        "id": "fffdeff1f1f1e70000c50000",
        "tags": [
            "white",
            "grey",
            "red",
            "maroon"
        ],
        "colors": [
            "fffdef",
            "f1f1f1",
            "e70000",
            "c50000"
        ]
    },
    {
        "id": "8aacff626fe66d42c7e85b48",
        "tags": [
            "blue",
            "purple",
            "orange"
        ],
        "colors": [
            "8aacff",
            "626fe6",
            "6d42c7",
            "e85b48"
        ]
    },
    {
        "id": "eeeeeeea92153a4750303841",
        "tags": [
            "grey",
            "orange",
            "space"
        ],
        "colors": [
            "eeeeee",
            "ea9215",
            "3a4750",
            "303841"
        ]
    },
    {
        "id": "45171df03861ff847cfecea8",
        "tags": [
            "maroon",
            "red",
            "orange",
            "peach",
            "beige",
            "warm"
        ],
        "colors": [
            "45171d",
            "f03861",
            "ff847c",
            "fecea8"
        ]
    },
    {
        "id": "fffceaa5f2e78983f33a0077",
        "tags": [
            "yellow",
            "teal",
            "purple",
            "retro",
            "happy"
        ],
        "colors": [
            "fffcea",
            "a5f2e7",
            "8983f3",
            "3a0077"
        ]
    },
    {
        "id": "d8dfe271adb5176d810d3446",
        "tags": [
            "grey",
            "teal",
            "navy",
            "winter",
            "cold",
            "sea"
        ],
        "colors": [
            "d8dfe2",
            "71adb5",
            "176d81",
            "0d3446"
        ]
    },
    {
        "id": "432c5153547454a4afecbc55",
        "tags": [
            "purple",
            "teal",
            "orange",
            "dark"
        ],
        "colors": [
            "432c51",
            "535474",
            "54a4af",
            "ecbc55"
        ]
    },
    {
        "id": "f9f3e6e2dcd5e8aa8c5e616a",
        "tags": [
            "beige",
            "grey",
            "orange",
            "coffee",
            "skin",
            "warm"
        ],
        "colors": [
            "f9f3e6",
            "e2dcd5",
            "e8aa8c",
            "5e616a"
        ]
    },
    {
        "id": "ffecbaff8d68a10054001f52",
        "tags": [
            "yellow",
            "orange",
            "maroon",
            "navy",
            "sunset",
            "fall"
        ],
        "colors": [
            "ffecba",
            "ff8d68",
            "a10054",
            "001f52"
        ]
    },
    {
        "id": "0730592866ab5fbdc5d8d95c",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "winter",
            "sea"
        ],
        "colors": [
            "073059",
            "2866ab",
            "5fbdc5",
            "d8d95c"
        ]
    },
    {
        "id": "ffdedef7f3cec5ecbe4797b1",
        "tags": [
            "pink",
            "peach",
            "yellow",
            "green",
            "blue",
            "light",
            "spring",
            "pastel",
            "kids",
            "happy"
        ],
        "colors": [
            "ffdede",
            "f7f3ce",
            "c5ecbe",
            "4797b1"
        ]
    },
    {
        "id": "3e3e3e40555968868cededed",
        "tags": [
            "black",
            "grey",
            "teal",
            "winter",
            "night"
        ],
        "colors": [
            "3e3e3e",
            "405559",
            "68868c",
            "ededed"
        ]
    },
    {
        "id": "fc8a15f6f6f61ee494009378",
        "tags": [
            "orange",
            "white",
            "green",
            "light",
            "kids"
        ],
        "colors": [
            "fc8a15",
            "f6f6f6",
            "1ee494",
            "009378"
        ]
    },
    {
        "id": "febfb3e1396c96d38cd0f9b1",
        "tags": [
            "peach",
            "red",
            "green",
            "food",
            "kids"
        ],
        "colors": [
            "febfb3",
            "e1396c",
            "96d38c",
            "d0f9b1"
        ]
    },
    {
        "id": "d3d6db3a4750303841be3144",
        "tags": [
            "grey",
            "black",
            "red",
            "wedding",
            "winter",
            "night"
        ],
        "colors": [
            "d3d6db",
            "3a4750",
            "303841",
            "be3144"
        ]
    },
    {
        "id": "c2faf1f6f6f6dfeff0295e6a",
        "tags": [
            "teal",
            "grey",
            "blue",
            "cold",
            "light"
        ],
        "colors": [
            "c2faf1",
            "f6f6f6",
            "dfeff0",
            "295e6a"
        ]
    },
    {
        "id": "eae7edb793e6646ecb3532a7",
        "tags": [
            "grey",
            "purple",
            "blue",
            "cold"
        ],
        "colors": [
            "eae7ed",
            "b793e6",
            "646ecb",
            "3532a7"
        ]
    },
    {
        "id": "ff6a389ed0e05c868e19483f",
        "tags": [
            "orange",
            "blue",
            "teal"
        ],
        "colors": [
            "ff6a38",
            "9ed0e0",
            "5c868e",
            "19483f"
        ]
    },
    {
        "id": "fffb85ffd464fa5b755a3662",
        "tags": [
            "yellow",
            "pink",
            "purple"
        ],
        "colors": [
            "fffb85",
            "ffd464",
            "fa5b75",
            "5a3662"
        ]
    },
    {
        "id": "205d67639a67d8ebb5d9bf77",
        "tags": [
            "blue",
            "green",
            "beige",
            "vintage",
            "nature"
        ],
        "colors": [
            "205d67",
            "639a67",
            "d8ebb5",
            "d9bf77"
        ]
    },
    {
        "id": "f5f7fa5be7c44fc1e97a57d1",
        "tags": [
            "white",
            "grey",
            "teal",
            "blue",
            "purple",
            "retro",
            "kids"
        ],
        "colors": [
            "f5f7fa",
            "5be7c4",
            "4fc1e9",
            "7a57d1"
        ]
    },
    {
        "id": "ff520000335504536cadaca7",
        "tags": [
            "orange",
            "navy",
            "blue",
            "grey",
            "space"
        ],
        "colors": [
            "ff5200",
            "003355",
            "04536c",
            "adaca7"
        ]
    },
    {
        "id": "defcf9cadefcc3bef0cca8e9",
        "tags": [
            "teal",
            "blue",
            "purple",
            "pastel",
            "light",
            "kids",
            "sky"
        ],
        "colors": [
            "defcf9",
            "cadefc",
            "c3bef0",
            "cca8e9"
        ]
    },
    {
        "id": "31588a638ccc90b2e4eacf79",
        "tags": [
            "navy",
            "blue",
            "yellow"
        ],
        "colors": [
            "31588a",
            "638ccc",
            "90b2e4",
            "eacf79"
        ]
    },
    {
        "id": "2f1b419f1e49fecd51f2f2f2",
        "tags": [
            "maroon",
            "yellow",
            "grey",
            "retro",
            "space"
        ],
        "colors": [
            "2f1b41",
            "9f1e49",
            "fecd51",
            "f2f2f2"
        ]
    },
    {
        "id": "11cbd79feed1fff6a2f60c86",
        "tags": [
            "blue",
            "teal",
            "yellow",
            "pink",
            "spring",
            "light",
            "happy",
            "rainbow"
        ],
        "colors": [
            "11cbd7",
            "9feed1",
            "fff6a2",
            "f60c86"
        ]
    },
    {
        "id": "99f0cac9fdd7fdffe78c7676",
        "tags": [
            "mint",
            "yellow",
            "brown",
            "earth"
        ],
        "colors": [
            "99f0ca",
            "c9fdd7",
            "fdffe7",
            "8c7676"
        ]
    },
    {
        "id": "1516801c44ac375fc0f1fea4",
        "tags": [
            "navy",
            "blue",
            "yellow",
            "cold"
        ],
        "colors": [
            "151680",
            "1c44ac",
            "375fc0",
            "f1fea4"
        ]
    },
    {
        "id": "d2d4d67d8df65a4db2ff771b",
        "tags": [
            "grey",
            "blue",
            "orange"
        ],
        "colors": [
            "d2d4d6",
            "7d8df6",
            "5a4db2",
            "ff771b"
        ]
    },
    {
        "id": "b9f9ffdafdfff7e590f5cd6d",
        "tags": [
            "blue",
            "yellow",
            "summer",
            "light"
        ],
        "colors": [
            "b9f9ff",
            "dafdff",
            "f7e590",
            "f5cd6d"
        ]
    },
    {
        "id": "222831393e460092caeeeeee",
        "tags": [
            "black",
            "grey",
            "blue",
            "winter",
            "night"
        ],
        "colors": [
            "222831",
            "393e46",
            "0092ca",
            "eeeeee"
        ]
    },
    {
        "id": "f6fea1ffb270f08e6bff7575",
        "tags": [
            "yellow",
            "orange",
            "peach",
            "red",
            "gold",
            "happy",
            "warm"
        ],
        "colors": [
            "f6fea1",
            "ffb270",
            "f08e6b",
            "ff7575"
        ]
    },
    {
        "id": "dafaf8d6e1a5027b7e2a014b",
        "tags": [
            "teal",
            "navy",
            "winter",
            "vintage"
        ],
        "colors": [
            "dafaf8",
            "d6e1a5",
            "027b7e",
            "2a014b"
        ]
    },
    {
        "id": "f49393f21368aa236d261d1d",
        "tags": [
            "peach",
            "red",
            "purple",
            "black"
        ],
        "colors": [
            "f49393",
            "f21368",
            "aa236d",
            "261d1d"
        ]
    },
    {
        "id": "22c7a92db6a3fccf4dfef3cc",
        "tags": [
            "teal",
            "yellow",
            "happy"
        ],
        "colors": [
            "22c7a9",
            "2db6a3",
            "fccf4d",
            "fef3cc"
        ]
    },
    {
        "id": "691a409e3668f6a9cefde3f0",
        "tags": [
            "maroon",
            "purple",
            "pink",
            "gradient"
        ],
        "colors": [
            "691a40",
            "9e3668",
            "f6a9ce",
            "fde3f0"
        ]
    },
    {
        "id": "4b4a5aa55540e79a58e1d5d2",
        "tags": [
            "brown",
            "orange",
            "grey",
            "fall",
            "coffee",
            "earth"
        ],
        "colors": [
            "4b4a5a",
            "a55540",
            "e79a58",
            "e1d5d2"
        ]
    },
    {
        "id": "fafafae8f1f5005691004a7c",
        "tags": [
            "white",
            "blue",
            "navy",
            "cold",
            "winter",
            "wedding"
        ],
        "colors": [
            "fafafa",
            "e8f1f5",
            "005691",
            "004a7c"
        ]
    },
    {
        "id": "f4f4ec76e2f4615dec301781",
        "tags": [
            "grey",
            "teal",
            "blue",
            "navy",
            "cold",
            "space"
        ],
        "colors": [
            "f4f4ec",
            "76e2f4",
            "615dec",
            "301781"
        ]
    },
    {
        "id": "a8e6cfdcedc1ffd3b6ffaaa5",
        "tags": [
            "teal",
            "green",
            "orange",
            "peach",
            "pastel",
            "kids",
            "food"
        ],
        "colors": [
            "a8e6cf",
            "dcedc1",
            "ffd3b6",
            "ffaaa5"
        ]
    },
    {
        "id": "f3f6f630e3ca11999e40514e",
        "tags": [
            "grey",
            "white",
            "teal"
        ],
        "colors": [
            "f3f6f6",
            "30e3ca",
            "11999e",
            "40514e"
        ]
    },
    {
        "id": "3d262a127c56eab64decf3f6",
        "tags": [
            "brown",
            "green",
            "orange",
            "white",
            "earth",
            "nature"
        ],
        "colors": [
            "3d262a",
            "127c56",
            "eab64d",
            "ecf3f6"
        ]
    },
    {
        "id": "2a2b5f393c833dc4d044d9e6",
        "tags": [
            "navy",
            "blue",
            "cold",
            "sea"
        ],
        "colors": [
            "2a2b5f",
            "393c83",
            "3dc4d0",
            "44d9e6"
        ]
    },
    {
        "id": "ff4545ff9867ffbf87ffedb2",
        "tags": [
            "red",
            "orange",
            "yellow",
            "warm",
            "kids"
        ],
        "colors": [
            "ff4545",
            "ff9867",
            "ffbf87",
            "ffedb2"
        ]
    },
    {
        "id": "e7f0d2d2ea9babcb8983b271",
        "tags": [
            "green",
            "cream",
            "nature"
        ],
        "colors": [
            "e7f0d2",
            "d2ea9b",
            "abcb89",
            "83b271"
        ]
    },
    {
        "id": "921224bce0daebf5eebdc6b8",
        "tags": [
            "red",
            "maroon",
            "blue",
            "grey",
            "vintage",
            "wedding"
        ],
        "colors": [
            "921224",
            "bce0da",
            "ebf5ee",
            "bdc6b8"
        ]
    },
    {
        "id": "f8fdc3facbf8efa7f3f677f7",
        "tags": [
            "yellow",
            "pink",
            "light",
            "happy"
        ],
        "colors": [
            "f8fdc3",
            "facbf8",
            "efa7f3",
            "f677f7"
        ]
    },
    {
        "id": "ddf5f7c0d9e544679f3b577d",
        "tags": [
            "blue",
            "navy",
            "cold",
            "sky"
        ],
        "colors": [
            "ddf5f7",
            "c0d9e5",
            "44679f",
            "3b577d"
        ]
    },
    {
        "id": "eceff400ad7cfbd490475762",
        "tags": [
            "grey",
            "green",
            "orange",
            "retro"
        ],
        "colors": [
            "eceff4",
            "00ad7c",
            "fbd490",
            "475762"
        ]
    },
    {
        "id": "14182921294cf2dea8f9f2d7",
        "tags": [
            "black",
            "navy",
            "beige",
            "wedding",
            "night"
        ],
        "colors": [
            "141829",
            "21294c",
            "f2dea8",
            "f9f2d7"
        ]
    },
    {
        "id": "fff6fbffbee3fc5bb6ff0592",
        "tags": [
            "white",
            "pink",
            "light",
            "wedding"
        ],
        "colors": [
            "fff6fb",
            "ffbee3",
            "fc5bb6",
            "ff0592"
        ]
    },
    {
        "id": "f2eee3baaf92785e4dff8426",
        "tags": [
            "beige",
            "brown",
            "orange",
            "fall",
            "coffee",
            "vintage",
            "warm"
        ],
        "colors": [
            "f2eee3",
            "baaf92",
            "785e4d",
            "ff8426"
        ]
    },
    {
        "id": "428b46b7b56ed6d88be9eab4",
        "tags": [
            "green",
            "brown",
            "beige",
            "nature",
            "summer"
        ],
        "colors": [
            "428b46",
            "b7b56e",
            "d6d88b",
            "e9eab4"
        ]
    },
    {
        "id": "7386d5a0b6f5ffefefff2c2c",
        "tags": [
            "blue",
            "white",
            "red"
        ],
        "colors": [
            "7386d5",
            "a0b6f5",
            "ffefef",
            "ff2c2c"
        ]
    },
    {
        "id": "0962ea0e7cf40aa0f6faf15d",
        "tags": [
            "blue",
            "yellow",
            "happy"
        ],
        "colors": [
            "0962ea",
            "0e7cf4",
            "0aa0f6",
            "faf15d"
        ]
    },
    {
        "id": "f9f8ebffe1b67a9eb1415865",
        "tags": [
            "beige",
            "blue",
            "navy"
        ],
        "colors": [
            "f9f8eb",
            "ffe1b6",
            "7a9eb1",
            "415865"
        ]
    },
    {
        "id": "f70776c3195d680747141010",
        "tags": [
            "red",
            "pink",
            "maroon",
            "purple",
            "black",
            "dark"
        ],
        "colors": [
            "f70776",
            "c3195d",
            "680747",
            "141010"
        ]
    },
    {
        "id": "2e2b2b388186a5e9e1fdf6f6",
        "tags": [
            "black",
            "teal",
            "white",
            "space",
            "sea"
        ],
        "colors": [
            "2e2b2b",
            "388186",
            "a5e9e1",
            "fdf6f6"
        ]
    },
    {
        "id": "fffe9fffd480fca180f56262",
        "tags": [
            "orange",
            "peach",
            "red",
            "warm",
            "happy"
        ],
        "colors": [
            "fffe9f",
            "ffd480",
            "fca180",
            "f56262"
        ]
    },
    {
        "id": "f2f9f1ddeedfb6cdbd5c715e",
        "tags": [
            "white",
            "grey",
            "sage",
            "vintage",
            "cream"
        ],
        "colors": [
            "f2f9f1",
            "ddeedf",
            "b6cdbd",
            "5c715e"
        ]
    },
    {
        "id": "c7f5fefcc8f8eab4f8f3f798",
        "tags": [
            "blue",
            "pink",
            "purple",
            "yellow",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "c7f5fe",
            "fcc8f8",
            "eab4f8",
            "f3f798"
        ]
    },
    {
        "id": "525252414141313131ec625f",
        "tags": [
            "grey",
            "black",
            "red",
            "dark",
            "night"
        ],
        "colors": [
            "525252",
            "414141",
            "313131",
            "ec625f"
        ]
    },
    {
        "id": "f0eec99ee6cf50c9ba4ba2ac",
        "tags": [
            "yellow",
            "beige",
            "teal",
            "pastel",
            "summer"
        ],
        "colors": [
            "f0eec9",
            "9ee6cf",
            "50c9ba",
            "4ba2ac"
        ]
    },
    {
        "id": "fafafaff6699c54c82512e67",
        "tags": [
            "white",
            "pink",
            "purple"
        ],
        "colors": [
            "fafafa",
            "ff6699",
            "c54c82",
            "512e67"
        ]
    },
    {
        "id": "7effdbb693fe8c82fcff9de2",
        "tags": [
            "mint",
            "purple",
            "pink",
            "neon",
            "kids"
        ],
        "colors": [
            "7effdb",
            "b693fe",
            "8c82fc",
            "ff9de2"
        ]
    },
    {
        "id": "1d7d81213458887575f6e8e8",
        "tags": [
            "teal",
            "navy",
            "brown",
            "vintage"
        ],
        "colors": [
            "1d7d81",
            "213458",
            "887575",
            "f6e8e8"
        ]
    },
    {
        "id": "57d1c9ed5485fffbcbffe869",
        "tags": [
            "teal",
            "pink",
            "yellow",
            "kids",
            "happy"
        ],
        "colors": [
            "57d1c9",
            "ed5485",
            "fffbcb",
            "ffe869"
        ]
    },
    {
        "id": "dff5f287dfd646b7b92f9296",
        "tags": [
            "teal",
            "kids",
            "winter"
        ],
        "colors": [
            "dff5f2",
            "87dfd6",
            "46b7b9",
            "2f9296"
        ]
    },
    {
        "id": "f3f3f3ffdd67ffcd384a4a4a",
        "tags": [
            "grey",
            "yellow",
            "gold"
        ],
        "colors": [
            "f3f3f3",
            "ffdd67",
            "ffcd38",
            "4a4a4a"
        ]
    },
    {
        "id": "280b4561105ec84771ffe98a",
        "tags": [
            "purple",
            "red",
            "yellow",
            "dark",
            "sunset"
        ],
        "colors": [
            "280b45",
            "61105e",
            "c84771",
            "ffe98a"
        ]
    },
    {
        "id": "8ef6e49896f1d59bf6edb1f1",
        "tags": [
            "mint",
            "purple",
            "pink",
            "kids"
        ],
        "colors": [
            "8ef6e4",
            "9896f1",
            "d59bf6",
            "edb1f1"
        ]
    },
    {
        "id": "a44a4add8968e4c478e8e46d",
        "tags": [
            "red",
            "orange",
            "yellow",
            "warm",
            "gold"
        ],
        "colors": [
            "a44a4a",
            "dd8968",
            "e4c478",
            "e8e46d"
        ]
    },
    {
        "id": "eeeeee59569df25292fea096",
        "tags": [
            "grey",
            "navy",
            "pink",
            "peach",
            "retro"
        ],
        "colors": [
            "eeeeee",
            "59569d",
            "f25292",
            "fea096"
        ]
    },
    {
        "id": "d3f6d1a7d7c574b49b5c8d89",
        "tags": [
            "green",
            "teal",
            "nature"
        ],
        "colors": [
            "d3f6d1",
            "a7d7c5",
            "74b49b",
            "5c8d89"
        ]
    },
    {
        "id": "ff6f6ffff46ef6f6f6a58bff",
        "tags": [
            "red",
            "yellow",
            "white",
            "purple",
            "light",
            "kids",
            "neon"
        ],
        "colors": [
            "ff6f6f",
            "fff46e",
            "f6f6f6",
            "a58bff"
        ]
    },
    {
        "id": "2f1b41872341be3144f05941",
        "tags": [
            "maroon",
            "red",
            "orange",
            "dark",
            "night",
            "halloween",
            "warm"
        ],
        "colors": [
            "2f1b41",
            "872341",
            "be3144",
            "f05941"
        ]
    },
    {
        "id": "dddddd574e6d43405d4b586e",
        "tags": [
            "grey",
            "winter",
            "cold",
            "night"
        ],
        "colors": [
            "dddddd",
            "574e6d",
            "43405d",
            "4b586e"
        ]
    },
    {
        "id": "1fad9fcd3131ab1212f6e4b5",
        "tags": [
            "teal",
            "red",
            "maroon",
            "beige",
            "kids"
        ],
        "colors": [
            "1fad9f",
            "cd3131",
            "ab1212",
            "f6e4b5"
        ]
    },
    {
        "id": "fc993cffe775bd46828c2057",
        "tags": [
            "orange",
            "yellow",
            "purple",
            "maroon"
        ],
        "colors": [
            "fc993c",
            "ffe775",
            "bd4682",
            "8c2057"
        ]
    },
    {
        "id": "fafbd4b2ebf9aea1ea8c54a1",
        "tags": [
            "yellow",
            "blue",
            "purple",
            "wedding",
            "retro"
        ],
        "colors": [
            "fafbd4",
            "b2ebf9",
            "aea1ea",
            "8c54a1"
        ]
    },
    {
        "id": "dde8b9e8d2aecb8589796465",
        "tags": [
            "sage",
            "beige",
            "brown",
            "pastel",
            "vintage",
            "earth",
            "food"
        ],
        "colors": [
            "dde8b9",
            "e8d2ae",
            "cb8589",
            "796465"
        ]
    },
    {
        "id": "070f4e2772db3ab1c8f5ebeb",
        "tags": [
            "navy",
            "blue",
            "teal",
            "grey",
            "cold",
            "space",
            "gradient"
        ],
        "colors": [
            "070f4e",
            "2772db",
            "3ab1c8",
            "f5ebeb"
        ]
    },
    {
        "id": "c8f4dea4e5d966c6ba649dad",
        "tags": [
            "green",
            "teal",
            "kids"
        ],
        "colors": [
            "c8f4de",
            "a4e5d9",
            "66c6ba",
            "649dad"
        ]
    },
    {
        "id": "bc4f4fe98b50f3cd97fef2a0",
        "tags": [
            "red",
            "orange",
            "beige",
            "yellow",
            "gold",
            "sunset",
            "warm",
            "gradient"
        ],
        "colors": [
            "bc4f4f",
            "e98b50",
            "f3cd97",
            "fef2a0"
        ]
    },
    {
        "id": "f9f8edf4e7d30881a31f4e5f",
        "tags": [
            "beige",
            "blue",
            "navy",
            "wedding"
        ],
        "colors": [
            "f9f8ed",
            "f4e7d3",
            "0881a3",
            "1f4e5f"
        ]
    },
    {
        "id": "d7aef394f6f2f7f680fbd0f5",
        "tags": [
            "purple",
            "teal",
            "yellow",
            "pink",
            "spring",
            "light",
            "kids",
            "neon"
        ],
        "colors": [
            "d7aef3",
            "94f6f2",
            "f7f680",
            "fbd0f5"
        ]
    },
    {
        "id": "ebe9f6453c386a5c55f66e00",
        "tags": [
            "grey",
            "brown",
            "orange",
            "coffee"
        ],
        "colors": [
            "ebe9f6",
            "453c38",
            "6a5c55",
            "f66e00"
        ]
    },
    {
        "id": "ddfee428cc9e196b69132f2b",
        "tags": [
            "mint",
            "green",
            "teal"
        ],
        "colors": [
            "ddfee4",
            "28cc9e",
            "196b69",
            "132f2b"
        ]
    },
    {
        "id": "ca3e6bfa83839dd3ccffe4b3",
        "tags": [
            "red",
            "peach",
            "teal",
            "beige",
            "happy"
        ],
        "colors": [
            "ca3e6b",
            "fa8383",
            "9dd3cc",
            "ffe4b3"
        ]
    },
    {
        "id": "f6f5f5e3e3e33bb4c1048998",
        "tags": [
            "grey",
            "teal",
            "cold"
        ],
        "colors": [
            "f6f5f5",
            "e3e3e3",
            "3bb4c1",
            "048998"
        ]
    },
    {
        "id": "ff006cd62b70973961623448",
        "tags": [
            "red",
            "maroon"
        ],
        "colors": [
            "ff006c",
            "d62b70",
            "973961",
            "623448"
        ]
    },
    {
        "id": "233142455d7af95959e3e3e3",
        "tags": [
            "black",
            "navy",
            "red",
            "grey",
            "space"
        ],
        "colors": [
            "233142",
            "455d7a",
            "f95959",
            "e3e3e3"
        ]
    },
    {
        "id": "f5fac8a5f0e482c7eb8ea1f0",
        "tags": [
            "yellow",
            "blue",
            "light",
            "happy"
        ],
        "colors": [
            "f5fac8",
            "a5f0e4",
            "82c7eb",
            "8ea1f0"
        ]
    },
    {
        "id": "4b2c34447878779977ddddbb",
        "tags": [
            "brown",
            "teal",
            "sage",
            "earth",
            "gradient",
            "sea"
        ],
        "colors": [
            "4b2c34",
            "447878",
            "779977",
            "ddddbb"
        ]
    },
    {
        "id": "f7f09bff5200c3120777024d",
        "tags": [
            "yellow",
            "orange",
            "red",
            "maroon",
            "purple",
            "warm",
            "gold"
        ],
        "colors": [
            "f7f09b",
            "ff5200",
            "c31207",
            "77024d"
        ]
    },
    {
        "id": "146c780e91a17dce94efede7",
        "tags": [
            "blue",
            "green",
            "grey",
            "cold"
        ],
        "colors": [
            "146c78",
            "0e91a1",
            "7dce94",
            "efede7"
        ]
    },
    {
        "id": "faee1cf3558e9c1de7581b98",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "rainbow"
        ],
        "colors": [
            "faee1c",
            "f3558e",
            "9c1de7",
            "581b98"
        ]
    },
    {
        "id": "a9eee6fefaecf9a1bc625772",
        "tags": [
            "teal",
            "yellow",
            "beige",
            "pink",
            "kids"
        ],
        "colors": [
            "a9eee6",
            "fefaec",
            "f9a1bc",
            "625772"
        ]
    },
    {
        "id": "1b805755a44ed7c37aede9a3",
        "tags": [
            "green",
            "beige",
            "yellow",
            "nature",
            "food"
        ],
        "colors": [
            "1b8057",
            "55a44e",
            "d7c37a",
            "ede9a3"
        ]
    },
    {
        "id": "3d1860643579bb99cdf5edf7",
        "tags": [
            "purple",
            "white",
            "cold",
            "winter"
        ],
        "colors": [
            "3d1860",
            "643579",
            "bb99cd",
            "f5edf7"
        ]
    },
    {
        "id": "e67676f2f062a9e6e67692e4",
        "tags": [
            "red",
            "yellow",
            "blue",
            "rainbow",
            "kids"
        ],
        "colors": [
            "e67676",
            "f2f062",
            "a9e6e6",
            "7692e4"
        ]
    },
    {
        "id": "1b3c5945617311bfaef2f2f0",
        "tags": [
            "navy",
            "teal",
            "white",
            "grey",
            "cold",
            "space"
        ],
        "colors": [
            "1b3c59",
            "456173",
            "11bfae",
            "f2f2f0"
        ]
    },
    {
        "id": "bff4ed280f34e41655b30753",
        "tags": [
            "teal",
            "black",
            "red",
            "maroon",
            "space"
        ],
        "colors": [
            "bff4ed",
            "280f34",
            "e41655",
            "b30753"
        ]
    },
    {
        "id": "f3f16946c3db2d6cdf482ff7",
        "tags": [
            "yellow",
            "blue",
            "happy"
        ],
        "colors": [
            "f3f169",
            "46c3db",
            "2d6cdf",
            "482ff7"
        ]
    },
    {
        "id": "f5e1daf1f1f140a798476268",
        "tags": [
            "beige",
            "grey",
            "teal",
            "vintage"
        ],
        "colors": [
            "f5e1da",
            "f1f1f1",
            "40a798",
            "476268"
        ]
    },
    {
        "id": "511e788b2f97cf56a1fcb2bf",
        "tags": [
            "purple",
            "pink",
            "peach",
            "gradient"
        ],
        "colors": [
            "511e78",
            "8b2f97",
            "cf56a1",
            "fcb2bf"
        ]
    },
    {
        "id": "90f6d735bcbf41506b263849",
        "tags": [
            "teal",
            "grey",
            "black",
            "cold"
        ],
        "colors": [
            "90f6d7",
            "35bcbf",
            "41506b",
            "263849"
        ]
    },
    {
        "id": "ecfffbb4f1f12d767f1e6262",
        "tags": [
            "blue",
            "teal",
            "cold"
        ],
        "colors": [
            "ecfffb",
            "b4f1f1",
            "2d767f",
            "1e6262"
        ]
    },
    {
        "id": "eeeeeefcc31494ac3c295ba7",
        "tags": [
            "grey",
            "yellow",
            "green",
            "blue",
            "spring",
            "kids"
        ],
        "colors": [
            "eeeeee",
            "fcc314",
            "94ac3c",
            "295ba7"
        ]
    },
    {
        "id": "f2e9d0eaceb4e79e85bb5a5a",
        "tags": [
            "beige",
            "orange",
            "red",
            "pastel",
            "vintage",
            "warm",
            "skin",
            "coffee",
            "fall",
            "food",
            "gradient"
        ],
        "colors": [
            "f2e9d0",
            "eaceb4",
            "e79e85",
            "bb5a5a"
        ]
    },
    {
        "id": "4027855f4e9efafb97fcc97b",
        "tags": [
            "purple",
            "yellow",
            "orange"
        ],
        "colors": [
            "402785",
            "5f4e9e",
            "fafb97",
            "fcc97b"
        ]
    },
    {
        "id": "ebfffac6fce56ef3d60dceda",
        "tags": [
            "teal",
            "green",
            "blue",
            "light",
            "cold",
            "sky"
        ],
        "colors": [
            "ebfffa",
            "c6fce5",
            "6ef3d6",
            "0dceda"
        ]
    },
    {
        "id": "f4f4f4fb9935b90b0b8c0909",
        "tags": [
            "grey",
            "white",
            "orange",
            "red",
            "maroon",
            "fall"
        ],
        "colors": [
            "f4f4f4",
            "fb9935",
            "b90b0b",
            "8c0909"
        ]
    },
    {
        "id": "ffabe5c7f5ffd89ffff6fcae",
        "tags": [
            "pink",
            "blue",
            "purple",
            "yellow",
            "spring",
            "light",
            "neon",
            "kids"
        ],
        "colors": [
            "ffabe5",
            "c7f5ff",
            "d89fff",
            "f6fcae"
        ]
    },
    {
        "id": "1c226b3e31ae4aa9afd1fffa",
        "tags": [
            "navy",
            "teal",
            "cold",
            "space"
        ],
        "colors": [
            "1c226b",
            "3e31ae",
            "4aa9af",
            "d1fffa"
        ]
    },
    {
        "id": "dc3737f7af1df5e180aeaf7a",
        "tags": [
            "red",
            "orange",
            "yellow",
            "fall",
            "gold",
            "warm"
        ],
        "colors": [
            "dc3737",
            "f7af1d",
            "f5e180",
            "aeaf7a"
        ]
    },
    {
        "id": "36d1c4a0eeccfff2bef6318c",
        "tags": [
            "teal",
            "mint",
            "yellow",
            "pink",
            "spring",
            "light",
            "happy"
        ],
        "colors": [
            "36d1c4",
            "a0eecc",
            "fff2be",
            "f6318c"
        ]
    },
    {
        "id": "4c698338556a273952b6fff9",
        "tags": [
            "grey",
            "black",
            "teal",
            "winter",
            "cold",
            "night"
        ],
        "colors": [
            "4c6983",
            "38556a",
            "273952",
            "b6fff9"
        ]
    },
    {
        "id": "be0eaaea2ba2fb9696f6ca97",
        "tags": [
            "purple",
            "pink",
            "peach",
            "beige",
            "spring",
            "happy",
            "gradient"
        ],
        "colors": [
            "be0eaa",
            "ea2ba2",
            "fb9696",
            "f6ca97"
        ]
    },
    {
        "id": "e0fcff90f2ff6eb6ff7098da",
        "tags": [
            "blue",
            "light",
            "cold",
            "kids"
        ],
        "colors": [
            "e0fcff",
            "90f2ff",
            "6eb6ff",
            "7098da"
        ]
    },
    {
        "id": "fbf7f7f9d00ff0ae2cf92727",
        "tags": [
            "white",
            "yellow",
            "red",
            "light",
            "gold",
            "kids"
        ],
        "colors": [
            "fbf7f7",
            "f9d00f",
            "f0ae2c",
            "f92727"
        ]
    },
    {
        "id": "1b5a7a1aa59aa6ed8ef3ffb9",
        "tags": [
            "navy",
            "teal",
            "green",
            "yellow",
            "nature",
            "gradient"
        ],
        "colors": [
            "1b5a7a",
            "1aa59a",
            "a6ed8e",
            "f3ffb9"
        ]
    },
    {
        "id": "ff9898cf455c971549470031",
        "tags": [
            "pink",
            "red",
            "maroon",
            "purple",
            "warm",
            "dark"
        ],
        "colors": [
            "ff9898",
            "cf455c",
            "971549",
            "470031"
        ]
    },
    {
        "id": "586e72fbf27c5c835a305c5c",
        "tags": [
            "grey",
            "yellow",
            "green",
            "retro"
        ],
        "colors": [
            "586e72",
            "fbf27c",
            "5c835a",
            "305c5c"
        ]
    },
    {
        "id": "eb89b5ffd7e9fffbf3fff8d2",
        "tags": [
            "pink",
            "white",
            "yellow",
            "light",
            "cream",
            "kids"
        ],
        "colors": [
            "eb89b5",
            "ffd7e9",
            "fffbf3",
            "fff8d2"
        ]
    },
    {
        "id": "f4f7f7aacfd05da0a234495e",
        "tags": [
            "white",
            "teal",
            "cold"
        ],
        "colors": [
            "f4f7f7",
            "aacfd0",
            "5da0a2",
            "34495e"
        ]
    },
    {
        "id": "7b77ff92cce1f68686ffe3b9",
        "tags": [
            "blue",
            "peach",
            "beige"
        ],
        "colors": [
            "7b77ff",
            "92cce1",
            "f68686",
            "ffe3b9"
        ]
    },
    {
        "id": "fff6f6eea1ebcb22d7891180",
        "tags": [
            "white",
            "pink",
            "purple"
        ],
        "colors": [
            "fff6f6",
            "eea1eb",
            "cb22d7",
            "891180"
        ]
    },
    {
        "id": "f6eb9a5853bc3623911c0c59",
        "tags": [
            "yellow",
            "blue",
            "navy"
        ],
        "colors": [
            "f6eb9a",
            "5853bc",
            "362391",
            "1c0c59"
        ]
    },
    {
        "id": "f03861fef2f2f5d97e7d5e3f",
        "tags": [
            "red",
            "white",
            "yellow",
            "brown",
            "vintage"
        ],
        "colors": [
            "f03861",
            "fef2f2",
            "f5d97e",
            "7d5e3f"
        ]
    },
    {
        "id": "d9f9f49cd9de86c1d45a92af",
        "tags": [
            "teal",
            "blue",
            "cold",
            "sky"
        ],
        "colors": [
            "d9f9f4",
            "9cd9de",
            "86c1d4",
            "5a92af"
        ]
    },
    {
        "id": "2aaf744ed99cd1ebfef7be7f",
        "tags": [
            "green",
            "blue",
            "orange",
            "nature"
        ],
        "colors": [
            "2aaf74",
            "4ed99c",
            "d1ebfe",
            "f7be7f"
        ]
    },
    {
        "id": "f69d9dffeab6fdffbac0ffc2",
        "tags": [
            "peach",
            "beige",
            "yellow",
            "mint",
            "green",
            "light",
            "rainbow",
            "happy"
        ],
        "colors": [
            "f69d9d",
            "ffeab6",
            "fdffba",
            "c0ffc2"
        ]
    },
    {
        "id": "253b6e1f5f8b1891acd2ecf9",
        "tags": [
            "navy",
            "blue",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "253b6e",
            "1f5f8b",
            "1891ac",
            "d2ecf9"
        ]
    },
    {
        "id": "f6faf7e7eaa8b4bb72303e27",
        "tags": [
            "white",
            "green",
            "yellow",
            "nature",
            "food"
        ],
        "colors": [
            "f6faf7",
            "e7eaa8",
            "b4bb72",
            "303e27"
        ]
    },
    {
        "id": "b80257dd356efc7fb6ffbbe1",
        "tags": [
            "maroon",
            "red",
            "pink",
            "kids"
        ],
        "colors": [
            "b80257",
            "dd356e",
            "fc7fb6",
            "ffbbe1"
        ]
    },
    {
        "id": "76d3ffd78bfffffa9dffbd74",
        "tags": [
            "blue",
            "purple",
            "yellow",
            "orange",
            "kids",
            "rainbow"
        ],
        "colors": [
            "76d3ff",
            "d78bff",
            "fffa9d",
            "ffbd74"
        ]
    },
    {
        "id": "f2f7ff0b409c10316bffce63",
        "tags": [
            "white",
            "blue",
            "navy",
            "yellow",
            "cold"
        ],
        "colors": [
            "f2f7ff",
            "0b409c",
            "10316b",
            "ffce63"
        ]
    },
    {
        "id": "1fab8962d2a29df3c4d7fbe8",
        "tags": [
            "green",
            "mint",
            "nature",
            "kids"
        ],
        "colors": [
            "1fab89",
            "62d2a2",
            "9df3c4",
            "d7fbe8"
        ]
    },
    {
        "id": "fee856ffce3ee65c7b834496",
        "tags": [
            "yellow",
            "red",
            "purple"
        ],
        "colors": [
            "fee856",
            "ffce3e",
            "e65c7b",
            "834496"
        ]
    },
    {
        "id": "07689fa2d5f2fafafaff7e67",
        "tags": [
            "blue",
            "white",
            "orange",
            "summer",
            "happy"
        ],
        "colors": [
            "07689f",
            "a2d5f2",
            "fafafa",
            "ff7e67"
        ]
    },
    {
        "id": "560764913175dd5b82fe9797",
        "tags": [
            "purple",
            "peach",
            "dark",
            "night",
            "gradient"
        ],
        "colors": [
            "560764",
            "913175",
            "dd5b82",
            "fe9797"
        ]
    },
    {
        "id": "266f893d93a33ec483d2e48e",
        "tags": [
            "blue",
            "green",
            "sea"
        ],
        "colors": [
            "266f89",
            "3d93a3",
            "3ec483",
            "d2e48e"
        ]
    },
    {
        "id": "29c6cdf6e4c4fea386f19584",
        "tags": [
            "teal",
            "beige",
            "orange",
            "pastel",
            "kids",
            "summer"
        ],
        "colors": [
            "29c6cd",
            "f6e4c4",
            "fea386",
            "f19584"
        ]
    },
    {
        "id": "ffd9e8de95ba7f4a884a266a",
        "tags": [
            "pink",
            "purple",
            "wedding",
            "gradient"
        ],
        "colors": [
            "ffd9e8",
            "de95ba",
            "7f4a88",
            "4a266a"
        ]
    },
    {
        "id": "2121213232320d737714ffec",
        "tags": [
            "black",
            "teal",
            "cold",
            "dark",
            "night",
            "space",
            "neon"
        ],
        "colors": [
            "212121",
            "323232",
            "0d7377",
            "14ffec"
        ]
    },
    {
        "id": "fd9191fddd8af5fc9e9efcb4",
        "tags": [
            "peach",
            "yellow",
            "green",
            "light",
            "kids",
            "rainbow",
            "summer",
            "happy"
        ],
        "colors": [
            "fd9191",
            "fddd8a",
            "f5fc9e",
            "9efcb4"
        ]
    },
    {
        "id": "eff7d3cedcc3a7b99e535a3b",
        "tags": [
            "yellow",
            "grey",
            "sage",
            "brown",
            "nature",
            "earth",
            "cream"
        ],
        "colors": [
            "eff7d3",
            "cedcc3",
            "a7b99e",
            "535a3b"
        ]
    },
    {
        "id": "3c3b5cd53939ffb5637b3c59",
        "tags": [
            "navy",
            "red",
            "orange",
            "halloween"
        ],
        "colors": [
            "3c3b5c",
            "d53939",
            "ffb563",
            "7b3c59"
        ]
    },
    {
        "id": "616eef09a8fa41c5d3d0f1cf",
        "tags": [
            "blue",
            "teal",
            "green",
            "cold",
            "gradient"
        ],
        "colors": [
            "616eef",
            "09a8fa",
            "41c5d3",
            "d0f1cf"
        ]
    },
    {
        "id": "658361d0dd97f8fae4f9de79",
        "tags": [
            "sage",
            "white",
            "yellow",
            "nature",
            "food",
            "kids",
            "summer"
        ],
        "colors": [
            "658361",
            "d0dd97",
            "f8fae4",
            "f9de79"
        ]
    },
    {
        "id": "2c3e5034495eecf0f1bdc3c7",
        "tags": [
            "navy",
            "grey",
            "night"
        ],
        "colors": [
            "2c3e50",
            "34495e",
            "ecf0f1",
            "bdc3c7"
        ]
    },
    {
        "id": "f3f6f690eee155b3f36356e5",
        "tags": [
            "grey",
            "teal",
            "blue",
            "cold"
        ],
        "colors": [
            "f3f6f6",
            "90eee1",
            "55b3f3",
            "6356e5"
        ]
    },
    {
        "id": "f6378fffdd00f5efe88ea5eb",
        "tags": [
            "pink",
            "yellow",
            "white",
            "blue",
            "spring"
        ],
        "colors": [
            "f6378f",
            "ffdd00",
            "f5efe8",
            "8ea5eb"
        ]
    },
    {
        "id": "388e3c8bc34adce775fff59d",
        "tags": [
            "green",
            "yellow",
            "nature",
            "happy",
            "gradient"
        ],
        "colors": [
            "388e3c",
            "8bc34a",
            "dce775",
            "fff59d"
        ]
    },
    {
        "id": "eff0f4d3d6db415f9d233b6e",
        "tags": [
            "grey",
            "blue",
            "navy",
            "winter",
            "cold"
        ],
        "colors": [
            "eff0f4",
            "d3d6db",
            "415f9d",
            "233b6e"
        ]
    },
    {
        "id": "f4f56e72e8e158b3d3418c9f",
        "tags": [
            "yellow",
            "teal",
            "blue"
        ],
        "colors": [
            "f4f56e",
            "72e8e1",
            "58b3d3",
            "418c9f"
        ]
    },
    {
        "id": "14103bf02a717ec0e46789ba",
        "tags": [
            "black",
            "pink",
            "space"
        ],
        "colors": [
            "14103b",
            "f02a71",
            "7ec0e4",
            "6789ba"
        ]
    },
    {
        "id": "eeeeee234c63379956ffc85b",
        "tags": [
            "grey",
            "navy",
            "green",
            "orange",
            "retro"
        ],
        "colors": [
            "eeeeee",
            "234c63",
            "379956",
            "ffc85b"
        ]
    },
    {
        "id": "e38ed2c756969d3978512e67",
        "tags": [
            "pink",
            "purple"
        ],
        "colors": [
            "e38ed2",
            "c75696",
            "9d3978",
            "512e67"
        ]
    },
    {
        "id": "006c9a00bebe00f3e49ff9c1",
        "tags": [
            "navy",
            "teal",
            "green",
            "mint",
            "cold",
            "sea"
        ],
        "colors": [
            "006c9a",
            "00bebe",
            "00f3e4",
            "9ff9c1"
        ]
    },
    {
        "id": "333c4a495664f6f7d3f8fceb",
        "tags": [
            "black",
            "grey",
            "yellow",
            "white",
            "space"
        ],
        "colors": [
            "333c4a",
            "495664",
            "f6f7d3",
            "f8fceb"
        ]
    },
    {
        "id": "ff8fe5fbff6476e3ff7bc7fa",
        "tags": [
            "pink",
            "yellow",
            "blue",
            "light",
            "rainbow",
            "neon",
            "kids",
            "spring"
        ],
        "colors": [
            "ff8fe5",
            "fbff64",
            "76e3ff",
            "7bc7fa"
        ]
    },
    {
        "id": "2a528a5d6ec79f71dbe9d498",
        "tags": [
            "navy",
            "blue",
            "purple",
            "beige",
            "pastel"
        ],
        "colors": [
            "2a528a",
            "5d6ec7",
            "9f71db",
            "e9d498"
        ]
    },
    {
        "id": "ffdd83e3f8ff31bccc405983",
        "tags": [
            "yellow",
            "teal",
            "navy",
            "summer"
        ],
        "colors": [
            "ffdd83",
            "e3f8ff",
            "31bccc",
            "405983"
        ]
    },
    {
        "id": "3a3a62604fdd26c6d0e6e993",
        "tags": [
            "purple",
            "teal",
            "yellow",
            "retro",
            "space"
        ],
        "colors": [
            "3a3a62",
            "604fdd",
            "26c6d0",
            "e6e993"
        ]
    },
    {
        "id": "499491a3dec9f7fed8fbd400",
        "tags": [
            "teal",
            "white",
            "yellow"
        ],
        "colors": [
            "499491",
            "a3dec9",
            "f7fed8",
            "fbd400"
        ]
    },
    {
        "id": "f70c9bcb007bd6e3ed99b0c2",
        "tags": [
            "pink",
            "purple",
            "grey"
        ],
        "colors": [
            "f70c9b",
            "cb007b",
            "d6e3ed",
            "99b0c2"
        ]
    },
    {
        "id": "f0fff3c6f1e770acb159606d",
        "tags": [
            "white",
            "teal",
            "grey",
            "winter"
        ],
        "colors": [
            "f0fff3",
            "c6f1e7",
            "70acb1",
            "59606d"
        ]
    },
    {
        "id": "b31313ff9000fdda16ffee82",
        "tags": [
            "maroon",
            "red",
            "orange",
            "yellow",
            "warm",
            "gold"
        ],
        "colors": [
            "b31313",
            "ff9000",
            "fdda16",
            "ffee82"
        ]
    },
    {
        "id": "4d12ee2f24c13fd1cbf8f6f6",
        "tags": [
            "blue",
            "navy",
            "teal",
            "white",
            "kids",
            "winter",
            "cold",
            "wedding"
        ],
        "colors": [
            "4d12ee",
            "2f24c1",
            "3fd1cb",
            "f8f6f6"
        ]
    },
    {
        "id": "34495d2c3d4fee7738f59d2a",
        "tags": [
            "black",
            "orange",
            "night"
        ],
        "colors": [
            "34495d",
            "2c3d4f",
            "ee7738",
            "f59d2a"
        ]
    },
    {
        "id": "8c767699f0cac9fdd7fdffe7",
        "tags": [
            "brown",
            "mint",
            "white",
            "light",
            "pastel",
            "earth",
            "cream",
            "kids",
            "spring",
            "nature"
        ],
        "colors": [
            "8c7676",
            "99f0ca",
            "c9fdd7",
            "fdffe7"
        ]
    },
    {
        "id": "f9f5f0f2ead3f4991a321313",
        "tags": [
            "white",
            "beige",
            "orange",
            "brown",
            "retro",
            "warm",
            "wedding",
            "coffee",
            "fall",
            "food",
            "skin"
        ],
        "colors": [
            "f9f5f0",
            "f2ead3",
            "f4991a",
            "321313"
        ]
    },
    {
        "id": "4e4e6a1f6cb070a3c4e7e8f5",
        "tags": [
            "grey",
            "blue",
            "cold",
            "night"
        ],
        "colors": [
            "4e4e6a",
            "1f6cb0",
            "70a3c4",
            "e7e8f5"
        ]
    },
    {
        "id": "f73f52ffea85f6f6f67986c7",
        "tags": [
            "red",
            "yellow",
            "white",
            "grey",
            "blue"
        ],
        "colors": [
            "f73f52",
            "ffea85",
            "f6f6f6",
            "7986c7"
        ]
    },
    {
        "id": "defbc290d26d459d72342b2b",
        "tags": [
            "green",
            "nature",
            "happy"
        ],
        "colors": [
            "defbc2",
            "90d26d",
            "459d72",
            "342b2b"
        ]
    },
    {
        "id": "f4f4f46decb911999e3c3c3c",
        "tags": [
            "grey",
            "mint",
            "green",
            "teal",
            "black",
            "cold"
        ],
        "colors": [
            "f4f4f4",
            "6decb9",
            "11999e",
            "3c3c3c"
        ]
    },
    {
        "id": "282f44e6af2ef5d061ececec",
        "tags": [
            "black",
            "yellow",
            "grey",
            "gold",
            "vintage"
        ],
        "colors": [
            "282f44",
            "e6af2e",
            "f5d061",
            "ececec"
        ]
    },
    {
        "id": "1044550a34423ad3cd7fffd6",
        "tags": [
            "navy",
            "teal",
            "mint",
            "cold",
            "space",
            "sea"
        ],
        "colors": [
            "104455",
            "0a3442",
            "3ad3cd",
            "7fffd6"
        ]
    },
    {
        "id": "d2f6fca9d2ff7984ee6730ec",
        "tags": [
            "blue",
            "cold"
        ],
        "colors": [
            "d2f6fc",
            "a9d2ff",
            "7984ee",
            "6730ec"
        ]
    },
    {
        "id": "f1ed63d97d979862ae815a8f",
        "tags": [
            "yellow",
            "red",
            "purple"
        ],
        "colors": [
            "f1ed63",
            "d97d97",
            "9862ae",
            "815a8f"
        ]
    },
    {
        "id": "ffd6b6ea7362b742425c2626",
        "tags": [
            "peach",
            "orange",
            "maroon",
            "warm",
            "gold",
            "food",
            "fall",
            "halloween"
        ],
        "colors": [
            "ffd6b6",
            "ea7362",
            "b74242",
            "5c2626"
        ]
    },
    {
        "id": "1b435d78bbe6d5eeffff895d",
        "tags": [
            "navy",
            "blue",
            "orange",
            "cold",
            "winter"
        ],
        "colors": [
            "1b435d",
            "78bbe6",
            "d5eeff",
            "ff895d"
        ]
    },
    {
        "id": "ffa0c2f9f5cee3ce8b9e7e44",
        "tags": [
            "pink",
            "yellow",
            "beige",
            "brown",
            "happy"
        ],
        "colors": [
            "ffa0c2",
            "f9f5ce",
            "e3ce8b",
            "9e7e44"
        ]
    },
    {
        "id": "fff2b29ed7632c9e4b0a4650",
        "tags": [
            "yellow",
            "green",
            "navy",
            "nature",
            "happy"
        ],
        "colors": [
            "fff2b2",
            "9ed763",
            "2c9e4b",
            "0a4650"
        ]
    },
    {
        "id": "f54ea2a94caf7b3b8c41228e",
        "tags": [
            "pink",
            "purple"
        ],
        "colors": [
            "f54ea2",
            "a94caf",
            "7b3b8c",
            "41228e"
        ]
    },
    {
        "id": "20decb41eecbf9f296fcd78e",
        "tags": [
            "teal",
            "yellow",
            "spring",
            "light"
        ],
        "colors": [
            "20decb",
            "41eecb",
            "f9f296",
            "fcd78e"
        ]
    },
    {
        "id": "2e94b9fffdc1f0b775fd5959",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "red",
            "rainbow"
        ],
        "colors": [
            "2e94b9",
            "fffdc1",
            "f0b775",
            "fd5959"
        ]
    },
    {
        "id": "e1eacdbad8b661b39001352c",
        "tags": [
            "sage",
            "teal",
            "black",
            "nature"
        ],
        "colors": [
            "e1eacd",
            "bad8b6",
            "61b390",
            "01352c"
        ]
    },
    {
        "id": "005689007cb9d5eeffff895d",
        "tags": [
            "navy",
            "blue",
            "orange"
        ],
        "colors": [
            "005689",
            "007cb9",
            "d5eeff",
            "ff895d"
        ]
    },
    {
        "id": "1b1f3a53354aa64942ff7844",
        "tags": [
            "black",
            "brown",
            "orange",
            "dark",
            "warm",
            "night",
            "gradient"
        ],
        "colors": [
            "1b1f3a",
            "53354a",
            "a64942",
            "ff7844"
        ]
    },
    {
        "id": "113f6734699a408ab465c6c4",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "night",
            "sea"
        ],
        "colors": [
            "113f67",
            "34699a",
            "408ab4",
            "65c6c4"
        ]
    },
    {
        "id": "f2ffdfb1f1b21e757b424d69",
        "tags": [
            "green",
            "teal",
            "navy",
            "cold"
        ],
        "colors": [
            "f2ffdf",
            "b1f1b2",
            "1e757b",
            "424d69"
        ]
    },
    {
        "id": "ffbc65ac4c5e5c476feeeeee",
        "tags": [
            "orange",
            "maroon",
            "red",
            "purple",
            "grey",
            "white",
            "vintage"
        ],
        "colors": [
            "ffbc65",
            "ac4c5e",
            "5c476f",
            "eeeeee"
        ]
    },
    {
        "id": "2729321c7293b9e3c6f1f2eb",
        "tags": [
            "black",
            "blue",
            "green",
            "grey",
            "cold"
        ],
        "colors": [
            "272932",
            "1c7293",
            "b9e3c6",
            "f1f2eb"
        ]
    },
    {
        "id": "c54c82ec729cf4aebafdfdcb",
        "tags": [
            "purple",
            "pink",
            "yellow",
            "warm",
            "happy"
        ],
        "colors": [
            "c54c82",
            "ec729c",
            "f4aeba",
            "fdfdcb"
        ]
    },
    {
        "id": "ff5656edf2f66a7efc494953",
        "tags": [
            "red",
            "white",
            "blue",
            "grey",
            "black"
        ],
        "colors": [
            "ff5656",
            "edf2f6",
            "6a7efc",
            "494953"
        ]
    },
    {
        "id": "f7f0e9ffaf9bdf5333424242",
        "tags": [
            "beige",
            "peach",
            "orange",
            "grey",
            "black",
            "warm"
        ],
        "colors": [
            "f7f0e9",
            "ffaf9b",
            "df5333",
            "424242"
        ]
    },
    {
        "id": "58828b5e9387c8e29df2f299",
        "tags": [
            "teal",
            "green",
            "yellow",
            "nature"
        ],
        "colors": [
            "58828b",
            "5e9387",
            "c8e29d",
            "f2f299"
        ]
    },
    {
        "id": "f23557f0d43a22b2da3b4a6b",
        "tags": [
            "red",
            "yellow",
            "blue",
            "navy",
            "rainbow"
        ],
        "colors": [
            "f23557",
            "f0d43a",
            "22b2da",
            "3b4a6b"
        ]
    },
    {
        "id": "f7f7f7fcd59b1fa8cf2657c1",
        "tags": [
            "white",
            "grey",
            "beige",
            "blue",
            "navy",
            "summer",
            "kids"
        ],
        "colors": [
            "f7f7f7",
            "fcd59b",
            "1fa8cf",
            "2657c1"
        ]
    },
    {
        "id": "3546496c7a89a3c6c4e0e7e9",
        "tags": [
            "black",
            "grey",
            "winter",
            "cold",
            "night",
            "gradient",
            "sky"
        ],
        "colors": [
            "354649",
            "6c7a89",
            "a3c6c4",
            "e0e7e9"
        ]
    },
    {
        "id": "faf4e1fabc41ec9454c72767",
        "tags": [
            "beige",
            "yellow",
            "orange",
            "maroon",
            "warm",
            "vintage",
            "gold",
            "gradient"
        ],
        "colors": [
            "faf4e1",
            "fabc41",
            "ec9454",
            "c72767"
        ]
    },
    {
        "id": "f2f2f2cdcdcd005691004a7c",
        "tags": [
            "grey",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "f2f2f2",
            "cdcdcd",
            "005691",
            "004a7c"
        ]
    },
    {
        "id": "fdf196f08edbbb47bea31c88",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "spring"
        ],
        "colors": [
            "fdf196",
            "f08edb",
            "bb47be",
            "a31c88"
        ]
    },
    {
        "id": "3038413a4750ea9215eeeeee",
        "tags": [
            "black",
            "orange",
            "grey",
            "night",
            "space"
        ],
        "colors": [
            "303841",
            "3a4750",
            "ea9215",
            "eeeeee"
        ]
    },
    {
        "id": "cbf9da3dd2cc3e6b89122d42",
        "tags": [
            "mint",
            "teal",
            "blue",
            "navy",
            "black",
            "cold",
            "winter",
            "sea"
        ],
        "colors": [
            "cbf9da",
            "3dd2cc",
            "3e6b89",
            "122d42"
        ]
    },
    {
        "id": "f47c7cf7f48ba1de9370a1d7",
        "tags": [
            "red",
            "yellow",
            "green",
            "blue",
            "kids",
            "rainbow",
            "happy"
        ],
        "colors": [
            "f47c7c",
            "f7f48b",
            "a1de93",
            "70a1d7"
        ]
    },
    {
        "id": "2837392c5d63a9c52ff5f5f5",
        "tags": [
            "black",
            "teal",
            "green",
            "white"
        ],
        "colors": [
            "283739",
            "2c5d63",
            "a9c52f",
            "f5f5f5"
        ]
    },
    {
        "id": "ed9153fbd157fbede153435b",
        "tags": [
            "orange",
            "yellow",
            "beige",
            "fall",
            "gold",
            "warm"
        ],
        "colors": [
            "ed9153",
            "fbd157",
            "fbede1",
            "53435b"
        ]
    },
    {
        "id": "e3fdfdcbf1f5a6e3e971c9ce",
        "tags": [
            "teal",
            "cold",
            "winter",
            "light",
            "cream"
        ],
        "colors": [
            "e3fdfd",
            "cbf1f5",
            "a6e3e9",
            "71c9ce"
        ]
    },
    {
        "id": "303a52574b909e579dfc85ae",
        "tags": [
            "purple",
            "pink",
            "dark",
            "night",
            "space",
            "gradient"
        ],
        "colors": [
            "303a52",
            "574b90",
            "9e579d",
            "fc85ae"
        ]
    },
    {
        "id": "798a65faf3dfd153858e415b",
        "tags": [
            "sage",
            "beige",
            "pink",
            "maroon",
            "vintage",
            "wedding"
        ],
        "colors": [
            "798a65",
            "faf3df",
            "d15385",
            "8e415b"
        ]
    },
    {
        "id": "f4f7ed86ee602e6e652b3752",
        "tags": [
            "white",
            "grey",
            "green",
            "teal",
            "navy",
            "nature"
        ],
        "colors": [
            "f4f7ed",
            "86ee60",
            "2e6e65",
            "2b3752"
        ]
    },
    {
        "id": "2e94b9475053acdceef0fbff",
        "tags": [
            "blue",
            "grey",
            "white",
            "cold"
        ],
        "colors": [
            "2e94b9",
            "475053",
            "acdcee",
            "f0fbff"
        ]
    },
    {
        "id": "f38181fce38ad6f7ad95e1d3",
        "tags": [
            "red",
            "peach",
            "yellow",
            "green",
            "blue",
            "rainbow",
            "happy"
        ],
        "colors": [
            "f38181",
            "fce38a",
            "d6f7ad",
            "95e1d3"
        ]
    },
    {
        "id": "2a363be84a5fff847bfecea8",
        "tags": [
            "black",
            "red",
            "orange",
            "peach",
            "beige",
            "warm"
        ],
        "colors": [
            "2a363b",
            "e84a5f",
            "ff847b",
            "fecea8"
        ]
    },
    {
        "id": "1333a6317ae11fdedbfffcbf",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "happy"
        ],
        "colors": [
            "1333a6",
            "317ae1",
            "1fdedb",
            "fffcbf"
        ]
    },
    {
        "id": "ffca61ffec85f2ffdfc9f0d6",
        "tags": [
            "orange",
            "yellow",
            "teal",
            "spring",
            "summer",
            "gold",
            "light",
            "happy"
        ],
        "colors": [
            "ffca61",
            "ffec85",
            "f2ffdf",
            "c9f0d6"
        ]
    },
    {
        "id": "283739228896a9c52ff5f5f5",
        "tags": [
            "black",
            "blue",
            "teal",
            "green",
            "grey",
            "white"
        ],
        "colors": [
            "283739",
            "228896",
            "a9c52f",
            "f5f5f5"
        ]
    },
    {
        "id": "7a08faa82ffcc264fef8ecfd",
        "tags": [
            "purple",
            "white",
            "cold"
        ],
        "colors": [
            "7a08fa",
            "a82ffc",
            "c264fe",
            "f8ecfd"
        ]
    },
    {
        "id": "adf7d195e8d77dace48971d0",
        "tags": [
            "green",
            "blue",
            "purple",
            "happy"
        ],
        "colors": [
            "adf7d1",
            "95e8d7",
            "7dace4",
            "8971d0"
        ]
    },
    {
        "id": "384259f738597ac7c4c4edde",
        "tags": [
            "navy",
            "red",
            "teal",
            "space"
        ],
        "colors": [
            "384259",
            "f73859",
            "7ac7c4",
            "c4edde"
        ]
    },
    {
        "id": "f9a828ececeb07617d2e383f",
        "tags": [
            "orange",
            "grey",
            "navy",
            "black",
            "retro"
        ],
        "colors": [
            "f9a828",
            "ececeb",
            "07617d",
            "2e383f"
        ]
    },
    {
        "id": "c2fcd9a0e4b0f8fba2fa7f7f",
        "tags": [
            "mint",
            "green",
            "yellow",
            "red",
            "peach",
            "summer",
            "light",
            "spring",
            "happy"
        ],
        "colors": [
            "c2fcd9",
            "a0e4b0",
            "f8fba2",
            "fa7f7f"
        ]
    },
    {
        "id": "425e920c81f65fe1d9f7fad1",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow",
            "beige"
        ],
        "colors": [
            "425e92",
            "0c81f6",
            "5fe1d9",
            "f7fad1"
        ]
    },
    {
        "id": "247291f8da5beef2e2f5f9ee",
        "tags": [
            "navy",
            "yellow",
            "beige",
            "grey",
            "summer",
            "kids",
            "happy"
        ],
        "colors": [
            "247291",
            "f8da5b",
            "eef2e2",
            "f5f9ee"
        ]
    },
    {
        "id": "fff200f5f5f5d6e6f2303841",
        "tags": [
            "yellow",
            "white",
            "grey",
            "black",
            "light"
        ],
        "colors": [
            "fff200",
            "f5f5f5",
            "d6e6f2",
            "303841"
        ]
    },
    {
        "id": "01566806648c0f81c70de2ea",
        "tags": [
            "navy",
            "blue",
            "teal",
            "cold",
            "night",
            "gradient",
            "sea"
        ],
        "colors": [
            "015668",
            "06648c",
            "0f81c7",
            "0de2ea"
        ]
    },
    {
        "id": "70198abb8fa9c1ea9ff6f1f8",
        "tags": [
            "purple",
            "green",
            "grey",
            "wedding",
            "retro"
        ],
        "colors": [
            "70198a",
            "bb8fa9",
            "c1ea9f",
            "f6f1f8"
        ]
    },
    {
        "id": "2f2b2bf3368dffc468fff7ca",
        "tags": [
            "black",
            "pink",
            "orange",
            "yellow"
        ],
        "colors": [
            "2f2b2b",
            "f3368d",
            "ffc468",
            "fff7ca"
        ]
    },
    {
        "id": "afffff74dbef5e88fc264e86",
        "tags": [
            "teal",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "afffff",
            "74dbef",
            "5e88fc",
            "264e86"
        ]
    },
    {
        "id": "2a3356f35b25fdfcfce8e2e2",
        "tags": [
            "navy",
            "orange",
            "white",
            "grey",
            "retro",
            "wedding"
        ],
        "colors": [
            "2a3356",
            "f35b25",
            "fdfcfc",
            "e8e2e2"
        ]
    },
    {
        "id": "45171de84a5fff847cfecea8",
        "tags": [
            "maroon",
            "brown",
            "red",
            "peach",
            "beige",
            "warm",
            "halloween"
        ],
        "colors": [
            "45171d",
            "e84a5f",
            "ff847c",
            "fecea8"
        ]
    },
    {
        "id": "c190f09876defdfe9a9adeb9",
        "tags": [
            "purple",
            "yellow",
            "green",
            "kids"
        ],
        "colors": [
            "c190f0",
            "9876de",
            "fdfe9a",
            "9adeb9"
        ]
    },
    {
        "id": "f4f7f779a8a94d727e1f4e5f",
        "tags": [
            "grey",
            "white",
            "teal",
            "cold",
            "winter"
        ],
        "colors": [
            "f4f7f7",
            "79a8a9",
            "4d727e",
            "1f4e5f"
        ]
    },
    {
        "id": "00ad7c52d681b5ff7dfff8b5",
        "tags": [
            "green",
            "yellow",
            "neon",
            "nature",
            "happy",
            "light",
            "summer",
            "gradient"
        ],
        "colors": [
            "00ad7c",
            "52d681",
            "b5ff7d",
            "fff8b5"
        ]
    },
    {
        "id": "f85f73fbe8d3928a97283c63",
        "tags": [
            "red",
            "beige",
            "grey",
            "navy",
            "vintage"
        ],
        "colors": [
            "f85f73",
            "fbe8d3",
            "928a97",
            "283c63"
        ]
    },
    {
        "id": "295e621c4648d5d46fdff09d",
        "tags": [
            "teal",
            "yellow",
            "nature"
        ],
        "colors": [
            "295e62",
            "1c4648",
            "d5d46f",
            "dff09d"
        ]
    },
    {
        "id": "baf5f0d17ae5e889e5f9fcc9",
        "tags": [
            "teal",
            "purple",
            "pink",
            "yellow",
            "spring",
            "light",
            "kids"
        ],
        "colors": [
            "baf5f0",
            "d17ae5",
            "e889e5",
            "f9fcc9"
        ]
    },
    {
        "id": "fcf0c8f7d098911f27630a10",
        "tags": [
            "beige",
            "yellow",
            "red",
            "maroon",
            "warm",
            "skin"
        ],
        "colors": [
            "fcf0c8",
            "f7d098",
            "911f27",
            "630a10"
        ]
    },
    {
        "id": "95efce2ea1d9395ea63e467f",
        "tags": [
            "mint",
            "teal",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "95efce",
            "2ea1d9",
            "395ea6",
            "3e467f"
        ]
    },
    {
        "id": "f9fcfdc9eff907a4b5fed8a7",
        "tags": [
            "white",
            "blue",
            "orange",
            "summer",
            "happy"
        ],
        "colors": [
            "f9fcfd",
            "c9eff9",
            "07a4b5",
            "fed8a7"
        ]
    },
    {
        "id": "392f2f3a756359a985e6d3a7",
        "tags": [
            "brown",
            "green",
            "beige",
            "earth",
            "vintage"
        ],
        "colors": [
            "392f2f",
            "3a7563",
            "59a985",
            "e6d3a7"
        ]
    },
    {
        "id": "fafafaff347fc9356cf48db4",
        "tags": [
            "white",
            "pink",
            "kids"
        ],
        "colors": [
            "fafafa",
            "ff347f",
            "c9356c",
            "f48db4"
        ]
    },
    {
        "id": "ffffe7c6e5f3539ddb084a83",
        "tags": [
            "yellow",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "ffffe7",
            "c6e5f3",
            "539ddb",
            "084a83"
        ]
    },
    {
        "id": "fa4659feffe4a3de832eb872",
        "tags": [
            "red",
            "green",
            "spring",
            "nature",
            "happy"
        ],
        "colors": [
            "fa4659",
            "feffe4",
            "a3de83",
            "2eb872"
        ]
    },
    {
        "id": "f5f5f5c5d20051710a424242",
        "tags": [
            "grey",
            "green",
            "nature"
        ],
        "colors": [
            "f5f5f5",
            "c5d200",
            "51710a",
            "424242"
        ]
    },
    {
        "id": "c7fffffbeeffebc6ff7e80ff",
        "tags": [
            "blue",
            "pink",
            "light",
            "happy"
        ],
        "colors": [
            "c7ffff",
            "fbeeff",
            "ebc6ff",
            "7e80ff"
        ]
    },
    {
        "id": "900c27c70039f6c667f1f8fd",
        "tags": [
            "maroon",
            "red",
            "yellow",
            "white",
            "warm",
            "christmas"
        ],
        "colors": [
            "900c27",
            "c70039",
            "f6c667",
            "f1f8fd"
        ]
    },
    {
        "id": "0037441a554ffda856f6fe91",
        "tags": [
            "green",
            "orange",
            "yellow",
            "space"
        ],
        "colors": [
            "003744",
            "1a554f",
            "fda856",
            "f6fe91"
        ]
    },
    {
        "id": "ffcfdffefdcae0f9b5a5dee5",
        "tags": [
            "pink",
            "yellow",
            "green",
            "blue",
            "pastel",
            "spring",
            "light",
            "happy"
        ],
        "colors": [
            "ffcfdf",
            "fefdca",
            "e0f9b5",
            "a5dee5"
        ]
    },
    {
        "id": "0f1021d01257fb90b7ffcee4",
        "tags": [
            "black",
            "red",
            "pink",
            "space"
        ],
        "colors": [
            "0f1021",
            "d01257",
            "fb90b7",
            "ffcee4"
        ]
    },
    {
        "id": "d7ffdface6c077b5a69d4545",
        "tags": [
            "mint",
            "green",
            "teal",
            "maroon",
            "nature"
        ],
        "colors": [
            "d7ffdf",
            "ace6c0",
            "77b5a6",
            "9d4545"
        ]
    },
    {
        "id": "fafafac7eeff0077c01d242b",
        "tags": [
            "white",
            "grey",
            "blue",
            "black",
            "cold"
        ],
        "colors": [
            "fafafa",
            "c7eeff",
            "0077c0",
            "1d242b"
        ]
    },
    {
        "id": "241e925432d37b6cf6e5a5ff",
        "tags": [
            "navy",
            "purple",
            "pink",
            "cold",
            "dark",
            "gradient"
        ],
        "colors": [
            "241e92",
            "5432d3",
            "7b6cf6",
            "e5a5ff"
        ]
    },
    {
        "id": "ffeee7fbb448e3670ccc3d0b",
        "tags": [
            "peach",
            "orange",
            "fall",
            "warm",
            "gold",
            "happy",
            "gradient"
        ],
        "colors": [
            "ffeee7",
            "fbb448",
            "e3670c",
            "cc3d0b"
        ]
    },
    {
        "id": "15b7b910ddc2f5f5f5f57170",
        "tags": [
            "teal",
            "white",
            "peach",
            "kids"
        ],
        "colors": [
            "15b7b9",
            "10ddc2",
            "f5f5f5",
            "f57170"
        ]
    },
    {
        "id": "2f3c4f506e86fcb040de703b",
        "tags": [
            "navy",
            "orange",
            "vintage"
        ],
        "colors": [
            "2f3c4f",
            "506e86",
            "fcb040",
            "de703b"
        ]
    },
    {
        "id": "e4fffea4f6f9ff99feba52ed",
        "tags": [
            "blue",
            "pink",
            "purple",
            "light",
            "neon",
            "happy"
        ],
        "colors": [
            "e4fffe",
            "a4f6f9",
            "ff99fe",
            "ba52ed"
        ]
    },
    {
        "id": "08383666d37ec6e872fbffa3",
        "tags": [
            "green",
            "yellow",
            "nature",
            "happy"
        ],
        "colors": [
            "083836",
            "66d37e",
            "c6e872",
            "fbffa3"
        ]
    },
    {
        "id": "f95959ffe1a1fcffccd3e785",
        "tags": [
            "red",
            "beige",
            "yellow",
            "green",
            "kids"
        ],
        "colors": [
            "f95959",
            "ffe1a1",
            "fcffcc",
            "d3e785"
        ]
    },
    {
        "id": "718ca159748c354d62d7f2f7",
        "tags": [
            "navy",
            "cold",
            "winter"
        ],
        "colors": [
            "718ca1",
            "59748c",
            "354d62",
            "d7f2f7"
        ]
    },
    {
        "id": "f7e74a09c6ab06888802556d",
        "tags": [
            "yellow",
            "teal",
            "navy"
        ],
        "colors": [
            "f7e74a",
            "09c6ab",
            "068888",
            "02556d"
        ]
    },
    {
        "id": "6251da828bff7ab7fff0fc93",
        "tags": [
            "blue",
            "purple",
            "yellow",
            "happy"
        ],
        "colors": [
            "6251da",
            "828bff",
            "7ab7ff",
            "f0fc93"
        ]
    },
    {
        "id": "eaefc49bdf4625a55f346473",
        "tags": [
            "beige",
            "green",
            "navy",
            "nature"
        ],
        "colors": [
            "eaefc4",
            "9bdf46",
            "25a55f",
            "346473"
        ]
    },
    {
        "id": "f1ffd98bdbf5b292eaeb55bf",
        "tags": [
            "yellow",
            "blue",
            "purple",
            "pink",
            "spring",
            "kids"
        ],
        "colors": [
            "f1ffd9",
            "8bdbf5",
            "b292ea",
            "eb55bf"
        ]
    },
    {
        "id": "2b4450497285dfebedf78536",
        "tags": [
            "navy",
            "orange"
        ],
        "colors": [
            "2b4450",
            "497285",
            "dfebed",
            "f78536"
        ]
    },
    {
        "id": "f1fafba0e4f19dc6ff4993fa",
        "tags": [
            "white",
            "teal",
            "blue",
            "cold",
            "sky"
        ],
        "colors": [
            "f1fafb",
            "a0e4f1",
            "9dc6ff",
            "4993fa"
        ]
    },
    {
        "id": "513c3c2a769a41c3bef7f36b",
        "tags": [
            "brown",
            "blue",
            "teal",
            "yellow"
        ],
        "colors": [
            "513c3c",
            "2a769a",
            "41c3be",
            "f7f36b"
        ]
    },
    {
        "id": "ecffc964fed682a6ee7871bf",
        "tags": [
            "yellow",
            "mint",
            "blue",
            "purple",
            "kids"
        ],
        "colors": [
            "ecffc9",
            "64fed6",
            "82a6ee",
            "7871bf"
        ]
    },
    {
        "id": "fffc3aea648d884ea23d3551",
        "tags": [
            "yellow",
            "pink",
            "purple"
        ],
        "colors": [
            "fffc3a",
            "ea648d",
            "884ea2",
            "3d3551"
        ]
    },
    {
        "id": "e6f8f6a0f6d272dfd003414d",
        "tags": [
            "teal",
            "navy"
        ],
        "colors": [
            "e6f8f6",
            "a0f6d2",
            "72dfd0",
            "03414d"
        ]
    },
    {
        "id": "683531bf382aef7079f7e8c3",
        "tags": [
            "brown",
            "maroon",
            "red",
            "beige",
            "warm",
            "gradient"
        ],
        "colors": [
            "683531",
            "bf382a",
            "ef7079",
            "f7e8c3"
        ]
    },
    {
        "id": "d1ffa200cf950098ef6d0ad3",
        "tags": [
            "green",
            "blue",
            "purple",
            "kids"
        ],
        "colors": [
            "d1ffa2",
            "00cf95",
            "0098ef",
            "6d0ad3"
        ]
    },
    {
        "id": "2f3032383a56b0a565ede68a",
        "tags": [
            "black",
            "navy",
            "yellow",
            "dark",
            "night"
        ],
        "colors": [
            "2f3032",
            "383a56",
            "b0a565",
            "ede68a"
        ]
    },
    {
        "id": "d5fdff9de5ffaca8ffac73ff",
        "tags": [
            "blue",
            "purple",
            "cold",
            "kids"
        ],
        "colors": [
            "d5fdff",
            "9de5ff",
            "aca8ff",
            "ac73ff"
        ]
    },
    {
        "id": "01005e22267b28518a17b794",
        "tags": [
            "navy",
            "green",
            "cold",
            "dark",
            "winter",
            "night",
            "gradient",
            "sea"
        ],
        "colors": [
            "01005e",
            "22267b",
            "28518a",
            "17b794"
        ]
    },
    {
        "id": "b062eaf392f2fed08ff6f39f",
        "tags": [
            "purple",
            "pink",
            "orange",
            "yellow",
            "light"
        ],
        "colors": [
            "b062ea",
            "f392f2",
            "fed08f",
            "f6f39f"
        ]
    },
    {
        "id": "d2fafb5acfd6189bfa0c4b8e",
        "tags": [
            "teal",
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "d2fafb",
            "5acfd6",
            "189bfa",
            "0c4b8e"
        ]
    },
    {
        "id": "feffa0acdb86547c663b5b5d",
        "tags": [
            "yellow",
            "green",
            "nature",
            "gradient"
        ],
        "colors": [
            "feffa0",
            "acdb86",
            "547c66",
            "3b5b5d"
        ]
    },
    {
        "id": "c9182bf23a3ae3f3ac44c662",
        "tags": [
            "red",
            "green",
            "christmas"
        ],
        "colors": [
            "c9182b",
            "f23a3a",
            "e3f3ac",
            "44c662"
        ]
    },
    {
        "id": "3f1263986eadd8cbbbf2f2f2",
        "tags": [
            "purple",
            "beige",
            "grey",
            "white",
            "vintage"
        ],
        "colors": [
            "3f1263",
            "986ead",
            "d8cbbb",
            "f2f2f2"
        ]
    },
    {
        "id": "f1fdf3e5f4e7d1e9d299cda9",
        "tags": [
            "white",
            "green",
            "cream",
            "light",
            "nature"
        ],
        "colors": [
            "f1fdf3",
            "e5f4e7",
            "d1e9d2",
            "99cda9"
        ]
    },
    {
        "id": "5f2f141297bd1ad7dbf3f1f1",
        "tags": [
            "brown",
            "blue",
            "grey",
            "vintage",
            "wedding"
        ],
        "colors": [
            "5f2f14",
            "1297bd",
            "1ad7db",
            "f3f1f1"
        ]
    },
    {
        "id": "00334e1453745588a3e8e8e8",
        "tags": [
            "navy",
            "grey",
            "cold",
            "winter",
            "night",
            "gradient"
        ],
        "colors": [
            "00334e",
            "145374",
            "5588a3",
            "e8e8e8"
        ]
    },
    {
        "id": "f5ff8d50cb864c74c9312f44",
        "tags": [
            "yellow",
            "green",
            "blue",
            "black"
        ],
        "colors": [
            "f5ff8d",
            "50cb86",
            "4c74c9",
            "312f44"
        ]
    },
    {
        "id": "2837392c5d63a2c11ce0e0e0",
        "tags": [
            "black",
            "teal",
            "green",
            "grey"
        ],
        "colors": [
            "283739",
            "2c5d63",
            "a2c11c",
            "e0e0e0"
        ]
    },
    {
        "id": "fbffe0ffd6a6ff8ab4d86eff",
        "tags": [
            "yellow",
            "orange",
            "pink",
            "purple",
            "spring",
            "happy"
        ],
        "colors": [
            "fbffe0",
            "ffd6a6",
            "ff8ab4",
            "d86eff"
        ]
    },
    {
        "id": "0c476251dacf9ef5cff4eeee",
        "tags": [
            "navy",
            "teal",
            "mint",
            "grey",
            "space"
        ],
        "colors": [
            "0c4762",
            "51dacf",
            "9ef5cf",
            "f4eeee"
        ]
    },
    {
        "id": "700961b80d57e03e36ff7c38",
        "tags": [
            "purple",
            "maroon",
            "orange",
            "warm"
        ],
        "colors": [
            "700961",
            "b80d57",
            "e03e36",
            "ff7c38"
        ]
    },
    {
        "id": "0eb29af5fdffddf0c28c999a",
        "tags": [
            "teal",
            "white",
            "green",
            "grey"
        ],
        "colors": [
            "0eb29a",
            "f5fdff",
            "ddf0c2",
            "8c999a"
        ]
    },
    {
        "id": "39627f4b788fe4de66beb000",
        "tags": [
            "navy",
            "blue",
            "yellow"
        ],
        "colors": [
            "39627f",
            "4b788f",
            "e4de66",
            "beb000"
        ]
    },
    {
        "id": "d65f5ffaf99fa1f6b678d8d0",
        "tags": [
            "red",
            "yellow",
            "teal",
            "green",
            "happy",
            "rainbow"
        ],
        "colors": [
            "d65f5f",
            "faf99f",
            "a1f6b6",
            "78d8d0"
        ]
    },
    {
        "id": "3c2f3d2eac6d9dda52f0f0f0",
        "tags": [
            "black",
            "green",
            "grey",
            "nature"
        ],
        "colors": [
            "3c2f3d",
            "2eac6d",
            "9dda52",
            "f0f0f0"
        ]
    },
    {
        "id": "f2f299c8e29d5e938758828b",
        "tags": [
            "yellow",
            "green"
        ],
        "colors": [
            "f2f299",
            "c8e29d",
            "5e9387",
            "58828b"
        ]
    },
    {
        "id": "fff9c1ffa1d0c244fb84e9ff",
        "tags": [
            "yellow",
            "pink",
            "peach",
            "purple",
            "blue",
            "happy",
            "neon"
        ],
        "colors": [
            "fff9c1",
            "ffa1d0",
            "c244fb",
            "84e9ff"
        ]
    },
    {
        "id": "005689007cb9f6c667f1f8fd",
        "tags": [
            "navy",
            "blue",
            "orange",
            "white"
        ],
        "colors": [
            "005689",
            "007cb9",
            "f6c667",
            "f1f8fd"
        ]
    },
    {
        "id": "00e0ff74f9ffa6fff2e8ffe8",
        "tags": [
            "blue",
            "teal",
            "light",
            "summer",
            "neon",
            "kids",
            "sky"
        ],
        "colors": [
            "00e0ff",
            "74f9ff",
            "a6fff2",
            "e8ffe8"
        ]
    },
    {
        "id": "b23256fcd47d31aa75a2ef44",
        "tags": [
            "red",
            "maroon",
            "yellow",
            "green",
            "christmas",
            "food"
        ],
        "colors": [
            "b23256",
            "fcd47d",
            "31aa75",
            "a2ef44"
        ]
    },
    {
        "id": "fffaa2d600b1a500a3680097",
        "tags": [
            "yellow",
            "purple",
            "kids"
        ],
        "colors": [
            "fffaa2",
            "d600b1",
            "a500a3",
            "680097"
        ]
    },
    {
        "id": "64868e98b4a6d1e4d1f3fbf1",
        "tags": [
            "teal",
            "sage",
            "grey",
            "white",
            "cream",
            "cold",
            "gradient"
        ],
        "colors": [
            "64868e",
            "98b4a6",
            "d1e4d1",
            "f3fbf1"
        ]
    },
    {
        "id": "f4f1aeff8d52f85a16ca005e",
        "tags": [
            "yellow",
            "orange",
            "maroon",
            "warm",
            "gold"
        ],
        "colors": [
            "f4f1ae",
            "ff8d52",
            "f85a16",
            "ca005e"
        ]
    },
    {
        "id": "007ab5005a85004262d8e6ec",
        "tags": [
            "blue",
            "navy",
            "cold",
            "sea"
        ],
        "colors": [
            "007ab5",
            "005a85",
            "004262",
            "d8e6ec"
        ]
    },
    {
        "id": "fffbafff5656cd0a0a42cfc4",
        "tags": [
            "yellow",
            "red",
            "maroon",
            "teal",
            "happy"
        ],
        "colors": [
            "fffbaf",
            "ff5656",
            "cd0a0a",
            "42cfc4"
        ]
    },
    {
        "id": "442a9df14e95b13cd5faf3fc",
        "tags": [
            "purple",
            "pink",
            "white"
        ],
        "colors": [
            "442a9d",
            "f14e95",
            "b13cd5",
            "faf3fc"
        ]
    },
    {
        "id": "191ba95cc2f2c1eaf2f7f3f3",
        "tags": [
            "blue",
            "grey",
            "white",
            "cold",
            "gradient"
        ],
        "colors": [
            "191ba9",
            "5cc2f2",
            "c1eaf2",
            "f7f3f3"
        ]
    },
    {
        "id": "fd5959ff9c6dfcff82afc5ff",
        "tags": [
            "red",
            "peach",
            "orange",
            "yellow",
            "blue",
            "rainbow",
            "kids"
        ],
        "colors": [
            "fd5959",
            "ff9c6d",
            "fcff82",
            "afc5ff"
        ]
    },
    {
        "id": "43496e544d7e65589cffc12d",
        "tags": [
            "navy",
            "purple",
            "orange",
            "night"
        ],
        "colors": [
            "43496e",
            "544d7e",
            "65589c",
            "ffc12d"
        ]
    },
    {
        "id": "fcf798e0fff974d2ff5ca4ca",
        "tags": [
            "yellow",
            "blue",
            "light",
            "summer",
            "happy"
        ],
        "colors": [
            "fcf798",
            "e0fff9",
            "74d2ff",
            "5ca4ca"
        ]
    },
    {
        "id": "fcfaefe2e0a5d3504aa63636",
        "tags": [
            "beige",
            "red",
            "maroon",
            "vintage",
            "food"
        ],
        "colors": [
            "fcfaef",
            "e2e0a5",
            "d3504a",
            "a63636"
        ]
    },
    {
        "id": "fe7187ca4b7c7a2e7aa8d7f7",
        "tags": [
            "pink",
            "purple",
            "blue"
        ],
        "colors": [
            "fe7187",
            "ca4b7c",
            "7a2e7a",
            "a8d7f7"
        ]
    },
    {
        "id": "daebeeb6d7defceddaff5126",
        "tags": [
            "blue",
            "beige",
            "orange",
            "wedding"
        ],
        "colors": [
            "daebee",
            "b6d7de",
            "fcedda",
            "ff5126"
        ]
    },
    {
        "id": "07588a6ac1b8bfe9dbe1f6f4",
        "tags": [
            "navy",
            "teal",
            "green",
            "cold",
            "gradient"
        ],
        "colors": [
            "07588a",
            "6ac1b8",
            "bfe9db",
            "e1f6f4"
        ]
    },
    {
        "id": "f8ecd9eebee3c576ac662753",
        "tags": [
            "beige",
            "pink",
            "purple",
            "vintage"
        ],
        "colors": [
            "f8ecd9",
            "eebee3",
            "c576ac",
            "662753"
        ]
    },
    {
        "id": "f8ffaef36363ef4a4ad32d2d",
        "tags": [
            "yellow",
            "red",
            "maroon",
            "warm"
        ],
        "colors": [
            "f8ffae",
            "f36363",
            "ef4a4a",
            "d32d2d"
        ]
    },
    {
        "id": "e8ecf1b5cfd87393a76c737e",
        "tags": [
            "grey",
            "blue",
            "winter",
            "pastel",
            "cold",
            "cream"
        ],
        "colors": [
            "e8ecf1",
            "b5cfd8",
            "7393a7",
            "6c737e"
        ]
    },
    {
        "id": "f2ff9b6af79a57acc5444b6c",
        "tags": [
            "yellow",
            "mint",
            "green",
            "blue",
            "navy"
        ],
        "colors": [
            "f2ff9b",
            "6af79a",
            "57acc5",
            "444b6c"
        ]
    },
    {
        "id": "65ead1f469a9ff917bfcffc1",
        "tags": [
            "teal",
            "pink",
            "orange",
            "peach",
            "yellow",
            "retro",
            "spring",
            "happy"
        ],
        "colors": [
            "65ead1",
            "f469a9",
            "ff917b",
            "fcffc1"
        ]
    },
    {
        "id": "3038413a4750d72323eeeeee",
        "tags": [
            "grey",
            "red",
            "white",
            "space",
            "night"
        ],
        "colors": [
            "303841",
            "3a4750",
            "d72323",
            "eeeeee"
        ]
    },
    {
        "id": "e4fcf9ace6f64b89ac446491",
        "tags": [
            "blue",
            "navy",
            "cold"
        ],
        "colors": [
            "e4fcf9",
            "ace6f6",
            "4b89ac",
            "446491"
        ]
    },
    {
        "id": "ee9494ebffafb4e8c0c3b9ea",
        "tags": [
            "red",
            "peach",
            "yellow",
            "green",
            "purple",
            "light",
            "rainbow",
            "kids"
        ],
        "colors": [
            "ee9494",
            "ebffaf",
            "b4e8c0",
            "c3b9ea"
        ]
    },
    {
        "id": "6f4f8b6d739d7dbcc8b9eaf5",
        "tags": [
            "purple",
            "teal",
            "night",
            "gradient"
        ],
        "colors": [
            "6f4f8b",
            "6d739d",
            "7dbcc8",
            "b9eaf5"
        ]
    },
    {
        "id": "2794ebbff8d447d6b617b3c1",
        "tags": [
            "blue",
            "mint",
            "green",
            "teal",
            "cold"
        ],
        "colors": [
            "2794eb",
            "bff8d4",
            "47d6b6",
            "17b3c1"
        ]
    },
    {
        "id": "f5f5f5b9e93757d131406661",
        "tags": [
            "grey",
            "white",
            "green"
        ],
        "colors": [
            "f5f5f5",
            "b9e937",
            "57d131",
            "406661"
        ]
    },
    {
        "id": "2e94b9fffdc1f0b775d25565",
        "tags": [
            "blue",
            "yellow",
            "orange",
            "red",
            "kids"
        ],
        "colors": [
            "2e94b9",
            "fffdc1",
            "f0b775",
            "d25565"
        ]
    },
    {
        "id": "3c90995fbdb0e3e2c3f0efe2",
        "tags": [
            "teal",
            "beige",
            "pastel"
        ],
        "colors": [
            "3c9099",
            "5fbdb0",
            "e3e2c3",
            "f0efe2"
        ]
    },
    {
        "id": "c4317bac7c7cd0baa8efe4e4",
        "tags": [
            "purple",
            "brown",
            "beige",
            "coffee",
            "vintage"
        ],
        "colors": [
            "c4317b",
            "ac7c7c",
            "d0baa8",
            "efe4e4"
        ]
    },
    {
        "id": "48f3db51c4e96150c14a3764",
        "tags": [
            "teal",
            "blue",
            "purple",
            "cold"
        ],
        "colors": [
            "48f3db",
            "51c4e9",
            "6150c1",
            "4a3764"
        ]
    },
    {
        "id": "7a4579d56073ec9e69ffff8f",
        "tags": [
            "purple",
            "red",
            "orange",
            "yellow",
            "sunset",
            "wedding",
            "warm",
            "gradient"
        ],
        "colors": [
            "7a4579",
            "d56073",
            "ec9e69",
            "ffff8f"
        ]
    },
    {
        "id": "f7fbfcd6e6f2b9d7ea769fcd",
        "tags": [
            "white",
            "grey",
            "blue",
            "light",
            "cold",
            "cream",
            "sky"
        ],
        "colors": [
            "f7fbfc",
            "d6e6f2",
            "b9d7ea",
            "769fcd"
        ]
    },
    {
        "id": "3434342d4059ea5455fde9c9",
        "tags": [
            "black",
            "navy",
            "red",
            "beige",
            "space"
        ],
        "colors": [
            "343434",
            "2d4059",
            "ea5455",
            "fde9c9"
        ]
    },
    {
        "id": "ebe8beb3c87a347a2a202e24",
        "tags": [
            "beige",
            "green",
            "black",
            "nature"
        ],
        "colors": [
            "ebe8be",
            "b3c87a",
            "347a2a",
            "202e24"
        ]
    },
    {
        "id": "415f77d1e9eafc5050ffd00c",
        "tags": [
            "navy",
            "blue",
            "red",
            "yellow"
        ],
        "colors": [
            "415f77",
            "d1e9ea",
            "fc5050",
            "ffd00c"
        ]
    },
    {
        "id": "f7b679e77c7cb55c6c61305d",
        "tags": [
            "orange",
            "peach",
            "purple",
            "warm",
            "skin"
        ],
        "colors": [
            "f7b679",
            "e77c7c",
            "b55c6c",
            "61305d"
        ]
    },
    {
        "id": "062d92046fdb03d6d2fffcbf",
        "tags": [
            "navy",
            "blue",
            "teal",
            "yellow"
        ],
        "colors": [
            "062d92",
            "046fdb",
            "03d6d2",
            "fffcbf"
        ]
    },
    {
        "id": "4b2b305e3b4daa96b7d9e2a8",
        "tags": [
            "brown",
            "purple",
            "green",
            "dark"
        ],
        "colors": [
            "4b2b30",
            "5e3b4d",
            "aa96b7",
            "d9e2a8"
        ]
    },
    {
        "id": "f4fab3a4eae853aca8498eb9",
        "tags": [
            "yellow",
            "teal",
            "blue",
            "summer"
        ],
        "colors": [
            "f4fab3",
            "a4eae8",
            "53aca8",
            "498eb9"
        ]
    },
    {
        "id": "dddddd516c8d28385e304163",
        "tags": [
            "grey",
            "navy",
            "cold",
            "winter"
        ],
        "colors": [
            "dddddd",
            "516c8d",
            "28385e",
            "304163"
        ]
    },
    {
        "id": "b8eef1bf68f6fd89ddf0e48e",
        "tags": [
            "blue",
            "purple",
            "pink",
            "yellow",
            "light",
            "retro",
            "happy"
        ],
        "colors": [
            "b8eef1",
            "bf68f6",
            "fd89dd",
            "f0e48e"
        ]
    },
    {
        "id": "cabfabdfd8c841444b52575d",
        "tags": [
            "beige",
            "black",
            "grey",
            "coffee",
            "earth",
            "pastel",
            "winter",
            "fall"
        ],
        "colors": [
            "cabfab",
            "dfd8c8",
            "41444b",
            "52575d"
        ]
    },
    {
        "id": "0411222590737fda89e6f99d",
        "tags": [
            "black",
            "green",
            "yellow"
        ],
        "colors": [
            "041122",
            "259073",
            "7fda89",
            "e6f99d"
        ]
    },
    {
        "id": "ff9090ffcf7ffffa6289c4ff",
        "tags": [
            "peach",
            "orange",
            "yellow",
            "blue",
            "kids",
            "neon"
        ],
        "colors": [
            "ff9090",
            "ffcf7f",
            "fffa62",
            "89c4ff"
        ]
    },
    {
        "id": "2daf943ec8ac4be4c5c8f6ed",
        "tags": [
            "green",
            "teal"
        ],
        "colors": [
            "2daf94",
            "3ec8ac",
            "4be4c5",
            "c8f6ed"
        ]
    },
    {
        "id": "ffdbc5ef4339b01c332e112d",
        "tags": [
            "beige",
            "peach",
            "red",
            "maroon",
            "black",
            "warm"
        ],
        "colors": [
            "ffdbc5",
            "ef4339",
            "b01c33",
            "2e112d"
        ]
    },
    {
        "id": "9ddcdcfff4e1ffebb7e67a7a",
        "tags": [
            "blue",
            "beige",
            "yellow",
            "red",
            "rainbow",
            "kids"
        ],
        "colors": [
            "9ddcdc",
            "fff4e1",
            "ffebb7",
            "e67a7a"
        ]
    },
    {
        "id": "414a5085a6b18bd7d1caedde",
        "tags": [
            "grey",
            "teal",
            "cold",
            "sea"
        ],
        "colors": [
            "414a50",
            "85a6b1",
            "8bd7d1",
            "caedde"
        ]
    },
    {
        "id": "f72464ff858afff3a7568564",
        "tags": [
            "red",
            "pink",
            "yellow",
            "green",
            "spring",
            "happy"
        ],
        "colors": [
            "f72464",
            "ff858a",
            "fff3a7",
            "568564"
        ]
    },
    {
        "id": "54777deadb9dfeffe4e7e3c5",
        "tags": [
            "teal",
            "yellow",
            "beige",
            "kids"
        ],
        "colors": [
            "54777d",
            "eadb9d",
            "feffe4",
            "e7e3c5"
        ]
    },
    {
        "id": "3841374066613bb87394ed88",
        "tags": [
            "green",
            "nature"
        ],
        "colors": [
            "384137",
            "406661",
            "3bb873",
            "94ed88"
        ]
    },
    {
        "id": "83580bd9b650f5dd7bfde994",
        "tags": [
            "brown",
            "beige",
            "yellow",
            "gold",
            "food",
            "warm",
            "fall"
        ],
        "colors": [
            "83580b",
            "d9b650",
            "f5dd7b",
            "fde994"
        ]
    },
    {
        "id": "4f1c4ca91d1dda4949fde9c9",
        "tags": [
            "purple",
            "maroon",
            "red",
            "beige",
            "vintage",
            "wedding"
        ],
        "colors": [
            "4f1c4c",
            "a91d1d",
            "da4949",
            "fde9c9"
        ]
    },
    {
        "id": "ffa5a5ffffc2c8e7edbfcfff",
        "tags": [
            "peach",
            "yellow",
            "blue",
            "pastel",
            "summer",
            "light",
            "rainbow",
            "happy"
        ],
        "colors": [
            "ffa5a5",
            "ffffc2",
            "c8e7ed",
            "bfcfff"
        ]
    },
    {
        "id": "f0f2aca7cbd97e94bf5357a6",
        "tags": [
            "yellow",
            "blue",
            "navy",
            "pastel"
        ],
        "colors": [
            "f0f2ac",
            "a7cbd9",
            "7e94bf",
            "5357a6"
        ]
    },
    {
        "id": "93e4c13baea0118a7e1f6f78",
        "tags": [
            "green",
            "teal",
            "cold"
        ],
        "colors": [
            "93e4c1",
            "3baea0",
            "118a7e",
            "1f6f78"
        ]
    },
    {
        "id": "bb2253ec185dff9171ffb383",
        "tags": [
            "red",
            "orange",
            "peach",
            "warm",
            "wedding"
        ],
        "colors": [
            "bb2253",
            "ec185d",
            "ff9171",
            "ffb383"
        ]
    },
    {
        "id": "121435faf9f0edebcaff5722",
        "tags": [
            "black",
            "white",
            "beige",
            "orange"
        ],
        "colors": [
            "121435",
            "faf9f0",
            "edebca",
            "ff5722"
        ]
    },
    {
        "id": "1d2b537e2553ff004dfff024",
        "tags": [
            "navy",
            "maroon",
            "red",
            "yellow",
            "neon",
            "space"
        ],
        "colors": [
            "1d2b53",
            "7e2553",
            "ff004d",
            "fff024"
        ]
    },
    {
        "id": "f5f5f5b9e93700b906424242",
        "tags": [
            "white",
            "grey",
            "green",
            "kids"
        ],
        "colors": [
            "f5f5f5",
            "b9e937",
            "00b906",
            "424242"
        ]
    },
    {
        "id": "353e55b36458bcd3c2e0e7b8",
        "tags": [
            "navy",
            "brown",
            "vintage",
            "pastel",
            "earth"
        ],
        "colors": [
            "353e55",
            "b36458",
            "bcd3c2",
            "e0e7b8"
        ]
    },
    {
        "id": "591fce0c9cee3dbdc2a1f480",
        "tags": [
            "purple",
            "blue",
            "teal",
            "green",
            "happy",
            "cold"
        ],
        "colors": [
            "591fce",
            "0c9cee",
            "3dbdc2",
            "a1f480"
        ]
    },
    {
        "id": "da1212f08c00c6da20f3f5d5",
        "tags": [
            "red",
            "orange",
            "green",
            "beige",
            "fall",
            "christmas",
            "food"
        ],
        "colors": [
            "da1212",
            "f08c00",
            "c6da20",
            "f3f5d5"
        ]
    },
    {
        "id": "fafafae1eeffc2cfd8543a3a",
        "tags": [
            "white",
            "grey",
            "blue",
            "brown",
            "vintage",
            "wedding",
            "cold"
        ],
        "colors": [
            "fafafa",
            "e1eeff",
            "c2cfd8",
            "543a3a"
        ]
    },
    {
        "id": "b8f7d46fe7db7fa6ee835af1",
        "tags": [
            "mint",
            "green",
            "teal",
            "blue",
            "purple",
            "cold"
        ],
        "colors": [
            "b8f7d4",
            "6fe7db",
            "7fa6ee",
            "835af1"
        ]
    },
    {
        "id": "fdffa3f59af0a980e4a2e4a2",
        "tags": [
            "yellow",
            "pink",
            "purple",
            "green",
            "spring",
            "kids"
        ],
        "colors": [
            "fdffa3",
            "f59af0",
            "a980e4",
            "a2e4a2"
        ]
    },
    {
        "id": "61b292aed09ef1e8a7a8896c",
        "tags": [
            "green",
            "yellow",
            "beige",
            "brown",
            "nature"
        ],
        "colors": [
            "61b292",
            "aed09e",
            "f1e8a7",
            "a8896c"
        ]
    },
    {
        "id": "1f024c45056e8f1383e47676",
        "tags": [
            "purple",
            "peach",
            "dark",
            "night",
            "space",
            "gradient"
        ],
        "colors": [
            "1f024c",
            "45056e",
            "8f1383",
            "e47676"
        ]
    },
    {
        "id": "f87d09f6f6f6a7cdcc004a55",
        "tags": [
            "orange",
            "white",
            "teal"
        ],
        "colors": [
            "f87d09",
            "f6f6f6",
            "a7cdcc",
            "004a55"
        ]
    },
    {
        "id": "1a1a1b333f4437aa9c94f3e4",
        "tags": [
            "black",
            "grey",
            "teal",
            "space",
            "dark"
        ],
        "colors": [
            "1a1a1b",
            "333f44",
            "37aa9c",
            "94f3e4"
        ]
    },
    {
        "id": "e0c97efcf8b3fb9378ab6088",
        "tags": [
            "brown",
            "beige",
            "yellow",
            "peach",
            "orange",
            "purple",
            "warm"
        ],
        "colors": [
            "e0c97e",
            "fcf8b3",
            "fb9378",
            "ab6088"
        ]
    },
    {
        "id": "efecea334854e04462f9c535",
        "tags": [
            "grey",
]
