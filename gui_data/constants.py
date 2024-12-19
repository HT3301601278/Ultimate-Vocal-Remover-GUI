import platform

#Platform Details
OPERATING_SYSTEM = platform.system()
SYSTEM_ARCH = platform.platform()
SYSTEM_PROC = platform.processor()
ARM = 'arm'

is_macos = False

CPU = 'cpu'
CUDA_DEVICE = 'cuda'
DIRECTML_DEVICE = "privateuseone"

#MAIN_FONT_NAME = "Century Gothic"
OPT_SEPARATOR_SAVE = '─'*25
BG_COLOR = '#0e0e0f'
FG_COLOR = '#13849f'

#Model Types
VR_ARCH_TYPE = 'VR Architecture'
MDX_ARCH_TYPE = 'MDX-Net'
DEMUCS_ARCH_TYPE = 'Demucs'
VR_ARCH_PM = 'VR Arch'
ENSEMBLE_MODE = '合奏模式'
ENSEMBLE_STEM_CHECK = '合奏检查'
SECONDARY_MODEL = 'Secondary Model'
DEMUCS_6_STEM_MODEL = 'htdemucs_6s'
DEFAULT = "Default"
ALIGNMENT_TOOL = '对齐工具'

SINGLE_FILE = 'SINGLE_FILE'
MULTIPLE_FILE = 'MULTI_FILE'
MAIN_MULTIPLE_FILE = 'MAIN_MULTI_FILE'
CHOOSE_EXPORT_FIR = 'CHOOSE_EXPORT_FIR'

DUAL = "dual"
FOUR_STEM = "fourstem"
ANY_STEM = "Any Stem"

DEMUCS_V3_ARCH_TYPE = 'Demucs v3'
DEMUCS_V4_ARCH_TYPE = 'Demucs v4'
DEMUCS_NEWER_ARCH_TYPES = [DEMUCS_V3_ARCH_TYPE, DEMUCS_V4_ARCH_TYPE]

DEMUCS_V1 = 'v1'
DEMUCS_V2 = 'v2'
DEMUCS_V3 = 'v3'
DEMUCS_V4 = 'v4'

DEMUCS_V1_TAG = 'v1 | '
DEMUCS_V2_TAG = 'v2 | '
DEMUCS_V3_TAG = 'v3 | '
DEMUCS_V4_TAG = 'v4 | '
DEMUCS_NEWER_TAGS = [DEMUCS_V3_TAG, DEMUCS_V4_TAG]

DEMUCS_VERSION_MAPPER = {
            DEMUCS_V1:DEMUCS_V1_TAG,
            DEMUCS_V2:DEMUCS_V2_TAG,
            DEMUCS_V3:DEMUCS_V3_TAG,
            DEMUCS_V4:DEMUCS_V4_TAG}

#Download Center
DOWNLOAD_FAILED = '下载失败'
DOWNLOAD_STOPPED = '下载已停止'
DOWNLOAD_COMPLETE = '下载完成'
DOWNLOAD_UPDATE_COMPLETE = '更新下载完成'
SETTINGS_MENU_EXIT = '退出'
NO_CONNECTION = '无网络连接'
VIP_SELECTION = 'VIP:'
DEVELOPER_SELECTION = 'VIP:'
NO_NEW_MODELS = '所有可用模型已下载'
ENSEMBLE_PARTITION = ': '
NO_MODEL = '未选择模型'
CHOOSE_MODEL = '选择模型'
SINGLE_DOWNLOAD = '正在下载项目 1/1...'
DOWNLOADING_ITEM = '正在下载项目'
FILE_EXISTS = '文件已存在!'
DOWNLOADING_UPDATE = '正在下载更新...'
DOWNLOAD_MORE = '下载更多模型'
IS_KARAOKEE = "is_karaoke"
IS_BV_MODEL = "is_bv_model"
IS_BV_MODEL_REBAL = "is_bv_model_rebalanced"
INPUT_STEM_NAME = '输入音轨名称'

#Menu Options

AUTO_SELECT = '自动'

#LINKS
DOWNLOAD_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/filelists/download_checks.json"
MDX_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_data_new.json"
VR_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/vr_model_data/model_data_new.json"
MDX23_CONFIG_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/mdx_c_configs/"
BULLETIN_CHECK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/bulletin.txt"

DEMUCS_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/demucs_model_data/model_name_mapper.json"
MDX_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_name_mapper.json"

DONATE_LINK_BMAC = "https://www.buymeacoffee.com/uvr5"
DONATE_LINK_PATREON = "https://www.patreon.com/uvr"

#DOWNLOAD REPOS
NORMAL_REPO = "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/"
UPDATE_REPO = "https://github.com/TRvlvr/model_repo/releases/download/uvr_update_patches/"

UPDATE_MAC_ARM_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg"
UPDATE_MAC_X86_64_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg"
UPDATE_LINUX_REPO = "https://github.com/Anjok07/ultimatevocalremovergui#linux-installation"

ISSUE_LINK = 'https://github.com/Anjok07/ultimatevocalremovergui/issues/new'
VIP_REPO = b'\xf3\xc2W\x19\x1foI)\xc2\xa9\xcc\xb67(Z\xf5',\
           b'gAAAAABjQAIQ-NpNMMxMedpKHHb7ze_nqB05hw0YhbOy3pFzuzDrfqumn8_qvraxEoUpZC5ZXC0gGvfDxFMqyq9VWbYKlA67SUFI_wZB6QoVyGI581vs7kaGfUqlXHIdDS6tQ_U-BfjbEAK9EU_74-R2zXjz8Xzekw=='
NO_CODE = 'incorrect_code'

#Extensions
ONNX = '.onnx'
CKPT = '.ckpt'
CKPT_C = '.ckptc'
YAML = '.yaml'
PTH = '.pth'
TH_EXT = '.th'
JSON = '.json'

#GUI Buttons
START_PROCESSING = 'Start Processing'
WAIT_PROCESSING = 'Please wait...'
STOP_PROCESSING = 'Halting process, please wait...'
LOADING_MODELS = '正在加载模型...'

#---Messages and Logs----

MISSING_MODEL = 'missing'
MODEL_PRESENT = 'present'

# 音轨类型
ALL_STEMS = '所有音轨'
VOCAL_STEM = '人声'
INST_STEM = '伴奏'
OTHER_STEM = '其他'
BASS_STEM = '贝斯'
DRUM_STEM = '鼓点'
GUITAR_STEM = '吉他'
PIANO_STEM = '钢琴'
SYNTH_STEM = '合成器'
STRINGS_STEM = '弦乐'
WOODWINDS_STEM = '木管乐器'
BRASS_STEM = '铜管乐器'
WIND_INST_STEM = '管乐器'

# 无某音轨标记
NO_OTHER_STEM = '无其他'
NO_BASS_STEM = '无贝斯'
NO_DRUM_STEM = '无鼓点'
NO_GUITAR_STEM = '无吉他'
NO_PIANO_STEM = '无钢琴'
NO_SYNTH_STEM = '无合成器'
NO_STRINGS_STEM = '无弦乐'
NO_WOODWINDS_STEM = '无木管'
NO_WIND_INST_STEM = '无管乐'
NO_BRASS_STEM = '无铜管'

# 主次音轨
PRIMARY_STEM = '主要音轨'
SECONDARY_STEM = '次要音轨'
LEAD_VOCAL_STEM = '主唱人声'
BV_VOCAL_STEM = '和声'
LEAD_VOCAL_STEM_I = '包含主唱'
BV_VOCAL_STEM_I = '包含和声'
LEAD_VOCAL_STEM_LABEL = '主唱人声'
BV_VOCAL_STEM_LABEL = '和声'

# 音轨组合标记
VOCAL_STEM_ONLY = f'{VOCAL_STEM}独立'
INST_STEM_ONLY = f'{INST_STEM}独立'
PRIMARY_STEM_ONLY = f'{PRIMARY_STEM}独立'

# 保存选项
IS_SAVE_INST_ONLY = '仅保存伴奏'
IS_SAVE_VOC_ONLY = '仅保存人声'

# 去混响映射
DEVERB_MAPPER = {
    '仅主要人声':VOCAL_STEM, 
    '仅主唱人声':LEAD_VOCAL_STEM_LABEL, 
    '仅和声':BV_VOCAL_STEM_LABEL, 
    '所有人声类型':'ALL'
}

# 平衡值
BALANCE_VALUES = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#Other Constants
DEMUCS_2_SOURCE = ["instrumental", "vocals"]
DEMUCS_4_SOURCE = ["drums", "bass", "other", "vocals"]

DEMUCS_2_SOURCE_MAPPER = {
                        INST_STEM: 0,
                        VOCAL_STEM: 1}

DEMUCS_4_SOURCE_MAPPER = {
                        BASS_STEM: 0,
                        DRUM_STEM: 1,
                        OTHER_STEM: 2,
                        VOCAL_STEM: 3}

DEMUCS_6_SOURCE_MAPPER = {
                        BASS_STEM:0,
                        DRUM_STEM:1,
                        OTHER_STEM:2,
                        VOCAL_STEM:3,
                        GUITAR_STEM:4,
                        PIANO_STEM:5}

DEMUCS_4_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM]
DEMUCS_6_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM, GUITAR_STEM, PIANO_STEM]

DEMUCS_UVR_MODEL = 'UVR_Model'

CHOOSE_STEM_PAIR = '选择音轨对'

STEM_SET_MENU = (VOCAL_STEM, 
                 INST_STEM, 
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM, 
                 WIND_INST_STEM)

STEM_SET_MENU_ONLY = list(STEM_SET_MENU) + [OPT_SEPARATOR_SAVE, INPUT_STEM_NAME]

STEM_SET_MENU_2 = (
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM, 
                 WIND_INST_STEM,
                 "噪音",
                 "混响")

STEM_PAIR_MAPPER = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            LEAD_VOCAL_STEM: BV_VOCAL_STEM,
            BV_VOCAL_STEM: LEAD_VOCAL_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

STEM_PAIR_MAPPER_FULL = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            OTHER_STEM: NO_OTHER_STEM,
            BASS_STEM: NO_BASS_STEM,
            DRUM_STEM: NO_DRUM_STEM,
            GUITAR_STEM: NO_GUITAR_STEM,
            PIANO_STEM: NO_PIANO_STEM,
            SYNTH_STEM: NO_SYNTH_STEM,
            STRINGS_STEM: NO_STRINGS_STEM,
            WOODWINDS_STEM: NO_WOODWINDS_STEM,
            BRASS_STEM: NO_BRASS_STEM,
            WIND_INST_STEM: NO_WIND_INST_STEM,
            NO_OTHER_STEM: OTHER_STEM,
            NO_BASS_STEM: BASS_STEM,
            NO_DRUM_STEM: DRUM_STEM,
            NO_GUITAR_STEM: GUITAR_STEM,
            NO_PIANO_STEM: PIANO_STEM,
            NO_SYNTH_STEM: SYNTH_STEM,
            NO_STRINGS_STEM: STRINGS_STEM,
            NO_WOODWINDS_STEM: WOODWINDS_STEM,
            NO_BRASS_STEM: BRASS_STEM,
            NO_WIND_INST_STEM: WIND_INST_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

