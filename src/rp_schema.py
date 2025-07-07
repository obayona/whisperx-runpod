INPUT_VALIDATIONS = {
    'audio_url': {
        'type': str,
        'required': True
    },
    'language': {
        'type': str,
        'required': False,
        'default': None
    },
    'language_detection_min_prob': {
        'type': float,
        'required': False,
        'default': 0
    },
    'language_detection_max_tries': {
        'type': int,
        'required': False,
        'default': 5
    },
    'initial_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'batch_size': {
        'type': int,
        'required': False,
        'default': 64
    },
    'temperature': {
        'type': float,
        'required': False,
        'default': 0
    },
    'vad_onset': {
        'type': float,
        'required': False,
        'default': 0.500
    },
    'vad_offset': {
        'type': float,
        'required': False,
        'default': 0.363
    },
    'min_speakers': {
        'type': int,
        'required': False,
        'default': 1
    },
    'max_speakers': {
        'type': int,
        'required': False,
        'default': 2
    },
    'debug': {
        'type': bool,
        'required': False,
        'default': False
    }
}