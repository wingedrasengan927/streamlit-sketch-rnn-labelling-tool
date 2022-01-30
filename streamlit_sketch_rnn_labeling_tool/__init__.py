import streamlit as st
import streamlit.components.v1 as components

import os

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "SketchCanvas",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "SketchCanvas", path=build_dir)

def st_sketch_tool(width=640, height=480, key=None):
    data = _component_func(width=width, height=height, key=key, default=[[0, 0, 0, 0, 0]])
    return data