NO_STEM = "无 "

NON_ACCOM_STEMS = (
            VOCAL_STEM,
            OTHER_STEM,
            BASS_STEM,
            DRUM_STEM,
            GUITAR_STEM,
            PIANO_STEM,
            SYNTH_STEM,
            STRINGS_STEM,
            WOODWINDS_STEM,
            BRASS_STEM,
            WIND_INST_STEM)

MDX_NET_FREQ_CUT = [VOCAL_STEM, INST_STEM]

DEMUCS_4_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM)
DEMUCS_6_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM, GUITAR_STEM, PIANO_STEM)
DEMUCS_2_STEM_OPTIONS = (VOCAL_STEM, INST_STEM)
DEMUCS_4_STEM_CHECK = (OTHER_STEM, BASS_STEM, DRUM_STEM)

#Menu Dropdowns

VOCAL_PAIR = f'{VOCAL_STEM}/{INST_STEM}'
INST_PAIR = f'{INST_STEM}/{VOCAL_STEM}'
OTHER_PAIR = f'{OTHER_STEM}/{NO_OTHER_STEM}'
DRUM_PAIR = f'{DRUM_STEM}/{NO_DRUM_STEM}'
BASS_PAIR = f'{BASS_STEM}/{NO_BASS_STEM}'
FOUR_STEM_ENSEMBLE = '四音轨合奏'
MULTI_STEM_ENSEMBLE = '多音轨合奏'

ENSEMBLE_MAIN_STEM = (CHOOSE_STEM_PAIR, VOCAL_PAIR, OTHER_PAIR, DRUM_PAIR, BASS_PAIR, FOUR_STEM_ENSEMBLE, MULTI_STEM_ENSEMBLE)

MIN_SPEC = '最小频谱'
MAX_SPEC = '最大频谱'
AUDIO_AVERAGE = '平均值'

MAX_MIN = f'{MAX_SPEC}/{MIN_SPEC}'
MAX_MAX = f'{MAX_SPEC}/{MAX_SPEC}'
MAX_AVE = f'{MAX_SPEC}/{AUDIO_AVERAGE}'
MIN_MAX = f'{MIN_SPEC}/{MAX_SPEC}'
MIN_MIX = f'{MIN_SPEC}/{MIN_SPEC}'
MIN_AVE = f'{MIN_SPEC}/{AUDIO_AVERAGE}'
AVE_MAX = f'{AUDIO_AVERAGE}/{MAX_SPEC}'
AVE_MIN = f'{AUDIO_AVERAGE}/{MIN_SPEC}'
AVE_AVE = f'{AUDIO_AVERAGE}/{AUDIO_AVERAGE}'

ENSEMBLE_TYPE = (MAX_MIN, MAX_MAX, MAX_AVE, MIN_MAX, MIN_MIX, MIN_AVE, AVE_MAX, AVE_MIN, AVE_AVE)
ENSEMBLE_TYPE_4_STEM = (MAX_SPEC, MIN_SPEC, AUDIO_AVERAGE)

BATCH_MODE = '批处理模式'
BETA_VERSION = '测试版'
DEF_OPT = '默认'
USER_INPUT = "用户输入"
OPT_SEPARATOR = '─'*65

CHUNKS = (AUTO_SELECT, '1', '5', '10', '15', '20', 
          '25', '30', '35', '40', '45', '50', 
          '55', '60', '65', '70', '75', '80', 
          '85', '90', '95', '完整')

BATCH_SIZE = (DEF_OPT, '2', '3', '4', '5', 
              '6', '7', '8', '9', '10')

VOL_COMPENSATION = (AUTO_SELECT, '1.035', '1.08')

MARGIN_SIZE = ('44100', '22050', '11025')

AUDIO_TOOLS = '音频工具'

MANUAL_ENSEMBLE = '手动合奏'
TIME_STRETCH = '时间拉伸'
CHANGE_PITCH = '音调变更'
ALIGN_INPUTS = '输入对齐'
MATCH_INPUTS = '音频匹配'
COMBINE_INPUTS = '输入合并'

if OPERATING_SYSTEM == 'Windows' or OPERATING_SYSTEM == 'Darwin':  
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, TIME_STRETCH, CHANGE_PITCH, ALIGN_INPUTS, MATCH_INPUTS)
else:
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, ALIGN_INPUTS, MATCH_INPUTS)

MANUAL_ENSEMBLE_OPTIONS = (MIN_SPEC, MAX_SPEC, AUDIO_AVERAGE, COMBINE_INPUTS)

PROCESS_METHODS = (VR_ARCH_PM, MDX_ARCH_TYPE, DEMUCS_ARCH_TYPE, ENSEMBLE_MODE, AUDIO_TOOLS)

DEMUCS_SEGMENTS = (DEF_OPT, '1', '5', '10', '15', '20', 
                  '25', '30', '35', '40', '45', '50', 
                  '55', '60', '65', '70', '75', '80', 
                  '85', '90', '95', '100')

DEMUCS_SHIFTS = (0, 1, 2, 3, 4, 5, 
                 6, 7, 8, 9, 10, 11, 
                 12, 13, 14, 15, 16, 17, 
                 18, 19, 20)

SEMI_DEF = ['0']
SEMITONE_SEL = (-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12)

NOUT_SEL = (8, 16, 32, 48, 64)
NOUT_LSTM_SEL = (64, 128)

DEMUCS_OVERLAP = (0.25, 0.50, 0.75, 0.99)
MDX_OVERLAP = (DEF_OPT, 0.25, 0.50, 0.75, 0.99)
MDX23_OVERLAP = range(2, 51)
VR_AGGRESSION = range(0, 51)

TIME_WINDOW_MAPPER = {
    "None": None,
    "1": [0.0625],
    "2": [0.125],
    "3": [0.25],
    "4": [0.5],
    "5": [0.75],
    "6": [1],
    "7": [2],
    "Shifts: Low": [0.0625, 0.5],
    "Shifts: Medium": [0.0625, 0.125, 0.5],
    "Shifts: High": [0.0625, 0.125, 0.25, 0.5]
}

INTRO_MAPPER = {
    "Default": [10],
    "1": [8],
    "2": [6],
    "3": [4],
    "4": [2],
    "Shifts: Low": [1, 10],
    "Shifts: Medium": [1, 10, 8],
    "Shifts: High": [1, 10, 8, 6, 4]
}

VOLUME_MAPPER = {
    "None": (0, [0]),
    "Low": (-4, range(0, 8)),
    "Medium": (-6, range(0, 12)),
    "High": (-6, [x * 0.5 for x in range(0, 25)]),
    "Very High": (-10, [x * 0.5 for x in range(0, 41)])
}

PHASE_MAPPER = {
    "None": [0],
    "Shifts Low": [0, 180],
    "Shifts Medium": [0],
    "Shifts High": [0],
    "Shifts Very High": [0]
}

NONE_P = "无"
VLOW_P = "移动: 极低"
LOW_P = "移动: 低"
MED_P = "移动: 中"
HIGH_P = "移动: 高"
VHIGH_P = "移动: 极高"
VMAX_P = "移动: 最大"

PHASE_SHIFTS_OPT = {
    NONE_P: 190,
    VLOW_P: 180,
    LOW_P: 90,
    MED_P: 45,
    HIGH_P: 20,
    VHIGH_P: 10,
    VMAX_P: 1
}

VR_WINDOW = ('320', '512','1024')
VR_CROP = ('256', '512', '1024')
POST_PROCESSES_THREASHOLD_VALUES = ('0.1', '0.2', '0.3')

MDX_POP_PRO = ('MDX-NET_噪声配置_14_kHz', 'MDX-NET_噪声配置_17_kHz', 'MDX-NET_噪声配置_全频段')
MDX_POP_STEMS = ('人声', '伴奏', '其他', '鼓点', '贝斯')
MDX_POP_NFFT = ('4096', '5120', '6144', '7680', '8192', '16384')
MDX_POP_DIMF = ('2048', '3072', '4096')
DENOISE_NONE, DENOISE_S, DENOISE_M = '无', '标准', '降噪模型'
MDX_DENOISE_OPTION = [DENOISE_NONE, DENOISE_S, DENOISE_M]
MDX_SEGMENTS = list(range(32, 4000+1, 32))

SAVE_ENSEMBLE = '保存合奏'
CLEAR_ENSEMBLE = '清除选择'
MENU_SEPARATOR = 35*'•'
CHOOSE_ENSEMBLE_OPTION = '选择选项'
ALL_TYPES = '全部'
INVALID_ENTRY = '输入无效，请重试'
ENSEMBLE_INPUT_RULE = '1. 仅允许字母、数字、空格和横线。\n2. 开头和结尾不能有横线或空格。'
STEM_INPUT_RULE = '1. 仅允许无空格的单词。\n2. 不允许空格、数字或特殊字符。'

ENSEMBLE_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_ENSEMBLE, CLEAR_ENSEMBLE]
ENSEMBLE_CHECK = '合奏检查'
KARAOKEE_CHECK = '卡拉OK检查'

AUTO_PHASE = "自动"
POSITIVE_PHASE = "正相位"
NEGATIVE_PHASE = "负相位"
OFF_PHASE = "原生相位"

ALIGN_PHASE_OPTIONS = [AUTO_PHASE, POSITIVE_PHASE, NEGATIVE_PHASE, OFF_PHASE]

SELECT_SAVED_ENSEMBLE = '选择已保存的合奏'
SELECT_SAVED_SETTING = '选择已保存的设置'
ENSEMBLE_OPTION = "合奏自定义选项"
MDX_OPTION = "MDX-Net高级选项"
DEMUCS_OPTION = "Demucs高级选项"
VR_OPTION = "VR高级选项"
HELP_OPTION = "打开帮助指南"
ERROR_OPTION = "打开错误日志"
VERIFY_BEGIN = '正在验证文件 '
SAMPLE_BEGIN = '正在创建样本 '
MODEL_MISSING_CHECK = '模型缺失:'
OPTION_LIST = [VR_OPTION, MDX_OPTION, DEMUCS_OPTION, ENSEMBLE_OPTION, ALIGNMENT_TOOL, HELP_OPTION, ERROR_OPTION]

#Menu Strings
VR_MENU ='VR菜单'
DEMUCS_MENU ='Demucs菜单'
MDX_MENU ='MDX-Net菜单'
ENSEMBLE_MENU ='合奏菜单'
HELP_MENU ='帮助菜单'
ERROR_MENU ='错误日志'
INPUTS_MENU ='输入菜单'
ALIGN_MENU ='对齐菜单'

