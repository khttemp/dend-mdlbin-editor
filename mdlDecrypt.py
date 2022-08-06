# -*- coding: utf-8 -*-

import struct
import os
import copy
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

cmdList = [
    "Tx",
    "TxSize",
    "Alpha",
    "End",
    "Pos",
    "ColorALL",
    "Move",
    "STAGE_BGM",
    "SetFlat3D",
    "ChangeFlat3D",
    "SetCamDir",
    "DisCamDir",
    "Set3DObj",
    "SetWAngleX",
    "SetWAngleY",
    "SetWAngleZ",
    "SetLAngleX",
    "SetLAngleY",
    "SetLAngleZ",
    "SetBoneWAngleX",
    "SetBoneWAngleY",
    "SetBoneWAngleZ",
    "SetBoneLAngleX",
    "SetBoneLAngleY",
    "SetBoneLAngleZ",
    "ShowMesh",
    "HideMesh",
    "PlayAnime",
    "Length_End",
    "SetScall",
    "RACE_START",
    "RACE_END",
    "FADE_STAGE_BGM",
    "CHANGE_SCENE",
    "LPos",
    "LMove",
    "LLoopX",
    "LLoopY",
    "LLoopZ",
    "Angle",
    "AngleLoop",
    "Move2",
    "PosX",
    "PosY",
    "PosZ",
    "PlaySE",
    "SET_MT_NONE",
    "SetCamPos",
    "SetCamTarget",
    "CamMoveWait",
    "SetComic",
    "ComicPos",
    "ComicAlpha",
    "ComicWait",
    "Scene_to_Comic",
    "SKY_DOME",
    "Fill_BG",
    "ComicEnd",
    "CamComtroll",
    "ComicSceneStop",
    "BtnWait",
    "EyeMove",
    "SetZoom",
    "BG_Alpha",
    "BG_Wait",
    "StartCount",
    "WaitMoveEye",
    "WaitFrame",
    "FTV_Play",
    "FTV_Wait",
    "HideMsgWnd",
    "FTV_End",
    "SkipEventPoint",
    "SkipEventFlg",
    "PlayComicSE",
    "StopComicSE",
    "PlayComicBGM",
    "StopComicBGM",
    "VolComicBGM",
    "HideALLComic",
    "Stage_BGM_Vol",
    "SET_CPU_FLG",
    "SET_CPU_MODE",
    "CHK_LENGTH",
    "END_CHK_LENGTH",
    "CHK_POSTION",
    "END_CHK_POSTION",
    "WAIT_MOTION",
    "END_WAIT_MOTION",
    "CHANGE_SPEED",
    "CHANGE_CAM_TYPE",
    "Set2P",
    "CharChk_and_Tx",
    "ChangeR",
    "ChangeG",
    "ChangeB",
    "ChangeColor",
    "SetGray",
    "MoveX",
    "MoveY",
    "MoveZ",
    "SetUV_X",
    "RePlay",
    "IsStart",
    "ShowGoal",
    "CHK_WIN_TRAIN",
    "END_CHK_WINTRAIN",
    "N_ADD_OBJ",
    "N_POS",
    "START_TIME_LINE",
    "N_MOVE",
    "WAIT_TIME_LINE",
    "N_DEL_OBJ",
    "SCREEN_FADE",
    "N_CHANGE_ANIME",
    "TRAIN_SPEED",
    "TRAIN_FLG",
    "SCENE_LIGHT",
    "CHANGE_CAM_LENGTH",
    "CHANGE_CAM_DIRX",
    "CHANGE_CAM_DIRY",
    "CHANGE_CAM_DIRZ",
    "R_Drift",
    "L_Drift",
    "IS_TRAIN_HIT",
    "TO_RAIL",
    "SLEEP_TRAIN",
    "RandWAngle",
    "RandMove",
    "ADD_OBJ",
    "START_COMIC",
    "SetRand3DObj",
    "Offset3DObj",
    "RandPos",
    "RandPlaySE",
    "RandAngleX",
    "RandAngleY",
    "RandAngleZ",
    "CHK_TRAIN_STATE",
    "END_CHK_TRAIN_STATE",
    "CHK_TRAIN_SPEED_U",
    "CHK_TRAIN_SPEED_D",
    "END_CHK_TRAIN_SPEED_U",
    "END_CHK_TRAIN_SPEED_D",
    "ChkStory_and_Tx",
    "ClearStory_and_Tx",
    "N_L_ANGLE_X",
    "N_L_ANGLE_Y",
    "N_L_ANGLE_Z",
    "Comic_Glay",
    "N_MoveMesh_X",
    "N_MoveMesh_Y",
    "N_MoveMesh_Z",
    "SetComic_Blur",
    "SetComic_Blur_Speed",
    "TRACK_BOMB",
    "Hide_Sky_Doom",
    "ADD_POINT",
    "CHK_POINT",
    "ELSE_CHK_POINT",
    "ELSE_IF_CHK_POINT",
    "END_CHK_POINT",
    "GOTO_SCRIPT",
    "SHEAK_COMIC",
    "STORY_OPEN",
    "STORY_CLEAR",
    "CHAR_OPEN",
    "SAVE_GAME",
    "KEISUKE_COUNT",
    "RandPlayComicSE",
    "TITLE_MODE",
    "GOING",
    "RAND_IF",
    "ELSE_RAND_IF",
    "END_RAND_IF",
    "CHK_SP_BREAK",
    "END_CHK_SP_BREAK",
    "CHK_DRIFT",
    "END_CHK_DRIFT",
    "ENDING_MODE",
    "ChkCause_and_Tx",
    "SET_DRAW_TYPE",
    "To_TxSize",
    "OPEN_CAUSE",
    "DIS_TRAIN_SPEED",
    "CHK_RACE_TIME",
    "END_CHK_RACE_TIME",
    "End_Comic",
    "WAIT_RAIL",
    "END_WAIT_RAIL",
    "COMIC_SCALE",
    "USO_COUNT",
    "WaitRandPlaySE",
    "FROM",
    "GOTO",
    "CHK_TRAIN_TYPE",
    "RAND_IF_AVG",
    "CHK_NOTCH",
    "WAIT_RAIL_ONLY",
    "ONE_TRACK_DRIFT",
    "LAST_STATION",
    "OSSAN",
    "SET_TAIL_SCALE",
    "OPEN_HUTA",
    "SET_GN",
    "MDL_GETINDEX",
    "INDEX_BONE_ROT_X",
    "INDEX_BONE_ROT_Y",
    "INDEX_BONE_ROT_Z",
    "INDEX_BONE_L_ROT_X",
    "INDEX_BONE_L_ROT_Y",
    "INDEX_BONE_L_ROT_Z",
    "CREATE_INDEX",
    "IB_LI_CREATE_ROT_X",
    "IB_LI_CREATE_ROT_Y",
    "IB_LI_CREATE_ROT_Z",
    "IB_LI_SET_ROT_X",
    "IB_LI_SET_ROT_Y",
    "IB_LI_SET_ROT_Z",
    "IB_LI_SET_LOOP_X",
    "IB_LI_SET_LOOP_Y",
    "IB_LI_SET_LOOP_Z",
    "ADD_MY_OBJ",
    "INDEX_BONE_L_POS_X",
    "INDEX_BONE_L_POS_Y",
    "INDEX_BONE_L_POS_Z",
    "IB_LI_CREATE_L_POS_X",
    "IB_LI_CREATE_L_POS_Y",
    "IB_LI_CREATE_L_POS_Z",
    "IB_LI_SET_L_POS_X",
    "IB_LI_SET_L_POS_Y",
    "IB_LI_SET_L_POS_Z",
    "FROM_ADDMT",
    "MOVE_UV_X",
    "MOVE_UV_Y",
    "CREATE_UV_MOVE_X",
    "IB_LI_SET_LOOP_LPOSX",
    "IB_LI_SET_LOOP_LPOSY",
    "IB_LI_SET_LOOP_LPOSZ",
    "RELEASE_ALL_IB_LIST",
    "ADD_MY_OBJ_INDEX",
    "TO_TAGET_POS",
    "ATK_HIT",
    "ATK_END",
    "SET_RELEASE_PARAM",
    "CREATE_LENSFLEAR",
    "SET_LENSFLEAR_PARAM",
    "SET_LENSFLEAR_MT",
    "RAIL_POS_TO_BUFF",
    "BUFF_TO_CAM_POS",
    "BUFF_TO_TARGET_POS",
    "FTV_BASE_PROC",
    "FTV_NEXT_PROC",
    "MDL_INDEX_TO_VIEW",
    "SET_FOG_LENGTH",
    "SET_UV_MOVE_X",
    "SET_UV_LOOP_X",
    "CREATE_MESH_INDEX",
    "SET_MESH_INDEX",
    "INDEX_BONE_L_ADD_ROT_X",
    "INDEX_BONE_L_ADD_ROT_Y",
    "INDEX_BONE_L_ADD_ROT_Z",
    "CHANGE_SCALL",
    "CHK_CLEAR_STORY",
    "CHK_OPEN_STORY",
    "SET_LENSFLEAR_ALL_FLG",
    "CHK_USE_CHAR",
    "SET_OBJ_FOG_NO",
    "SET_OBJ_RENDER_ID",
    "PLAY_STAGE_BGM",
    "CHANGE_TRAIN_FOG",
    "FIRST_OBJ_SET_ANIME",
    "SET_CAMPOINT_2P2C",
    "SET_CAMPOINT_1P2C",
    "CAM_POINT_PER",
    "CAM_TARGET_PER",
    "SET_CAM_POINT_LENGTH",
    "SET_CAM_OFFSET",
    "START_WIPER",
    "CREATE_TRAIN_ORG",
    "ORG_SET_RAIL",
    "ORG_ADD",
    "SET_CAMPOINT_K",
    "ORG_SET_POS",
    "ORG_SET_FOG",
    "ORG_RELEASE",
    "PLAY_FTV_END",
    "CNG_TRAIN_MAT_COL",
    "CNG_ORG_MAT_COL",
    "IS_CAUTION",
    "ENDWAIT_COMIC",
    "SET_COMIC_BG_COLOR",
    "TX_2_TRAIN",
    "CHANGE_MT_COL_TRAIN",
    "CNG_MT_COL",
    "RETURN",
    "ReLoadSE",
    "BASE_POINT_CAM",
    "STOP_3D",
    "STOP_STAGE_BGM",
    "TRAIN_UD",
    "SET_CAM_TARGET_OFFSET",
    "SET_CAM_POINT_1T_ROT",
    "SET_CAM_T_LENGHT",
    "SET_CAM_T_ROT_X",
    "SET_CAM_T_ROT_Y",
    "SET_CAM_T_OFFSET",
    "NO_OUTRUN",
    "SET_WHEEL_FIRE",
    "RELOAD_OP_TRAIN",
    "BackR_Drift",
    "BackL_Drift",
    "CHK_MOTION",
    "ORG_SET_STYLE_POS",
    "RECREATE_TRAIN",
    "SET_CAMPOINT_1P2T",
    "BUFF_TO_SC_CAM_POS",
    "SC_ORG_MODE_CHANGE",
    "SC_ORG_INIT_POS",
    "SC_ORG_SET_POS",
    "SC_ORG_SET_ROT",
    "SC_ORG_SET_X_ROT",
    "SC_ORG_SET_Y_ROT",
    "SC_ORG_SET_Z_ROT",
    "SET_SC_KOTEI_CAM_POS",
    "SET_SC_KOTEI_CAM_T_POS",
    "START_SC_WIPER",
    "SUPER_DRIFT",
    "CNG_TRAIN_NO_MAT_COL",
    "ERR_CMD",
    "K_HN",
    "TO_TRACK_RAIL",
    "IS_NO_DRAMA",
    "CNG_TRAIN_NO_MAT_RGBA",
    "SHOW_RECORD",
    "WAIT_RECORD_END",
    "IB_LI_SET_UPDATE_FLG",
    "PTCL_SCALL",
    "PTCL_COLOR",
    "PTCL_ALPHA",
    "PTCL_DRAWTYPE",
    "PTCL_ANGLE",
    "PTCL_RAND_ANGLE",
    "PTCL_RAND_COLOR",
    "PTCL_RAND_ALPHA",
    "PTCL_RAND_SCALL",
    "IB_ADD_PTCL",
    "PTCL_RAND_TONE_COLOR",
    "IS_ALPHA_END",
    "PTCL_L_POS",
    "PTCL_RAND_L_POS",
    "CREATE_MAT_COLOR_R_INTERLIST",
    "CREATE_MAT_EMISSIVE_R_INTERLIST",
    "SET_MAT_COLOR_R",
    "SET_MAT_COLOR_G",
    "SET_MAT_COLOR_B",
    "SET_MAT_COLOR_LOOP",
    "SET_MAT_EMISSIVE_R",
    "SET_MAT_EMISSIVE_G",
    "SET_MAT_EMISSIVE_B",
    "SET_MAT_EMISSIVE_LOOP",
    "CREATE_MAT_COLOR_G_INTERLIST",
    "CREATE_MAT_EMISSIVE_G_INTERLIST",
    "CREATE_MAT_COLOR_B_INTERLIST",
    "CREATE_MAT_EMISSIVE_B_INTERLIST",
    "CREATE_UV_MOVE_Y",
    "SET_UV_MOVE_Y",
    "SET_UV_LOOP_Y",
    "INDEX_RAND_ROT_X",
    "INDEX_RAND_ROT_Y",
    "INDEX_RAND_ROT_Z",
    "INDEX_RAND_POS_X",
    "INDEX_RAND_POS_Y",
    "INDEX_RAND_POS_Z",
    "RAND_SHOW_MESH",
    "INDEX_RAND_SCALL",
    "ADD_CHILD_OBJ",
    "ADD_OBJ_INDEX",
    "GAS_TARBIN",
    "ENGINE_START",
    "CHANGE_CHILDOBJ_ANIME",
    "IB_SET_W_MT",
    "CHK_OBJ_PARAM",
    "SET_OBJ_PARAM",
    "INDEX_DIR_CAM",
    "CNG_MT_LIGHT",
    "ADD_OBJ_INDEX2",
    "CNG_MT_ALPHA",
    "CREATE_MAT_ALPHA_INTERLIST",
    "SET_MAT_ALPHA",
    "RESTART_MESH_LIST",
    "RAIL_ANIME_CHANGE",
    "STOP_COMIC_SE_ALL",
    "HURIKO",
    "FTV_PLAY_AND_PREV",
    "FTV_END_INHERIT",
    "STATION_NAME_PRIORITY",
    "ALL_FIT",
    "SWAP_TX",
    "CNG_TX",
    "CHK_CAUSE",
    "CNG_ANIME",
    "CHK_OUHUKU",
    "SET_TRAIN_PTCL_AREA",
    "WAIT_DOSAN_LENGTH",
    "END_DOSAN_LENGTH",
    "DOSANSEN",
    "MESH_INDEX_SE_UV_ANIME_FLG",
    "WEATHER",
    "TRAIN_DIR",
    "IS_USE_CHAR",
    "QUICK_SAVE_EVENT",
    "NONE_GOAL",
    "ENGINE_STOP",
    "IS_BTL_MODE",
    "IS_FREE_MODE",
    "FIRST_OBJ_SET_ANIME_SCENE",
    "G_HIDE_MESH",
    "G_SHOW_MESH",
    "STOP_WIPER",
    "TRAIN_ANIME_CHANGE",
    "MESH_INDEX_UV_RESTRT",
    "SET_COMIC_COLOR",
    "CHK_OUTRUN_CNT",
    "CHK_D_AND_NOTCH",
    "ADD_CPU_LEN_OUTRUN",
    "ADD_CPU_SPEED_D_AND_NOTCH",
    "CHK_HIT_CNT",
    "TOP_SPEED_HOSYO",
    "SET_ROOT_BLOCK",
    "RIFT",
    "COLLISION",
    "DIR_VIEW_CHANGE",
    "CHK_RAIL_NO",
    "TRACK_CHANGE",
    "CHK_LENGTH_DIR",
    "CHK_POS_DIR",
    "TRUE_CLASH",
    "KATARIN_RUN",
    "DRAW_UI",
    "STOP_SCRIPT_BGM",
    "SET_STATION_NO",
    "SET_CPU_BREAKE",
    "AMB_ANIME",
    "ONE_DRIFT_FALSE",
    "L_One_Drift",
    "R_One_Drift",
    "Ret_One_Drift",
    "FRONT_JUMP",
    "REAR_JUMP",
    "FRONT_MOVE_X",
    "TRACK_MOVE",
    "TRAIN_JUMP",
    "SET_LIGHT",
    "SET_COL_KASENCHU",
    "SET_KAISO",
    "SET_FOR",
    "CHK_TRAIN_COL",
    "VOL_SCRIPT_BGM",
    "IF_NOTCH",
    "SET_BRIND_SW",
    "SET_MIKOSHI",
    "ADD_FIRE",
    "BREAKE_OR_HIT",
    "OUTRUN",
    "SOFT_ATK",
    "RAIL_STOP",
    "CHANGE_OUHUKU_LINE",
    "BRIND_ATK",
    "OPEN_POS_DLG",
    "PLAY_STAGEBGM_BLOCK",
    "SET_BTL_POINT",
    "CAM_TRAIN",
    "PLAY_SCRIPT_BGM",
    "CNG_FOR",
    "SET_RAILBLOCK_CHECKER",
    "RAIN_SE",
    "TRAIN_STOP",
    "KOTEICAM_BLEND",
    "SCRIPT_RAIN",
    "LINE_CHANGE",
    "WAIT_RAIL_MORE_ONLY",
    "SET_SE_VOL",
    "CAM_TARGET_TRACK",
    "DECAL_D37",
    "DECAL_D39",
    "DECAL_SMOKE",
    "RAIL_PRIORITY",
    "GET_KEY",
    "SHOW_LIGHT",
    "SHOW_IN_LIGHT",
    "FOG_POW",
    "STORY_WIN",
    "RAIN_PARTICLE",
    "D39_FIRE",
    "SET_CPU_SPEED",
    "BODY_AUDIO_PLAY",
    "BODY_AUDIO_STOP",
    "CNG_FADE_SPRITE",
    "RAIL_DRIFT_CHK",
    "INQ_WAIT",
    "CNG_SCCAM_TRAIN",
    "STOP_TRAIN_SE",
    "PLAY_SCRIPT_BGM_TIME",
    "CNG_BODY_COLOR",
    "LOAD_TRAIN",
    "SHOW_BLOCK",
    "UPDATE_LIGHT_FRARE",
    "WAIT_RAIL_MORE_GOTO",
    "CREATE_AURA",
    "AURA_ALPHA",
    "SET_LV_JUMP",
    "CREATE_EFFECT_CAM",
    "TO_EFFECT_CAM",
    "EFFECT_CAM_POW",
    "EFFECT_CAM_COLOR",
    "EFFECT_CAM_ALPHA",
    "HIDE_LIGHT",
    "USE_EFFECT_CAM",
    "USE_EFFECT_CAM_RGB",
    "EFFECT_CAM_RGB",
    "COPY_TRAIN_POS",
    "COL_SET",
    "CNG_CPU_TRAIN",
    "BTN_GOTO",
    "NO_TIMESCALE_KOMA",
    "EFFCAM_NOIZE",
    "EFFCAM_GRI",
    "EFFCAM_BLOCKNOISE",
    "CREATE_TQ5000_FLAGMENT",
    "USE_TQ5000_FLAGMENT",
    "TQ5000_FLAGPOS",
    "HUMIKIRI_VOL",
    "TO_EFFECT_CAM_BODY",
    "TO_NORM_CAM",
    "TO_920",
    "NO_TIMESCALE_FVT",
    "CNG_TARGET_BODY",
    "SC_ADD_POINT",
    "CHK_SC_POINT",
    "KAISO_TO_DUEL",
    "SHOW_ST",
    "ORG_UPDATE",
    "SET_RAILBLOCK_POS",
    "SET_LIGHT_OVER",
    "CREATE_STAFFROLL",
    "STAFFROLL_START",
    "WAIT_STAFFROLL",
    "SC_OUTRUN",
    "CREATE_TAKMIS",
    "SET_TAKMIS_POS",
    "SET_TAKMIS_ALPHA",
    "FRONT_DOOR",
    "SET_KOMA_DEPTH",
    "D37_FIRE",
    "AMB_HIT_WAIT",
    "ShowRecord",
    "FIT_PER",
    "CREATE_COMIC_PC",
    "SET_COMIC_PC",
    "PAUSE_STAGE_BGM",
    "SET_KAKAPO",
    "KOMA_KAKAPO",
    "START_TARBINE",
    "END_TARBINE",
    "TARBINE_FTV_START",
    "TARBINE_FTV_END",
    "STORY_ENGINE",
    "RAND_GOTO",
    "KQ_SOUND",
    "STORY_GOTO",
    "PLAY223HONE",
    "RB26",
    "PLAYORGSE",
    "H2300_GOAL",
    "SCRIPT_CMD_MAX"
]

