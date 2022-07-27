# STML#AO*LMNW

KEYS = (
	'S-', 'T-', 'M-', 'L-',
	'A-', '#', '*', '-O',
	'-L', '-M', '-N', '-W'
)

IMPLICIT_HYPHEN_KEYS = (
	'A-', '-O', '*', '#'
)

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = '*'

SUFFIX_KEYS = ()

KEYMAPS = {
	'Keyboard': {
		'S-': 'q',
		'T-': 'w',
		'M-': 'e',
		'L-': 'r',
		'#': 't',
		'A-': 'v',
		'-O': 'n',
		'*': 'y',
		'-L': 'u',
		'-M': 'i',
		'-N': 'o',
		'-W': 'p',
		'arpeggiate': 'space',
		'no-op': ('[','a','s','d','f','g','h','j','k','l',';','\'','z','x','c','b','m',',','.','/'),
	},
	'Gemini PR': {
		'#': '*1',
		'S-': 'S1-',
		'T-': 'T-',
		'M-': 'P-',
		'L-': 'H-',
		'A-': 'O-',
		'*': '*3',
		'-O': '-E',
		'-L': '-F',
		'-M': '-P',
		'-N': '-L',
		'-W': '-T',
		'no-op': ('Fn', 'pwr', 'res1', 'res2','*3','*4','#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C','S2-','K-','W-','R-','A-','-U','-R','-B','-G','-S','-D','-Z'),
	}
}

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

DICTIONARIES_ROOT = 'asset:plover_toki_pona_jnl:dictionaries'

DEFAULT_DICTIONARIES = (
	'kipisi_nimi.json', 'nimi_ku_suli.json', 'sitelen.json'
)