# Audio Player
PLAYING_SONG = ": 播放中"
PAUSE_SONG = ": 已暂停"
STOP_SONG = ": 已停止"

SELECTED_VER = '已选择'
DETECTED_VER = '已检测'

SAMPLE_MODE_CHECKBOX = lambda v:f'样本模式 ({v}秒)'
REMOVED_FILES = lambda r, e:f'音频输入验证报告:\n\n已移除文件:\n\n{r}\n\n错误详情:\n\n{e}'
ADVANCED_SETTINGS = (ENSEMBLE_OPTION, MDX_OPTION, DEMUCS_OPTION, VR_OPTION, HELP_OPTION, ERROR_OPTION)

# 音频格式
WAV = 'WAV'
FLAC = 'FLAC'
MP3 = 'MP3'

# 音频参数选项
MP3_BIT_RATES = ('96k', '128k', '160k', '224k', '256k', '320k')
WAV_TYPE = ('PCM_U8', 'PCM_16', 'PCM_24', 'PCM_32', '32位浮点', '64位浮点')
GPU_DEVICE_NUM_OPTS = (DEFAULT, '0', '1', '2', '3', '4', '5', '6', '7', '8')

# 设置选项
SELECT_SAVED_SET = '选择选项'
SAVE_SETTINGS = '保存当前设置'
RESET_TO_DEFAULT = '重置为默认'
RESET_FULL_TO_DEFAULT = '重置为默认'
RESET_PM_TO_DEFAULT = '重置所有应用设置为默认'

SAVE_SET_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_SETTINGS, RESET_TO_DEFAULT]

# 时间和音高
TIME_PITCH = ('1.0', '2.0', '3.0', '4.0')
TIME_TEXT = '_时间拉伸'
PITCH_TEXT = '_音高偏移'

#RegEx Input Validation
REG_PITCH = r'^[-+]?(1[0]|[0-9]([.][0-9]*)?)$'  # 音高验证
REG_TIME = r'^[+]?(1[0]|[0-9]([.][0-9]*)?)$'  # 时间验证
REG_COMPENSATION = r'\b^(1[0]|[0-9]([.][0-9]*)?|自动|无)$\b'  # 补偿验证
REG_THES_POSTPORCESS = r'\b^([0]([.][0-9]{0,6})?)$\b'  # 后处理阈值验证
REG_CHUNKS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|自动|完整)$\b'  # 分块验证
REG_CHUNKS_DEMUCS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|自动|完整)$\b'  # Demucs分块验证
REG_MARGIN = r'\b^[0-9]*$\b'  # 边缘验证
REG_SEGMENTS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|默认)$\b'  # 分段验证
REG_SAVE_INPUT = r'\b^([a-zA-Z0-9 -]{0,25})$\b'  # 保存输入验证
REG_INPUT_STEM_NAME = r'^(管乐器|[a-zA-Z]{1,25})$'  # 音轨名称验证
REG_SEMITONES = r'^-?(20\.00|[01]?\d(\.\d{1,2})?|20)$'  # 半音验证
REG_AGGRESSION = r'^[-+]?[0-9]\d*?$'  # 激进度验证
REG_WINDOW = r'\b^[0-9]{0,4}$\b'  # 窗口验证
REG_SHIFTS = r'\b^[0-9]*$\b'  # 移位验证
REG_BATCHES = r'\b^([0-9]*?|默认)$\b'  # 批次验证
REG_OVERLAP = r'\b^([0]([.][0-9]{0,6})?|默认)$\b'  # 重叠验证
REG_OVERLAP23 = r'\b^([1][0-9]|[2-9][0-9]*|默认)$\b'  # 重叠23验证
REG_MDX_SEG = r'\b(?:' + '|'.join([str(num) for num in range(32, 1000001, 32)]) + r')\b'  # MDX分段验证
REG_ALIGN = r'^[-+]?[0-9]\d*?$'  # 对齐验证
REG_VOL_COMP = r'^\d+\.\d{1,9}$'  # 音量补偿验证

# 子菜单
VR_ARCH_SETTING_LOAD = '加载VR架构设置'
MDX_SETTING_LOAD = '加载MDX-Net设置'
DEMUCS_SETTING_LOAD = '加载Demucs设置'
ALL_ARCH_SETTING_LOAD = '加载完整应用设置'

# 默认数据
DEFAULT_DATA = {
    'chosen_process_method': MDX_ARCH_TYPE,
    'vr_model': CHOOSE_MODEL,
    'aggression_setting': 5,
    'window_size': 512,
    'mdx_segment_size': 256,
    'batch_size': DEF_OPT,
    'crop_size': 256, 
    'is_tta': False,
    'is_output_image': False,
    'is_post_process': False,
    'is_high_end_process': False,
    'post_process_threshold': 0.2,
    'vr_voc_inst_secondary_model': NO_MODEL,
    'vr_other_secondary_model': NO_MODEL,
    'vr_bass_secondary_model': NO_MODEL,
    'vr_drums_secondary_model': NO_MODEL,
    'vr_is_secondary_model_activate': False,        
    'vr_voc_inst_secondary_model_scale': 0.9,
    'vr_other_secondary_model_scale': 0.7,
    'vr_bass_secondary_model_scale': 0.5,
    'vr_drums_secondary_model_scale': 0.5,
    'demucs_model': CHOOSE_MODEL,
    'segment': DEMUCS_SEGMENTS[0],
    'overlap': DEMUCS_OVERLAP[0],
    'overlap_mdx': MDX_OVERLAP[0],
    'overlap_mdx23': '8',
    'shifts': 2,
    'chunks_demucs': CHUNKS[0],
    'margin_demucs': 44100,
    'is_chunk_demucs': False,
    'is_chunk_mdxnet': False,
    'is_primary_stem_only_Demucs': False,
    'is_secondary_stem_only_Demucs': False,
    'is_split_mode': True,
    'is_demucs_combine_stems': True,
    'is_mdx23_combine_stems': True,
    'demucs_voc_inst_secondary_model': NO_MODEL,
    'demucs_other_secondary_model': NO_MODEL,
    'demucs_bass_secondary_model': NO_MODEL,
    'demucs_drums_secondary_model': NO_MODEL,
    'demucs_is_secondary_model_activate': False,
    'demucs_voc_inst_secondary_model_scale': 0.9,
    'demucs_other_secondary_model_scale': 0.7,
    'demucs_bass_secondary_model_scale': 0.5,
    'demucs_drums_secondary_model_scale': 0.5,
    'demucs_stems': ALL_STEMS,
    'demucs_pre_proc_model': NO_MODEL,
    'is_demucs_pre_proc_model_activate': False,
    'is_demucs_pre_proc_model_inst_mix': False,
    'mdx_net_model': CHOOSE_MODEL,
    'chunks': CHUNKS[0],
    'margin': 44100,
    'compensate': AUTO_SELECT,
    'is_denoise': False,
    'denoise_option': '无',
    'phase_option': AUTO_PHASE,
    'phase_shifts': NONE_P,
    'is_save_align': False,
    'is_match_frequency_pitch': True,
    'is_match_silence': True,
    'is_spec_match': False,
    'is_mdx_c_seg_def': False,
    'is_invert_spec': False,
    'is_deverb_vocals': False,
    'deverb_vocal_opt': '仅主要人声',
    'voc_split_save_opt': '仅主唱',
    'is_mixer_mode': False,
    'mdx_batch_size': DEF_OPT,
    'mdx_voc_inst_secondary_model': NO_MODEL,
    'mdx_other_secondary_model': NO_MODEL,
    'mdx_bass_secondary_model': NO_MODEL,
    'mdx_drums_secondary_model': NO_MODEL,
    'mdx_is_secondary_model_activate': False,
    'mdx_voc_inst_secondary_model_scale': 0.9,
    'mdx_other_secondary_model_scale': 0.7,
    'mdx_bass_secondary_model_scale': 0.5,
    'mdx_drums_secondary_model_scale': 0.5,
    'mdx_stems': ALL_STEMS,
    'is_save_all_outputs_ensemble': True,
    'is_append_ensemble_name': False,
    'chosen_audio_tool': AUDIO_TOOL_OPTIONS[0],
    'choose_algorithm': MANUAL_ENSEMBLE_OPTIONS[0],
    'time_stretch_rate': 2.0,
    'pitch_rate': 2.0,
    'is_time_correction': True,
    'is_gpu_conversion': False,
    'is_primary_stem_only': False,
    'is_secondary_stem_only': False,
    'is_testing_audio': False,
    'is_auto_update_model_params': True,
    'is_add_model_name': False,
    'is_accept_any_input': False,
    'is_task_complete': False,
    'is_normalization': False,
    'is_use_opencl': False,
    'is_wav_ensemble': False,
    'is_create_model_folder': False,
    'mp3_bit_set': '320k',
    'semitone_shift': '0',
    'save_format': WAV,
    'wav_type_set': 'PCM_16',
    'device_set': DEFAULT,
    'user_code': '',
    'export_path': '',
    'input_paths': [],
    'lastDir': None,
    'time_window': "3",
    'intro_analysis': DEFAULT,
    'db_analysis': "中等",
    'fileOneEntry': '',
    'fileOneEntry_Full': '',
    'fileTwoEntry': '',
    'fileTwoEntry_Full': '',
    'DualBatch_inputPaths': [],
    'model_hash_table': {},
    'help_hints_var': True,
    'set_vocal_splitter': NO_MODEL,
    'is_set_vocal_splitter': False,
    'is_save_inst_set_vocal_splitter': False,
    'model_sample_mode': False,
    'model_sample_mode_duration': 30
}