ver = 0
index = None
line = None
indexInfoList = []
byteArr = []
scriptDataAllInfoList = []
file_path = ""
max_param = 0
frame = None
copyScriptData = None

def readFile():
    #print("="*30)
    global ver
    global index
    global line

    ver = line[0]
    index = 1
    imgCnt = line[index]
    index += 1
    
    for img in range(imgCnt):
        imgNameLen = line[index]
        index += 1
        imgName = line[index:index+imgNameLen].decode("shift-jis")
        #print(imgName)
        index += imgNameLen
        if ver == 4:
            tmp = line[index]
            index += 1
            if tmp != 0:
                index += 2

    imgSizeCnt = line[index]
    index += 1

    for imgSize in range(imgSizeCnt):
        imgIdx = line[index]
        index += 1
        for i in range(4):
            size = struct.unpack("<f", line[index:index+4])[0]
            index += 4

    smfCnt = line[index]
    index += 1
    for i in range(smfCnt):
        smfLen = line[index]
        index += 1
        smfName = line[index:index+smfLen].decode("shift-jis")
        #print(smfName)
        index += smfLen

    wavCnt = line[index]
    index += 1
    for i in range(wavCnt):
        wavLen = line[index]
        index += 1
        wavName = line[index:index+wavLen].decode("shift-jis")
        #print(wavName)
        index += wavLen
        index += 1

    if ver != 1:
        lightTgaCnt = line[index]
        index += 1
        for i in range(lightTgaCnt):
            for j in range(2):
                lightTgaLen = line[index]
                index += 1
                lightTgaName = line[index:index+lightTgaLen].decode("shift-jis")
                #print("tga:", lightTgaName)
                index += lightTgaLen

            for i in range(2):
                tempF = struct.unpack("<f", line[index:index+4])[0]
                #print("tgaF:",tempF)
                index += 4
            #print(struct.unpack("<4c", line[index:index+4]))
            index += 4
            #print(struct.unpack("<h", line[index:index+2])[0])
            index += 2

    readScript()

