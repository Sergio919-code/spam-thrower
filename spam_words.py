import random
import asyncio


words = [
    "apple",
    "banana",
    "orange",
    "cat",
    "dog",
    "fish",
    "house",
    "chair",
    "table",
    "school",
    "castle",
    "bridge",
    "forest",
    "flower",
    "animal",
    "window",
    "thunder",
    "monkey",
    "people",
    "dragon",
    "algorithm",
    "python",
    "hangman",
    "mystery",
    "sapphire",
    "justice",
    "freedom",
    "equation",
    "philosopher",
    "astronaut",
    "mountain",
    "volcano",
    "hurricane",
    "tornado",
    "glacier",
    "desert",
    "ocean",
    "waterfall",
    "rainbow",
    "eclipse",
    "molecule",
    "gravity",
    "electron",
    "neutron",
    "element",
    "biology",
    "chemistry",
    "physics",
    "atom",
    "experiment",
    "Zeus",
    "Hera",
    "Apollo",
    "Athena",
    "Poseidon",
    "Hades",
    "Odin",
    "Thor",
    "Loki",
    "Freya",
    "universe",
    "galaxy",
    "planet",
    "asteroid",
    "comet",
    "nebula",
    "blackhole",
    "satellite",
    "rocket",
    "spacecraft",
    "constellation",
    "weather",
    "cyclone",
    "earthquake",
    "tsunami",
    "avalanche",
    "tsar",
    "bomb",
    "iceberg",
    "canyon",
    "ridge",
    "valley",
    "plateau",
    "dune",
    "sandstorm",
    "oasis",
    "pyramid",
    "labyrinth",
    "octopus",
    "penguin",
    "dolphin",
    "whale",
    "jellyfish",
    "shark",
    "turtle",
    "eagle",
    "panther",
    "tiger",
    "cheetah",
    "leopard",
    "giraffe",
    "zebra",
    "rhinoceros",
    "hippopotamus",
    "platypus",
    "meerkat",
    "lemur",
    "koala",
    "kangaroo",
    "crocodile",
    "alligator",
    "anaconda",
    "python",
    "cobra",
    "viper",
    "tarantula",
    "scorpion",
    "lobster",
    "shrimp",
    "oyster",
    "clam",
    "squid",
    "seahorse",
    "starfish",
    "coral",
    "plankton",
    "anchor",
    "vessel",
    "captain",
    "crew",
    "island",
    "cargo",
    "shipwreck",
    "treasure",
    "mermaid",
    "buccaneer",
    "pirate",
    "parrot",
    "kraken",
    "seafarer",
    "nautical",
    "compass",
    "map",
    "journey",
    "adventure",
    "legend",
    "folklore",
    "myth",
    "saga",
    "fable",
    "epic",
    "hero",
    "villain",
    "wizard",
    "sorcerer",
    "enchantress",
    "witch",
    "warlock",
    "alchemy",
    "magic",
    "spell",
    "curse",
    "potion",
    "artifact",
    "relic",
    "amulet",
    "charm",
    "scepter",
    "crown",
    "throne",
    "kingdom",
    "realm",
    "empire",
    "dynasty",
    "monarchy",
    "republic",
    "democracy",
    "constitution",
    "treaty",
    "pact",
    "alliance",
    "coalition",
    "war",
    "battle",
    "conflict",
    "revolution",
    "rebellion",
    "crusade",
    "expedition",
    "voyage",
    "exploration",
    "discovery",
    "invention",
    "innovation",
    "technology",
    "engineering",
    "robotics",
    "cybernetics",
    "ai",
    "neuralnetwork",
    "algorithm",
    "computation",
    "simulation",
    "modeling",
    "data",
    "analytics",
    "statistics",
    "probability",
    "geometry",
    "trigonometry",
    "calculus",
    "algebra",
    "numbertheory",
    "topology",
    "logic",
    "settheory",
    "graph",
    "tree",
    "matrix",
    "tensor",
    "vector",
    "scalar",
    "quaternion",
    "complex",
    "imaginary",
    "integer",
    "rational",
    "irrational",
    "prime",
    "fibonacci",
    "sequence",
    "series",
    "fractal",
    "dimension",
    "chaos",
    "order",
    "system",
    "entropy",
    "synthesis",
    "analysis",
    "design",
    "architecture",
    "structure",
    "function",
    "operation",
    "process",
    "mechanism",
    "dynamics",
    "kinematics",
    "statics",
    "thermodynamics",
    "electromagnetism",
    "optics",
    "quantum",
    "relativity",
    "particle",
    "nucleus",
    "proton",
    "neutron",
    "electron",
    "photon",
    "quark",
    "lepton",
    "boson",
    "fermion",
    "string",
    "vibration",
    "resonance",
    "frequency",
    "amplitude",
    "hologram",
    "laser",
    "photonics",
    "nanotechnology",
    "biotechnology",
    "genetics",
    "genome",
    "chromosome",
    "dna",
    "rna",
    "protein",
    "enzyme",
    "cell",
    "organism",
    "species",
    "evolution",
    "ecology",
    "environment",
    "climate",
    "weather",
    "atmosphere",
    "biosphere",
    "geosphere",
    "hydrosphere",
    "lithosphere",
    "cryosphere",
    "exosphere",
    "magnetosphere",
    "ionosphere",
    "stratosphere",
    "troposphere",
    "mesosphere",
    "thermosphere",
    "ozone",
    "greenhouse",
    "carbon",
    "methane",
    "nitrogen"]



async def a_get_spam(length : int) -> str:
    sentence = ""
    word_list = [random.choices(words) for _ in range(length)]
    for word in word_list:
        sentence += word[0] + " "
    return sentence

def get_spam(length : int) -> str:
    sentence = ""
    word_list = [random.choices(words) for _ in range(length)]
    for word in word_list:
        sentence += word[0] + " "
    return sentence

async def get_one_spam() ->str:
    return random.choice(words)

async def main():
    word = await get_spam(10)
    print(word)

if __name__ == "__main__":
    asyncio.run(main())




    

    