SETTING_CHECK = ('vr_model',
               'aggression_setting',
               'window_size',
               'mdx_segment_size',
               'batch_size',
               'crop_size',
               'is_tta',
               'is_output_image',
               'is_post_process',
               'is_high_end_process',
               'post_process_threshold',
               'vr_voc_inst_secondary_model',
               'vr_other_secondary_model',
               'vr_bass_secondary_model',
               'vr_drums_secondary_model',
               'vr_is_secondary_model_activate',
               'vr_voc_inst_secondary_model_scale',
               'vr_other_secondary_model_scale',
               'vr_bass_secondary_model_scale',
               'vr_drums_secondary_model_scale',
               'demucs_model',
               'segment',
               'overlap',
               'overlap_mdx',
               'shifts',
               'chunks_demucs',
               'margin_demucs',
               'is_chunk_demucs',
               'is_primary_stem_only_Demucs',
               'is_secondary_stem_only_Demucs',
               'is_split_mode',
               'is_demucs_combine_stems',#
               'is_mdx23_combine_stems',#
               'demucs_voc_inst_secondary_model',
               'demucs_other_secondary_model',
               'demucs_bass_secondary_model',
               'demucs_drums_secondary_model',
               'demucs_is_secondary_model_activate',
               'demucs_voc_inst_secondary_model_scale',
               'demucs_other_secondary_model_scale',
               'demucs_bass_secondary_model_scale',
               'demucs_drums_secondary_model_scale',
               'demucs_stems',
               'mdx_net_model',
               'chunks',
               'margin',
               'compensate',
               'is_denoise',#
               'denoise_option',#
               'phase_option',#
               'phase_shifts',#
               'is_save_align',#,
               'is_match_silence',
               'is_spec_match',#,
               'is_match_frequency_pitch',#
               'is_mdx_c_seg_def',
               'is_invert_spec',#
               'is_deverb_vocals',#
               'deverb_vocal_opt',#
               'voc_split_save_opt',#
               'mdx_batch_size',
               'mdx_voc_inst_secondary_model',
               'mdx_other_secondary_model',
               'mdx_bass_secondary_model',
               'mdx_drums_secondary_model',
               'mdx_is_secondary_model_activate',
               'mdx_voc_inst_secondary_model_scale',
               'mdx_other_secondary_model_scale',
               'mdx_bass_secondary_model_scale',
               'mdx_drums_secondary_model_scale',
               'is_save_all_outputs_ensemble',
               'is_append_ensemble_name',
               'chosen_audio_tool',
               'choose_algorithm',
               'time_stretch_rate',
               'pitch_rate',
               'is_time_correction',
               'is_primary_stem_only',
               'is_secondary_stem_only',
               'is_testing_audio',#
               'is_auto_update_model_params',#
               'is_add_model_name',
               "is_accept_any_input",
               'is_task_complete',
               'is_create_model_folder',
               'mp3_bit_set',#
               'semitone_shift',#
               'save_format',
               'wav_type_set',
               'device_set',
               'user_code',
               'is_gpu_conversion',
               'is_normalization',
               'is_use_opencl',
               'is_wav_ensemble',
               'help_hints_var',
               'set_vocal_splitter',
               'is_set_vocal_splitter',#
               'is_save_inst_set_vocal_splitter',#
               'model_sample_mode',
               'model_sample_mode_duration',
               'time_window',
               'intro_analysis',
               'db_analysis',
               'fileOneEntry',
               'fileOneEntry_Full',
               'fileTwoEntry',
               'fileTwoEntry_Full',
               'DualBatch_inputPaths'
               )

NEW_LINES = "\n\n"
NEW_LINE = "\n"
NO_LINE = ''

FFMPEG_EXT = (".aac", ".aiff", ".alac" ,".flac", ".FLAC", ".mov", ".mp4", ".MP4", 
              ".m4a", ".M4A", ".mp2", ".mp3", "MP3", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".OGG", ".tta", ".wav", ".wave", ".WAV", ".WAVE", ".wma", ".webm", ".eac3", ".mkv", ".opus", ".OPUS")

FFMPEG_MORE_EXT = (".aa", ".aac", ".ac3", ".aiff", ".alac", ".avi", ".f4v",".flac", ".flic", ".flv",
              ".m4v",".mlv", ".mov", ".mp4", ".m4a", ".mp2", ".mp3", ".mp4", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".tta", ".tty", ".vcd", ".wav", ".wma")
ANY_EXT = ""

# Secondary Menu Constants

VOCAL_PAIR_PLACEMENT = 1, 2, 3, 4
OTHER_PAIR_PLACEMENT = 5, 6, 7, 8
BASS_PAIR_PLACEMENT = 9, 10, 11, 12
DRUMS_PAIR_PLACEMENT = 13, 14, 15, 16

# Drag n Drop String Checks

DOUBLE_BRACKET = "} {"
RIGHT_BRACKET = "}"
LEFT_BRACKET = "{"
#DND CONSTS

MAC_DND_CHECK = ('/Users/',
                 '/Applications/',
                 '/Library/',
                 '/System/')
LINUX_DND_CHECK = ('/home/',
                   '/usr/')
WINDOWS_DND_CHECK = ('A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:')

WOOD_INST_MODEL_HASH = '0ec76fd9e65f81d8b4fbd13af4826ed8'
WOOD_INST_PARAMS = {
    "vr_model_param": "4band_v3",
    "primary_stem": NO_WIND_INST_STEM
                     }

READ_ONLY = 'readonly'

FILE_1 = 'file1'
FILE_2 = 'file2'

FILE_1_LB = 'file1_lb'
FILE_2_LB = 'file1_2b'
BATCH_MODE_DUAL = " : 批处理模式"

CODEC_DICT = {
    'PCM_U8':   {"sample_width": 1, "codec": None},        # 8-bit unsigned PCM
    'PCM_16':   {"sample_width": 2, "codec": None},        # 16-bit signed PCM
    'PCM_24':   {"sample_width": 3, "codec": None},        # 24-bit signed PCM
    'PCM_32':   {"sample_width": 4, "codec": None},        # 32-bit signed PCM
    'FLOAT32':  {"sample_width": None, "codec": "pcm_f32le"},  # 32-bit float
    'FLOAT64':  {"sample_width": None, "codec": "pcm_f64le"}   # 64-bit float
}


# Manual Downloads
VR_PLACEMENT_TEXT = '将模型放置在 "models/VR_Models" 目录中。'
MDX_PLACEMENT_TEXT = '将模型放置在 "models/MDX_Net_Models" 目录中。'
DEMUCS_PLACEMENT_TEXT = '将模型放置在 "models/Demucs_Models" 目录中。'
DEMUCS_V3_V4_PLACEMENT_TEXT = '将项目放置在 "models/Demucs_Models/v3_v4_repo" 目录中。'
MDX_23_NAME = "MDX23C 模型"

# Liscense info
if OPERATING_SYSTEM=="Darwin":
   is_macos = True
   LICENSE_OS_SPECIFIC_TEXT = '• 此应用程序适用于运行 macOS Catalina 及更高版本的用户。\n' +\
                              '• 不保证运行 macOS Mojave 或更低版本的系统的应用程序功能。\n' +\
                              '• 不保证运行旧系统或预算 Mac 系统的应用程序功能。\n\n'
elif OPERATING_SYSTEM=="Linux":
   LICENSE_OS_SPECIFIC_TEXT = '• 此应用程序适用于运行 Linux Ubuntu 18.04+ 的用户。\n' +\
                              '• 不保证运行其他 Linux 平台的系统的应用程序功能。\n' +\
                              '• 不保证运行旧系统或预算系统的应用程序功能。\n\n'
elif OPERATING_SYSTEM=="Windows":
   LICENSE_OS_SPECIFIC_TEXT = '• 此应用程序适用于运行 Windows 10 或更高版本的用户。\n' +\
                              '• 不保证运行 Windows 7 或更低版本的系统的应用程序功能。\n' +\
                              '• 不保证运行 Intel Pentium & Celeron CPUs 系统的应用程序功能。\n\n'

LICENSE_TEXT = lambda a, p:f'当前应用程序版本: Ultimate Vocal Remover {a}\n' +\
               f'当前补丁版本: {p}\n\n' +\
               'Copyright (c) 2022 Ultimate Vocal Remover\n\n' +\
               'UVR 是免费开源的，但 MIT 许可的。请在未与 UVR 相关的项目中使用我们的\n' +\
               f'模型或代码时给予我们信用。\n\n{LICENSE_OS_SPECIFIC_TEXT}' +\
               '此捆绑包包含运行应用程序所需的 UVR 界面、Python、PyTorch 和其他\n' +\
               '依赖项。\n\n' +\
               '网站链接: 此应用程序、系统或服务(s)可能包含链接到\n' +\
               '其他网站和下载，并且仅为您提供了额外的便利。您理解并确认，通过单击\n' +\
               '或激活这些链接，您正在访问此应用程序之外的站点或服务，并且我们不会筛选、审查、批准或以任何方式\n' +\
               '认可这些链接网站中包含的任何内容或信息。\n' +\
               '您确认并同意，我们、我们的附属公司和合作伙伴对这些链接网站中包含的任何内容，包括\n' +\
               '这些链接网站提供的信息的准确性或可用性，以及我们对您使用\n' +\
               '这些链接网站的任何行为不承担任何责任。\n\n' +\
               '此应用程序是 MIT 许可的\n\n' +\
               '特此免费授予任何获得本软件副本和\n' +\
               '相关文档文件(以下简称 "软件")的人，无限制地处理该软件，包括但不限于权利\n' +\
               '使用、复制、修改、合并、发布、分发、再许可和/或出售\n' +\
               '软件的副本，并允许将软件提供给他人，前提是\n' +\
               '以下条件：\n\n' +\
               '上述版权声明和本许可声明应包含在所有\n' +\
               '软件的副本或实质部分。\n\n' +\
               '本软件"按原样"提供，不附带任何形式的保修，无论是明示的\n' +\
               '还是暗示的，包括但不限于对适销性、特定用途适用性和\n' +\
               '非侵权性的保证。根据任何理由，无论是合同诉讼、侵权行为或其他\n' +\
               '责任行为，作者或版权持有人均不对任何人承担任何责任\n' +\
               '因软件或软件的使用或其他处理而产生的任何索赔、损害或其他\n' +\
               '责任，无论是根据、来自或与软件有关。'

# Message Box Text
INVALID_INPUT = '无效输入', '输入无效。\n\n请验证输入是否仍然存在或有效，然后重试。'
INVALID_EXPORT = '无效的导出目录', '您选择了无效的导出目录。\n\n请确保所选目录仍然存在。'
INVALID_ENSEMBLE = '模型不足', '您必须选择 2 个或更多模型才能运行合奏。'
INVALID_MODEL = '未选择模型', '您必须选择一个模型才能继续。'
MISSING_MODEL = '模型缺失', '所选模型缺失或无效。'
ERROR_OCCURED = '发生错误', '\n\n您是否想打开错误日志以获取更多详细信息?\n'
PROCESS_COMPLETE = '\n处理完成\n'
PROCESS_COMPLETE_2 = '处理完成\n'

# GUI Text Constants
BACK_TO_MAIN_MENU = '返回主菜单'

# Help Hint Text
INTERNAL_MODEL_ATT = '这是一个内部模型设置。 \n\n***除非您确定，否则不要更改它!***'
STOP_HELP = '停止正在进行的任务。\n• 停止前会出现确认弹出窗口。'
SETTINGS_HELP = '访问主设置和 "下载中心"。'
COMMAND_TEXT_HELP = '显示正在进行任务的状态和进度。'
SAVE_CURRENT_SETTINGS_HELP = '加载或保存应用程序设置。'
PITCH_SHIFT_HELP = ('选择处理曲目的音调：\n\n'
                '• 整数表示半音。\n'
                '• 使用更高的音调可能会在高质量模型中切断上带宽，即使是在高质量模型中。\n'
                '• 提高音调可能更适合有深层女声的曲目。\n'
                '• 降低音调可能需要更长的处理时间，但对于有高音女声的曲目效果更好。')