def nextSection(line, cmdDiffIdx = None):
    global ver
    global index
    global max_param

    scriptDataInfo = []
    if ver != 1:
        if line[index] != 0:
            index += 1
            index += 5
        else:
            index += 1
    else:
        index += 6
        
    cmdcnt = line[index]
    index += 1
    if cmdDiffIdx != None:
        cmdcnt = cmdDiffIdx
        
    for i in range(cmdcnt):
        scriptData = []
        idx = struct.unpack("<h", line[index:index+2])[0]
        index += 2
        scriptData.append(idx)

        cmdNum = struct.unpack("<h", line[index:index+2])[0]
        index += 2
        scriptData.append(cmdNum)
        
        paraCnt = line[index]
        if max_param < paraCnt:
            max_param = paraCnt
        index += 1
        scriptData.append(paraCnt)

        if ver >= 3:
            fileCnt = line[index]
            index += 1
        elif ver == 2 and cmdList[cmdNum] in ["MDL_GETINDEX", "SET_LENSFLEAR_MT"]:
            fileCnt = 1
        else:
            fileCnt = 0xFF
        scriptData.append(fileCnt)

        if fileCnt != 0xFF:
            paraCnt -= fileCnt

        for j in range(paraCnt):
            temp = struct.unpack("<f", line[index:index+4])[0]
            temp = round(temp, 5)
            index += 4 
            scriptData.append(temp)

        if fileCnt != 0xFF:
            for j in range(fileCnt):
                txtLen = line[index]
                index += 1
                temp = line[index:index+txtLen].decode("shift-jis")
                index += txtLen
                scriptData.append(temp)

        scriptDataInfo.append(scriptData)
    return scriptDataInfo

