'''
Author: dylan
Date: 2022-05-04 23:30:42
LastEditTime: 2022-05-04 23:31:06
LastEditors: dylan
Description: 
FilePath: \serverDemo\styles\default.py
'''
"""
    pygments.styles.default
    ~~~~~~~~~~~~~~~~~~~~~~~
    The default highlighting style.
    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class DefaultStyle(Style):
    """
    The default style (inspired by Emacs 22).
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "#3D7B7B",
        Comment.Preproc:           "#9C6500",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "#008000",
        # Keyword.Pseudo:            "nobold",
        Keyword.Type:              "#B00040",

        Operator:                  "#666666",
        Operator.Word:             "#AA22FF",

        Name.Builtin:              "#008000",
        Name.Function:             "#0000FF",
        Name.Class:                "#0000FF",
        Name.Namespace:            "#0000FF",
        Name.Exception:            "#CB3F38",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#767600",
        Name.Entity:               "#717171",
        Name.Attribute:            "#687822",
        Name.Tag:                  "#008000",
        Name.Decorator:            "#AA22FF",

        String:                    "#BA2121",
        # String.Doc:                "italic",
        String.Interpol:           "#A45A77",
        String.Escape:             "#AA5D1F",
        String.Regex:              "#A45A77",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#008000",
        Number:                    "#666666",

        Generic.Heading:           "#000080",
        Generic.Subheading:        "#800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#008400",
        Generic.Error:             "#E40000",
        # Generic.Emph:              "italic",
        # Generic.Strong:            "bold",
        Generic.Prompt:            "#000080",
        Generic.Output:            "#717171",
        Generic.Traceback:         "#04D",

        Error:                     "#FF0000"
    }