AGGRESSION_SETTING_HELP = ('调整主干提取的强度：\n\n'
                           '• 范围从 -100 - 100。\n'
                           '• 数值越大，提取越深。\n' 
                           '• 通常设置为 5 用于女声和乐器曲目。 \n'
                           '• 超过 5 的值可能会使非女声模型的声音变得混乱。')
WINDOW_SIZE_HELP = ('选择窗口大小以平衡质量和速度：\n\n'
                    '• 1024 - 速度快但质量较差。\n'
                    '• 512 - 中等速度和质量。\n'
                    '• 320 - 需要更长时间，但可能提供更好的质量。')
MDX_SEGMENT_SIZE_HELP = ('选择分段大小以平衡速度、资源使用和质量：\n'
                         '• 较小的大小消耗较少的资源。\n'
                         '• 较大的大小消耗更多的资源，但可能提供更好的结果。\n'
                         '• 默认大小为 256。质量可能会因您的选择而变化。')
DEMUCS_STEMS_HELP = ('选择要使用所选模型提取的茎：\n\n'
                     '• 所有茎 - 提取所有可用的茎。\n'
                     '• 女声 - 仅 "女声" 茎。\n'
                     '• 其他 - 仅 "其他" 茎。\n'
                     '• 低音 - 仅 "低音" 茎。\n'
                     '• 鼓点 - 仅 "鼓点" 茎。')
SEGMENT_HELP = ('调整分段以管理 RAM 或 V-RAM 使用：\n\n'
               '• 较小的大小消耗较少的资源。\n'
               '• 较大的大小消耗更多的资源，但可能提供更好的结果。\n'
               '• "默认" 会选择最佳大小。')

ENSEMBLE_MAIN_STEM_HELP = (
    '选择用于合奏的茎类型：\n\n'
    
    f'• {VOCAL_PAIR}:\n'
    '  - 主茎: 女声\n'
    '  - 次茎: 乐器 (混合减去女声)\n\n'
    
    f'• {OTHER_PAIR}:\n'
    '  - 主茎: 其他\n'
    '  - 次茎: 无其他 (混合减去 "其他")\n\n'
    
    f'• {BASS_PAIR}:\n'
    '  - 主茎: 低音\n'
    '  - 次茎: 无低音 (混合减去低音)\n\n'
    
    f'• {DRUM_PAIR}:\n'
    '  - 主茎: 鼓点\n'
    '  - 次茎: 无鼓点 (混合减去鼓点)\n\n'
    
    f'• {FOUR_STEM_ENSEMBLE}:\n'
    '  - 收集所有 4 茎 Demucs 模型并合奏所有输出。\n\n'
    
    f'• {MULTI_STEM_ENSEMBLE}:\n'
    '  - "丛林合奏" 收集所有模型并合奏任何相关输出。'
)

ENSEMBLE_TYPE_HELP = (
    '选择用于生成最终输出的合奏算法：\n\n'
    
    f'• {MAX_MIN}:\n'
    '  - 主茎使用 "Max Spec" 算法处理。\n'
    '  - 次茎使用 "Min Spec" 算法处理。\n\n'
    
    '注意: 对于 "4 茎合奏" 选项，只会显示一个算法。\n\n'
    
    '算法详细信息：\n'
    
    f'• {MAX_SPEC}:\n'
    '  - 产生最高可能的输出。\n'
    '  - 适用于女声茎以获得更丰富的声音，但可能会引入不需要的伪影。\n'
    '  - 适用于乐器茎，但避免在合奏中使用 VR Arch 模型。\n\n'
    
    f'• {MIN_SPEC}:\n'
    '  - 产生最低可能的输出。\n'
    '  - 适用于乐器茎以获得更清晰的结果。可能会导致 "泥泞" 的声音。\n\n'
    
    f'• {AUDIO_AVERAGE}:\n'
    '  - 平均所有结果以获得最终输出。'
)

ENSEMBLE_LISTBOX_HELP = (
    '显示所选主茎对的所有可用模型。'
)

if OPERATING_SYSTEM == 'darwin':
   IS_GPU_CONVERSION_HELP = (
      '• 使用 GPU 进行处理 (如果可用):\n'
      '  - 如果选中，应用程序将尝试使用您的 GPU 进行更快的处理。\n'
      '  - 如果未检测到 GPU，将默认使用 CPU 处理。\n'
      '  - macOS 上的 GPU 处理仅适用于 VR Arch 模型。\n\n'
      '• 请注意:\n'
      '  - CPU 处理比 GPU 处理慢得多。\n'
      '  - 只有配备 M1 芯片的 Mac 才能用于 GPU 处理。'
   )
else:
   IS_GPU_CONVERSION_HELP = (
      '• 使用 GPU 进行处理 (如果可用):\n'
      '  - 如果选中，应用程序将尝试使用您的 GPU 进行更快的处理。\n'
      '  - 如果未检测到 GPU，将默认使用 CPU 处理。\n\n'
      '• 请注意:\n'
      '  - CPU 处理比 GPU 处理慢得多。\n'
      '  - 只有 Nvidia GPU 才能用于 GPU 处理。'
   )

IS_TIME_CORRECTION_HELP = ('选中后，输出将保留输入的原始 BPM。')
SAVE_STEM_ONLY_HELP = '允许用户仅保存所选的茎。'
IS_NORMALIZATION_HELP = '归一化输出以防止裁剪。'
IS_CUDA_SELECT_HELP = "如果您有多个 GPU，您可以选择哪个 GPU 用于处理。"
CROP_SIZE_HELP = '**仅与选定模型兼容!**\n\n 设置应与训练裁剪大小值匹配。如果不确定，请保持默认。'
IS_TTA_HELP = ('此选项执行测试时增强以提高分离质量。\n\n'
               '注意: 选择此选项将增加完成转换所需的时间。')
IS_POST_PROCESS_HELP = ('此选项可能会识别女声输出中剩余的乐器伪影。 \n此选项可能会改善某些歌曲的分离。\n\n' +\
                       '注意: 选择此选项可能会对处理过程产生不利影响，具体取决于曲目。因此，仅在最后一步作为最后的手段推荐。')
IS_HIGH_END_PROCESS_HELP = '应用程序将镜像输出的缺失频率范围。'
SHIFTS_HELP = ('执行多次预测，随机移位输入并对它们进行平均。\n\n'
              '• 移位次数越多，预测时间越长。 \n- 不建议除非您有 GPU。')
OVERLAP_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
               '       - 较高的值可以提供更好的结果，但会导致处理时间更长。\n'
               '       - 您可以选择 0.001-0.999')
MDX_OVERLAP_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
               '       - 较高的值可以提供更好的结果，但会导致处理时间更长。\n'
               '       - 对于非 MDX23C 模型: 您可以选择 0.001-0.999')
OVERLAP_23_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
                  '       - 较高的值可以提供更好的结果，但会导致处理时间更长。')
IS_SEGMENT_DEFAULT_HELP = '• 分段大小是根据所选模型的相关 \nconfig 文件 (yaml) 中提供的值设置的。'
IS_SPLIT_MODE_HELP = '• 启用 "分段"。 \n• 不建议取消选择此选项，除非您拥有强大的 PC。'
IS_DEMUCS_COMBINE_STEMS_HELP = '应用程序将通过组合剩余的茎而不是反转主茎与混合来创建次茎。'
COMPENSATE_HELP = '补偿主茎的音频以允许更好的次茎。'
IS_DENOISE_HELP = ('• 标准: 此设置减少 MDX-Net 模型产生的噪声。\n' 
                   '       - 此选项仅减少非 MDX23 模型的噪声。\n'
                   '• 降噪模型: 此设置使用特殊降噪模型消除任何 MDX-Net 模型产生的噪声。\n'
                   '       - 此选项适用于所有 MDX-Net 模型。\n'
                   '       - 您必须安装 "UVR-DeNoise-Lite" VR Arch 模型才能使用此选项。\n'
                   '• 请注意: 这两个选项都会增加分离时间。')

VOC_SPLIT_MODEL_SELECT_HELP = '• 从主唱和伴奏模型列表中选择一个模型，以自动处理女声茎。'
IS_VOC_SPLIT_INST_SAVE_SELECT_HELP = '• 启用后，您将收到额外的仪器输出，其中包括: 仅有主唱的一个和仅有伴奏的另一个。'
IS_VOC_SPLIT_MODEL_SELECT_HELP = ('• 启用后，此选项会自动处理生成的女声茎，使用卡拉 OK 模型去除主唱或使用另一个模型去除伴奏。\n'
                                 '       - 此选项将女声轨道分为两个独立的部分: 主唱和伴奏，提供两个额外的女声输出。\n'
                                 '       - 无论您使用卡拉 OK 模型还是背景女声模型，结果都会以相同的方式组织。\n'
                                 '       - 此选项目前不适用于合奏模式。')
IS_DEVERB_OPT_HELP = ('• 选择要自动去除混响的女声类型。\n'
                     '       - 示例: 选择 "仅主要女声" 将仅从主要女声茎中去除混响。')
IS_DEVERB_VOC_HELP = ('• 此选项从女声茎中去除混响。\n'
                     '       - 您必须安装 "UVR-DeEcho-DeReverb" VR Arch 模型才能使用此选项。\n'
                     '       - 此选项目前不适用于合奏模式。')
IS_FREQUENCY_MATCH_HELP = '将主茎的频率截止与次茎的频率截止匹配。'
CLEAR_CACHE_HELP = '清除用户选择的未识别模型的设置。'
IS_SAVE_ALL_OUTPUTS_ENSEMBLE_HELP = '启用后，将保留所有合奏生成的单独输出。'
IS_APPEND_ENSEMBLE_NAME_HELP = '启用后，将合奏名称添加到最终输出中。'
IS_WAV_ENSEMBLE_HELP = (
    '启用后，使用波形而不是频谱进行合奏算法处理:\n'
    '• 可能会增加失真。\n'
    '• 波形合奏比频谱合奏快。'
)
DONATE_HELP = '打开官方 UVR "Buy Me a Coffee" 外部链接以捐赠项目！'
IS_INVERT_SPEC_HELP = (
    '可能增强次茎质量:\n'
    '• 使用频谱而不是波形反转主茎。\n'
    '• 稍微慢一些的反转方法。'
)
IS_TESTING_AUDIO_HELP = '在保存的文件中附加 10 位数字以避免意外覆盖。'
IS_MODEL_TESTING_AUDIO_HELP = '在输出中附加模型名称以便在不同模型之间进行比较。'
IS_ACCEPT_ANY_INPUT_HELP = (
    '启用后，允许所有类型的输入，甚至非音频格式。\n'
    '仅用于实验，不建议用于常规使用。'
)
IS_TASK_COMPLETE_HELP = '启用后，处理完成或失败时会播放提示音。'
DELETE_YOUR_SETTINGS_HELP = (
    '包含您保存的设置。删除所选设置前会请求确认。'
)
SET_STEM_NAME_HELP = '选择给定模型的主茎。'
IS_CREATE_MODEL_FOLDER_HELP = ('在每次转换后，在导出目录中生成两个新目录以保存输出。\n\n'
                              '• 示例: \n'
                              '─ 导出目录\n'
                              '   └── 第一个目录 (以模型命名)\n'
                              '           └── 第二个目录 (以曲目命名)\n'
                              '                    └── 输出文件(s)')