def readScript():
    global ver
    global index
    global line
    global indexInfoList
    global scriptDataAllInfoList

    indexInfoList = []
    scriptDataAllInfoList = []

    allSectionCnt = line[index]
    index += 1

    for section in range(allSectionCnt):
        indexInfo = []
        cnt = line[index]
        index += 1

        flag = False

        scriptDataInfoList = []
        for c in range(cnt):
            indexInfo.append(index)
            scriptDataInfo = nextSection(line)
            scriptDataInfoList.append(scriptDataInfo)
            
        indexInfoList.append(indexInfo)
        scriptDataAllInfoList.append(scriptDataInfoList)
###

class Scrollbarframe():
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(expand=True, fill=BOTH)

        self.tree = ttk.Treeview(self.frame, selectmode="browse")

        self.scrollbar_x = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=lambda f, l: self.scrollbar_x.set(f, l))
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        self.scrollbar_y = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=lambda f, l: self.scrollbar_y.set(f, l))
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        self.tree.pack(expand=True, fill=BOTH)
        self.tree.bind("<<TreeviewSelect>>", self.treeSelect)
        
    def treeSelect(self, event):
        selectId = self.tree.selection()[0]
        selectItem = self.tree.set(selectId)
        editLineBtn['state'] = 'normal'
        insertLineBtn['state'] = 'normal'
        deleteLineBtn['state'] = 'normal'
        copyLineBtn['state'] = 'normal'
        
        if "#" in selectItem["コマンド名"]:
            listNumModifyBtn['state'] = 'normal'
            editLineBtn['state'] = 'disabled'
            deleteLineBtn['state'] = 'disabled'
            copyLineBtn['state'] = 'disabled'
        else:
            listNumModifyBtn['state'] = 'disabled'
            editLineBtn['state'] = 'normal'
        v_select.set(selectItem["番号"])
        