MDX_DIM_T_SET_HELP = INTERNAL_MODEL_ATT
MDX_DIM_F_SET_HELP = INTERNAL_MODEL_ATT

MDX_N_FFT_SCALE_SET_HELP = '指定模型训练期间使用的 N_FFT 大小。'
POPUP_COMPENSATE_HELP = (
    f'选择所选模型的适当音量补偿。\n'
    f'提醒: {COMPENSATE_HELP}'
)
VR_MODEL_PARAM_HELP = '选择运行所选模型所需的参数。'
CHOSEN_ENSEMBLE_HELP = (
    '默认合奏选择:\n'
    '• 保存当前合奏配置。\n'
    '• 清除所有选定模型。\n'
    '注意: 您还可以选择先前保存的合奏。'
)
CHOSEN_PROCESS_METHOD_HELP = (
    '选择处理方法:\n'
    '选择各种 AI 网络和算法以处理您的曲目:\n'
    '\n'
    '• VR 架构: 使用幅度频谱图进行源分离。\n'
    '• MDX-Net: 使用混合频谱图网络进行源分离。\n'
    '• Demucs v3: 也使用混合频谱图网络进行源分离。\n'
    '• 合奏模式: 结合多个模型和网络的结果以获得最佳结果。\n'
    '• 音频工具: 额外的实用工具以便更方便。'
)        

INPUT_FOLDER_ENTRY_HELP = (
    '选择输入:\n'
    '选择要处理的音频文件(s)。'
)
INPUT_FOLDER_ENTRY_HELP_2 = (
    '输入选项菜单:\n'
    '单击以访问输入选项菜单。'
)
OUTPUT_FOLDER_ENTRY_HELP = (
    '选择输出:\n'
    '选择保存处理文件的目录。'
)
INPUT_FOLDER_BUTTON_HELP = (
    '打开输入文件夹按钮:\n'
    '打开包含所选输入音频文件(s)的目录。'
)
OUTPUT_FOLDER_BUTTON_HELP = (
    '打开输出文件夹按钮:\n'
    '打开所选的输出文件夹。'
)
CHOOSE_MODEL_HELP = (
    '每种处理方法都有自己的选项和模型。\n'
    '在此处选择与所选处理方法关联的模型。'
)
FORMAT_SETTING_HELP = '保存输出为: '
SECONDARY_MODEL_ACTIVATE_HELP = (
    '启用后，应用程序将使用上面选择的模型(s)执行额外的推理。'
)
SECONDARY_MODEL_HELP = (
    '选择次要模型:\n'
    '选择与要使用当前方法处理的茎关联的次要模型。'
)

INPUT_SEC_FIELDS_HELP = (
    '右键单击此处选择您的输入!'
)

SECONDARY_MODEL_SCALE_HELP = ('比例决定了最终音频输出将如何平均主模型和次模型的结果。\n\n例如:\n\n'
                             '• 10% - 主模型结果的 10% 将被计入最终结果。\n'
                             '• 50% - 主模型和次模型的结果将平均。\n'
                             '• 90% - 主模型结果的 90% 将被计入最终结果。')
PRE_PROC_MODEL_ACTIVATE_HELP = (
    '启用后，应用程序将使用所选模型隔离仪器茎。\n'
    '随后，所有非女声茎将从此生成的仪器中提取出来。\n'
    '\n'
    '关键点:\n'
    '• 此功能可以显著减少非女声茎中的女声泄漏。\n'
    '• 仅在 Demucs 工具中可用。\n'
    '• 仅与非女声和非仪器茎输出兼容。\n'
    '• 预计总处理时间将增加。\n'
    '• 只能选择 VR 或 MDX-Net 女声乐器/女声模型进行此过程。'
)
      
AUDIO_TOOLS_HELP = (
    'Select from various audio tools to process your track:\n'
    '\n'
    '• Manual Ensemble: Requires 2 or more selected files as inputs. This allows tracks to be processed using the algorithms from Ensemble Mode.\n'
    '• Time Stretch: Adjust the playback speed of the selected inputs to be faster or slower.\n'
    '• Change Pitch: Modify the pitch of the selected inputs.\n'
    '• Align Inputs: Choose 2 audio file and the application will align them and provide the difference in alignment.\n'
    '    - This tool provides similar functionality to "Utagoe."\n'
    '    - Primary Audio: This is usually a mixture.\n'
    '    - Secondary Audio: This is usually an instrumental.\n'
    '• Matchering: Choose 2 audio files. The matchering algorithm will master the target audio to have the same RMS, FR, peak amplitude, and stereo width as the reference audio.'
)
             
PRE_PROC_MODEL_INST_MIX_HELP = 'When enabled, the application will generate a third output without the selected stem and vocals.'         
MODEL_SAMPLE_MODE_HELP = ('Allows the user to process only part of a track to sample settings or a model without running a full conversion.\n\nNotes:\n\n'
                         '• The number in the parentheses is the current number of seconds the generated sample will be.\n'
                         '• You can choose the number of seconds to extract from the track in the \"Additional Settings\" menu.')
                    
POST_PROCESS_THREASHOLD_HELP = ('Allows the user to control the intensity of the Post_process option.\n\nNotes:\n\n'
                               '• Higher values potentially remove more artifacts. However, bleed might increase.\n'
                               '• Lower values limit artifact removal.')

BATCH_SIZE_HELP = ('指定一次处理的批次数量。\n\n注意事项：\n\n'
                                '• 较高的值会增加RAM使用量，但处理时间会稍微更快。\n'
                                '• 较低的值会减少RAM使用量，但处理时间会稍微更长。\n'
                                '• 批次大小的值不会影响输出质量。')
         
VR_MODEL_NOUT_HELP = ""
VR_MODEL_NOUT_LSTM_HELP = ""
  
IS_PHASE_HELP = '选择次要音频的相位。\n• 注意：强烈建议使用"自动"选项。'
IS_ALIGN_TRACK_HELP = '启用此选项以保存对齐后的次要音轨。'
IS_MATCH_SILENCE_HELP = (
    '将次要音频的初始静音与主音频对齐。\n'
    '• 注意：如果主音频仅以人声开头，请避免使用此选项。'
)
IS_MATCH_SPEC_HELP = '根据主音频的频谱图对齐次要音频。\n• 注意：这可能会在特定情况下增强对齐效果。'

TIME_WINDOW_ALIGN_HELP = (
                           '此设置确定用于对齐分析的窗口大小，特别是对于存在轻微时间差异的配对：\n'
                           '\n'
                           '• 无：禁用时间窗口分析。\n'
                           '• 1：以0.0625秒的窗口分析配对。\n'
                           '• 2：以0.125秒的窗口分析配对。\n'
                           '• 3：以0.25秒的窗口分析配对。\n'
                           '• 4：以0.50秒的窗口分析配对。\n'
                           '• 5：以0.75秒的窗口分析配对。\n'
                           '• 6：以1秒的窗口分析配对。\n'
                           '• 7：以2秒的窗口分析配对。\n'
                           '\n'
                           '移位选项：\n'
                           '• 低：循环使用0.0625和0.5秒的窗口，以找到最佳匹配。\n'
                           '• 中：循环使用0.0625、0.125和0.5秒的窗口，以找到最佳匹配。\n'
                           '• 高：循环使用0.0625、0.125、0.25和0.5秒的窗口，以找到最佳匹配。\n'
                           '\n'
                           '需要考虑的重要事项：\n'
                           '    - 使用"移位"选项可能需要更长的处理时间，并且可能无法保证更好的结果。\n'
                           '    - 选择较小的分析窗口可能会增加处理时间。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而有所不同。'
)
INTRO_ANALYSIS_ALIGN_HELP = (
                           '此设置确定用于初始对齐分析的音频输入部分：\n'
                           '\n'
                           '• 默认：分析音频总长度的10%（或1/10）。\n'
                           '• 1：分析音频总长度的12.5%（或1/8）。\n'
                           '• 2：分析音频总长度的16.67%（或1/6）。\n'
                           '• 3：分析音频总长度的25%（或1/4）。\n'
                           '• 4：分析音频总长度的50%（或一半）。\n'
                           '\n'
                           '移位选项：\n'
                           '• 低：循环使用2个介绍分析值。\n'
                           '• 中：循环使用3个介绍分析值。\n'
                           '• 高：循环使用5个介绍分析值。\n'
                           '\n'
                           '需要考虑的重要事项：\n'
                           '    - 使用"移位"选项将需要更长的处理时间，并且可能无法保证更好的结果。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而有所不同。'
)

VOLUME_ANALYSIS_ALIGN_HELP = (
                           '此设置指定要对次要输入进行的音量调整：\n'
                           '\n'
                           '• 无：不进行音量调整。\n'
                           '• 低：在4dB范围内分析音频，以1dB为增量进行调整。\n'
                           '• 中：在6dB范围内分析音频，以1dB为增量进行调整。\n'
                           '• 高：在6dB范围内分析音频，以0.5dB为增量进行调整。\n'
                           '• 非常高：在10dB范围内分析音频，以0.5dB为增量进行调整。\n'
                           '\n'
                           '需要考虑的重要事项：\n'
                           '    - 选择更广泛的分析选项（例如高、非常高）将需要更长的处理时间。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而有所不同。'
)

PHASE_SHIFTS_ALIGN_HELP = (
                           '此设置指定要对次要输入进行的相位调整：\n'
                           '\n'
                           '移位选项：\n'
                           '• 无：不进行相位调整。\n'
                           '• 非常低：在2个不同相位位置的范围内分析音频。\n'
                           '• 低：在4个不同相位位置的范围内分析音频。\n'
                           '• 中：在8个不同相位位置的范围内分析音频。\n'
                           '• 高：在18个不同相位位置的范围内分析音频。\n'
                           '• 非常高：在36个不同相位位置的范围内分析音频。\n'
                           '• 最大：在所有360个相位位置分析音频。\n'
                           '\n'
                           '需要考虑的重要事项：\n'
                           '    - 此选项仅适用于时间校正。\n'
                           '    - 如果其中一个输入来自模拟源，此选项可能会有所帮助。\n'
                           '    - 选择更广泛的分析选项（例如高、非常高）将需要更长的处理时间。\n'
                           '    - 选择"最大"可能需要数小时才能处理完成。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而有所不同。'
)

# 警告消息
STORAGE_ERROR = '存储空间不足', '主驱动器上的存储空间不足，应用程序无法正常运行。 \n\n请确保主驱动器至少有3GB的存储空间，然后重试。\n\n'
STORAGE_WARNING = '可用存储空间低', '您的主驱动器存储空间不足。应用程序需要至少3GB的存储空间才能正常运行。\n\n'
CONFIRM_WARNING = '\n您确定要继续吗？'
PROCESS_FAILED = '处理失败，请查看错误日志\n'
EXIT_PROCESS_ERROR = '活动进程', '请停止活动进程或等待其完成后再退出。'
EXIT_HALTED_PROCESS_ERROR = '正在停止进程', '请等待应用程序完成停止进程后再退出。'
EXIT_DOWNLOAD_ERROR = '活动下载', '请停止下载或等待其完成后再退出。'
SET_TO_DEFAULT_PROCESS_ERROR = '活动进程', '您无法在活动进程期间重置所有应用程序设置。'
SET_TO_ANY_PROCESS_ERROR = '活动进程', '您无法在活动进程期间重置应用程序设置。'
RESET_ALL_TO_DEFAULT_WARNING = '重置设置确认', '所有应用程序设置将恢复为出厂默认设置。\n\n您确定要继续吗？'
AUDIO_VERIFICATION_CHECK = lambda i, e:f'++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n已移除损坏文件： \n\n{i}\n\n错误详细信息：\n\n{e}\n++++++++++++++++++++++++++++++++++++++++++++++++++++'
INVALID_ONNX_MODEL_ERROR = '无效模型', '选择的文件不是有效的MDX-Net模型。请查看错误日志以获取更多信息。'
INVALID_PARAM_MODEL_ERROR = '选择模型参数', '请选择模型参数或单击"取消"。'
UNRECOGNIZED_MODEL = '检测到未识别的模型', '是未识别的模型。\n\n' + \
                     '您是否希望在继续之前选择正确的参数？'
STOP_PROCESS_CONFIRM = '确认', '您将停止所有活动进程。\n\n您确定要继续吗？'
NO_ENSEMBLE_SELECTED = '未选择模型', '请选择合奏后重试。'
PICKLE_CORRU = '文件已损坏', '无法加载此合奏。\n\n' + \
               '您是否希望从列表中删除此合奏？'
DELETE_ENS_ENTRY = '确认删除', '您确定要删除此条目吗？'

# 分离文本
LOADING_MODEL = '正在加载模型...'
INFERENCE_STEP_1 = '正在推理...'
INFERENCE_STEP_1_SEC = '正在推理(次要模型)...'
INFERENCE_STEP_1_4_STEM = lambda stem:f'正在推理({stem}的次要模型)...'
INFERENCE_STEP_1_PRE = '正在推理(预处理模型)...'
INFERENCE_STEP_1_VOC_S = '正在分离人声...'
INFERENCE_STEP_2_PRE = lambda pm, m:f'正在加载预处理模型({pm}: {m})...'
INFERENCE_STEP_2_SEC = lambda pm, m:f'正在加载次要模型({pm}: {m})...'
INFERENCE_STEP_2_VOC_S = lambda pm, m:f'正在加载人声分离模型({pm}: {m})...'
INFERENCE_STEP_2_SEC_CACHED_MODOEL = lambda pm, m:f'次要模型({pm}: {m})缓存已加载。\n'
INFERENCE_STEP_2_PRE_CACHED_MODOEL = lambda pm, m:f'预处理模型({pm}: {m})缓存已加载。\n'
INFERENCE_STEP_2_SEC_CACHED = '正在加载缓存的次要模型源... 完成!\n'
INFERENCE_STEP_2_PRIMARY_CACHED = ' 模型缓存已加载。\n'
INFERENCE_STEP_2 = '推理完成。'
INFERENCE_STEP_DEVERBING = ' 正在去混响...'
SAVING_STEM = '正在保存', '音轨...'
SAVING_ALL_STEMS = '正在保存所有音轨...'
ENSEMBLING_OUTPUTS = '正在合奏输出...'
DONE = ' 完成!\n'
ENSEMBLES_SAVED = '合奏输出已保存!\n\n'