class inputDialog(sd.Dialog):
    def __init__(self, master, num, cmdItem=None):
        self.v_paramList = []
        self.num = num
        self.cmdItem = cmdItem
        if self.cmdItem != None:
            self.mode = "edit"
            self.info = "このまま修正してもよろしいですか？"
            self.p_cmd = self.cmdItem["コマンド名"]
            self.p_cnt = len(self.cmdItem)-4
        else:
            self.mode = "insert"
            self.info = "このまま挿入してもよろしいですか？"
            self.p_cmd = None
            self.p_cnt = None
        super().__init__(master)
    def body(self, master):
        self.resizable(False, False)
        self.idxLb = ttk.Label(master, text="index", width=12, font=("", 14))
        self.idxLb.grid(row=0, column=0, sticky=N+S)
        self.v_idx = StringVar()
        if self.cmdItem != None:
            self.v_idx.set(self.cmdItem["index"])
        else:
            self.v_idx.set(0)
        self.idxEt = ttk.Entry(master, textvariable=self.v_idx, width=33)
        self.idxEt.grid(row=0, column=1, sticky=N+S, pady=10)
        
        self.cmdLb = ttk.Label(master, text="コマンド名", width=12, font=("", 14))
        self.cmdLb.grid(row=1, column=0, sticky=N+S)
        self.v_cmd = StringVar()
        cmdCopy = copy.deepcopy(cmdList)
        cmdCopy.sort()
        self.cmdCb = ttk.Combobox(master, textvariable=self.v_cmd, width=30, state="readonly", value=cmdCopy)
        self.cmdCb.grid(row=1, column=1, sticky=N+S, pady=10)
        if self.p_cmd != None:
            self.v_cmd.set(self.p_cmd)
        else:
            self.v_cmd.set(cmdCopy[0])

        self.paramCntLb = ttk.Label(master, text="パラメータ数", width=12, font=("", 14))
        self.paramCntLb.grid(row=2, column=0, sticky=N+S)
        self.v_paramCnt = IntVar()
        paramCntList = [cnt for cnt in range(0, 16)]
        self.paramCntCb = ttk.Combobox(master, textvariable=self.v_paramCnt, width=30, state="readonly", value=paramCntList)
        self.paramCntCb.grid(row=2, column=1, sticky=N+S, pady=10)
        if self.p_cnt != None:
            self.v_paramCnt.set(self.p_cnt)
        else:
            self.v_paramCnt.set(0)

        if self.cmdItem == None:
            self.position = ttk.Label(master, text="挿入する位置", width=12, font=("", 14))
            self.position.grid(row=3, column=0, sticky=N+S)
            self.v_position = StringVar()
            positionList = ["後", "前"]
            self.positionCb = ttk.Combobox(master, textvariable=self.v_position, width=30, state="readonly", value=positionList)
            self.positionCb.grid(row=3, column=1, sticky=N+S, pady=10)
            self.v_position.set(positionList[0])

        self.xLine = ttk.Separator(master, orient=HORIZONTAL)
        self.xLine.grid(columnspan=2, row=4, column=0, sticky=E+W, pady=10)

        self.paramFrame = ttk.Frame(master)
        self.paramFrame.grid(columnspan=2, row=5, column=0, sticky=N+E+W+S)

        self.paramLb = ttk.Label(self.paramFrame)
        self.paramLb.grid(row=0, column=0)

        if ver == 2:
            self.cmdCb.bind('<<ComboboxSelected>>', lambda e: self.cmdLock())
            self.cmdLock()
            
        self.paramCntCb.bind('<<ComboboxSelected>>', lambda e: self.selectParam(self.v_paramCnt.get(), self.paramFrame))
        if self.p_cnt != 0:
            self.selectParam(self.v_paramCnt.get(), self.paramFrame, self.cmdItem)

    def selectParam(self, paramCnt, frame, cmdItem=None):
        global ver
        
        self.v_paramList = []
        children = frame.winfo_children()
        for child in children:
            child.destroy()

        if paramCnt == 0:
            self.paramLb = ttk.Label(frame)
            self.paramLb.grid(row=0, column=0)

        for i in range(paramCnt):
            self.paramLb = ttk.Label(frame, text="param{0}".format(i+1), font=("", 14))
            self.paramLb.grid(row=i, column=0, sticky=N+S)
            v_param = StringVar()
            self.v_paramList.append(v_param)
            self.paramEt = ttk.Entry(frame, textvariable=v_param, width=30)
            self.paramEt.grid(row=i, column=1, sticky=N+S)
        if cmdItem != None:
            for i in range(len(self.v_paramList)):
                self.v_paramList[i].set(cmdItem["param{0}".format(i+1)])

    def cmdLock(self):
        global ver
        if ver == 2:
            if self.v_cmd.get() in ["MDL_GETINDEX", "SET_LENSFLEAR_MT"]:
                self.paramCntCb["state"] = "disabled"
                self.paramCntCb.current(2)
                self.selectParam(self.v_paramCnt.get(), self.paramFrame)
            else:
                self.paramCntCb["state"] = "normal"

    def buttonbox(self):
        box = Frame(self, padx=5, pady=5)
        self.okBtn = Button(box, text="OK", width=10, command=self.okPress)
        self.okBtn.grid(row=0, column=0, padx=5)
        self.cancelBtn = Button(box, text="Cancel", width=10, command=self.cancel)
        self.cancelBtn.grid(row=0, column=1, padx=5)
        box.pack()

    def okPress(self):
        global ver
        editParamList = []
        textParamList = []
        paramIdx = 0
        floatFlag = True
        errorFlag = False
        for var in self.v_paramList:
            num = 0
            if floatFlag:
                try:
                    num = float(var.get())
                except:
                    floatFlag = False
                    if ver < 3:
                        if ver != 2:
                            errorFlag = True
                        elif self.v_cmd.get() not in ["MDL_GETINDEX", "SET_LENSFLEAR_MT"]:
                            errorFlag = True
                        else:
                            if paramIdx != 1:
                                errorFlag = True

            if ver == 2:
                if self.v_cmd.get() in ["MDL_GETINDEX", "SET_LENSFLEAR_MT"] and paramIdx == 1:
                    floatFlag = False

            if floatFlag:
                editParamList.append(num)
            else:
                editParamList.append(var.get())
                textParamList.append(paramIdx)
            paramIdx += 1

        if errorFlag:
            mb.showerror(title="エラー", message="不正な値があります")
            return

        msg = ""
        infoMsg = self.info
        for param in textParamList:
            msg += "param{0}\n".format(param+1)

        if len(textParamList) > 0:
            msg += "※上記のparamは文字として保存されます\n\n"
            infoMsg = msg + self.info

        result = mb.askokcancel(title="確認", message=infoMsg, parent=self)
        if result:
            self.ok()
            scriptData = []
            scriptData.append(int(self.v_idx.get()))
            scriptData.append(cmdList.index(self.v_cmd.get()))
            scriptData.append(self.v_paramCnt.get())
            if len(textParamList) == 0:
                scriptData.append(0xFF)
            else:
                scriptData.append(len(textParamList))
                
            for i in range(self.v_paramCnt.get()):
                scriptData.append(editParamList[i])
                    
            (num, listNum, cmdDiffIdx) = searchNums(self.num)

            if self.mode == "insert":
                if self.v_position.get() == "後":
                    cmdDiffIdx += 1

            saveFile(num, listNum, cmdDiffIdx, self.mode, scriptData)