# 其他文本
CHOOSE_PROC_METHOD_MAIN_LABEL = '选择处理方法'
SELECT_SAVED_SETTINGS_MAIN_LABEL = '选择已保存的设置'
CHOOSE_MDX_MODEL_MAIN_LABEL = '选择MDX-NET模型'
BATCHES_MDX_MAIN_LABEL = '批次大小'
VOL_COMP_MDX_MAIN_LABEL = '音量补偿'
SEGMENT_MDX_MAIN_LABEL = '分段大小'
SELECT_VR_MODEL_MAIN_LABEL = '选择VR模型'
AGGRESSION_SETTING_MAIN_LABEL = '激进度设置'
WINDOW_SIZE_MAIN_LABEL = '窗口大小'
CHOOSE_DEMUCS_MODEL_MAIN_LABEL = '选择DEMUCS模型'
CHOOSE_STEMS_MAIN_LABEL = '选择音轨'
CHOOSE_SEGMENT_MAIN_LABEL = '分段'
ENSEMBLE_OPTIONS_MAIN_LABEL = '合奏选项'
CHOOSE_MAIN_PAIR_MAIN_LABEL = '主音轨配对'
CHOOSE_ENSEMBLE_ALGORITHM_MAIN_LABEL = '合奏算法'
AVAILABLE_MODELS_MAIN_LABEL = '可用模型'
CHOOSE_AUDIO_TOOLS_MAIN_LABEL = '选择音频工具'
CHOOSE_MANUAL_ALGORITHM_MAIN_LABEL = '选择算法'
CHOOSE_RATE_MAIN_LABEL = '比率'
CHOOSE_SEMITONES_MAIN_LABEL = '半音'
GPU_CONVERSION_MAIN_LABEL = 'GPU转换'
CHANGE_LOG_HEADER = lambda patch:f"补丁版本:\n\n{patch}"
INVALID_INPUT_E = ' 无效输入! '
LB_UP = "向上移动选择"
LB_DOWN = "向下移动选择"
LB_CLEAR = "清除框"
LB_MOVE_OVER_P = "将选择移至次要列表"
LB_MOVE_OVER_S = "将选择移至主要列表"
FILE_ONE_MAIN_LABEL = "主音频"
FILE_TWO_MAIN_LABEL = "次要音频"
FILE_ONE_MATCH_MAIN_LABEL = "目标音频"
FILE_TWO_MATCH_MAIN_LABEL = "参考音频"
TIME_WINDOW_MAIN_LABEL = "时间调整"
INTRO_ANALYSIS_MAIN_LABEL = "介绍分析"
VOLUME_ADJUSTMENT_MAIN_LABEL = "音量调整"
SELECT_INPUTS = "选择输入"
SELECTED_INPUTS = '已选择的输入'
WIDEN_BOX = '扩大框'
CONFIRM_ENTRIES = '确认条目'
CLOSE_WINDOW = '关闭窗口'
DUAL_AUDIO_PROCESSING = '双音频批处理'
CANCEL_TEXT = "取消"
CONFIRM_TEXT = "确认"
SELECT_MODEL_TEXT = '选择模型'
NONE_SELECTED = '未选择'
SAVE_TEXT = '保存'
OVERLAP_TEXT = '重叠'
ACCEPT_ANY_INPUT_TEXT = '接受任何输入'
ACTIVATE_PRE_PROCESS_MODEL_TEXT = '激活预处理模型'
ACTIVATE_SECONDARY_MODEL_TEXT = '激活次要模型'
ADDITIONAL_MENUS_INFORMATION_TEXT = '附加菜单和信息'
ADDITIONAL_SETTINGS_TEXT = '附加设置'
ADVANCED_ALIGN_TOOL_OPTIONS_TEXT = '高级对齐工具选项'
ADVANCED_DEMUCS_OPTIONS_TEXT = '高级Demucs选项'
ADVANCED_ENSEMBLE_OPTIONS_TEXT = '高级合奏选项'
ADVANCED_MDXNET23_OPTIONS_TEXT = '高级MDX-NET23选项'
ADVANCED_MDXNET_OPTIONS_TEXT = '高级MDX-Net选项'
ADVANCED_OPTION_MENU_TEXT = '高级选项菜单'
ADVANCED_VR_OPTIONS_TEXT = '高级VR选项'
AGGRESSION_SETTING_TEXT = '激进度设置'
APPEND_ENSEMBLE_NAME_TEXT = '附加合奏名称'
APPLICATION_DOWNLOAD_CENTER_TEXT = '应用程序下载中心'
APPLICATION_UPDATES_TEXT = '应用程序更新'
AUDIO_FORMAT_SETTINGS_TEXT = '音频格式设置'
BALANCE_VALUE_TEXT = '平衡值'
BATCH_SIZE_TEXT = '批次大小'
BV_MODEL_TEXT = 'BV模型'
CHANGE_MODEL_DEFAULT_TEXT = '更改模型默认值'
CHANGE_MODEL_DEFAULTS_TEXT = '更改模型默认值'
CHANGE_PARAMETERS_TEXT = '更改参数'
CHOOSE_ADVANCED_MENU_TEXT = '选择高级菜单' 
CHOOSE_MODEL_PARAM_TEXT = '选择模型参数'
CLEAR_AUTOSET_CACHE_TEXT = '清除自动设置缓存'
COMBINE_STEMS_TEXT = '合并音轨'
CONFIRM_UPDATE_TEXT = '确认更新'
COPIED_TEXT = '已复制!'
COPY_ALL_TEXT_TEXT = '复制所有文本'
DEFINED_PARAMETERS_DELETED_TEXT = '已删除定义的参数'
DELETE_PARAMETERS_TEXT = '删除参数'
DELETE_USER_SAVED_SETTING_TEXT = '删除用户保存的设置'
DEMUCS_TEXT = 'Demucs'
DENOISE_OUTPUT_TEXT = '去噪输出'
DEVERB_VOCALS_TEXT = '去混响人声'
DONE_TEXT = '完成'
DOWNLOAD_CENTER_TEXT = '下载中心'
DOWNLOAD_CODE_TEXT = '下载代码'
DOWNLOAD_LINKS_TEXT = '下载链接'
DOWNLOAD_UPDATE_IN_APPLICATION_TEXT = '在应用程序中下载更新'
ENABLE_HELP_HINTS_TEXT = '启用帮助提示'
ENABLE_TTA_TEXT = '启用TTA'
ENABLE_VOCAL_SPLIT_MODE_TEXT = '启用人声分离模式'
ENSEMBLE_NAME_TEXT = '合奏名称'
ENSEMBLE_WAVFORMS_TEXT = '合奏波形'
ERROR_CONSOLE_TEXT = '错误控制台'
GENERAL_MENU_TEXT = '通用菜单'
GENERAL_PROCESS_SETTINGS_TEXT = '通用处理设置'
GENERATE_MODEL_FOLDER_TEXT = '生成模型文件夹'
HIGHEND_PROCESS_TEXT = '高端处理'
INPUT_CODE_TEXT = '输入代码'
INPUT_STEM_NAME_TEXT = '输入音轨名称'
INPUT_UNIQUE_STEM_NAME_TEXT = '输入唯一音轨名称'
IS_INVERSE_STEM_TEXT = '是反向音轨'
KARAOKE_MODEL_TEXT = '卡拉OK模型'
MANUAL_DOWNLOADS_TEXT = '手动下载'
MATCH_FREQ_CUTOFF_TEXT = '匹配频率截止'
MDXNET_C_MODEL_PARAMETERS_TEXT = 'MDX-Net C模型参数'
MDXNET_MODEL_SETTINGS_TEXT = 'MDX-Net模型设置'
MDXNET_TEXT = 'MDX-Net'
MODEL_PARAMETERS_CHANGED_TEXT = '模型参数已更改'
MODEL_SAMPLE_MODE_SETTINGS_TEXT = '模型示例模式设置'
MODEL_TEST_MODE_TEXT = '模型测试模式'
MP3_BITRATE_TEXT = 'Mp3比特率'
NAME_SETTINGS_TEXT = '名称设置'
NO_DEFINED_PARAMETERS_FOUND_TEXT = '未找到定义的参数'
NO_TEXT = '否'
NORMALIZE_OUTPUT_TEXT = '归一化输出'
USE_OPENCL_TEXT = '使用OpenCL'
NOT_ENOUGH_MODELS_TEXT = '模型不足'
NOTIFICATION_CHIMES_TEXT = '通知提示音'
OPEN_APPLICATION_DIRECTORY_TEXT = '打开应用程序目录'
OPEN_LINK_TO_MODEL_TEXT = '打开模型链接'
OPEN_MODEL_DIRECTORY_TEXT = '打开模型目录'
OPEN_MODEL_FOLDER_TEXT = '打开模型文件夹'
OPEN_MODELS_FOLDER_TEXT = '打开模型文件夹'
PHASE_SHIFTS_TEXT = '相位移位'
POST_PROCESS_TEXT = '后处理'
POST_PROCESS_THRESHOLD_TEXT = '后处理阈值'
PREPROCESS_MODEL_CHOOSE_TEXT = '预处理模型'
PRIMARY_STEM_TEXT = '主音轨'
REFRESH_LIST_TEXT = '刷新列表'
REMOVE_SAVED_ENSEMBLE_TEXT = '移除保存的合奏'
REPORT_ISSUE_TEXT = '报告问题'
RESET_ALL_SETTINGS_TO_DEFAULT_TEXT = '重置所有设置为默认值'
RESTART_APPLICATION_TEXT = '重启应用程序'
SAMPLE_CLIP_DURATION_TEXT = '示例剪辑持续时间'
SAVE_ALIGNED_TRACK_TEXT = '保存对齐的音轨'
SAVE_ALL_OUTPUTS_TEXT = '保存所有输出'
SAVE_CURRENT_ENSEMBLE_TEXT = '保存当前合奏'
SAVE_CURRENT_SETTINGS_TEXT = '保存当前设置'
SAVE_INSTRUMENTAL_MIXTURE_TEXT = '保存乐器混合'
SAVE_SPLIT_VOCAL_INSTRUMENTALS_TEXT = '保存分离的人声乐器'
SECONDARY_MODEL_TEXT = '次要模型'
SECONDARY_PHASE_TEXT = '次要相位'
SECONDS_TEXT = '秒'
SEGMENT_DEFAULT_TEXT = '分段默认值'
SEGMENT_SIZE_TEXT = '分段大小'
SEGMENTS_TEXT = '分段'
SELECT_DOWNLOAD_TEXT = '选择下载'
SELECT_MODEL_PARAM_TEXT = '选择模型参数'
SELECT_VOCAL_TYPE_TO_DEVERB_TEXT = '选择去混响的人声类型'
SELECTED_MODEL_PLACEMENT_PATH_TEXT = '选择模型放置路径'
SETTINGS_GUIDE_TEXT = '设置指南'
SETTINGS_TEST_MODE_TEXT = '设置测试模式'
SHIFT_CONVERSION_PITCH_TEXT = '移位转换音调'
SHIFTS_TEXT = '移位'
SILENCE_MATCHING_TEXT = '静音匹配'
SPECIFY_MDX_NET_MODEL_PARAMETERS_TEXT = '指定MDX-Net模型参数'
SPECIFY_PARAMETERS_TEXT = '指定参数'
SPECIFY_VR_MODEL_PARAMETERS_TEXT = '指定VR模型参数'
SPECTRAL_INVERSION_TEXT = '频谱反转'
SPECTRAL_MATCHING_TEXT = '频谱匹配'   
SPLIT_MODE_TEXT = '分离模式'
STEM_NAME_TEXT = '音轨名称'
STOP_DOWNLOAD_TEXT = '停止下载'
SUPPORT_UVR_TEXT = '支持UVR'
TRY_MANUAL_DOWNLOAD_TEXT = '尝试手动下载'
UPDATE_FOUND_TEXT = '发现更新'
USER_DOWNLOAD_CODES_TEXT = '用户下载代码'
UVR_BUY_ME_A_COFFEE_LINK_TEXT = 'UVR \'请我喝杯咖啡\'链接'
UVR_ERROR_LOG_TEXT = 'UVR错误日志'
UVR_PATREON_LINK_TEXT = 'UVR Patreon链接'
VOCAL_DEVERB_OPTIONS_TEXT = '人声去混响选项'
VOCAL_SPLIT_MODE_OPTIONS_TEXT = '人声分离模式选项'
VOCAL_SPLIT_OPTIONS_TEXT = '人声分离选项'
VOLUME_COMPENSATION_TEXT = '音量补偿'
VR_51_MODEL_TEXT = 'VR 5.1模型'
VR_ARCH_TEXT = 'VR架构'
WAV_TYPE_TEXT = 'WAV类型'
CUDA_NUM_TEXT = 'GPU设备'
WINDOW_SIZE_TEXT = '窗口大小'
YES_TEXT = '是'
VERIFY_INPUTS_TEXT = '验证输入'
AUDIO_INPUT_TOTAL_TEXT = '音频输入总数'
MDX23C_ONLY_OPTIONS_TEXT = '仅MDXNET23选项'
PROCESS_STARTING_TEXT = '处理开始... '
MISSING_MESS_TEXT = '缺失或损坏。'
SIMILAR_TEXT = "相同。"
LOADING_VERSION_INFO_TEXT = '正在加载版本信息...'
CHECK_FOR_UPDATES_TEXT = '检查更新'
INFO_UNAVAILABLE_TEXT = "信息不可用。"
UPDATE_CONFIRMATION_TEXT = '您确定要继续吗？\n\n应用程序需要重启。\n'
BROKEN_OR_INCOM_TEXT = '已移除损坏或不兼容的文件。请查看错误日志以获取详细信息。'
BMAC_UVR_TEXT = 'UVR \'请我喝杯咖啡\'链接'
MDX_MENU_WAR_TEXT = '(如果您不确定，请保持此设置不变。)'
NO_FILES_TEXT = '无文件'
CHOOSE_INPUT_TEXT = '选择输入'
OPEN_INPUT_DIR_TEXT = '打开输入目录'
BATCH_PROCESS_MENU_TEXT = '批处理菜单'
TEMP_FILE_DELETION_TEXT = '临时文件删除'
VOCAL_SPLITTER_OPTIONS_TEXT = '人声分离器选项'
WAVEFORM_ENSEMBLE_TEXT = '波形合奏'
SELECT_INPUT_TEXT = '选择输入'
SELECT_OUTPUT_TEXT = '选择输出'
TIME_CORRECTION_TEXT = '时间校正'
UVR_LIS_INFO_TEXT = 'UVR许可证信息'
ADDITIONAL_RES_CREDITS_TEXT = '附加资源和鸣谢'
SAVE_INST_MIXTURE_TEXT = '保存乐器混合'
DOWNLOAD_UPDATE_IN_APP_TEXT = '在应用程序中下载更新'
WAVE_TYPE_TEXT = 'WAVE类型'
OPEN_LINK_TO_MODEL_TEXT = "打开模型链接"
OPEN_MODEL_DIRECTORY = "打开模型目录"
SELECTED_MODEL_PLACE_PATH_TEXT = '选择模型放置路径'
IS_INVERSE_STEM_TEXT = "是反向音轨"
INPUT_STEM_NAME_TEXT = "输入音轨名称"
INPUT_UNIQUE_STEM_NAME_TEXT = "输入唯一音轨名称"
DONE_MENU_TEXT = "完成"
OK_TEXT = "确定"
ENSEMBLE_WARNING_NOT_ENOUGH_SHORT_TEXT = "模型不足"
ENSEMBLE_WARNING_NOT_ENOUGH_TEXT = "您必须选择2个或更多模型才能保存合奏。"
NOT_ENOUGH_ERROR_TEXT = "文件数量不足，无法处理。\n"
INVALID_FOLDER_ERROR_TEXT = '无效文件夹', '您给定的导出路径不是有效的文件夹！'

GET_DL_VIP_CODE_TEXT = ("通过访问以下链接之一获取代码。\n从那里您可以捐赠、捐助，\n或仅获取代码！\n（获取VIP代码不需要捐赠）")
CONFIRM_RESTART_TEXT = '重启确认', '这将重启应用程序并停止任何正在运行的进程。您当前的设置将被保存。 \n\n您确定要继续吗？'
ERROR_LOADING_FILE_TEXT = '加载以下文件时出错', '原始错误详细信息'
LOADING_MODEL_TEXT = '正在加载模型'
FULL_APP_SET_TEXT = '完整应用程序设置'
PROCESS_STARTING_TEXT = '处理开始... '
PROCESS_STOPPED_BY_USER = '\n\n处理已被用户停止。'
NEW_UPDATE_FOUND_TEXT = lambda version:f"\n\n发现新更新: {version}\n\n在\"设置\"菜单中单击更新按钮以下载并安装！"
ROLL_BACK_TEXT = '单击此处回滚'

def secondary_stem(stem:str):
    """Determines secondary stem"""
    
    stem = stem if stem else NO_STEM
    
    if stem in STEM_PAIR_MAPPER.keys():
        for key, value in STEM_PAIR_MAPPER.items():
            if stem in key:
                secondary_stem = value
    else:
        secondary_stem = stem.replace(NO_STEM, "") if NO_STEM in stem else f"{NO_STEM}{stem}"
    
    return secondary_stem