class pasteDialog(sd.Dialog):
    def __init__(self, master, num):
        self.num = num
        super().__init__(master)
    def body(self, master):
        self.resizable(False, False)
        self.posLb = ttk.Label(master, text="挿入する位置を選んでください", font=("", 14))
        self.posLb.pack(padx=10, pady=10)
    def buttonbox(self):
        box = Frame(self, padx=5, pady=5)
        self.frontBtn = Button(box, text="前", font=("", 12), width=10, command=self.frontInsert)
        self.frontBtn.grid(row=0, column=0, padx=5)
        self.backBtn = Button(box, text="後", font=("", 12), width=10, command=self.backInsert)
        self.backBtn.grid(row=0, column=1, padx=5)
        self.cancelBtn = Button(box, text="Cancel", font=("", 12), width=10, command=self.cancel)
        self.cancelBtn.grid(row=0, column=2, padx=5)
        box.pack()
    def frontInsert(self):
        self.ok()
        (num, listNum, cmdDiffIdx) = searchNums(self.num)
        saveFile(num, listNum, cmdDiffIdx, "insert", copyScriptData)
    def backInsert(self):
        self.ok()
        (num, listNum, cmdDiffIdx) = searchNums(self.num)
        saveFile(num, listNum, cmdDiffIdx+1, "insert", copyScriptData)

class listNumModifyDialog(sd.Dialog):
    def __init__(self, master, num, curVal):
        self.num = num
        self.curVal = curVal
        super().__init__(master)
    def body(self, master):
        self.resizable(False, False)
        self.listLb = ttk.Label(master, text="リスト{0}の数を".format(self.num), font=("", 14))
        self.listLb.grid(row=0, column=0)

        self.v_listNum = IntVar()
        self.v_listNum.set(self.curVal)
        self.sp = ttk.Spinbox(master, textvariable=self.v_listNum, font=("", 12), from_=1, to=100, width=5)
        self.sp.grid(row=0, column=1, padx=10)

        self.list2Lb = ttk.Label(master, text="に修正する".format(self.num), font=("", 14))
        self.list2Lb.grid(row=0, column=2)
    def validate(self):
        if self.v_listNum.get() < self.curVal:
            warnMsg = "選択した数は現在より少なく設定してます\nこの数で修正しますか？"
            result = mb.askokcancel(title="確認", message=warnMsg, icon="warning", parent=self)
        else:
            infoMsg = "この数で修正しますか？"
            result = mb.askokcancel(title="確認", message=infoMsg, parent=self)
            
        if result:
            return True
    def apply(self):
        saveFile(int(self.num), 0, -1, "list", self.v_listNum.get())

###

def searchNums(index):
    global frame
    for i in range(index, -1, -1):
        info = frame.tree.set(i)
        if "#" in info["コマンド名"]:
            arr = info["コマンド名"].split(", ")
            num = arr[0].strip("-").strip("#")
            listNum = arr[1].strip("-").strip("#")
            return (int(num), int(listNum), int(index-int(info["番号"])-1))

    return None

def openFile():
    global line
    global byteArr
    global file_path
    file_path = fd.askopenfilename(filetypes=[("MODEL_SCRIPT", "*.BIN")])

    errorMsg = "予想外のエラーが出ました。\n電車でDのコミックスクリプトではない、またはファイルが壊れた可能性があります。"
    if file_path:
        try:
            filename = os.path.basename(file_path)
            v_fileName.set(filename)
            file = open(file_path, "rb")
            line = file.read()
            byteArr = bytearray(line)
            deleteWidget()
            readFile()
            createWidget()
            file.close()
        except Exception as e:
            print(e)
            mb.showerror(title="エラー", message=errorMsg)

def editLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    inputDialog(root, int(selectItem["番号"]), selectItem)

def insertLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    inputDialog(root, int(selectItem["番号"]))

def deleteLine():
    global frame
    selectId = int(frame.tree.selection()[0])
    warnMsg = "選択した行を削除します。\nそれでもよろしいですか？"
    result = mb.askokcancel(title="警告", message=warnMsg, icon="warning")
    if result:
        (num, listNum, cmdDiffIdx) = searchNums(selectId)
        saveFile(num, listNum, cmdDiffIdx, "delete")

def copyLine():
    global frame
    global copyScriptData
    scriptData = []
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    scriptData.append(int(selectItem["index"]))
    scriptData.append(cmdList.index(selectItem["コマンド名"]))
    paramCnt = len(selectItem)-4
    scriptData.append(paramCnt)
    scriptData.append(int(selectItem["ファイルフラグ"]))
    for i in range(paramCnt):
        try:
            temp = float(selectItem["param{0}".format(i+1)])
        except:
            temp = selectItem["param{0}".format(i+1)]
        scriptData.append(temp)
    copyScriptData = copy.deepcopy(scriptData)

    mb.showinfo(title="成功", message="コピーしました")
    pasteLineBtn['state'] = 'normal'

def pasteLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    num = int(selectItem["番号"])
    pasteDialog(root, num)
        
def saveFile(num, listNum, cmdDiffIdx, mode, scriptData = None):
    global ver
    global index
    global byteArr
    global file_path
    global indexInfoList
    global scriptDataAllInfoList

    index = indexInfoList[num][listNum]

    if mode == "list":
        listIdx = index-1
        listcnt = byteArr[listIdx]
        byteArr[listIdx] = scriptData

        for i in range(listcnt):
            if i == scriptData:
                break

            nextSection(byteArr)

        newByteArr = copy.deepcopy(byteArr[0:index])
        if scriptData < listcnt:
            for i in range(listcnt-scriptData):
                nextSection(byteArr)
        else:
            for i in range(scriptData-listcnt):
                newByteArr.extend([1, 0, 0, 0, 1, 0])
                newByteArr.append(0)

        newByteArr.extend(byteArr[index:])
    else:
        cntIdx = index
        if ver != 1:
            if byteArr[cntIdx] != 0:
                cntIdx += 6
            else:
                cntIdx += 1
        else:
            cntIdx += 6

        startIdx = index
        
        if mode == "insert":
            cnt = byteArr[cntIdx]
            byteArr[cntIdx] = (cnt + 1)
        elif mode == "delete":
            cnt = byteArr[cntIdx]
            byteArr[cntIdx] = (cnt - 1)

        nextSection(byteArr, cmdDiffIdx)
        newByteArr = copy.deepcopy(byteArr[0:index])

        if mode == "edit" or mode == "insert":
            bIdx = struct.pack("<h", scriptData[0])
            for n in bIdx:
                newByteArr.append(n)

            bCmd = struct.pack("<h", scriptData[1])
            for n in bCmd:
                newByteArr.append(n)

            newByteArr.append(scriptData[2])
            if ver >= 3:
                newByteArr.append(scriptData[3])

            floatFlag = True
            for i in range(scriptData[2]):
                temp = 0
                if floatFlag:
                    try:
                        temp = float(scriptData[4+i])
                    except:
                        floatFlag = False

                if ver == 2:
                    if cmdList[scriptData[1]] in ["MDL_GETINDEX", "SET_LENSFLEAR_MT"] and i == 1:
                        floatFlag = False
                    
                if floatFlag:
                    bTemp = struct.pack("<f", temp)
                    for n in bTemp:
                        newByteArr.append(n)
                else:
                    temp = scriptData[4+i].encode("shift-jis")
                    newByteArr.append(len(temp))
                    newByteArr.extend(temp)

        index = startIdx
        if mode == "edit" or mode == "delete":
            nextSection(byteArr, cmdDiffIdx+1)
        elif mode == "insert":
            nextSection(byteArr, cmdDiffIdx)
            
        newByteArr.extend(byteArr[index:])

    errorMsg = "保存に失敗しました。\nファイルが他のプログラムによって開かれている\nまたは権限問題の可能性があります"
    try:
        w = open(file_path, "wb")
        w.write(newByteArr)
        w.close()
        mb.showinfo(title="成功", message="スクリプトを改造しました")
        reloadFile()
    except Exception as e:
        print(e)
        mb.showerror(title="保存エラー", message=errorMsg)

def reloadFile():
    global line
    global frame
    global byteArr
    global file_path
    errorMsg = "予想外のエラーが出ました。\n電車でDのコミックスクリプトではない、またはファイルが壊れた可能性があります。"
    if file_path:
        try:
            filename = os.path.basename(file_path)
            v_fileName.set(filename)
            file = open(file_path, "rb")
            line = file.read()
            file.close()
            byteArr = bytearray(line)
            selectId = int(v_select.get())
            deleteWidget()
            readFile()
            createWidget()
            if selectId - 3 < 0:
                frame.tree.see(0)
            else:
                frame.tree.see(selectId-3)
            frame.tree.selection_set(selectId)
        except Exception as e:
            print(e)
            mb.showerror(title="エラー", message=errorMsg)


def listNumModifyBtn():
    global frame
    global scriptDataAllInfoList
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    arr = selectItem["コマンド名"].split(", ")
    num = arr[0].strip("-").strip("#")

    scriptDataInfoList = scriptDataAllInfoList[int(num)]
    listNumModifyDialog(root, num, len(scriptDataInfoList))

root = Tk()
root.title("電車でD モデルバイナリ 改造 1.0.3")
root.geometry("960x640")

menubar = Menu(root)
menubar.add_cascade(label='ファイルを開く', command= lambda: openFile())
root.config(menu=menubar)

v_fileName = StringVar()
fileNameEt = ttk.Entry(root, textvariable=v_fileName, font=("",14), width=20, state="readonly", justify="center")
fileNameEt.place(relx=0.053, rely=0.03)

selectLb = ttk.Label(text="選択した行番号：", font=("",14))
selectLb.place(relx=0.05, rely=0.11)

v_select = StringVar()
selectEt = ttk.Entry(root, textvariable=v_select, font=("",14), width=5, state="readonly", justify="center")
selectEt.place(relx=0.22, rely=0.11)

editLineBtn = ttk.Button(root, text="選択した行を修正する", width=25, state="disabled", command=editLine)
editLineBtn.place(relx=0.32, rely=0.03)

insertLineBtn = ttk.Button(root, text="選択した行に挿入する", width=25, state="disabled", command=insertLine)
insertLineBtn.place(relx=0.54, rely=0.03)

deleteLineBtn = ttk.Button(root, text="選択した行を削除する", width=25, state="disabled", command=deleteLine)
deleteLineBtn.place(relx=0.76, rely=0.03)

copyLineBtn = ttk.Button(root, text="選択した行をコピーする", width=25, state="disabled", command=copyLine)
copyLineBtn.place(relx=0.32, rely=0.11)

pasteLineBtn = ttk.Button(root, text="選択した行に貼り付けする", width=25, state="disabled", command=pasteLine)
pasteLineBtn.place(relx=0.54, rely=0.11)

listNumModifyBtn = ttk.Button(root, text="リストの数を修正する", width=25, state="disabled", command=listNumModifyBtn)
listNumModifyBtn.place(relx=0.32, rely=0.19)

scriptLf = ttk.LabelFrame(root, text="スクリプト内容")
scriptLf.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.70)

def createWidget():
    global scriptDataAllInfoList
    global max_param
    global frame
    frame = Scrollbarframe(scriptLf)

    col_tuple = ('番号', 'index', 'コマンド名', 'ファイルフラグ')
    paramList = []
    for i in range(max_param):
        paramList.append("param{0}".format(i+1))
    col_tuple = col_tuple + tuple(paramList)

    frame.tree['columns'] = col_tuple
    
    frame.tree.column('#0',width=0, stretch=False)
    frame.tree.column('番号', anchor=CENTER, width=50)
    frame.tree.column('index', anchor=CENTER, width=50)
    frame.tree.column('コマンド名',anchor=CENTER, width=130)
    frame.tree.column('ファイルフラグ',width=20, stretch=False)
    for i in range(max_param):
        col_name = "param{0}".format(i+1)
        frame.tree.column(col_name, anchor=CENTER, width=100)

    displayList = []

    frame.tree.heading('番号', text='番号',anchor=CENTER)
    frame.tree.heading('index', text='index',anchor=CENTER)
    frame.tree.heading('コマンド名', text='コマンド名', anchor=CENTER)
    for i in range(max_param):
        col_name = "param{0}".format(i+1)
        displayList.append(col_name)
        frame.tree.heading(col_name,text=col_name, anchor=CENTER)

    frame.tree["displaycolumns"] = ["番号", "index", "コマンド名"]
    frame.tree["displaycolumns"] += tuple(displayList)

    index = 0
    num = 0
    for scriptDataInfoList in scriptDataAllInfoList:
        listNum = 0
        for scriptDataInfo in scriptDataInfoList:
            frame.tree.insert(parent='', index='end', iid=index ,values=(index, "-", "---#{0}, {1}#---".format(num, listNum) ))
            listNum += 1
            index += 1
            for scriptData in scriptDataInfo:
                data = (index, scriptData[0], cmdList[scriptData[1]], scriptData[3])
                paramCnt = scriptData[2]
                paramList = []
                for i in range(paramCnt):
                    paramList.append(scriptData[4+i])
                data = data + tuple(paramList)
                frame.tree.insert(parent='', index='end', iid=index ,values=data)
                index += 1
        num += 1

def deleteWidget():
    global scriptLf
    global indexList
    global scriptDataInfo
    global scriptDataInfoList
    global scriptDataAllInfoList
    
    children = scriptLf.winfo_children()
    for child in children:
        child.destroy()

    indexList = []
    scriptDataInfo = []
    scriptDataInfoList = []
    scriptDataAllInfoList = []
    v_select.set("")
    editLineBtn['state'] = 'disabled'
    insertLineBtn['state'] = 'disabled'
    deleteLineBtn['state'] = 'disabled'

root.mainloop()
