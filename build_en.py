"""
ColorKit 영어 버전 자동 생성 스크립트
실행: python build_en.py
결과: en/ 폴더에 영어 버전 HTML 파일 생성
"""

import os, re, shutil, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(BASE, 'en')
os.makedirs(EN_DIR, exist_ok=True)

# ── 1. 페이지별 메타 번역 ─────────────────────────────────────────────────────
PAGE_META = {
    'index.html': {
        'title': 'Free Online Color Tools – Picker, Palette, Gradient, Converter | WooaColor',
        'desc':  'HEX·RGB·HSL conversion, color extraction, gradient & palette generation, WCAG contrast checking, CSS box/text-shadow and more. Free online color tools at WooaColor.',
        'kw':    'color converter, color picker, palette generator, gradient generator, HEX RGB HSL, color contrast, WCAG, box shadow, text shadow, opacity converter, free color tools',
        'og_title': 'Free Online Color Tools – Picker, Palette & Gradient | WooaColor',
        'og_desc':  'Color picker, palette generator, gradient maker, WCAG contrast checker and more. Free, browser-based color tools — no signup needed.',
        'app_name': 'WooaColor – Free Online Color Tools',
        'faq': [
            ('What color tools are available on WooaColor?',
             'WooaColor provides HEX/RGB/HSL conversion, image color picker, gradient generator, palette generator, WCAG contrast checker, color mixer, CSS box/text-shadow generators, opacity converter, and more — all free.'),
            ('Are files or color data sent to a server?',
             'No. All processing happens locally in your browser. Nothing is sent to any server.'),
            ('Do I need to sign up to use WooaColor?',
             'No. All tools are completely free and require no signup or login.'),
        ],
        'h1': 'All Your Color Work — Free, in One Place',
        'tool_desc': 'Color picker, palette, gradient, conversion and more — 100% free. No signup required. All processing happens in your browser.',
        'breadcrumb': 'Home',
        'cross_banner_text': None,
        'cross_banner_link_text': None,
        'cross_banner_href': None,
    },
    'color-converter.html': {
        'title': 'HEX RGB HSL Color Converter Free Online | WooaColor',
        'desc':  'Convert HEX, RGB, and HSL color codes instantly. Real-time conversion with one-click CSS code copy. Free online color converter for designers and developers.',
        'kw':    'HEX RGB HSL converter, color code converter, HEX to RGB, RGB to HSL, CSS color codes, online color converter free, WooaColor',
        'og_title': 'HEX RGB HSL Color Converter Free Online | WooaColor',
        'og_desc':  'Convert between HEX, RGB, and HSL color codes instantly. Real-time conversion. Free online tool.',
        'app_name': 'HEX RGB HSL Color Converter',
        'faq': [
            ('What are HEX, RGB, and HSL?',
             'They are different formats for expressing colors. HEX is the most common web format using hexadecimal notation. RGB specifies red, green, and blue channel values. HSL represents hue, saturation, and lightness.'),
            ('Is conversion done in real time?',
             'Yes. As soon as you type a value in any format, the other formats are updated instantly.'),
            ('Can I copy the converted code directly for CSS?',
             'Yes. Each color format has a copy button so you can paste the code directly into your CSS.'),
        ],
        'h1': 'HEX RGB HSL Color Converter',
        'tool_desc': 'Enter any color code in HEX, RGB, or HSL format and instantly see the equivalent in all other formats. Click to copy for CSS.',
        'breadcrumb': 'HEX ↔ RGB ↔ HSL',
        'cross_banner_text': 'Need to generate a full color palette from this color?',
        'cross_banner_link_text': '🎨 Palette Generator →',
        'cross_banner_href': 'palette-generator.html',
    },
    'color-picker.html': {
        'title': 'Image Color Picker Free Online – Pixel Color Extractor | WooaColor',
        'desc':  'Upload an image and click any pixel to extract its color. Get HEX and RGB codes instantly. Free online image color picker for designers and brand color extraction.',
        'kw':    'image color picker, pixel color extractor, HEX from image, color picker online, pick color from image, brand color, photo color code, WooaColor',
        'og_title': 'Image Color Picker Free Online – Extract Pixel Colors | WooaColor',
        'og_desc':  'Upload an image and click any pixel to get its HEX and RGB color code. Free online color picker.',
        'app_name': 'Image Color Picker',
        'faq': [
            ('How do I extract a color from an image?',
             'Upload an image, then click any pixel on the canvas. The HEX and RGB color codes for that pixel are displayed instantly.'),
            ('What image formats are supported?',
             'JPG, PNG, WebP, and GIF images are all supported.'),
            ('Is my image uploaded to a server?',
             'No. All processing happens locally in your browser using the Canvas API. Your image is never sent anywhere.'),
        ],
        'h1': 'Image Color Picker – Extract Pixel Colors',
        'tool_desc': 'Upload an image and click any pixel to instantly get its HEX and RGB color code. Great for picking brand colors from photos.',
        'breadcrumb': 'Color Picker',
        'cross_banner_text': 'Want to extract the dominant color palette from your image?',
        'cross_banner_link_text': '🖼️ Image Palette Extractor →',
        'cross_banner_href': 'image-palette.html',
    },
    'gradient-generator.html': {
        'title': 'CSS Gradient Generator Free Online – Linear & Radial | WooaColor',
        'desc':  'Generate CSS linear-gradient and radial-gradient code in real time. Add/remove color stops, choose direction, preview instantly. Free online CSS gradient generator.',
        'kw':    'CSS gradient generator, linear-gradient, radial-gradient, CSS background gradient, gradient code, color gradient online free, WooaColor',
        'og_title': 'CSS Gradient Generator Free Online | WooaColor',
        'og_desc':  'Generate CSS linear and radial gradient code in real time. Preview and copy with one click. Free online tool.',
        'app_name': 'CSS Gradient Generator',
        'faq': [
            ('What types of gradients can I create?',
             'You can create CSS linear-gradient (directional) and radial-gradient (radial) styles with any number of color stops.'),
            ('Can I add multiple color stops?',
             'Yes. You can add, remove, and reorder color stops freely to create complex multi-color gradients.'),
            ('How do I use the generated CSS code?',
             'Click the copy button next to the generated CSS code and paste it directly into your stylesheet.'),
        ],
        'h1': 'CSS Gradient Generator – Free Online',
        'tool_desc': 'Create beautiful CSS linear or radial gradients. Add color stops, adjust direction, and copy the generated code straight into your CSS.',
        'breadcrumb': 'Gradient Generator',
        'cross_banner_text': 'Looking for ready-made gradient presets?',
        'cross_banner_link_text': '🌅 Gradient Gallery →',
        'cross_banner_href': 'gradient-gallery.html',
    },
    'palette-generator.html': {
        'title': 'Color Palette Generator Free Online – Complementary, Analogous, Triadic | WooaColor',
        'desc':  'Generate complementary, analogous, triadic, split-complementary, and monochromatic color palettes automatically from any base color. Copy HEX codes. Free online palette generator.',
        'kw':    'color palette generator, complementary colors, analogous colors, triadic palette, color scheme, palette from color, free palette generator, WooaColor',
        'og_title': 'Color Palette Generator Free Online | WooaColor',
        'og_desc':  'Generate complementary, analogous, triadic, and monochromatic palettes from any color. Copy HEX codes. Free online tool.',
        'app_name': 'Color Palette Generator',
        'faq': [
            ('What palette types can I generate?',
             'Complementary, analogous, triadic, split-complementary, and monochromatic palettes are all supported.'),
            ('Can I copy the generated color codes?',
             'Yes. Click any color swatch to copy its HEX code to the clipboard.'),
            ('Is this tool free?',
             'Yes. The color palette generator is completely free with no signup required.'),
        ],
        'h1': 'Color Palette Generator – Free Online',
        'tool_desc': 'Enter a base color and instantly generate complementary, analogous, triadic, and more palette types. Click any swatch to copy its HEX code.',
        'breadcrumb': 'Palette Generator',
        'cross_banner_text': 'Want to check accessibility contrast for your palette?',
        'cross_banner_link_text': '👁️ Palette Contrast Checker →',
        'cross_banner_href': 'palette-contrast.html',
    },
    'contrast-checker.html': {
        'title': 'WCAG Color Contrast Checker Free Online – AA & AAA | WooaColor',
        'desc':  'Check foreground and background color contrast ratio against WCAG accessibility standards. Instant AA/AAA pass/fail results. Free online color contrast checker.',
        'kw':    'WCAG contrast checker, color contrast ratio, accessibility contrast, AA standard, AAA standard, web accessibility, contrast ratio online free, WooaColor',
        'og_title': 'WCAG Color Contrast Checker Free Online | WooaColor',
        'og_desc':  'Check color contrast ratio against WCAG AA/AAA accessibility standards. Instant pass/fail results. Free online tool.',
        'app_name': 'WCAG Color Contrast Checker',
        'faq': [
            ('What is WCAG color contrast?',
             'WCAG (Web Content Accessibility Guidelines) defines minimum contrast ratios between text and background colors to ensure readability for all users, including those with visual impairments.'),
            ('What are AA and AAA standards?',
             'WCAG AA requires a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text. AAA requires 7:1 for normal text and 4.5:1 for large text.'),
            ('How do I use the contrast checker?',
             'Enter the foreground (text) and background colors in HEX format, and the tool instantly shows the contrast ratio and whether it passes AA or AAA standards.'),
        ],
        'h1': 'WCAG Color Contrast Checker – Free Online',
        'tool_desc': 'Enter text and background colors to check their WCAG contrast ratio. Instantly see if your color combination passes AA or AAA accessibility standards.',
        'breadcrumb': 'Contrast Checker',
        'cross_banner_text': 'Need to check contrast across your entire palette?',
        'cross_banner_link_text': '🔲 Palette Contrast Matrix →',
        'cross_banner_href': 'palette-contrast.html',
    },
    'color-mixer.html': {
        'title': 'Color Mixer Free Online – Blend Two Colors by Ratio | WooaColor',
        'desc':  'Blend two colors in any ratio and see the resulting mixed color. Copy HEX/RGB code instantly. Adjust the mix slider for real-time preview. Free online color mixer.',
        'kw':    'color mixer, color blending, blend two colors, color ratio mix, HEX color blend, RGB color mix, online color mixer free, WooaColor',
        'og_title': 'Color Mixer Free Online – Blend Colors by Ratio | WooaColor',
        'og_desc':  'Mix two colors by ratio and get the blended HEX/RGB result instantly. Free online color mixing tool.',
        'app_name': 'Color Mixer',
        'faq': [
            ('How does the color mixer work?',
             'Select two colors and adjust the ratio slider. The tool calculates the blended RGB values in real time and shows the resulting color with its HEX and RGB codes.'),
            ('Can I copy the mixed color code?',
             'Yes. Click the copy button to copy the blended color\'s HEX or RGB code to the clipboard.'),
            ('Is this tool free?',
             'Yes. The color mixer is completely free with no signup required.'),
        ],
        'h1': 'Color Mixer – Blend Two Colors Free Online',
        'tool_desc': 'Pick two colors and drag the ratio slider to blend them. The resulting mixed color is shown with its HEX and RGB codes for immediate use.',
        'breadcrumb': 'Color Mixer',
        'cross_banner_text': 'Want to explore color harmonies from a base color?',
        'cross_banner_link_text': '🎨 Color Harmony Generator →',
        'cross_banner_href': 'color-harmony.html',
    },
    'box-shadow.html': {
        'title': 'CSS Box Shadow Generator Free Online – box-shadow Code | WooaColor',
        'desc':  'Generate CSS box-shadow code instantly with sliders. Set H-offset, V-offset, blur, spread, color, and inset. Real-time preview and one-click copy. Free online box shadow generator.',
        'kw':    'CSS box shadow generator, box-shadow code, CSS shadow, inset shadow, box shadow online free, CSS effect generator, WooaColor',
        'og_title': 'CSS Box Shadow Generator Free Online | WooaColor',
        'og_desc':  'Generate CSS box-shadow code with sliders. Live preview and one-click copy. Free online tool.',
        'app_name': 'CSS Box Shadow Generator',
        'faq': [
            ('What box-shadow properties can I control?',
             'You can adjust horizontal offset, vertical offset, blur radius, spread radius, shadow color, opacity, and toggle inset mode.'),
            ('Can I add multiple shadows?',
             'Yes. You can stack multiple shadow layers to create complex effects.'),
            ('How do I copy the generated code?',
             'Click the copy button next to the CSS output to copy the box-shadow code directly to your clipboard.'),
        ],
        'h1': 'CSS Box Shadow Generator – Free Online',
        'tool_desc': 'Use the sliders to configure your CSS box-shadow. See a live preview and copy the generated code to paste directly into your stylesheet.',
        'breadcrumb': 'Box Shadow Generator',
        'cross_banner_text': 'Need a CSS text shadow for typography?',
        'cross_banner_link_text': '🔤 Text Shadow Generator →',
        'cross_banner_href': 'text-shadow.html',
    },
    'text-shadow.html': {
        'title': 'CSS Text Shadow Generator Free Online – text-shadow Code | WooaColor',
        'desc':  'Generate CSS text-shadow code instantly with sliders. Set H-offset, V-offset, blur, color, and sample text. Real-time preview and one-click copy. Free online text shadow generator.',
        'kw':    'CSS text shadow generator, text-shadow code, CSS typography effect, text shadow online free, CSS text effect, WooaColor',
        'og_title': 'CSS Text Shadow Generator Free Online | WooaColor',
        'og_desc':  'Generate CSS text-shadow code with sliders. Live preview and one-click copy. Free online tool.',
        'app_name': 'CSS Text Shadow Generator',
        'faq': [
            ('What text-shadow properties can I control?',
             'You can adjust horizontal offset, vertical offset, blur radius, and shadow color with live preview on sample text.'),
            ('Can I preview the shadow on custom text?',
             'Yes. Type any text in the sample field to preview how the shadow looks on your own content.'),
            ('How do I copy the generated code?',
             'Click the copy button next to the CSS output to copy the text-shadow code directly to your clipboard.'),
        ],
        'h1': 'CSS Text Shadow Generator – Free Online',
        'tool_desc': 'Adjust sliders to configure your CSS text-shadow. Live preview on sample text, then copy the generated code straight to your stylesheet.',
        'breadcrumb': 'Text Shadow Generator',
        'cross_banner_text': 'Need a CSS box shadow for elements?',
        'cross_banner_link_text': '🟦 Box Shadow Generator →',
        'cross_banner_href': 'box-shadow.html',
    },
    'opacity-converter.html': {
        'title': 'Opacity Converter Free Online – HEX to RGBA & 8-digit HEX | WooaColor',
        'desc':  'Add opacity to a HEX color and get rgba(), 8-digit HEX (#RRGGBBAA), and hsla() codes instantly. Checkerboard preview included. Free online opacity/alpha converter.',
        'kw':    'opacity converter, rgba converter, 8-digit HEX, RRGGBBAA, alpha channel, CSS transparency, HEX to rgba, hsla converter, color opacity online free, WooaColor',
        'og_title': 'Opacity Converter Free Online – HEX to RGBA & 8-Digit HEX | WooaColor',
        'og_desc':  'Add opacity to a HEX color to get rgba / 8-digit HEX / hsla codes instantly. Free online converter.',
        'app_name': 'Opacity Converter',
        'faq': [
            ('What output formats does this converter provide?',
             'It generates rgba(), 8-digit HEX (#RRGGBBAA), and hsla() codes from any HEX color with adjustable opacity.'),
            ('What is an 8-digit HEX color?',
             'An 8-digit HEX color (e.g. #FF5733CC) appends an alpha channel byte to the standard 6-digit HEX, defining both color and opacity in one value.'),
            ('Can I preview the transparent color?',
             'Yes. A checkerboard background is shown behind the color preview to help you visualize transparency.'),
        ],
        'h1': 'Opacity Converter – HEX to RGBA Free Online',
        'tool_desc': 'Enter a HEX color and set the opacity level. Instantly get the equivalent rgba(), 8-digit HEX, and hsla() codes with a transparency preview.',
        'breadcrumb': 'Opacity Converter',
        'cross_banner_text': 'Need to generate CSS variables for your color system?',
        'cross_banner_link_text': '📦 CSS Variables Generator →',
        'cross_banner_href': 'css-variables.html',
    },
    'image-palette.html': {
        'title': 'Image Palette Extractor Free Online – Extract Colors from Photo | WooaColor',
        'desc':  'Upload an image to automatically extract its dominant colors. Copy HEX and RGB codes. Free online image color palette extractor for brand colors, design work, and more.',
        'kw':    'image palette extractor, extract colors from image, photo color palette, dominant colors, brand color extractor, color palette from photo, image color analysis, WooaColor',
        'og_title': 'Image Palette Extractor Free Online | WooaColor',
        'og_desc':  'Upload an image to automatically extract dominant colors. Copy HEX and RGB codes. Free online tool.',
        'app_name': 'Image Palette Extractor',
        'faq': [
            ('How does the palette extraction work?',
             'The tool uses color quantization to analyze your image and identify the most prominent colors, returning them as a palette with HEX and RGB codes.'),
            ('How many colors are extracted?',
             'Up to 10 dominant colors are extracted from the uploaded image.'),
            ('Is my image uploaded to a server?',
             'No. All processing happens locally in your browser. Your image is never sent to any server.'),
        ],
        'h1': 'Image Palette Extractor – Free Online',
        'tool_desc': 'Upload any image to automatically extract its dominant color palette. Copy HEX or RGB codes for each color. Everything runs in your browser.',
        'breadcrumb': 'Image Palette',
        'cross_banner_text': 'Want to pick exact colors pixel by pixel from an image?',
        'cross_banner_link_text': '🖼️ Image Color Picker →',
        'cross_banner_href': 'color-picker.html',
    },
    'gradient-gallery.html': {
        'title': 'CSS Gradient Gallery – 50+ Trendy Gradient Code Presets Free | WooaColor',
        'desc':  'Browse 50+ trendy CSS gradient presets. Click to copy CSS code. Categories include nature, pastel, vivid, dark, business, and trending gradients. Free online CSS gradient gallery.',
        'kw':    'CSS gradient gallery, gradient presets, CSS gradient code, background gradient, pastel gradient, dark gradient, trendy gradient, gradient collection free, WooaColor',
        'og_title': 'CSS Gradient Gallery – 50+ Trendy Presets Free | WooaColor',
        'og_desc':  '50+ trendy CSS gradient presets. Click any gradient to copy its CSS code. Free online gallery.',
        'app_name': 'CSS Gradient Gallery',
        'faq': [
            ('How many gradient presets are available?',
             'The gallery includes 50+ carefully curated CSS gradient presets across multiple categories.'),
            ('How do I use a gradient from the gallery?',
             'Click any gradient card to copy its CSS code. Paste it directly into your stylesheet as a background property.'),
            ('Can I create a custom gradient?',
             'Yes. Use the Gradient Generator tool to create a fully custom gradient with your own colors and direction.'),
        ],
        'h1': 'CSS Gradient Gallery – 50+ Trendy Presets',
        'tool_desc': 'Browse curated CSS gradient presets by category: nature, pastel, vivid, dark, business, and more. Click any gradient to copy its CSS code instantly.',
        'breadcrumb': 'Gradient Gallery',
        'cross_banner_text': 'Want to create a fully custom gradient?',
        'cross_banner_link_text': '🌈 Gradient Generator →',
        'cross_banner_href': 'gradient-generator.html',
    },
    'tints-shades.html': {
        'title': 'Tints and Shades Generator Free Online – 10-Step Color Scale | WooaColor',
        'desc':  'Enter any color and generate 10 tints (lighter) and 10 shades (darker) automatically. Copy as Tailwind-style CSS variables. Free online tints and shades generator.',
        'kw':    'tints shades generator, color tints, color shades, Tailwind colors, CSS variables, color scale, color steps, design system colors, WooaColor',
        'og_title': 'Tints and Shades Generator Free Online | WooaColor',
        'og_desc':  'Generate 10 tints and 10 shades from any color. Copy as Tailwind-style CSS variables. Free online tool.',
        'app_name': 'Tints & Shades Generator',
        'faq': [
            ('What are tints and shades?',
             'Tints are lighter variations of a color (mixed with white) and shades are darker variations (mixed with black). They are essential for building consistent color scales in design systems.'),
            ('Can I copy the generated colors as CSS variables?',
             'Yes. The tool generates Tailwind-compatible CSS custom property declarations that you can copy and paste directly into your project.'),
            ('How many steps are generated?',
             '10 tint steps and 10 shade steps are generated for each color, giving you a full 20-step scale.'),
        ],
        'h1': 'Tints & Shades Generator – Free Online',
        'tool_desc': 'Enter a base color to generate a 10-step tint scale (lighter) and 10-step shade scale (darker). Copy as Tailwind-style CSS variables for your design system.',
        'breadcrumb': 'Tints & Shades',
        'cross_banner_text': 'Need to generate CSS variables for your full palette?',
        'cross_banner_link_text': '📦 CSS Variables Generator →',
        'cross_banner_href': 'css-variables.html',
    },
    'color-name.html': {
        'title': 'Color Name Finder Free Online – HEX & RGB to Color Name | WooaColor',
        'desc':  'Enter a HEX or RGB color code to find the closest color name in English and Korean. Shows 5 similar colors too. Free online color name lookup tool.',
        'kw':    'color name finder, HEX color name, RGB color name, color name lookup, CSS color names, closest color name, color identifier, WooaColor',
        'og_title': 'Color Name Finder Free Online – HEX & RGB to Color Name | WooaColor',
        'og_desc':  'Enter HEX or RGB to find the closest color name (English & Korean) with 5 similar colors. Free online tool.',
        'app_name': 'Color Name Finder',
        'faq': [
            ('How does the color name finder work?',
             'Enter a HEX or RGB value and the tool searches a database of named colors to find the closest match using color distance calculations.'),
            ('What color name databases are included?',
             'The tool includes standard CSS named colors and an extended list of common English and Korean color names.'),
            ('Are similar colors also shown?',
             'Yes. In addition to the closest match, 5 similar named colors are displayed so you can explore nearby options.'),
        ],
        'h1': 'Color Name Finder – Free Online',
        'tool_desc': 'Enter a HEX or RGB color code to find the closest color name in English and Korean. Similar colors are also shown for reference.',
        'breadcrumb': 'Color Name',
        'cross_banner_text': 'Want to convert between HEX, RGB, and HSL?',
        'cross_banner_link_text': '🔄 Color Converter →',
        'cross_banner_href': 'color-converter.html',
    },
    'css-variables.html': {
        'title': 'CSS Variables Generator Free Online – Custom Properties & SCSS | WooaColor',
        'desc':  'Enter a color palette and auto-generate CSS Custom Properties, SCSS variables, Tailwind config, and JS token code. Free online CSS variables generator for design systems.',
        'kw':    'CSS variables generator, CSS custom properties, SCSS variables, Tailwind config, design system tokens, color tokens, CSS code generator, WooaColor',
        'og_title': 'CSS Variables Generator Free Online | WooaColor',
        'og_desc':  'Generate CSS Custom Properties, SCSS variables, Tailwind config, and JS tokens from a color palette. Free online tool.',
        'app_name': 'CSS Variables Generator',
        'faq': [
            ('What output formats does this tool support?',
             'The tool generates CSS Custom Properties (:root variables), SCSS variables, Tailwind CSS config, and JavaScript token objects from your color palette.'),
            ('How do I add colors to the palette?',
             'Enter color names and HEX values, then click Generate to produce all output formats at once.'),
            ('Can I copy the generated code?',
             'Yes. Each output section has a copy button so you can paste directly into your project files.'),
        ],
        'h1': 'CSS Variables Generator – Free Online',
        'tool_desc': 'Build a color palette and generate CSS Custom Properties, SCSS variables, Tailwind config, and JS token code automatically. Perfect for design systems.',
        'breadcrumb': 'CSS Variables',
        'cross_banner_text': 'Need a tint and shade scale for each color?',
        'cross_banner_link_text': '🎚️ Tints & Shades Generator →',
        'cross_banner_href': 'tints-shades.html',
    },
    'color-converter-full.html': {
        'title': 'Color Converter HEX RGB HSL CMYK HSV Free Online | WooaColor',
        'desc':  'Convert between HEX, RGB, HSL, CMYK, and HSV color formats in real time. Supports print CMYK values too. Free online full color converter for web and print.',
        'kw':    'CMYK converter, HEX RGB HSL converter, HSV converter, color format converter, print color, CMYK color, full color converter online free, WooaColor',
        'og_title': 'Color Converter HEX RGB HSL CMYK HSV Free Online | WooaColor',
        'og_desc':  'Convert between HEX, RGB, HSL, CMYK, and HSV color formats instantly. Supports print-ready CMYK. Free online tool.',
        'app_name': 'Full Color Converter (HEX RGB HSL CMYK HSV)',
        'faq': [
            ('What color formats are supported?',
             'HEX, RGB, HSL, CMYK, and HSV are all supported. Enter a value in any format and the rest update instantly.'),
            ('Why would I need CMYK conversion?',
             'CMYK is used in print design. Converting your web colors (HEX/RGB) to CMYK ensures accurate color reproduction when printing.'),
            ('Is conversion done in real time?',
             'Yes. As soon as you enter a value in any format field, all other formats are recalculated and displayed instantly.'),
        ],
        'h1': 'Full Color Converter – HEX RGB HSL CMYK HSV',
        'tool_desc': 'Convert any color between HEX, RGB, HSL, CMYK, and HSV formats in real time. Supports print-ready CMYK values for both web and print workflows.',
        'breadcrumb': 'Full Color Converter',
        'cross_banner_text': 'Want to find the name of your color?',
        'cross_banner_link_text': '🏷️ Color Name Finder →',
        'cross_banner_href': 'color-name.html',
    },
    'palette-contrast.html': {
        'title': 'Palette Contrast Checker Free Online – WCAG Accessibility Matrix | WooaColor',
        'desc':  'Check WCAG contrast ratios across all color combinations in your palette with an N×N matrix. Instant AA/AAA pass/fail. Free online palette contrast checker for design systems.',
        'kw':    'palette contrast checker, WCAG contrast matrix, accessibility palette, color contrast matrix, design system accessibility, AA AAA contrast, WooaColor',
        'og_title': 'Palette Contrast Checker Free Online – WCAG Matrix | WooaColor',
        'og_desc':  'Check WCAG contrast ratios across all palette color combinations in an N×N matrix. Instant AA/AAA results. Free online tool.',
        'app_name': 'Palette Contrast Checker',
        'faq': [
            ('What is a palette contrast matrix?',
             'It displays the WCAG contrast ratio for every combination of colors in your palette in an N×N grid, making it easy to spot accessible and inaccessible pairings at a glance.'),
            ('How many colors can I add to the palette?',
             'You can add multiple colors to the palette. The matrix scales automatically to show all pairwise combinations.'),
            ('What do the AA/AAA labels mean?',
             'AA means the pair meets the WCAG 2.1 minimum contrast standard (4.5:1 for normal text). AAA means it meets the enhanced standard (7:1).'),
        ],
        'h1': 'Palette Contrast Checker – WCAG Matrix',
        'tool_desc': 'Add your palette colors and see a full N×N contrast matrix showing WCAG pass/fail for every color pair. Essential for accessible design system validation.',
        'breadcrumb': 'Palette Contrast',
        'cross_banner_text': 'Want to check contrast between two specific colors?',
        'cross_banner_link_text': '👁️ Contrast Checker →',
        'cross_banner_href': 'contrast-checker.html',
    },
    'random-color.html': {
        'title': 'Random Color Generator Free Online – HEX RGB HSL | WooaColor',
        'desc':  'Generate a random color with one click and get its HEX, RGB, and HSL codes instantly. Includes a 10-color history. Free online random color generator for design inspiration.',
        'kw':    'random color generator, random HEX color, random color code, color inspiration, random RGB, random HSL, color generator online free, WooaColor',
        'og_title': 'Random Color Generator Free Online – HEX RGB HSL | WooaColor',
        'og_desc':  'Generate a random color and get HEX, RGB, and HSL codes instantly. Includes color history. Free online tool.',
        'app_name': 'Random Color Generator',
        'faq': [
            ('How do I generate a random color?',
             'Click the Generate button and a new random color is created instantly with its HEX, RGB, and HSL codes displayed.'),
            ('How many colors are kept in history?',
             'The last 10 generated colors are shown in the history panel so you can revisit and copy any previous color.'),
            ('Can I copy the generated color codes?',
             'Yes. Each code format (HEX, RGB, HSL) has a copy button for immediate use.'),
        ],
        'h1': 'Random Color Generator – Free Online',
        'tool_desc': 'Click to generate a random color and instantly get its HEX, RGB, and HSL codes. Your last 10 generated colors are saved in history for quick reference.',
        'breadcrumb': 'Random Color',
        'cross_banner_text': 'Want to explore color palettes based on a specific color?',
        'cross_banner_link_text': '🎨 Palette Generator →',
        'cross_banner_href': 'palette-generator.html',
    },
    'color-harmony.html': {
        'title': 'Color Harmony Generator Free Online – Complementary, Analogous, Triadic | WooaColor',
        'desc':  'Enter a base color to automatically generate complementary, analogous, triadic, split-complementary, and square color harmony palettes. Copy HEX codes. Free online color harmony tool.',
        'kw':    'color harmony generator, complementary colors, analogous colors, triadic colors, split complementary, square color harmony, color palette online free, WooaColor',
        'og_title': 'Color Harmony Generator Free Online | WooaColor',
        'og_desc':  'Generate complementary, analogous, triadic, and more harmony palettes from any color. Copy HEX codes. Free online tool.',
        'app_name': 'Color Harmony Generator',
        'faq': [
            ('What color harmony types are supported?',
             'Complementary, analogous, triadic, split-complementary, and square (tetradic) harmonies are all supported.'),
            ('What is the difference between a harmony generator and a palette generator?',
             'The harmony generator focuses on color theory relationships (e.g. angles on the color wheel), while the palette generator produces multi-swatch palettes. Both are complementary tools.'),
            ('Can I copy the generated colors?',
             'Yes. Click any color swatch to copy its HEX code to the clipboard.'),
        ],
        'h1': 'Color Harmony Generator – Free Online',
        'tool_desc': 'Enter a base color and generate 5 types of color harmony palettes: complementary, analogous, triadic, split-complementary, and square. Click any swatch to copy HEX.',
        'breadcrumb': 'Color Harmony',
        'cross_banner_text': 'Want to generate a full multi-step color palette?',
        'cross_banner_link_text': '🎨 Palette Generator →',
        'cross_banner_href': 'palette-generator.html',
    },
    'color-blindness.html': {
        'title': 'Color Blindness Simulator Free Online – Preview Image for All Color Vision Types | WooaColor',
        'desc':  'Upload an image to preview how it appears with Protanopia, Deuteranopia, Tritanopia, and Achromatopsia color blindness. Free online color blindness simulator.',
        'kw':    'color blindness simulator, Protanopia, Deuteranopia, Tritanopia, Achromatopsia, color vision deficiency, accessibility design, color blind test online free, WooaColor',
        'og_title': 'Color Blindness Simulator Free Online | WooaColor',
        'og_desc':  'Upload an image to preview how it looks for different types of color blindness. Free online accessibility design tool.',
        'app_name': 'Color Blindness Simulator',
        'faq': [
            ('What types of color blindness are simulated?',
             'Protanopia (red-blind), Deuteranopia (green-blind), Tritanopia (blue-yellow blind), and Achromatopsia (full color blindness / grayscale) are all simulated.'),
            ('Why is this tool useful for designers?',
             'It helps designers verify that their images, illustrations, and interfaces are accessible to users with color vision deficiencies, ensuring no critical information is conveyed by color alone.'),
            ('Is my image uploaded to a server?',
             'No. All simulation processing happens locally in your browser using Canvas filters. Your image is never sent anywhere.'),
        ],
        'h1': 'Color Blindness Simulator – Free Online',
        'tool_desc': 'Upload an image to preview how it appears to users with Protanopia, Deuteranopia, Tritanopia, or Achromatopsia. A must-have tool for accessible design.',
        'breadcrumb': 'Color Blindness Simulator',
        'cross_banner_text': 'Want to check color contrast for accessibility compliance?',
        'cross_banner_link_text': '👁️ WCAG Contrast Checker →',
        'cross_banner_href': 'contrast-checker.html',
    },
}

# ── 2. 공통 문자열 치환 ──────────────────────────────────────────────────────
COMMON = [
    # lang
    ('<html lang="ko">', '<html lang="en">'),
    # locale
    ('ko_KR', 'en_US'),
    # inLanguage
    ('"inLanguage": "ko"', '"inLanguage": "en"'),
    # priceCurrency
    ('"priceCurrency": "KRW"', '"priceCurrency": "USD"'),
    # paths: CSS, JS, manifest
    ('href="css/style.css"', 'href="../css/style.css"'),
    ('href="/manifest.json"', 'href="../manifest.json"'),
    ('src="js/', 'src="../js/'),
    ('href="js/', 'href="../js/'),

    # ── header nav ──
    ('>변환<', '>Convert<'),
    ('>생성<', '>Generate<'),
    ('>분석<', '>Analyze<'),
    ('>CSS 도구<', '>CSS Tools<'),
    ('>색상 추출<', '>Color Picker<'),
    ('>소개<', '>About<'),
    ('>전체 도구 ›<', '>All Tools ›<'),

    # ── breadcrumb home ──
    ('>🏠 홈<', '>🏠 Home<'),

    # ── our-sites-bar WooaColor active → en/ ──
    ('href="https://colorkit.wooahouse.com/" target="_blank" rel="noopener" class="active"',
     'href="https://colorkit.wooahouse.com/en/" target="_blank" rel="noopener" class="active"'),

    # ── pwa install button ──
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),

    # ── hero section ──
    ('모든 색상 작업 무료로, 한 곳에서',
     'All Your Color Work — Free, in One Place'),
    ('컬러 피커·팔레트·그라디언트·변환까지 <strong style="color:#FFD700;">100% 무료</strong><br>회원가입 없이, 모든 처리가 브라우저에서 완결됩니다',
     'Color picker, palette, gradient, conversion and more — <strong style="color:#FFD700;">100% free</strong><br>No signup. All processing happens in your browser.'),
    ('디자인에 어울리는 폰트도 찾아보세요',
     'Find the perfect font for your design'),
    ('WooaFont에서 무료 폰트 보기 →', 'Browse free fonts at WooaFont →'),

    # ── index category titles ──
    ('>변환<', '>Conversion<'),
    ('색상 코드를 다양한 형식으로 변환하는 도구', 'Tools to convert color codes between formats'),
    ('>생성<', '>Generation<'),
    ('그라디언트, 팔레트, 랜덤 색상 생성 도구', 'Tools for generating gradients, palettes, and random colors'),
    ('>분석<', '>Analysis<'),
    ('색상 대비·접근성·혼합 분석 도구', 'Tools for color contrast, accessibility, and blending'),
    ('>CSS 도구<', '>CSS Tools<'),
    ('CSS 색상 관련 코드 생성 도구', 'Tools for generating CSS color-related code'),

    # ── tool card names & descriptions ──
    ('세 가지 색상 코드 상호 변환', 'Convert between three color code formats'),
    ('이미지에서 색상 추출 (캔버스 픽셀 샘플링)', 'Extract colors from images (canvas pixel sampling)'),
    ('HEX·RGB·HSL·HSV·CMYK 5가지 형식 상호 변환', 'Convert between HEX, RGB, HSL, HSV, and CMYK'),
    ('HEX 입력 → 가장 가까운 색상 이름(한/영) 반환', 'Enter HEX → find closest color name (EN/KO)'),
    ('CSS 그라디언트 코드 생성 및 미리보기', 'Generate CSS gradient code with live preview'),
    ('보색, 유사색, 트라이어드 등 팔레트 생성', 'Generate complementary, analogous, triadic palettes'),
    ('랜덤 색상과 HEX/RGB/HSL 코드 생성', 'Generate random colors with HEX/RGB/HSL codes'),
    ('색상의 밝기 단계별 스케일 생성 및 CSS 변수 복사', 'Generate tint/shade scales and copy CSS variables'),
    ('보색·유사색·삼색 등 조화로운 색상 팔레트 자동 생성', 'Auto-generate complementary, analogous, triadic palettes'),
    ('WCAG 접근성 기준 대비율 검사', 'Check contrast ratio against WCAG standards'),
    ('두 색상을 비율로 혼합한 결과 색상', 'Blend two colors by ratio to see the result'),
    ('팔레트 색상 간 WCAG 대비율 N×N 매트릭스 분석', 'Analyze WCAG contrast in an N×N palette matrix'),
    ('적록색맹·청황색맹·전색맹 등 색맹 유형별 이미지 미리보기', 'Preview images for Protanopia, Tritanopia, Achromatopsia'),
    ('CSS box-shadow 코드 생성기', 'CSS box-shadow code generator'),
    ('CSS text-shadow 코드 생성기', 'CSS text-shadow code generator'),
    ('HEX 색상에 투명도 추가 → rgba 변환', 'Add opacity to HEX color → convert to rgba'),
    ('팔레트 → CSS / SCSS / Tailwind / JS 변수 코드 생성', 'Palette → CSS / SCSS / Tailwind / JS variable code'),
    ('이미지를 업로드하면 주요 색상을 자동으로 추출합니다. HEX, RGB 코드 복사 가능.', 'Upload an image to auto-extract dominant colors. Copy HEX/RGB codes.'),
    ('트렌디한 CSS 그라디언트 50가지 모음. 클릭 한 번으로 코드 복사.', '50+ trendy CSS gradient presets. Click to copy code.'),
    ('<div class="tool-name">HEX ↔ RGB ↔ HSL</div>', '<div class="tool-name">HEX ↔ RGB ↔ HSL</div>'),
    ('<div class="tool-name">색상 추출</div>', '<div class="tool-name">Color Picker</div>'),
    ('<div class="tool-name">전체 색상 변환기</div>', '<div class="tool-name">Full Color Converter</div>'),
    ('<div class="tool-name">색상 이름 찾기</div>', '<div class="tool-name">Color Name Finder</div>'),
    ('<div class="tool-name">그라디언트 생성기</div>', '<div class="tool-name">Gradient Generator</div>'),
    ('<div class="tool-name">팔레트 생성기</div>', '<div class="tool-name">Palette Generator</div>'),
    ('<div class="tool-name">랜덤 색상 생성기</div>', '<div class="tool-name">Random Color</div>'),
    ('<div class="tool-name">틴트·셰이드 생성기</div>', '<div class="tool-name">Tints & Shades</div>'),
    ('<div class="tool-name">색상 조화 생성기</div>', '<div class="tool-name">Color Harmony</div>'),
    ('<div class="tool-name">색상 대비 검사기</div>', '<div class="tool-name">Contrast Checker</div>'),
    ('<div class="tool-name">색상 혼합기</div>', '<div class="tool-name">Color Mixer</div>'),
    ('<div class="tool-name">팔레트 대비 검사기</div>', '<div class="tool-name">Palette Contrast</div>'),
    ('<div class="tool-name">색맹 시뮬레이터</div>', '<div class="tool-name">Color Blindness Sim</div>'),
    ('<div class="tool-name">박스 그림자 생성기</div>', '<div class="tool-name">Box Shadow</div>'),
    ('<div class="tool-name">텍스트 그림자 생성기</div>', '<div class="tool-name">Text Shadow</div>'),
    ('<div class="tool-name">불투명도 변환기</div>', '<div class="tool-name">Opacity Converter</div>'),
    ('<div class="tool-name">CSS 변수 생성기</div>', '<div class="tool-name">CSS Variables</div>'),
    ('<div class="tool-name">이미지 팔레트 추출</div>', '<div class="tool-name">Image Palette</div>'),
    ('<div class="tool-name">CSS 그라디언트 갤러리</div>', '<div class="tool-name">Gradient Gallery</div>'),

    # ── free/new badges ──
    ('<span class="free-badge">무료</span>', '<span class="free-badge">FREE</span>'),

    # ── buttons common ──
    ('>복사<', '>Copy<'),
    ('>코드 복사<', '>Copy Code<'),
    ('>복사됨!<', '>Copied!<'),
    ('>초기화<', '>Reset<'),
    ('>색상 생성<', '>Generate<'),
    ('>생성<', '>Generate<'),
    ('>추가<', '>Add<'),
    ('>삭제<', '>Delete<'),
    ('>다운로드<', '>Download<'),
    ('>파일 선택<', '>Select File<'),
    ('>이미지 선택<', '>Select Image<'),
    ('>⬇️ 다운로드<', '>⬇️ Download<'),
    ('>적용<', '>Apply<'),
    ('>검사<', '>Check<'),
    ('>전체 복사<', '>Copy All<'),

    # ── button text states ──
    ("btn.textContent = '복사됨!';", "btn.textContent = 'Copied!';"),
    ("btn.textContent = '복사';", "btn.textContent = 'Copy';"),
    ("btn.textContent = '코드 복사';", "btn.textContent = 'Copy Code';"),

    # ── color-converter UI ──
    ('HEX 입력', 'Enter HEX'),
    ('RGB 입력', 'Enter RGB'),
    ('HSL 입력', 'Enter HSL'),
    ('CMYK 입력', 'Enter CMYK'),
    ('HSV 입력', 'Enter HSV'),

    # ── contrast checker UI ──
    ('전경색 (텍스트)', 'Foreground (Text)'),
    ('배경색', 'Background'),
    ('대비율', 'Contrast Ratio'),
    ('일반 텍스트 AA', 'Normal Text AA'),
    ('일반 텍스트 AAA', 'Normal Text AAA'),
    ('큰 텍스트 AA', 'Large Text AA'),
    ('큰 텍스트 AAA', 'Large Text AAA'),
    ('>합격<', '>Pass<'),
    ('>불합격<', '>Fail<'),

    # ── palette generator UI ──
    ('기준 색상', 'Base Color'),
    ('보색', 'Complementary'),
    ('유사색', 'Analogous'),
    ('트라이어드', 'Triadic'),
    ('분할보색', 'Split-Complementary'),
    ('단색', 'Monochromatic'),
    ('정사각형', 'Square'),

    # ── gradient generator UI ──
    ('방향', 'Direction'),
    ('색상 정지점', 'Color Stops'),
    ('정지점 추가', 'Add Stop'),
    ('미리보기', 'Preview'),
    ('CSS 코드', 'CSS Code'),
    ('linear', 'linear'),
    ('radial', 'radial'),

    # ── box shadow / text shadow UI ──
    ('수평 오프셋', 'H-Offset'),
    ('수직 오프셋', 'V-Offset'),
    ('블러 반지름', 'Blur Radius'),
    ('확산 반지름', 'Spread Radius'),
    ('그림자 색상', 'Shadow Color'),
    ('inset (안쪽 그림자)', 'inset (inner shadow)'),
    ('샘플 텍스트', 'Sample Text'),
    ('텍스트 색상', 'Text Color'),

    # ── opacity converter UI ──
    ('불투명도', 'Opacity'),
    ('투명도', 'Transparency'),
    ('알파 채널', 'Alpha Channel'),
    ('8자리 HEX', '8-digit HEX'),

    # ── image palette UI ──
    ('이미지를 업로드하세요', 'Upload an image'),
    ('이미지 파일을 여기에 끌어다 놓으세요', 'Drop image files here'),
    ('주요 색상', 'Dominant Colors'),
    ('색상 추출 중...', 'Extracting colors...'),

    # ── random color UI ──
    ('색상 생성하기', 'Generate Color'),
    ('최근 색상', 'Recent Colors'),
    ('히스토리', 'History'),

    # ── tints-shades UI ──
    ('밝은 (Tints)', 'Tints (Lighter)'),
    ('어두운 (Shades)', 'Shades (Darker)'),
    ('CSS 변수로 복사', 'Copy as CSS Variables'),

    # ── color-name UI ──
    ('가장 가까운 색상 이름', 'Closest Color Name'),
    ('유사 색상', 'Similar Colors'),
    ('한국어', 'Korean'),
    ('영어', 'English'),

    # ── color blindness UI ──
    ('정상 시각', 'Normal Vision'),
    ('적록색맹 (Protanopia)', 'Protanopia (Red-Blind)'),
    ('녹색맹 (Deuteranopia)', 'Deuteranopia (Green-Blind)'),
    ('청황색맹 (Tritanopia)', 'Tritanopia (Blue-Yellow Blind)'),
    ('전색맹 (Achromatopsia)', 'Achromatopsia (Grayscale)'),

    # ── color harmony UI ──
    ('색상 조화 유형', 'Harmony Type'),
    ('색상 팔레트', 'Color Palette'),

    # ── css-variables UI ──
    ('색상 이름', 'Color Name'),
    ('색상 코드', 'Color Code'),
    ('색상 추가', 'Add Color'),
    ('CSS 변수', 'CSS Variables'),
    ('SCSS 변수', 'SCSS Variables'),
    ('Tailwind 설정', 'Tailwind Config'),
    ('JS 객체', 'JS Object'),

    # ── palette contrast UI ──
    ('색상 추가하기', 'Add Color'),
    ('대비율 매트릭스', 'Contrast Matrix'),

    # ── color mixer UI ──
    ('색상 1', 'Color 1'),
    ('색상 2', 'Color 2'),
    ('혼합 비율', 'Mix Ratio'),
    ('혼합 결과', 'Mixed Result'),

    # ── features section ──
    ('100% 안전', '100% Private'),
    ('모든 처리가 브라우저 안에서 이루어집니다. 서버로 데이터가 전송되지 않습니다.',
     'All processing happens in your browser. No data is ever sent to a server.'),
    ('즉시 반응', 'Instant Response'),
    ('입력과 동시에 실시간으로 결과를 확인할 수 있습니다.',
     'Results update in real time as you type or adjust settings.'),
    ('완전 무료', 'Completely Free'),
    ('회원가입 없이 모든 기능을 무제한 무료로 사용할 수 있습니다.',
     'All features are unlimited and free — no signup required.'),
    ('모든 기기 지원', 'All Devices'),
    ('PC, 태블릿, 스마트폰 어디서나 사용 가능한 반응형 디자인.',
     'Responsive design works on PC, tablet, and smartphone.'),

    # ── footer ──
    ('모든 권리 보유.', 'All rights reserved.'),
    ('href="privacy.html"', 'href="../privacy.html"'),
    ('href="about.html"', 'href="../about.html"'),
    ('>개인정보처리방침<', '>Privacy Policy<'),
    ('>서비스 소개<', '>About<'),
    ('무료 온라인 색상 도구 모음. 변환, 생성, 분석, CSS 코드까지 모든 색상 작업을 브라우저에서 처리하세요.',
     'Free online color tools. Convert, generate, analyze, and code — all in your browser.'),

    # footer-links headings
    ('<h4>변환</h4>', '<h4>Conversion</h4>'),
    ('<h4>생성</h4>', '<h4>Generation</h4>'),
    ('<h4>분석</h4>', '<h4>Analysis</h4>'),
    ('<h4>CSS 도구</h4>', '<h4>CSS Tools</h4>'),
    ('<h4>정보</h4>', '<h4>Info</h4>'),
    ('<h4>WooaHouse 서비스</h4>', '<h4>WooaHouse Services</h4>'),

    # footer tool links
    ('<a href="color-converter.html">HEX ↔ RGB ↔ HSL</a>', '<a href="../color-converter.html">HEX ↔ RGB ↔ HSL</a>'),
    ('<a href="color-converter-full.html">전체 색상 변환기</a>', '<a href="../color-converter-full.html">Full Color Converter</a>'),
    ('<a href="color-picker.html">색상 추출</a>', '<a href="../color-picker.html">Color Picker</a>'),
    ('<a href="color-name.html">색상 이름 찾기</a>', '<a href="../color-name.html">Color Name Finder</a>'),
    ('<a href="gradient-generator.html">그라디언트 생성기</a>', '<a href="../gradient-generator.html">Gradient Generator</a>'),
    ('<a href="palette-generator.html">팔레트 생성기</a>', '<a href="../palette-generator.html">Palette Generator</a>'),
    ('<a href="random-color.html">랜덤 색상 생성기</a>', '<a href="../random-color.html">Random Color</a>'),
    ('<a href="tints-shades.html">틴트·셰이드 생성기</a>', '<a href="../tints-shades.html">Tints & Shades</a>'),
    ('<a href="contrast-checker.html">색상 대비 검사기</a>', '<a href="../contrast-checker.html">Contrast Checker</a>'),
    ('<a href="color-mixer.html">색상 혼합기</a>', '<a href="../color-mixer.html">Color Mixer</a>'),
    ('<a href="palette-contrast.html">팔레트 대비 검사기</a>', '<a href="../palette-contrast.html">Palette Contrast</a>'),
    ('<a href="box-shadow.html">박스 그림자 생성기</a>', '<a href="../box-shadow.html">Box Shadow</a>'),
    ('<a href="text-shadow.html">텍스트 그림자 생성기</a>', '<a href="../text-shadow.html">Text Shadow</a>'),
    ('<a href="opacity-converter.html">불투명도 변환기</a>', '<a href="../opacity-converter.html">Opacity Converter</a>'),
    ('<a href="css-variables.html">CSS 변수 생성기</a>', '<a href="../css-variables.html">CSS Variables</a>'),
    ('<a href="about.html">서비스 소개</a>', '<a href="../about.html">About</a>'),
    ('<a href="privacy.html">개인정보처리방침</a>', '<a href="../privacy.html">Privacy Policy</a>'),

    # ── tool-section internal nav links (sidebar / cross-links) ──
    ('href="color-converter.html"', 'href="../color-converter.html"'),
    ('href="color-picker.html"', 'href="../color-picker.html"'),
    ('href="gradient-generator.html"', 'href="../gradient-generator.html"'),
    ('href="palette-generator.html"', 'href="../palette-generator.html"'),
    ('href="contrast-checker.html"', 'href="../contrast-checker.html"'),
    ('href="color-mixer.html"', 'href="../color-mixer.html"'),
    ('href="box-shadow.html"', 'href="../box-shadow.html"'),
    ('href="text-shadow.html"', 'href="../text-shadow.html"'),
    ('href="opacity-converter.html"', 'href="../opacity-converter.html"'),
    ('href="image-palette.html"', 'href="../image-palette.html"'),
    ('href="gradient-gallery.html"', 'href="../gradient-gallery.html"'),
    ('href="tints-shades.html"', 'href="../tints-shades.html"'),
    ('href="color-name.html"', 'href="../color-name.html"'),
    ('href="css-variables.html"', 'href="../css-variables.html"'),
    ('href="color-converter-full.html"', 'href="../color-converter-full.html"'),
    ('href="palette-contrast.html"', 'href="../palette-contrast.html"'),
    ('href="random-color.html"', 'href="../random-color.html"'),
    ('href="color-harmony.html"', 'href="../color-harmony.html"'),
    ('href="color-blindness.html"', 'href="../color-blindness.html"'),
    ('href="index.html"', 'href="../index.html"'),

    # ── FAQ section heading ──
    ('>자주 묻는 질문<', '>Frequently Asked Questions<'),

    # ── common JS strings ──
    ("'복사됨!'", "'Copied!'"),
    ('"복사됨!"', '"Copied!"'),
    ('복사 완료', 'Copied'),
    ('처리 중...', 'Processing...'),
    ('생성 중...', 'Generating...'),
    ('업로드 중...', 'Uploading...'),
    ('오류', 'Error'),

    # ── footer breadcrumb / links ──
    ('>전체 도구<', '>All Tools<'),
    ('>홈<', '>Home<'),

    # ── footer copyright ──
    ('© 2026 WooaColor by WooaHouse. 모든 권리 보유.', '© 2026 WooaColor by WooaHouse. All rights reserved.'),

    # ── about link in header ──
    ('>소개</a>', '>About</a>'),

    # ── about.html page content ──
    ('<p class="subtitle">WooaColor에 대해 알아보세요</p>',
     '<p class="subtitle">Learn about WooaColor</p>'),
    ('<h2>🎨 WooaColor이란?</h2>', '<h2>🎨 What is WooaColor?</h2>'),
    ('<p>WooaColor(WooaColor)은 디자이너, 개발자, 크리에이터를 위한 무료 온라인 색상 도구 모음입니다.</p>',
     '<p>WooaColor is a free online color toolkit for designers, developers, and creators.</p>'),
    ('<p>HEX·RGB·HSL 색상 변환, 이미지 색상 추출, 그라디언트 및 팔레트 생성, WCAG 접근성 대비 검사, CSS 박스·텍스트 그림자 코드 생성까지 색상 작업에 필요한 모든 도구를 한 곳에서 무료로 제공합니다.</p>',
     '<p>HEX/RGB/HSL conversion, image color picking, gradient and palette generation, WCAG contrast checking, CSS shadow code generation — all the color tools you need, free in one place.</p>'),
    ('<h2>✅ 서비스 특징</h2>', '<h2>✅ Features</h2>'),
    ('<li>HEX, RGB, HSL 세 가지 색상 코드 상호 변환</li>',
     '<li>HEX, RGB, HSL color code conversion</li>'),
    ('<li>이미지에서 색상 직접 추출 (캔버스 픽셀 샘플링)</li>',
     '<li>Extract colors from images (canvas pixel sampling)</li>'),
    ('<li>CSS 그라디언트 코드 즉시 생성</li>',
     '<li>Instant CSS gradient code generation</li>'),
    ('<li>보색·유사색·트라이어드 팔레트 생성</li>',
     '<li>Complementary, analogous, triadic palette generation</li>'),
    ('<li>WCAG AA·AAA 접근성 대비율 검사</li>',
     '<li>WCAG AA/AAA accessibility contrast checking</li>'),
    ('<li>CSS box-shadow / text-shadow 코드 생성기</li>',
     '<li>CSS box-shadow / text-shadow code generator</li>'),
    ('<li>불투명도 변환 (rgba / 8자리 HEX / hsla)</li>',
     '<li>Opacity conversion (rgba / 8-digit HEX / hsla)</li>'),
    ('<li>모든 처리가 브라우저 안에서 완결 — 서버로 데이터 전송 없음</li>',
     '<li>All processing in your browser — no data sent to any server</li>'),
    ('<li>회원가입 없이 무제한 무료 사용</li>',
     '<li>Unlimited free use with no signup required</li>'),
    ('<li>PC·태블릿·스마트폰 반응형 지원</li>',
     '<li>Responsive design for PC, tablet, and smartphone</li>'),
    ('<h2>🏠 WooaHouse 네트워크</h2>', '<h2>🏠 WooaHouse Network</h2>'),
    ('<p>WooaColor은 WooaHouse가 운영하는 서비스 중 하나입니다. 현재 운영 중인 서비스:</p>',
     '<p>WooaColor is one of the services operated by WooaHouse. Currently running services:</p>'),
    ('<h2>📬 문의</h2>', '<h2>📬 Contact</h2>'),
    ('<p>도구 추가 요청, 오류 제보, 제휴 문의 등은 아래 이메일로 연락 주세요.</p>',
     '<p>For tool requests, bug reports, or partnership inquiries, please contact us at the email below.</p>'),

    # ── privacy.html page content ──
    ('<p class="updated">최종 업데이트: 2026년 3월 15일</p>',
     '<p class="updated">Last updated: March 15, 2026</p>'),
    ('<h2>1. 개인정보 수집 여부</h2>', '<h2>1. Data Collection</h2>'),
    ('<p>WooaColor(colorkit.wooahouse.com)은 회원가입, 로그인 등의 기능이 없으며, 사용자의 개인정보를 직접 수집하지 않습니다. 본 서비스는 정적 웹사이트로 운영되며 서버 측에서 별도의 데이터를 저장하지 않습니다. 모든 색상 처리는 사용자의 브라우저 내에서만 이루어집니다.</p>',
     '<p>WooaColor (colorkit.wooahouse.com) has no signup or login features and does not directly collect personal data. This service operates as a static website with no server-side data storage. All color processing happens only within your browser.</p>'),
    ('<h2>2. 제3자 서비스</h2>', '<h2>2. Third-Party Services</h2>'),
    ('<p>WooaColor은 아래 제3자 서비스를 사용하며, 각 서비스의 개인정보 처리방침이 적용됩니다.</p>',
     '<p>WooaColor uses the following third-party services, each governed by their own privacy policies.</p>'),
    ('<li><strong>Google AdSense:</strong> 광고 게재를 위해 사용됩니다. Google은 쿠키를 통해 광고 관련 정보를 수집할 수 있습니다.</li>',
     '<li><strong>Google AdSense:</strong> Used to display ads. Google may collect ad-related information via cookies.</li>'),
    ('<li><strong>Google Analytics (해당 시):</strong> 익명화된 방문 통계 수집에 사용될 수 있습니다.</li>',
     '<li><strong>Google Analytics (if applicable):</strong> May be used to collect anonymized visit statistics.</li>'),
    ('<h2>3. 쿠키</h2>', '<h2>3. Cookies</h2>'),
    ('<p>WooaColor은 자체적으로 쿠키를 사용하지 않습니다. 다만 Google AdSense 등 제3자 서비스에서 광고 목적으로 쿠키를 사용할 수 있습니다. 브라우저 설정에서 쿠키를 비활성화할 수 있습니다.</p>',
     '<p>WooaColor does not use its own cookies. However, third-party services such as Google AdSense may use cookies for advertising purposes. You can disable cookies in your browser settings.</p>'),
    ('<h2>4. 로컬 스토리지</h2>', '<h2>4. Local Storage</h2>'),
    ('<p>WooaColor의 일부 기능(PWA 설치 배너 제어 등)은 브라우저의 sessionStorage를 사용합니다. 이 데이터는 사용자의 기기에만 저장되며 서버로 전송되지 않습니다.</p>',
     '<p>Some WooaColor features (such as controlling the PWA install banner) use the browser\'s sessionStorage. This data is stored only on your device and is never sent to a server.</p>'),
    ('<h2>5. 외부 링크</h2>', '<h2>5. External Links</h2>'),
    ('<p>WooaColor의 링크는 WooaHouse 네트워크 사이트 및 제3자 사이트로 연결될 수 있습니다. 해당 사이트의 개인정보 처리방침은 각 사이트에서 확인하시기 바랍니다. WooaColor은 외부 사이트의 개인정보 처리에 대해 책임지지 않습니다.</p>',
     '<p>WooaColor links may lead to WooaHouse network sites or third-party sites. Please review each site\'s privacy policy independently. WooaColor is not responsible for the privacy practices of external sites.</p>'),
    ('<h2>6. 문의</h2>', '<h2>6. Contact</h2>'),
    ('<p>개인정보 처리방침 관련 문의는 아래 이메일로 연락 주세요.</p>',
     '<p>For questions about this Privacy Policy, please contact us at the email below.</p>'),

    # ── index.html ld+json ListItem names ──
    ('"name": "HEX RGB HSL 변환"', '"name": "HEX RGB HSL Converter"'),
    ('"name": "색상 추출"', '"name": "Color Picker"'),
    ('"name": "그라디언트 생성기"', '"name": "Gradient Generator"'),
    ('"name": "색상 팔레트 생성기"', '"name": "Color Palette Generator"'),
    ('"name": "랜덤 색상 생성기"', '"name": "Random Color Generator"'),
    ('"name": "색상 대비 검사기"', '"name": "Color Contrast Checker"'),
    ('"name": "색상 혼합기"', '"name": "Color Mixer"'),
    ('"name": "박스 그림자 생성기"', '"name": "Box Shadow Generator"'),
    ('"name": "텍스트 그림자 생성기"', '"name": "Text Shadow Generator"'),
    ('"name": "불투명도 변환기"', '"name": "Opacity Converter"'),
    ('"name": "이미지 팔레트 추출"', '"name": "Image Palette Extractor"'),
    ('"name": "CSS 그라디언트 갤러리"', '"name": "CSS Gradient Gallery"'),
    ('"name": "틴트·셰이드 생성기"', '"name": "Tints & Shades Generator"'),
    ('"name": "색상 이름 찾기"', '"name": "Color Name Finder"'),
    ('"name": "CSS 변수 생성기"', '"name": "CSS Variables Generator"'),
    ('"name": "전체 색상 변환기"', '"name": "Full Color Converter"'),
    ('"name": "팔레트 대비 검사기"', '"name": "Palette Contrast Checker"'),
    ('"name": "색상 도구 목록"', '"name": "Color Tools List"'),

    # ── color-converter.html UI ──
    ('<span>HEX ↔ RGB ↔ HSL 변환</span>', '<span>HEX ↔ RGB ↔ HSL</span>'),
    ('<div class="panel-title">색상 정보</div>', '<div class="panel-title">Color Info</div>'),
    ('<div style="font-size:0.75rem;color:var(--text-light);margin-bottom:4px;">밝기</div>',
     '<div style="font-size:0.75rem;color:var(--text-light);margin-bottom:4px;">Brightness</div>'),
    ('<div id="infoBrightness" style="font-weight:700;font-size:0.95rem;">어두움</div>',
     '<div id="infoBrightness" style="font-weight:700;font-size:0.95rem;">Dark</div>'),
    ("document.getElementById('infoBrightness').textContent = lum > 0.179 ? '밝음' : '어두움';",
     "document.getElementById('infoBrightness').textContent = lum > 0.179 ? 'Light' : 'Dark';"),
    ("document.getElementById('errorMsg').textContent = '올바른 HEX 코드를 입력하세요 (예: #8B5CF6)';",
     "document.getElementById('errorMsg').textContent = 'Enter a valid HEX code (e.g. #8B5CF6)';"),
    ("document.getElementById('errorMsg').textContent = '올바른 RGB 형식을 입력하세요 (예: rgb(139, 92, 246))';",
     "document.getElementById('errorMsg').textContent = 'Enter a valid RGB format (e.g. rgb(139, 92, 246))';"),
    ("document.getElementById('errorMsg').textContent = '올바른 HSL 형식을 입력하세요 (예: hsl(263, 90%, 66%))';",
     "document.getElementById('errorMsg').textContent = 'Enter a valid HSL format (e.g. hsl(263, 90%, 66%))';"),
    ('💡 색상 코드를 모른다면 <a href="color-picker.html">색상 추출</a>로 이미지에서 직접 추출해 보세요.',
     '💡 If you don\'t know the color code, use the <a href="../color-picker.html">Color Picker</a> to extract it from an image.'),

    # ── color-picker.html UI ──
    ('<h3>이미지를 드래그하거나 클릭하여 업로드</h3>',
     '<h3>Drag or click to upload an image</h3>'),
    ('<p>JPG, PNG, GIF, WebP, BMP 지원</p>',
     '<p>JPG, PNG, GIF, WebP, BMP supported</p>'),
    ('<div class="panel-title">이미지 클릭으로 색상 추출</div>',
     '<div class="panel-title">Click Image to Pick Color</div>'),
    ('<div class="panel-title">현재 선택 색상</div>',
     '<div class="panel-title">Selected Color</div>'),
    ('📍 클릭 위치: <span id="clickPos">—</span>',
     '📍 Click position: <span id="clickPos">—</span>'),
    ('<div class="panel-title" style="margin-bottom:0;">최근 추출 색상 (최대 10개)</div>',
     '<div class="panel-title" style="margin-bottom:0;">Recent Colors (up to 10)</div>'),
    ('<span style="color:var(--text-light);font-size:0.85rem;">이미지를 클릭하면 여기에 색상이 쌓입니다</span>',
     '<span style="color:var(--text-light);font-size:0.85rem;">Click the image to collect colors here</span>'),
    ("el.innerHTML = '<span style=\"color:var(--text-light);font-size:0.85rem;\">이미지를 클릭하면 여기에 색상이 쌓입니다</span>';",
     "el.innerHTML = '<span style=\"color:var(--text-light);font-size:0.85rem;\">Click the image to collect colors here</span>';"),
    ('💡 추출한 색상을 다른 형식으로 변환하려면 <a href="color-converter.html">HEX ↔ RGB ↔ HSL 변환기</a>를 이용하세요.',
     '💡 To convert extracted colors to other formats, use the <a href="../color-converter.html">HEX ↔ RGB ↔ HSL Converter</a>.'),

    # ── contrast-checker.html UI ──
    ('<button class="swap-btn" onclick="swapColors()">⇄ 전경/배경 교체</button>',
     '<button class="swap-btn" onclick="swapColors()">⇄ Swap FG/BG</button>'),
    ('<div class="ratio-label">색상 대비율 (Contrast Ratio)</div>',
     '<div class="ratio-label">Contrast Ratio</div>'),
    ('<div class="wcag-item-label">AA 일반 텍스트</div>', '<div class="wcag-item-label">AA Normal Text</div>'),
    ('<div class="wcag-item-desc">최소 4.5:1 필요</div>', '<div class="wcag-item-desc">Min 4.5:1 required</div>'),
    ('<span id="badge-aa-normal" class="wcag-badge wcag-pass">✓ 통과</span>',
     '<span id="badge-aa-normal" class="wcag-badge wcag-pass">✓ Pass</span>'),
    ('<div class="wcag-item-label">AA 큰 텍스트</div>', '<div class="wcag-item-label">AA Large Text</div>'),
    ('<div class="wcag-item-desc">최소 3:1 필요 (18pt+)</div>', '<div class="wcag-item-desc">Min 3:1 required (18pt+)</div>'),
    ('<span id="badge-aa-large" class="wcag-badge wcag-pass">✓ 통과</span>',
     '<span id="badge-aa-large" class="wcag-badge wcag-pass">✓ Pass</span>'),
    ('<div class="wcag-item-label">AAA 일반 텍스트</div>', '<div class="wcag-item-label">AAA Normal Text</div>'),
    ('<div class="wcag-item-desc">최소 7:1 필요</div>', '<div class="wcag-item-desc">Min 7:1 required</div>'),
    ('<span id="badge-aaa-normal" class="wcag-badge wcag-pass">✓ 통과</span>',
     '<span id="badge-aaa-normal" class="wcag-badge wcag-pass">✓ Pass</span>'),
    ('<div class="wcag-item-label">AAA 큰 텍스트</div>', '<div class="wcag-item-label">AAA Large Text</div>'),
    ('<div class="wcag-item-desc">최소 4.5:1 필요</div>', '<div class="wcag-item-desc">Min 4.5:1 required</div>'),
    ('<span id="badge-aaa-large" class="wcag-badge wcag-pass">✓ 통과</span>',
     '<span id="badge-aaa-large" class="wcag-badge wcag-pass">✓ Pass</span>'),
    ('<div class="panel-title">미리보기</div>', '<div class="panel-title">Preview</div>'),
    ('<div class="preview-large">큰 텍스트 미리보기 (18pt 이상)</div>',
     '<div class="preview-large">Large Text Preview (18pt+)</div>'),
    ('<div class="preview-normal">일반 텍스트 미리보기입니다. This is a normal text preview for contrast check.</div>',
     '<div class="preview-normal">Normal text preview. This is a normal text preview for contrast check.</div>'),
    ('<div class="preview-small">작은 텍스트 미리보기. Small text preview for accessibility testing.</div>',
     '<div class="preview-small">Small text preview. Small text preview for accessibility testing.</div>'),
    ("el.textContent = '✓ 통과';", "el.textContent = '✓ Pass';"),
    ("el.textContent = '✗ 실패';", "el.textContent = '✗ Fail';"),
    ('💡 색상 코드를 모른다면 <a href="color-converter.html">색상 변환기</a>에서 HEX 코드를 확인하세요.',
     '💡 If you don\'t know the color code, check the <a href="../color-converter.html">Color Converter</a> for HEX codes.'),

    # ── color-mixer.html UI ──
    ('<label>색상 A</label>', '<label>Color A</label>'),
    ('<label>색상 B</label>', '<label>Color B</label>'),
    ('<label>색상 A 비율: <span id="ratioLabel">50%</span></label>',
     '<label>Color A Ratio: <span id="ratioLabel">50%</span></label>'),
    ('<div class="panel-title">혼합 결과</div>', '<div class="panel-title">Mixed Result</div>'),
    ('<div style="font-size:0.75rem;color:var(--text-light);text-align:center;margin-top:6px;">← 색상 A 100% &nbsp;&nbsp; 색상 B 100% →</div>',
     '<div style="font-size:0.75rem;color:var(--text-light);text-align:center;margin-top:6px;">← Color A 100% &nbsp;&nbsp; Color B 100% →</div>'),
    ('💡 혼합된 색상의 접근성을 확인하려면 <a href="contrast-checker.html">색상 대비 검사기</a>를 사용해 보세요.',
     '💡 To check the accessibility of the mixed color, use the <a href="../contrast-checker.html">Contrast Checker</a>.'),

    # ── box-shadow.html UI ──
    ('<div class="panel-title">생성된 CSS 코드</div>', '<div class="panel-title">Generated CSS Code</div>'),
    ('💡 텍스트에 그림자를 적용하려면 <a href="text-shadow.html">텍스트 그림자 생성기</a>를 사용해 보세요.',
     '💡 To apply a shadow to text, use the <a href="../text-shadow.html">Text Shadow Generator</a>.'),

    # ── text-shadow.html UI ──
    ('<label>샘플 텍스트</label>', '<label>Sample Text</label>'),
    ('<input type="text" id="sampleText" value="WooaColor WooaColor" placeholder="미리볼 텍스트 입력">',
     '<input type="text" id="sampleText" value="WooaColor WooaColor" placeholder="Enter preview text">'),
    ('<label>투명도 (Alpha)</label>', '<label>Opacity (Alpha)</label>'),
    ('💡 박스에 그림자를 적용하려면 <a href="box-shadow.html">박스 그림자 생성기</a>를 사용해 보세요.',
     '💡 To apply a shadow to a box element, use the <a href="../box-shadow.html">Box Shadow Generator</a>.'),

    # ── opacity-converter.html UI ──
    ('<label>불투명도 (Opacity): <span id="opacityLabel">80%</span></label>',
     '<label>Opacity: <span id="opacityLabel">80%</span></label>'),
    ('<div class="panel-title">변환 결과</div>', '<div class="panel-title">Conversion Result</div>'),
    ('<span class="code-result-label">8자리 HEX</span>', '<span class="code-result-label">8-digit HEX</span>'),
    ('💡 색상 코드를 모른다면 <a href="color-converter.html">색상 변환기</a>에서 HEX 코드를 확인하세요.',
     '💡 If you don\'t know the color code, check the <a href="../color-converter.html">Color Converter</a>.'),

    # ── image-palette.html UI ──
    ('<h3>이미지를 드래그 앤 드롭하세요</h3>', '<h3>Drag and drop an image here</h3>'),
    ('<p>JPG, PNG, WebP 등 이미지 파일 지원</p>', '<p>Supports JPG, PNG, WebP, and other image formats</p>'),
    ('<img id="imagePreview" alt="업로드된 이미지 미리보기">',
     '<img id="imagePreview" alt="Uploaded image preview">'),
    ('<div class="panel-title">추출 색상 수</div>', '<div class="panel-title">Number of Colors</div>'),
    ('<button class="count-btn" data-count="4">4색</button>', '<button class="count-btn" data-count="4">4</button>'),
    ('<button class="count-btn" data-count="6">6색</button>', '<button class="count-btn" data-count="6">6</button>'),
    ('<button class="count-btn active" data-count="8">8색</button>', '<button class="count-btn active" data-count="8">8</button>'),
    ('<button class="count-btn" data-count="10">10색</button>', '<button class="count-btn" data-count="10">10</button>'),
    ('<button class="count-btn" data-count="12">12색</button>', '<button class="count-btn" data-count="12">12</button>'),
    ('<div class="panel-title">주요 색상 (Dominant)</div>', '<div class="panel-title">Dominant Color</div>'),
    ('<div class="dominant-label">가장 눈에 띄는 색상</div>', '<div class="dominant-label">Most prominent color</div>'),
    ('<div class="panel-title">팔레트 프리뷰</div>', '<div class="panel-title">Palette Preview</div>'),
    ('<div class="panel-title">추출된 색상</div>', '<div class="panel-title">Extracted Colors</div>'),
    ('<button class="btn btn-primary" onclick="copyAllHex()">팔레트 코드 전체 복사</button>',
     '<button class="btn btn-primary" onclick="copyAllHex()">Copy All HEX Codes</button>'),
    ('<button class="btn btn-secondary" onclick="copyCssVars()">CSS 변수 복사</button>',
     '<button class="btn btn-secondary" onclick="copyCssVars()">Copy CSS Variables</button>'),
    ("showToast('이미지 파일만 지원합니다.');", "showToast('Only image files are supported.');"),
    ("showToast('색상 추출 중 오류가 발생했습니다. 다른 이미지를 시도해 주세요.');",
     "showToast('An error occurred during color extraction. Please try another image.');"),
    ("navigator.clipboard.writeText(text).then(() => showToast('복사됨! ' + text));",
     "navigator.clipboard.writeText(text).then(() => showToast('Copied! ' + text));"),
    ("navigator.clipboard.writeText(str).then(() => showToast('팔레트 전체 코드가 복사되었습니다!'));",
     "navigator.clipboard.writeText(str).then(() => showToast('All palette codes copied!'));"),
    ("showToast('CSS 변수 코드가 복사되었습니다!');", "showToast('CSS variable code copied!');"),
    ('💡 추출한 색상을 활용해 <a href="gradient-generator.html">그라디언트를 만들어 보세요</a> 또는 <a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">WooaImage에서 이미지 편집하기 →</a>',
     '💡 Use the extracted colors to <a href="../gradient-generator.html">create a gradient</a> or <a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">edit your image at WooaImage →</a>'),
    # image-palette color name arrays (Korean color names in JS)
    ("{ name: '빨강', h: [0, 15] }, { name: '주황', h: [15, 40] },",
     "{ name: 'Red', h: [0, 15] }, { name: 'Orange', h: [15, 40] },"),
    ("{ name: '노랑', h: [40, 65] }, { name: '연두', h: [65, 80] },",
     "{ name: 'Yellow', h: [40, 65] }, { name: 'Yellow-Green', h: [65, 80] },"),
    ("{ name: '초록', h: [80, 160] }, { name: '청록', h: [160, 190] },",
     "{ name: 'Green', h: [80, 160] }, { name: 'Cyan', h: [160, 190] },"),
    ("{ name: '파랑', h: [190, 260] }, { name: '남색', h: [260, 280] },",
     "{ name: 'Blue', h: [190, 260] }, { name: 'Indigo', h: [260, 280] },"),
    ("{ name: '보라', h: [280, 320] }, { name: '분홍', h: [320, 345] },",
     "{ name: 'Purple', h: [280, 320] }, { name: 'Pink', h: [320, 345] },"),
    ("{ name: '빨강', h: [345, 361] }", "{ name: 'Red', h: [345, 361] }"),
    ("if (l < 40) return '검정';", "if (l < 40) return 'Black';"),
    ("if (l > 220) return '흰색';", "if (l > 220) return 'White';"),
    ("return '회색';", "return 'Gray';"),
    ("return '색상';", "return 'Color';"),

    # ── gradient-generator.html UI ──
    ('<div style="font-size:0.82rem;font-weight:600;color:var(--text-light);margin-bottom:8px;">유형</div>',
     '<div style="font-size:0.82rem;font-weight:600;color:var(--text-light);margin-bottom:8px;">Type</div>'),
    ('<button class="direction-btn active" onclick="setType(\'linear\',this)">Linear (선형)</button>',
     '<button class="direction-btn active" onclick="setType(\'linear\',this)">Linear</button>'),
    ('<button class="direction-btn" onclick="setType(\'radial\',this)">Radial (방사형)</button>',
     '<button class="direction-btn" onclick="setType(\'radial\',this)">Radial</button>'),
    ('<button class="direction-btn" onclick="setType(\'conic\',this)">Conic (원추형)</button>',
     '<button class="direction-btn" onclick="setType(\'conic\',this)">Conic</button>'),
    ('<div style="font-size:0.82rem;font-weight:600;color:var(--text-light);margin-bottom:8px;">방향</div>',
     '<div style="font-size:0.82rem;font-weight:600;color:var(--text-light);margin-bottom:8px;">Direction</div>'),
    ('<button class="direction-btn" onclick="setDir(\'to right\',this)">→ 오른쪽</button>',
     '<button class="direction-btn" onclick="setDir(\'to right\',this)">→ Right</button>'),
    ('<button class="direction-btn" onclick="setDir(\'to left\',this)">← 왼쪽</button>',
     '<button class="direction-btn" onclick="setDir(\'to left\',this)">← Left</button>'),
    ('<button class="direction-btn active" onclick="setDir(\'135deg\',this)">↘ 대각선</button>',
     '<button class="direction-btn active" onclick="setDir(\'135deg\',this)">↘ Diagonal</button>'),
    ('<button class="direction-btn" onclick="setDir(\'to bottom\',this)">↓ 아래</button>',
     '<button class="direction-btn" onclick="setDir(\'to bottom\',this)">↓ Down</button>'),
    ('<button class="direction-btn" onclick="setDir(\'to top\',this)">↑ 위</button>',
     '<button class="direction-btn" onclick="setDir(\'to top\',this)">↑ Up</button>'),
    ('<button class="direction-btn" onclick="setDir(\'45deg\',this)">↗ 반대각선</button>',
     '<button class="direction-btn" onclick="setDir(\'45deg\',this)">↗ Anti-diagonal</button>'),
    ('<label style="font-size:0.82rem;color:var(--text-light);min-width:60px;">각도 직접:</label>',
     '<label style="font-size:0.82rem;color:var(--text-light);min-width:60px;">Custom angle:</label>'),
    ('<div class="panel-title" style="margin-bottom:0;">색상 정지점</div>',
     '<div class="panel-title" style="margin-bottom:0;">Color Stops</div>'),
    ('<button class="btn-copy" onclick="addStop()">+ 색상 추가</button>',
     '<button class="btn-copy" onclick="addStop()">+ Add Color</button>'),
    ('<div class="panel-title">생성된 CSS 코드</div>', '<div class="panel-title">Generated CSS Code</div>'),
    ('전체 속성 (background-image)도 함께 제공됩니다',
     'Full property (background-image) is also included'),
    ('💡 생성한 색상으로 팔레트를 만들어 보려면 <a href="palette-generator.html">팔레트 생성기</a>를 이용하세요.',
     '💡 To create a palette from your colors, use the <a href="../palette-generator.html">Palette Generator</a>.'),
    ('<span style="font-size:0.82rem;color:var(--text-light);min-width:28px;">정지점 ${i+1}</span>',
     '<span style="font-size:0.82rem;color:var(--text-light);min-width:28px;">Stop ${i+1}</span>'),
    ('title="삭제">✕</button>', 'title="Remove">✕</button>'),

    # ── gradient-gallery.html UI ──
    ('<input type="text" class="search-input" id="searchInput" placeholder="그라디언트 이름 검색...">',
     '<input type="text" class="search-input" id="searchInput" placeholder="Search gradient name...">'),
    ('<button class="filter-btn active" data-cat="all">전체</button>',
     '<button class="filter-btn active" data-cat="all">All</button>'),
    ('<button class="filter-btn" data-cat="nature">자연</button>',
     '<button class="filter-btn" data-cat="nature">Nature</button>'),
    ('<button class="filter-btn" data-cat="pastel">파스텔</button>',
     '<button class="filter-btn" data-cat="pastel">Pastel</button>'),
    ('<button class="filter-btn" data-cat="vivid">비비드</button>',
     '<button class="filter-btn" data-cat="vivid">Vivid</button>'),
    ('<button class="filter-btn" data-cat="dark">다크</button>',
     '<button class="filter-btn" data-cat="dark">Dark</button>'),
    ('<button class="filter-btn" data-cat="business">비즈니스</button>',
     '<button class="filter-btn" data-cat="business">Business</button>'),
    ('<button class="filter-btn" data-cat="trend">트렌드 2025</button>',
     '<button class="filter-btn" data-cat="trend">Trending 2025</button>'),
    ('<button class="filter-btn" data-cat="direction">방향별</button>',
     '<button class="filter-btn" data-cat="direction">By Direction</button>'),
    ("grid.innerHTML = '<div class=\"no-results\">검색 결과가 없습니다.</div>';",
     "grid.innerHTML = '<div class=\"no-results\">No results found.</div>';"),
    ('<div class="gradient-card-preview" style="background:${g.css};" title="클릭하여 코드 복사"></div>',
     '<div class="gradient-card-preview" style="background:${g.css};" title="Click to copy code"></div>'),
    ('<button class="copy-bg-btn" data-css="background: ${g.css};">코드 복사</button>',
     '<button class="copy-bg-btn" data-css="background: ${g.css};">Copy Code</button>'),
    ('<button class="copy-var-btn" data-css="${g.css}">CSS값 복사</button>',
     '<button class="copy-var-btn" data-css="${g.css}">Copy CSS</button>'),
    ('💡 그라디언트를 직접 커스터마이징하려면 <a href="gradient-generator.html">그라디언트 생성기</a>를 사용해 보세요. 색상이 마음에 드셨다면 <a href="https://fontkit.wooahouse.com/" target="_blank" rel="noopener">WooaFont에서 어울리는 폰트도 찾아보세요 →</a>',
     '💡 To customize a gradient, use the <a href="../gradient-generator.html">Gradient Generator</a>. If you like the colors, <a href="https://fontkit.wooahouse.com/" target="_blank" rel="noopener">find matching fonts at WooaFont →</a>'),
    # gradient gallery JS gradient names
    ("{ name: '일출',", "{ name: 'Sunrise',"),
    ("{ name: '바다',", "{ name: 'Ocean',"),
    ("{ name: '숲',", "{ name: 'Forest',"),
    ("{ name: '하늘',", "{ name: 'Sky',"),
    ("{ name: '노을',", "{ name: 'Sunset',"),
    ("{ name: '새벽',", "{ name: 'Dawn',"),
    ("{ name: '은하수',", "{ name: 'Galaxy',"),
    ("{ name: '초원',", "{ name: 'Meadow',"),
    ("{ name: '라벤더',", "{ name: 'Lavender',"),
    ("{ name: '복숭아',", "{ name: 'Peach',"),
    ("{ name: '민트',", "{ name: 'Mint',"),
    ("{ name: '바닐라',", "{ name: 'Vanilla',"),
    ("{ name: '라임',", "{ name: 'Lime',"),
    ("{ name: '코랄',", "{ name: 'Coral',"),
    ("{ name: '블루밍',", "{ name: 'Blooming',"),
    ("{ name: '소다',", "{ name: 'Soda',"),
    ("{ name: '퍼플레인',", "{ name: 'Purple Rain',"),
    ("{ name: '핫핑크',", "{ name: 'Hot Pink',"),
    ("{ name: '전기파랑',", "{ name: 'Electric Blue',"),
    ("{ name: '오렌지',", "{ name: 'Orange',"),
    ("{ name: '에메랄드',", "{ name: 'Emerald',"),
    ("{ name: '루비',", "{ name: 'Ruby',"),
    ("{ name: '네온그린',", "{ name: 'Neon Green',"),
    ("{ name: '사이버',", "{ name: 'Cyber',"),
    ("{ name: '미드나잇',", "{ name: 'Midnight',"),
    ("{ name: '딥스페이스',", "{ name: 'Deep Space',"),
    ("{ name: '블루나이트',", "{ name: 'Blue Night',"),
    ("{ name: '퍼플다크',", "{ name: 'Purple Dark',"),
    ("{ name: '차콜',", "{ name: 'Charcoal',"),
    ("{ name: '인디고',", "{ name: 'Indigo',"),
    ("{ name: '슬레이트',", "{ name: 'Slate',"),
    ("{ name: '실버',", "{ name: 'Silver',"),
    ("{ name: '코발트',", "{ name: 'Cobalt',"),
    ("{ name: '트러스트',", "{ name: 'Trust',"),
    ("{ name: '그린민트',", "{ name: 'Green Mint',"),
    ("{ name: '애쉬',", "{ name: 'Ash',"),
    ("{ name: '코튼캔디',", "{ name: 'Cotton Candy',"),
    ("{ name: '딸기우유',", "{ name: 'Strawberry Milk',"),
    ("{ name: '오로라',", "{ name: 'Aurora',"),
    ("{ name: '하이퍼',", "{ name: 'Hyper',"),
    ("{ name: '크리스탈',", "{ name: 'Crystal',"),
    ("{ name: '젤리',", "{ name: 'Jelly',"),
    ("{ name: '모카',", "{ name: 'Mocha',"),
    ("{ name: '세이지',", "{ name: 'Sage',"),
    ("{ name: '선셋 (→)',", "{ name: 'Sunset (→)',"),
    ("{ name: '오션 (↓)',", "{ name: 'Ocean (↓)',"),
    ("{ name: '네온 (45deg)',", "{ name: 'Neon (45deg)',"),
    ("{ name: '솔라 (↗)',", "{ name: 'Solar (↗)',"),
    ("{ name: '파도 (←)',", "{ name: 'Wave (←)',"),
    ("{ name: '원형 빛',", "{ name: 'Radial Light',"),
    ("{ name: '코닉 무지개',", "{ name: 'Conic Rainbow',"),
    ("{ name: '원형 글로우',", "{ name: 'Radial Glow',"),

    # ── tints-shades.html UI ──
    ('<div class="panel-title">기준 색상 선택</div>', '<div class="panel-title">Base Color</div>'),
    ('<button class="copy-css-btn" onclick="copyCSSVars()" title="Tailwind 스타일 CSS 변수 복사">',
     '<button class="copy-css-btn" onclick="copyCSSVars()" title="Copy Tailwind-style CSS Variables">'),
    ('CSS 변수 복사', 'Copy CSS Variables'),
    ('☀️ Tints — 밝은 계열', '☀️ Tints — Lighter'),
    ('<span>원색 + 흰색 혼합</span>', '<span>Base + White mix</span>'),
    ('<div class="ts-section-title">⬛ 원색 (Base Color)</div>',
     '<div class="ts-section-title">⬛ Base Color</div>'),
    ('🌙 Shades — 어두운 계열', '🌙 Shades — Darker'),
    ('<span>원색 + 검정 혼합</span>', '<span>Base + Black mix</span>'),
    ('💡 생성한 색상의 가독성을 확인하려면 <a href="contrast-checker.html">색상 대비 검사기(WCAG)</a>를 이용하세요. 팔레트 조합이 필요하면 <a href="palette-generator.html">팔레트 생성기</a>도 확인해보세요.',
     '💡 To check readability of the generated colors, use the <a href="../contrast-checker.html">Contrast Checker (WCAG)</a>. For palette combinations, check the <a href="../palette-generator.html">Palette Generator</a>.'),
    ("navigator.clipboard.writeText(hex).then(()=>showToast('✅ ' + hex + ' 복사됨!')).catch(()=>{});",
     "navigator.clipboard.writeText(hex).then(()=>showToast('✅ ' + hex + ' Copied!')).catch(()=>{});"),
    ("// Tints: 10% ~ 90% 흰색 혼합 (밝은 → 원색 순)",
     "// Tints: 10% ~ 90% white mix (light → base)"),
    ("// 90%흰→10%흰 순으로 나열 (왼쪽=가장 밝음)",
     "// 90%white→10%white order (left=lightest)"),
    ("tintsRow.appendChild(makeSwatchEl(mixed, `+${Math.round(ratio*100)}% 흰색`));",
     "tintsRow.appendChild(makeSwatchEl(mixed, `+${Math.round(ratio*100)}% White`));"),
    ("baseRow.appendChild(makeSwatchEl(hex, '원색'));",
     "baseRow.appendChild(makeSwatchEl(hex, 'Base'));"),
    ("// Shades: 원색 → 검정 방향", "// Shades: base → black direction"),
    ("shadesRow.appendChild(makeSwatchEl(mixed, `+${Math.round(ratio*100)}% 검정`));",
     "shadesRow.appendChild(makeSwatchEl(mixed, `+${Math.round(ratio*100)}% Black`));"),
    ("if(!isValidHex(hex)) { showToast('올바른 HEX 코드를 입력하세요'); return; }",
     "if(!isValidHex(hex)) { showToast('Enter a valid HEX code'); return; }"),
    ("// Tailwind 번호: 50,100,200,300,400,500,600,700,800,900,950",
     "// Tailwind numbers: 50,100,200,300,400,500,600,700,800,900,950"),
    ("// 50=가장밝음(90%흰), 100=80%흰 ... 500=원색 ... 900=80%검정, 950=90%검정",
     "// 50=lightest(90%white), 100=80%white ... 500=base ... 900=80%black, 950=90%black"),
    (".then(()=>showToast('✅ CSS 변수 복사됨!'))",
     ".then(()=>showToast('✅ CSS Variables Copied!'))"),
    ("showToast('✅ CSS 변수 복사됨!');", "showToast('✅ CSS Variables Copied!');"),

    # ── css-variables.html UI ──
    ('<div class="panel-title">색상 팔레트 입력</div>', '<div class="panel-title">Color Palette Input</div>'),
    ('<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">변수 이름과 색상을 입력하세요. 순서대로 CSS 변수가 생성됩니다.</div>',
     '<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">Enter variable names and colors. CSS variables are generated in order.</div>'),
    ('<button class="add-color-btn" id="addColorBtn">+ 색상 추가</button>',
     '<button class="add-color-btn" id="addColorBtn">+ Add Color</button>'),
    ('<div style="font-size:0.82rem;font-weight:600;color:#64748b;margin-bottom:6px;">팔레트 미리보기</div>',
     '<div style="font-size:0.82rem;font-weight:600;color:#64748b;margin-bottom:6px;">Palette Preview</div>'),
    ('<div class="panel-title" style="margin-bottom:10px;">생성된 코드</div>',
     '<div class="panel-title" style="margin-bottom:10px;">Generated Code</div>'),
    ('<button class="output-tab active" onclick="setTab(\'css\')">CSS 변수</button>',
     '<button class="output-tab active" onclick="setTab(\'css\')">CSS Variables</button>'),
    ('<button class="output-tab" onclick="setTab(\'scss\')">SCSS 변수</button>',
     '<button class="output-tab" onclick="setTab(\'scss\')">SCSS Variables</button>'),
    ('<button class="output-tab" onclick="setTab(\'js\')">JS 객체</button>',
     '<button class="output-tab" onclick="setTab(\'js\')">JS Object</button>'),
    ('<button class="copy-code-btn" id="copyCodeBtn">📋 코드 복사</button>',
     '<button class="copy-code-btn" id="copyCodeBtn">📋 Copy Code</button>'),
    ('💡 색상 밝기 변형이 필요하다면 <a href="tints-shades.html">Tints &amp; Shades 생성기</a>를 활용하세요.',
     '💡 For tint and shade variations, use the <a href="../tints-shades.html">Tints &amp; Shades Generator</a>.'),
    ('placeholder="변수 이름 (예: primary)" oninput="updateName(${i}, this.value)">',
     'placeholder="Variable name (e.g. primary)" oninput="updateName(${i}, this.value)">'),
    ("code += '}\\n\\n/* 사용 예시 */\\n';", "code += '}\\n\\n/* Usage example */\\n';"),
    ("code += '\\n// 사용 예시\\n';", "code += '\\n// Usage example\\n';"),
    ("btn.textContent = '✅ 복사됨!';", "btn.textContent = '✅ Copied!';"),
    ("setTimeout(() => { btn.textContent = '📋 코드 복사'; }, 1500);",
     "setTimeout(() => { btn.textContent = '📋 Copy Code'; }, 1500);"),

    # ── palette-contrast.html UI ──
    ('<div class="panel-title">색상 팔레트 입력</div>', '<div class="panel-title">Color Palette</div>'),
    ('<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">2~8개 색상을 입력하면 모든 조합의 대비율을 매트릭스로 표시합니다.</div>',
     '<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">Enter 2–8 colors to display all pairwise contrast ratios in a matrix.</div>'),
    ('<button class="add-palette-btn" id="addPaletteBtn">+ 색상 추가</button>',
     '<button class="add-palette-btn" id="addPaletteBtn">+ Add Color</button>'),
    ('<div class="legend-item"><div class="legend-dot" style="background:#dcfce7;border:1px solid #86efac;"></div> AAA 통과 (≥7:1)</div>',
     '<div class="legend-item"><div class="legend-dot" style="background:#dcfce7;border:1px solid #86efac;"></div> AAA Pass (≥7:1)</div>'),
    ('<div class="legend-item"><div class="legend-dot" style="background:#fef9c3;border:1px solid #fcd34d;"></div> AA 통과 (≥4.5:1)</div>',
     '<div class="legend-item"><div class="legend-dot" style="background:#fef9c3;border:1px solid #fcd34d;"></div> AA Pass (≥4.5:1)</div>'),
    ('<div class="legend-item"><div class="legend-dot" style="background:#fee2e2;border:1px solid #fca5a5;"></div> 미통과 (&lt;4.5:1)</div>',
     '<div class="legend-item"><div class="legend-dot" style="background:#fee2e2;border:1px solid #fca5a5;"></div> Fail (&lt;4.5:1)</div>'),
    ('💡 두 색상만 비교할 때는 <a href="contrast-checker.html">색상 대비 검사기</a>를 이용하세요.',
     '💡 To compare just two colors, use the <a href="../contrast-checker.html">Contrast Checker</a>.'),
    ("{ label:'배경(흰색)',  hex:'#FFFFFF' },", "{ label:'Background(White)',  hex:'#FFFFFF' },"),
    ("{ label:'본문',        hex:'#1E293B' },", "{ label:'Body Text',        hex:'#1E293B' },"),
    ("{ label:'성공',        hex:'#22C55E' },", "{ label:'Success',        hex:'#22C55E' },"),
    ("{ label:'경고',        hex:'#F59E0B' },", "{ label:'Warning',        hex:'#F59E0B' },"),
    ('<input type="text" value="${p.label}" placeholder="이름"',
     '<input type="text" value="${p.label}" placeholder="Name"'),
    ("palette.push({ label:`색상 ${palette.length+1}`, hex:'#'+Math.floor(Math.random()*0xFFFFFF).toString(16).padStart(6,'0') });",
     "palette.push({ label:`Color ${palette.length+1}`, hex:'#'+Math.floor(Math.random()*0xFFFFFF).toString(16).padStart(6,'0') });"),

    # ── palette-generator.html UI ──
    ('<div class="panel-title">기준 색상</div>', '<div class="panel-title">Base Color</div>'),
    ('<button class="btn-primary btn" onclick="generateAll()">팔레트 생성</button>',
     '<button class="btn-primary btn" onclick="generateAll()">Generate Palette</button>'),
    ('💡 색상 대비가 충분한지 확인하려면 <a href="contrast-checker.html">색상 대비 검사기</a>를 이용하세요.',
     '💡 To verify sufficient color contrast, use the <a href="../contrast-checker.html">Contrast Checker</a>.'),
    ("name: '🔵 보색 (Complementary)',", "name: '🔵 Complementary',"),
    ("desc: '색상환에서 정반대의 색상',", "desc: 'Opposite on the color wheel',"),
    ("name: '🟢 유사색 (Analogous)',", "name: '🟢 Analogous',"),
    ("desc: '색상환에서 인접한 색상들',", "desc: 'Adjacent colors on the color wheel',"),
    ("name: '🔺 트라이어드 (Triadic)',", "name: '🔺 Triadic',"),
    ("desc: '색상환에서 120° 간격의 세 색상',", "desc: 'Three colors 120° apart on the wheel',"),
    ("name: '✂️ 분할 보색 (Split-Complementary)',", "name: '✂️ Split-Complementary',"),
    ("desc: '보색의 인접 두 색상',", "desc: 'Two colors adjacent to the complement',"),
    ("name: '⬜ 단색 (Monochromatic)',", "name: '⬜ Monochromatic',"),
    ("desc: '같은 색조의 밝기·채도 변형',", "desc: 'Brightness and saturation variations of the same hue',"),
    ("tip.textContent = hex + ' 복사됨!';", "tip.textContent = hex + ' Copied!';"),
    # palette-generator CSS content property
    ("content:'복사'; position:absolute; inset:0;", "content:'Copy'; position:absolute; inset:0;"),

    # ── random-color.html UI ──
    ('<button class="generate-btn" onclick="generateRandom()">🎲 다시 생성</button>',
     '<button class="generate-btn" onclick="generateRandom()">🎲 Generate</button>'),
    ('<div class="history-title">최근 색상 히스토리</div>',
     '<div class="history-title">Recent Color History</div>'),
    ('<span style="font-size:0.82rem;color:var(--text-light);">아직 생성된 색상이 없습니다.</span>',
     '<span style="font-size:0.82rem;color:var(--text-light);">No colors generated yet.</span>'),
    ("container.innerHTML = '<span style=\"font-size:0.82rem;color:var(--text-light);\">아직 생성된 색상이 없습니다.</span>';",
     "container.innerHTML = '<span style=\"font-size:0.82rem;color:var(--text-light);\">No colors generated yet.</span>';"),
    ('💡 생성된 색상이 마음에 드셨나요? <a href="palette-generator.html">팔레트 생성기</a>로 어울리는 색상 조합을 만들어 보세요.',
     '💡 Like the generated color? Use the <a href="../palette-generator.html">Palette Generator</a> to create a matching color palette.'),

    # ── color-converter-full.html UI ──
    ('<div class="format-title">CMYK (인쇄용)</div>', '<div class="format-title">CMYK (Print)</div>'),
    ('💡 기본 HEX/RGB/HSL 변환만 필요하다면 <a href="color-converter.html">색상 변환기</a>를 이용하세요.',
     '💡 If you only need basic HEX/RGB/HSL conversion, use the <a href="../color-converter.html">Color Converter</a>.'),
    ('<div class="copied-toast" id="toast">✅ 복사됨!</div>',
     '<div class="copied-toast" id="toast">✅ Copied!</div>'),
    ("<div class=\"info-cell\"><div class=\"info-cell-label\">밝기</div><div class=\"info-cell-val\">${lum < 128 ? '어두움 🌑' : '밝음 ☀️'}</div></div>",
     "<div class=\"info-cell\"><div class=\"info-cell-label\">Brightness</div><div class=\"info-cell-val\">${lum < 128 ? 'Dark 🌑' : 'Light ☀️'}</div></div>"),

    # ── color-harmony.html UI ──
    ('<div class="panel-title">기준 색상 선택</div>', '<div class="panel-title">Select Base Color</div>'),
    ('<p style="font-size:0.85rem;color:var(--text-light);">색상을 선택하거나 HEX 코드를 직접 입력하세요. 스와치를 클릭하면 HEX가 클립보드에 복사됩니다.</p>',
     '<p style="font-size:0.85rem;color:var(--text-light);">Select a color or enter a HEX code directly. Click any swatch to copy its HEX to the clipboard.</p>'),
    ('보색 (Complementary)', 'Complementary'),
    ('<div class="harmony-desc">색상환에서 정반대에 위치한 색으로, 강한 대비와 생동감을 줍니다.</div>',
     '<div class="harmony-desc">The color directly opposite on the color wheel, giving strong contrast and vibrancy.</div>'),
    ('유사색 (Analogous)', 'Analogous'),
    ('<div class="harmony-desc">색상환에서 인접한 색으로, 부드럽고 조화로운 느낌을 줍니다.</div>',
     '<div class="harmony-desc">Colors adjacent on the color wheel, creating a smooth and harmonious feel.</div>'),
    ('삼색 (Triadic)', 'Triadic'),
    ('<div class="harmony-desc">색상환을 세 등분한 색상들로, 균형감 있으면서 다채로운 배색입니다.</div>',
     '<div class="harmony-desc">Three colors evenly spaced on the color wheel, offering a balanced and vibrant palette.</div>'),
    ('분보색 (Split-Complementary)', 'Split-Complementary'),
    ('<div class="harmony-desc">보색 양쪽의 색상을 사용해 보색보다 부드럽고 대비가 있는 배색입니다.</div>',
     '<div class="harmony-desc">Uses colors on either side of the complement, softer than pure complementary yet still contrasty.</div>'),
    ('정사각형 (Tetradic)', 'Tetradic (Square)'),
    ('<div class="harmony-desc">색상환을 네 등분한 색상들로, 풍부하고 다양한 배색을 만들 수 있습니다.</div>',
     '<div class="harmony-desc">Four colors evenly spaced on the color wheel, creating a rich and varied palette.</div>'),
    ('💡 추출한 색상을 다른 형식으로 변환하려면 <a href="color-converter.html">HEX ↔ RGB ↔ HSL 변환기</a>를 이용하세요.',
     '💡 To convert the extracted colors to other formats, use the <a href="../color-converter.html">HEX ↔ RGB ↔ HSL Converter</a>.'),
    ('<div class="copy-toast" id="copyToast">복사되었습니다!</div>',
     '<div class="copy-toast" id="copyToast">Copied!</div>'),
    ("card.title = `클릭해서 ${hex} 복사`;", "card.title = `Click to copy ${hex}`;"),
    ("toast.textContent = hex + ' 복사됨!';", "toast.textContent = hex + ' Copied!';"),
    ("{ hex: baseHex, label: '기준색' },", "{ hex: baseHex, label: 'Base' },"),
    ("{ hex: hslShift(hsl, 180), label: '보색' }", "{ hex: hslShift(hsl, 180), label: 'Complement' }"),

    # ── color-blindness.html UI ──
    ('<h3>이미지를 드래그하거나 클릭하여 업로드</h3>',
     '<h3>Drag or click to upload an image</h3>'),
    ('<p>JPG, PNG, GIF, WebP, BMP 지원 · 모든 처리가 브라우저에서 이루어져 이미지가 서버로 전송되지 않습니다</p>',
     '<p>Supports JPG, PNG, GIF, WebP, BMP · All processing happens in your browser — no data sent to any server</p>'),
    ('<div class="panel-title">시뮬레이션 보기 방식</div>',
     '<div class="panel-title">Simulation View Mode</div>'),
    ('<button class="sim-tab active" data-view="all" onclick="setView(\'all\', this)">모두 보기</button>',
     '<button class="sim-tab active" data-view="all" onclick="setView(\'all\', this)">View All</button>'),
    ('<button class="sim-tab" data-view="normal" onclick="setView(\'normal\', this)">원본</button>',
     '<button class="sim-tab" data-view="normal" onclick="setView(\'normal\', this)">Original</button>'),
    ('<button class="sim-tab" data-view="protanopia" onclick="setView(\'protanopia\', this)">적록색맹 (Protanopia)</button>',
     '<button class="sim-tab" data-view="protanopia" onclick="setView(\'protanopia\', this)">Protanopia</button>'),
    ('<button class="sim-tab" data-view="deuteranopia" onclick="setView(\'deuteranopia\', this)">녹색맹 (Deuteranopia)</button>',
     '<button class="sim-tab" data-view="deuteranopia" onclick="setView(\'deuteranopia\', this)">Deuteranopia</button>'),
    ('<button class="sim-tab" data-view="tritanopia" onclick="setView(\'tritanopia\', this)">청황색맹 (Tritanopia)</button>',
     '<button class="sim-tab" data-view="tritanopia" onclick="setView(\'tritanopia\', this)">Tritanopia</button>'),
    ('<button class="sim-tab" data-view="achromatopsia" onclick="setView(\'achromatopsia\', this)">전색맹 (Achromatopsia)</button>',
     '<button class="sim-tab" data-view="achromatopsia" onclick="setView(\'achromatopsia\', this)">Achromatopsia</button>'),
    ('원본 <span class="active-label">Normal</span>',
     'Original <span class="active-label">Normal</span>'),
    ('<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-normal\', \'원본\')">⬇ 다운로드</a>',
     '<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-normal\', \'Original\')">⬇ Download</a>'),
    ('<div class="preview-card-header">적록색맹 <span class="active-label">Protanopia</span></div>',
     '<div class="preview-card-header">Protanopia <span class="active-label">Protanopia</span></div>'),
    ('<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-protanopia\', \'적록색맹\')">⬇ 다운로드</a>',
     '<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-protanopia\', \'Protanopia\')">⬇ Download</a>'),
    ('<div class="preview-card-header">녹색맹 <span class="active-label">Deuteranopia</span></div>',
     '<div class="preview-card-header">Deuteranopia <span class="active-label">Deuteranopia</span></div>'),
    ('<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-deuteranopia\', \'녹색맹\')">⬇ 다운로드</a>',
     '<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-deuteranopia\', \'Deuteranopia\')">⬇ Download</a>'),
    ('<div class="preview-card-header">청황색맹 <span class="active-label">Tritanopia</span></div>',
     '<div class="preview-card-header">Tritanopia <span class="active-label">Tritanopia</span></div>'),
    ('<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-tritanopia\', \'청황색맹\')">⬇ 다운로드</a>',
     '<a class="preview-card-dl" onclick="downloadCanvas(\'canvas-tritanopia\', \'Tritanopia\')">⬇ Download</a>'),
    ('<div class="preview-card-header">전색맹 <span class="active-label">Achromatopsia</span></div>',
     '<div class="preview-card-header">Achromatopsia <span class="active-label">Achromatopsia</span></div>'),
    ('<a class="preview-card-dl" id="downloadBtn" onclick="downloadCanvas(\'canvas-achromatopsia\', \'전색맹\')">⬇ 다운로드</a>',
     '<a class="preview-card-dl" id="downloadBtn" onclick="downloadCanvas(\'canvas-achromatopsia\', \'Achromatopsia\')">⬇ Download</a>'),
    ('<a class="preview-card-dl" style="display:inline-block;padding:10px 28px;border-radius:8px;border:1.5px solid var(--primary);text-decoration:none;" onclick="downloadSingle()">⬇ 현재 보기 다운로드</a>',
     '<a class="preview-card-dl" style="display:inline-block;padding:10px 28px;border-radius:8px;border:1.5px solid var(--primary);text-decoration:none;" onclick="downloadSingle()">⬇ Download Current View</a>'),
    ('<button onclick="resetUpload()" class="btn btn-outline" style="margin-top:12px;">🔄 다른 이미지 사용</button>',
     '<button onclick="resetUpload()" class="btn btn-outline" style="margin-top:12px;">🔄 Use Another Image</button>'),
    ('💡 색상 대비(접근성 기준)를 확인하려면 <a href="contrast-checker.html">색상 대비 검사기 (WCAG)</a>를 이용하세요.',
     '💡 To check color contrast (accessibility), use the <a href="../contrast-checker.html">Contrast Checker (WCAG)</a>.'),
    ("normal: '원본',", "normal: 'Original',"),
    ("protanopia: '적록색맹 (Protanopia)',", "protanopia: 'Protanopia',"),
    ("deuteranopia: '녹색맹 (Deuteranopia)',", "deuteranopia: 'Deuteranopia',"),
    ("tritanopia: '청황색맹 (Tritanopia)',", "tritanopia: 'Tritanopia',"),
    ("achromatopsia: '전색맹 (Achromatopsia)'", "achromatopsia: 'Achromatopsia'"),
    ("document.getElementById('singleView').querySelector('a').textContent = '⬇ ' + labels[type] + ' 다운로드';",
     "document.getElementById('singleView').querySelector('a').textContent = '⬇ Download ' + labels[type];"),
    ("link.download = '색맹시뮬레이션_' + label + '.png';",
     "link.download = 'color_blindness_simulation_' + label + '.png';"),

    # ── color-name.html UI ──
    ('<div class="panel-title">색상 입력</div>', '<div class="panel-title">Color Input</div>'),
    ('<label>HEX 코드</label>', '<label>HEX Code</label>'),
    ('<label>R (빨강) — <span id="rVal">139</span></label>',
     '<label>R (Red) — <span id="rVal">139</span></label>'),
    ('<label>G (초록) — <span id="gVal">92</span></label>',
     '<label>G (Green) — <span id="gVal">92</span></label>'),
    ('<label>B (파랑) — <span id="bVal">246</span></label>',
     '<label>B (Blue) — <span id="bVal">246</span></label>'),
    ('<div class="panel-title">가장 가까운 색상 이름</div>',
     '<div class="panel-title">Closest Color Name</div>'),
    ('<div class="cn-similar-title">유사 색상 TOP 5</div>',
     '<div class="cn-similar-title">Top 5 Similar Colors</div>'),
    ('💡 색상 코드를 서로 변환하려면 <a href="color-converter.html">색상 변환기(HEX↔RGB↔HSL)</a>를 이용하세요. 색상 팔레트가 필요하면 <a href="palette-generator.html">팔레트 생성기</a>도 확인해보세요.',
     '💡 To convert color codes, use the <a href="../color-converter.html">Color Converter (HEX↔RGB↔HSL)</a>. For palette generation, check the <a href="../palette-generator.html">Palette Generator</a>.'),
    (".then(()=>showToast('✅ ' + hex + ' 복사됨!'))",
     ".then(()=>showToast('✅ ' + hex + ' Copied!'))"),
    ("showToast('✅ ' + hex + ' 복사됨!');", "showToast('✅ ' + hex + ' Copied!');"),
    ('<div class="cn-similarity">유사도 ${sim}%</div>',
     '<div class="cn-similarity">Similarity ${sim}%</div>'),
    ("${best.dist===0?'<span style=\"font-size:0.78rem;color:#059669;font-weight:600;\">정확히 일치</span>':''}",
     "${best.dist===0?'<span style=\"font-size:0.78rem;color:#059669;font-weight:600;\">Exact match</span>':''}"),
    ('<button class="cn-copy-btn" onclick="copyHex(\'${best.hex}\')">HEX 복사</button>',
     '<button class="cn-copy-btn" onclick="copyHex(\'${best.hex}\')">Copy HEX</button>'),
    ('<div class="cn-similar-badge">유사도 ${s}%</div>',
     '<div class="cn-similar-badge">Similarity ${s}%</div>'),
    ('<button class="cn-similar-copy" onclick="copyHex(\'${c.hex}\')">복사</button>',
     '<button class="cn-similar-copy" onclick="copyHex(\'${c.hex}\')">Copy</button>'),

    # ── index.html footer links with full href ──
    ('<a href="color-converter-full.html">전체 색상 변환기</a>',
     '<a href="../color-converter-full.html">Full Color Converter</a>'),
    ('<a href="color-picker.html">색상 추출</a>',
     '<a href="../color-picker.html">Color Picker</a>'),
    ('<a href="color-name.html">색상 이름 찾기</a>',
     '<a href="../color-name.html">Color Name Finder</a>'),
    ('<a href="gradient-generator.html">그라디언트 생성기</a>',
     '<a href="../gradient-generator.html">Gradient Generator</a>'),
    ('<a href="palette-generator.html">팔레트 생성기</a>',
     '<a href="../palette-generator.html">Palette Generator</a>'),
    ('<a href="random-color.html">랜덤 색상 생성기</a>',
     '<a href="../random-color.html">Random Color</a>'),
    ('<a href="tints-shades.html">틴트·셰이드 생성기</a>',
     '<a href="../tints-shades.html">Tints &amp; Shades</a>'),
    ('<a href="contrast-checker.html">색상 대비 검사기</a>',
     '<a href="../contrast-checker.html">Contrast Checker</a>'),
    ('<a href="color-mixer.html">색상 혼합기</a>',
     '<a href="../color-mixer.html">Color Mixer</a>'),
    ('<a href="palette-contrast.html">팔레트 대비 검사기</a>',
     '<a href="../palette-contrast.html">Palette Contrast</a>'),
    ('<a href="box-shadow.html">박스 그림자 생성기</a>',
     '<a href="../box-shadow.html">Box Shadow</a>'),
    ('<a href="text-shadow.html">텍스트 그림자 생성기</a>',
     '<a href="../text-shadow.html">Text Shadow</a>'),
    ('<a href="opacity-converter.html">불투명도 변환기</a>',
     '<a href="../opacity-converter.html">Opacity Converter</a>'),
    ('<a href="css-variables.html">CSS 변수 생성기</a>',
     '<a href="../css-variables.html">CSS Variables</a>'),
    ('<a href="about.html">서비스 소개</a>',
     '<a href="../about.html">About</a>'),
    ('<a href="privacy.html">개인정보처리방침</a>',
     '<a href="../privacy.html">Privacy Policy</a>'),
    ('<a href="index.html">색상 이름 찾기</a>',
     '<a href="../index.html">Color Name Finder</a>'),
    ('<a href="index.html">전체 도구</a>',
     '<a href="../index.html">All Tools</a>'),
    ('<a href="index.html">홈</a>',
     '<a href="../index.html">Home</a>'),
    ('<a href="index.html">홈페이지</a>',
     '<a href="../index.html">Home</a>'),

    # ── footer description for index ──
    ('<p>무료 온라인 색상 도구 모음. 변환, 생성, 분석, CSS 코드까지 모든 색상 작업을 브라우저에서 처리하세요.</p>',
     '<p>Free online color tools. Convert, generate, analyze, and code — all in your browser.</p>'),

    # ── color-name.html inline footer link ──
    ('<a href="index.html">색상 이름 찾기</a>', '<a href="../index.html">Color Name Finder</a>'),

    # ── fix: 생성된 CSS Code (partial transform: CSS 코드→CSS Code already ran) ──
    ('<div class="panel-title">생성된 CSS Code</div>',
     '<div class="panel-title">Generated CSS Code</div>'),

    # ── breadcrumb spans (no id attribute) ──
    ('<span>박스 그림자 생성기</span>', '<span>Box Shadow</span>'),
    ('<span>텍스트 그림자 생성기</span>', '<span>Text Shadow</span>'),
    ('<span>색맹 시뮬레이터</span>', '<span>Color Blindness Sim</span>'),
    ('<span>색상 변환기 (전체)</span>', '<span>Full Color Converter</span>'),
    ('<span>HEX ↔ RGB ↔ HSL 변환</span>', '<span>HEX ↔ RGB ↔ HSL</span>'),
    ('<span>색상 조화 생성기</span>', '<span>Color Harmony</span>'),
    ('<span>색상 혼합기</span>', '<span>Color Mixer</span>'),
    ('<span>Color Name 찾기</span>', '<span>Color Name Finder</span>'),
    ('<span>이미지 Color Palette 추출</span>', '<span>Image Palette</span>'),
    ('<span>CSS 색상 변수 생성기</span>', '<span>CSS Variables</span>'),
    ('<span>CSS 그라디언트 갤러리</span>', '<span>Gradient Gallery</span>'),
    ('<span>그라디언트 생성기</span>', '<span>Gradient Generator</span>'),
    ('<span>Opacity 변환기</span>', '<span>Opacity Converter</span>'),
    ('<span>팔레트 대비 검사기</span>', '<span>Palette Contrast</span>'),
    ('<span>팔레트 생성기</span>', '<span>Palette Generator</span>'),
    ('<span>색상 대비 검사기</span>', '<span>Contrast Checker</span>'),
    ('<span>랜덤 색상 생성기</span>', '<span>Random Color</span>'),
    ('<span>Tints &amp; Shades 생성기</span>', '<span>Tints &amp; Shades</span>'),

    # ── tool header <p> (tool desc without id) ──
    ('<p>슬라이더로 CSS box-shadow 코드를 즉시 생성하세요</p>',
     '<p>Configure CSS box-shadow with sliders and copy the code instantly.</p>'),
    ('<p>슬라이더로 CSS text-shadow 코드를 즉시 생성하세요</p>',
     '<p>Configure CSS text-shadow with sliders and copy the code instantly.</p>'),
    ('<p>이미지를 업로드하면 4가지 색맹 유형으로 보이는 모습을 시뮬레이션합니다</p>',
     '<p>Upload an image to simulate how it appears to viewers with four types of color blindness.</p>'),
    ('<p>5가지 색상 형식을 실시간으로 상호 변환합니다. 인쇄용 CMYK까지 지원.</p>',
     '<p>Convert between five color formats in real time. Supports print-ready CMYK.</p>'),
    ('<p>세 가지 Color Code를 실시간으로 상호 변환합니다</p>',
     '<p>Convert between three color code formats in real time.</p>'),
    ('<p>기준 색상을 선택하면 5가지 색상 조화 이론에 따른 팔레트를 자동으로 생성합니다</p>',
     '<p>Select a base color to auto-generate palettes based on five color harmony theories.</p>'),
    ('<p>Base Color을 선택하면 5가지 색상 조화 이론에 따른 팔레트를 자동으로 생성합니다</p>',
     '<p>Select a base color to auto-generate palettes based on five color harmony theories.</p>'),
    ('<p>두 색상을 원하는 비율로 혼합한 결과를 확인하세요</p>',
     '<p>Blend two colors in any ratio and see the resulting color.</p>'),
    ('<p>Color Code를 입력하면 Closest Color Name(Korean+English)과 Similar Colors 5개를 찾아드립니다</p>',
     '<p>Enter a color code to find the closest color name and top 5 similar colors.</p>'),
    ('<p>이미지를 업로드하고 원하는 픽셀을 클릭해 색상을 추출하세요</p>',
     '<p>Upload an image and click any pixel to extract its color code.</p>'),
    ('<p>WCAG 접근성 기준에 따른 색상 Contrast Ratio을 즉시 검사합니다</p>',
     '<p>Instantly check color contrast ratios against WCAG accessibility standards.</p>'),
    ('<p>Color Palette를 입력하면 CSS Variables, SCSS Variables, Tailwind Config 코드를 즉시 생성합니다.</p>',
     '<p>Enter your color palette to instantly generate CSS Variables, SCSS Variables, and Tailwind Config code.</p>'),
    ('<p>트렌디한 CSS 그라디언트 50가지 이상. 클릭 한 번으로 코드를 복사하세요.</p>',
     '<p>50+ trendy CSS gradient presets. Click to copy the code instantly.</p>'),
    ('<p>CSS 그라디언트 코드를 실시간으로 생성하고 Preview</p>',
     '<p>Generate CSS gradient code in real time with a live preview.</p>'),
    ('<p>HEX 색상에 Transparency를 추가해 rgba, 8-digit HEX, hsla 코드를 얻으세요</p>',
     '<p>Add transparency to any HEX color to get rgba, 8-digit HEX, and hsla codes.</p>'),
    ('<p>Color Palette 전체의 조합별 Contrast Ratio을 매트릭스로 한눈에 확인하세요. AA/AAA 통과 여부 즉시 표시.</p>',
     '<p>View contrast ratios for all color pairs in your palette as a matrix. AA/AAA pass/fail shown instantly.</p>'),
    ('<p>Base Color에서 5가지 조화 팔레트를 자동 생성합니다</p>',
     '<p>Auto-generate five harmony palettes from a base color.</p>'),
    ('<p>버튼 한 번으로 새로운 색상을 생성하고 코드를 바로 복사하세요</p>',
     '<p>Generate a new random color and copy its code with one click.</p>'),
    ('<p>색상 하나로 밝은 계열(Tints) 10단계 + 어두운 계열(Shades) 10단계를 즉시 생성합니다</p>',
     '<p>Generate 10 tints and 10 shades from a single color instantly.</p>'),

    # ── cross-link tips (partially transformed) ──
    ('💡 텍스트에 그림자를 적용하려면 <a href="../text-shadow.html">Text Shadow</a>를 사용해 보세요.',
     '💡 To add a shadow to text, try the <a href="../text-shadow.html">Text Shadow Generator</a>.'),
    ('💡 박스에 그림자를 적용하려면 <a href="../box-shadow.html">Box Shadow</a>를 사용해 보세요.',
     '💡 To add a shadow to a box, try the <a href="../box-shadow.html">Box Shadow Generator</a>.'),
    ('💡 색상 대비(접근성 기준)를 확인하려면 <a href="../contrast-checker.html">색상 대비 검사기 (WCAG)</a>를 이용하세요.',
     '💡 To check color contrast for accessibility, use the <a href="../contrast-checker.html">Contrast Checker (WCAG)</a>.'),
    ('💡 기본 HEX/RGB/HSL 변환만 필요하다면 <a href="../color-converter.html">색상 변환기</a>를 이용하세요.',
     '💡 For basic HEX/RGB/HSL conversion, use the <a href="../color-converter.html">Color Converter</a>.'),
    ('💡 Color Code를 모른다면 <a href="../color-converter.html">색상 변환기</a>에서 HEX 코드를 확인하세요.',
     '💡 If you don\'t know the color code, look it up with the <a href="../color-converter.html">Color Converter</a>.'),
    ('💡 추출한 색상을 다른 형식으로 변환하려면 <a href="../color-converter.html">HEX ↔ RGB ↔ HSL 변환기</a>를 이용하세요.',
     '💡 To convert extracted colors to other formats, use the <a href="../color-converter.html">HEX ↔ RGB ↔ HSL Converter</a>.'),
    ('💡 Color Code를 서로 변환하려면 <a href="../color-converter.html">색상 변환기(HEX↔RGB↔HSL)</a>를 이용하세요. Color Palette가 필요하면 <a href="../palette-generator.html">팔레트 생성기</a>도 확인해보세요.',
     '💡 To convert color codes, use the <a href="../color-converter.html">Color Converter (HEX↔RGB↔HSL)</a>. For palette generation, see the <a href="../palette-generator.html">Palette Generator</a>.'),
    ('💡 혼합된 색상의 접근성을 확인하려면 <a href="../contrast-checker.html">Contrast Checker</a>를 사용해 보세요.',
     '💡 To check the accessibility of the mixed color, use the <a href="../contrast-checker.html">Contrast Checker</a>.'),
    ('💡 추출한 색상을 활용해 <a href="../gradient-generator.html">그라디언트를 만들어 보세요</a>',
     '💡 Use the extracted colors to <a href="../gradient-generator.html">create a gradient</a>'),
    ('💡 생성된 색상이 마음에 드셨나요? <a href="../palette-generator.html">Palette Generator</a>로 어울리는 색상 조합을 만들어 보세요.',
     '💡 Like the generated color? Use the <a href="../palette-generator.html">Palette Generator</a> to find a matching palette.'),
    ('💡 생성한 색상의 가독성을 확인하려면 <a href="../contrast-checker.html">색상 대비 검사기(WCAG)</a>를 이용하세요. 팔레트 조합이 필요하면 <a href="../palette-generator.html">Palette Generator</a>도 확인해보세요.',
     '💡 To check the readability of generated colors, use the <a href="../contrast-checker.html">Contrast Checker (WCAG)</a>. For palette combinations, see the <a href="../palette-generator.html">Palette Generator</a>.'),
    ('💡 그라디언트를 직접 커스터마이징하려면 <a href="../gradient-generator.html">Gradient Generator</a>를 사용해 보세요. 색상이 마음에 드셨다면',
     '💡 To customize gradients directly, try the <a href="../gradient-generator.html">Gradient Generator</a>. If you love the colors,'),
    ('💡 색상 대비가 충분한지 확인하려면 <a href="../contrast-checker.html">Contrast Checker</a>를 이용하세요.',
     '💡 To verify sufficient color contrast, use the <a href="../contrast-checker.html">Contrast Checker</a>.'),
    ('💡 두 색상만 비교할 때는 <a href="../contrast-checker.html">Contrast Checker</a>를 이용하세요.',
     '💡 To compare just two colors, use the <a href="../contrast-checker.html">Contrast Checker</a>.'),
    ('💡 색상 밝기 변형이 필요하다면 <a href="../tints-shades.html">Tints &amp; Shades 생성기</a>를 활용하세요.',
     '💡 For brightness variations, use the <a href="../tints-shades.html">Tints &amp; Shades Generator</a>.'),
    ('💡 생성한 색상으로 팔레트를 만들어 보려면 <a href="../palette-generator.html">Palette Generator</a>를 이용하세요.',
     '💡 To build a palette from the generated colors, use the <a href="../palette-generator.html">Palette Generator</a>.'),

    # ── index.html ListItem "name":"..." (no space after colon) ──
    ('"name":"HEX RGB HSL 변환"', '"name":"HEX RGB HSL Converter"'),
    ('"name":"색상 추출"', '"name":"Color Picker"'),
    ('"name":"그라디언트 생성기"', '"name":"Gradient Generator"'),
    ('"name":"색상 팔레트 생성기"', '"name":"Color Palette Generator"'),
    ('"name":"Color Palette 생성기"', '"name":"Color Palette Generator"'),
    ('"name":"랜덤 색상 생성기"', '"name":"Random Color Generator"'),
    ('"name":"색상 대비 검사기"', '"name":"Color Contrast Checker"'),
    ('"name":"색상 혼합기"', '"name":"Color Mixer"'),
    ('"name":"박스 그림자 생성기"', '"name":"Box Shadow Generator"'),
    ('"name":"텍스트 그림자 생성기"', '"name":"Text Shadow Generator"'),
    ('"name":"Opacity 변환기"', '"name":"Opacity Converter"'),
    ('"name":"불투명도 변환기"', '"name":"Opacity Converter"'),
    ('"name":"이미지 팔레트 추출"', '"name":"Image Palette Extractor"'),
    ('"name":"CSS 그라디언트 갤러리"', '"name":"CSS Gradient Gallery"'),
    ('"name":"틴트·셰이드 생성기"', '"name":"Tints & Shades Generator"'),
    ('"name":"Color Name 찾기"', '"name":"Color Name Finder"'),
    ('"name":"색상 이름 찾기"', '"name":"Color Name Finder"'),
    ('"name":"CSS Variables 생성기"', '"name":"CSS Variables Generator"'),
    ('"name":"전체 색상 변환기"', '"name":"Full Color Converter"'),
    ('"name":"팔레트 대비 검사기"', '"name":"Palette Contrast Checker"'),

    # ── index.html footer links ──
    ('<a href="../color-name.html">Color Name 찾기</a>',
     '<a href="../color-name.html">Color Name Finder</a>'),
    ('<a href="../opacity-converter.html">Opacity 변환기</a>',
     '<a href="../opacity-converter.html">Opacity Converter</a>'),
    ('<a href="../css-variables.html">CSS Variables 생성기</a>',
     '<a href="../css-variables.html">CSS Variables Generator</a>'),

    # ── index.html hero/feature description ──
    ('<p>무료 온라인 색상 도구 모음. 변환, 생성, 분석, CSS Code까지 모든 색상 작업을 브라우저에서 처리하세요.</p>',
     '<p>Free online color tools. Convert, generate, analyze, and code — all in your browser.</p>'),

    # ── about.html remaining items ──
    ('<li>보색·유사색·트라이어드 팔레트 생성</li>',
     '<li>Complementary, analogous, triadic palette generation</li>'),
    ('<li>WCAG AA·AAA 접근성 대비율 검사</li>',
     '<li>WCAG AA/AAA accessibility contrast ratio check</li>'),
    ('<li>불투명도 변환 (rgba / 8자리 HEX / hsla)</li>',
     '<li>Opacity conversion (rgba / 8-digit HEX / hsla)</li>'),
    ('<p>도구 추가 요청, 오류 제보, 제휴 문의 등은 아래 이메일로 연락 주세요.</p>',
     '<p>For tool requests, bug reports, or partnership inquiries, please contact us by email.</p>'),

    # ── about.html og:title / og:description (partially transformed) ──
    # These are handled by ABOUT_EXTRA, but in case they remain:

    # ── contrast-checker.html ──
    ('<div class="ratio-label">색상 Contrast Ratio (Contrast Ratio)</div>',
     '<div class="ratio-label">Color Contrast Ratio</div>'),
    ('<div class="preview-large">큰 텍스트 Preview (18pt 이상)</div>',
     '<div class="preview-large">Large Text Preview (18pt+)</div>'),
    ('<div class="preview-normal">일반 텍스트 Preview입니다. This is a normal text preview for contrast check.</div>',
     '<div class="preview-normal">Normal text preview. This is a normal text preview for contrast check.</div>'),
    ('<div class="preview-small">작은 텍스트 Preview. Small text preview for accessibility testing.</div>',
     '<div class="preview-small">Small text preview. Small text preview for accessibility testing.</div>'),

    # ── css-variables.html ──
    ('<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">변수 이름과 색상을 입력하세요. 순서대로 CSS Variables가 생성됩니다.</div>',
     '<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">Enter variable names and colors. CSS variables are generated in order.</div>'),
    ('<div style="font-size:0.82rem;font-weight:600;color:#64748b;margin-bottom:6px;">팔레트 Preview</div>',
     '<div style="font-size:0.82rem;font-weight:600;color:#64748b;margin-bottom:6px;">Palette Preview</div>'),

    # ── gradient-gallery.html ──
    ('<button class="filter-btn" data-cat="direction">Direction별</button>',
     '<button class="filter-btn" data-cat="direction">By Direction</button>'),
    ('"description": "트렌디한 CSS 그라디언트 50가지 모음. 클릭 한 번으로 CSS Code 복사."',
     '"description": "50+ trendy CSS gradient presets. Click once to copy the CSS code."'),

    # ── gradient-generator.html ──
    ("setTimeout(() => { btns[1].textContent = '복사'; btns[1].classList.remove('copied'); }, 1500);",
     "setTimeout(() => { btns[1].textContent = 'Copy'; btns[1].classList.remove('copied'); }, 1500);"),

    # ── image-palette.html ──
    ('<img id="imagePreview" alt="업로드된 이미지 Preview">',
     '<img id="imagePreview" alt="Uploaded image preview">'),
    ('<button class="btn-copy mt-8" onclick="copyText(document.getElementById(\'dominantHex\').textContent)">HEX 복사</button>',
     '<button class="btn-copy mt-8" onclick="copyText(document.getElementById(\'dominantHex\').textContent)">Copy HEX</button>'),
    ('<button class="btn btn-secondary" onclick="copyCssVars()">CSS Variables 복사</button>',
     '<button class="btn btn-secondary" onclick="copyCssVars()">Copy CSS Variables</button>'),
    ('<button class="btn-copy" onclick="event.stopPropagation();copyText(\'${hex}\')">HEX 복사</button>',
     '<button class="btn-copy" onclick="event.stopPropagation();copyText(\'${hex}\')">Copy HEX</button>'),
    ("showToast('색상 추출 중 Error가 발생했습니다. 다른 이미지를 시도해 주세요.');",
     "showToast('An error occurred while extracting colors. Please try another image.');"),
    ("showToast('CSS Variables 코드가 복사되었습니다!');",
     "showToast('CSS Variables copied!');"),

    # ── palette-contrast.html ──
    ('<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">2~8개 색상을 입력하면 모든 조합의 Contrast Ratio을 매트릭스로 표시합니다.</div>',
     '<div style="font-size:0.82rem;color:#64748b;margin-bottom:12px;">Enter 2–8 colors to display all pairwise contrast ratios in a matrix.</div>'),

    # ── palette-generator.html ──
    ("name: '✂️ 분할 Complementary (Split-Complementary)',",
     "name: '✂️ Split-Complementary',"),
    ("desc: 'Complementary의 인접 두 색상',",
     "desc: 'Two colors adjacent to the complement',"),

    # ── tints-shades.html ──
    ('<button class="copy-css-btn" onclick="copyCSSVars()" title="Tailwind 스타일 CSS Variables 복사">',
     '<button class="copy-css-btn" onclick="copyCSSVars()" title="Copy Tailwind-style CSS Variables">'),
    ('CSS Variables 복사\n',
     'Copy CSS Variables\n'),
    ('.then(()=>showToast(\'✅ CSS Variables 복사됨!\'))',
     '.then(()=>showToast(\'✅ CSS Variables Copied!\'))'),
    ("showToast('✅ CSS Variables 복사됨!');",
     "showToast('✅ CSS Variables Copied!');"),

    # ── color-harmony.html remaining ──
    ('<div class="panel-title">Base Color 선택</div>',
     '<div class="panel-title">Base Color</div>'),
    ('분Complementary (Split-Complementary)',
     'Split-Complementary'),
    ('<div class="harmony-desc">Complementary 양쪽의 색상을 사용해 Complementary보다 부드럽고 대비가 있는 배색입니다.</div>',
     '<div class="harmony-desc">Uses colors on either side of the complement for a softer yet contrasting palette.</div>'),

    # ── color-converter.html remaining ──
    ('💡 Color Code를 모른다면 <a href="../color-picker.html">Color Picker</a>로 이미지에서 직접 추출해 보세요.',
     '💡 Don\'t know the color code? Use the <a href="../color-picker.html">Color Picker</a> to extract it from an image.'),

    # ── color-picker.html remaining ──
    ('💡 추출한 색상을 다른 형식으로 변환하려면 <a href="../color-converter.html">HEX ↔ RGB ↔ HSL 변환기</a>를 이용하세요.',
     '💡 To convert extracted colors to other formats, use the <a href="../color-converter.html">HEX ↔ RGB ↔ HSL Converter</a>.'),

    # ── HTML comments containing Korean (partial-English prefix) ──
    ('<!-- AdSense 상단 -->', '<!-- AdSense Top -->'),
    ('<!-- AdSense 중단 -->', '<!-- AdSense Mid -->'),

    # ── JS/CSS comments that don't match the general Korean-comment regex ──
    ('/* 초기 실행 */', '/* Initial run */'),
    ('/* ── CSS Variables 복사 (Tailwind 스타일) ── */', '/* ── Copy CSS Variables (Tailwind style) ── */'),
    ('// ratio: 0=원색, 1=흰색', '// ratio: 0=base, 1=white'),
    ('// ratio: 0=원색, 1=검정', '// ratio: 0=base, 1=black'),
    ('// Shades: 원색 → 검정 방향', '// Shades: base → black direction'),
    ('// Shades: 원색 → 검정 Direction', '// Shades: base → black direction'),
    ('// Direction별 (Directions)', '// By Direction'),

    # ── panel-title: partial translate (색상 팔레트 → Color Palette already ran) ──
    ('<div class="panel-title">Color Palette 입력</div>',
     '<div class="panel-title">Color Palette Input</div>'),

    # ── image-palette: tool desc (plain <p>, no id="toolDesc") ──
    ('<p>이미지를 업로드하면 Dominant Colors을 자동으로 추출합니다</p>',
     '<p>Upload any image to automatically extract its dominant color palette.</p>'),

    # ── gradient-gallery: WooaFont link text remaining after partial translate ──
    ('WooaFont에서 어울리는 폰트도 찾아보세요 →</a>',
     'find matching fonts at WooaFont →</a>'),

    # ── image-palette: 또는 + WooaImage link remaining ──
    (' 또는 <a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">WooaImage에서 이미지 편집하기 →</a>',
     ' or <a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">edit your image at WooaImage →</a>'),

    # ── color-name: cross-link tip (partially translated — Palette Generator already replaced) ──
    ('💡 Color Code를 서로 변환하려면 <a href="../color-converter.html">색상 변환기(HEX↔RGB↔HSL)</a>를 이용하세요. Color Palette가 필요하면 <a href="../palette-generator.html">Palette Generator</a>도 확인해보세요.',
     '💡 To convert color codes, use the <a href="../color-converter.html">Color Converter (HEX↔RGB↔HSL)</a>. For palette generation, see the <a href="../palette-generator.html">Palette Generator</a>.'),
]

# ── 3. 언어 선택기 CSS ────────────────────────────────────────────────────────
LANG_SWITCHER_CSS = """    .lang-switcher { display:flex; align-items:center; gap:4px; }
    .lang-switcher a { color:rgba(255,255,255,0.7); text-decoration:none; font-size:0.8rem; font-weight:600; padding:3px 8px; border-radius:12px; transition:background 0.15s; }
    .lang-switcher a.active { color:white; background:rgba(255,255,255,0.25); }
    .lang-switcher a:hover { color:white; background:rgba(255,255,255,0.18); }
    .lang-switcher span { color:rgba(255,255,255,0.3); font-size:0.75rem; }
"""

def build_page(filename, meta):
    ko_path = os.path.join(BASE, filename)
    en_path = os.path.join(EN_DIR, filename)

    with open(ko_path, encoding='utf-8') as f:
        html = f.read()

    # ── 메타 태그 교체 ──
    html = re.sub(r'<title>[^<]+</title>', f'<title>{meta["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{meta["desc"]}"', html)
    html = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{meta["kw"]}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{meta["og_title"]}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{meta["og_desc"]}"', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://colorkit.wooahouse.com/en/{filename}"', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://colorkit.wooahouse.com/en/{filename}"', html)

    # ── hreflang 추가 (canonical 바로 뒤) ──
    hreflang = (f'\n  <link rel="alternate" hreflang="ko" href="https://colorkit.wooahouse.com/{filename}">'
                f'\n  <link rel="alternate" hreflang="en" href="https://colorkit.wooahouse.com/en/{filename}">'
                f'\n  <link rel="alternate" hreflang="x-default" href="https://colorkit.wooahouse.com/en/{filename}">')
    html = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1' + hreflang, html)

    # ── ld+json 업데이트 ──
    html = re.sub(r'"name": "([^"]*[가-힣][^"]*)"', f'"name": "{meta["app_name"]}"', html)
    html = re.sub(r'"description": "([^"]*[가-힣][^"]*)"', f'"description": "{meta["desc"]}"', html)
    html = re.sub(r'"url": "https://colorkit\.wooahouse\.com/' + re.escape(filename) + '"',
                  f'"url": "https://colorkit.wooahouse.com/en/{filename}"', html)

    # ── FAQ 교체 ──
    if meta.get('faq'):
        faq_items = meta['faq']
        faq_html_parts = []
        for i, (q, a) in enumerate(faq_items):
            is_last = (i == len(faq_items) - 1)
            mb = '' if is_last else 'margin-bottom:1.2rem;'
            faq_html_parts.append(
                f'      <div class="faq-item" style="{mb}padding:1rem;background:#f8f9fa;border-radius:8px;">\n'
                f'        <h3 style="font-size:1rem;font-weight:600;margin-bottom:0.5rem;">Q. {q}</h3>\n'
                f'        <p style="color:#555;margin:0;">{a}</p>\n'
                f'      </div>'
            )
        faq_inner = '\n'.join(faq_html_parts)
        html = re.sub(
            r'<div class="faq-list">.*?</div>\s*</section>',
            f'<div class="faq-list">\n{faq_inner}\n    </div>\n  </section>',
            html, flags=re.DOTALL
        )
        # Handle <details>/<summary> FAQ format
        faq_details_parts = []
        for i, (q, a) in enumerate(faq_items):
            is_last = (i == len(faq_items) - 1)
            border = '' if is_last else 'border-bottom:1px solid #E5E7EB;'
            faq_details_parts.append(
                f'      <details style="{border}padding:16px">\n'
                f'        <summary style="font-weight:700;cursor:pointer;color:#111827">{q}</summary>\n'
                f'        <p style="margin-top:10px;color:#6B7280;line-height:1.6">{a}</p>\n'
                f'      </details>'
            )
        faq_details_inner = '\n'.join(faq_details_parts)
        html = re.sub(
            r'(<div[^>]*border[^>]*border-radius[^>]*overflow[^>]*>)\s*<details.*?</details>\s*</div>',
            r'\1\n' + faq_details_inner + '\n    </div>',
            html, flags=re.DOTALL
        )
        html = re.sub(r'<h2[^>]*>자주 묻는 질문</h2>', '<h2 style="font-size:1.4rem;margin-bottom:1.5rem;">Frequently Asked Questions</h2>', html)
        html = re.sub(r'<h2[^>]*font-weight:800[^>]*>자주 묻는 질문</h2>', '<h2 style="font-size:1.1rem;font-weight:800;color:#374151;margin-bottom:16px">Frequently Asked Questions</h2>', html)
        # ── FAQPage ld+json 교체 ──
        import json as _json
        faq_entities = []
        for q, a in faq_items:
            faq_entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
        new_faq_json = _json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }, ensure_ascii=False, indent=2)
        html = re.sub(
            r'<script type="application/ld\+json">\s*\{[^<]*"FAQPage"[^<]*\}[^<]*</script>',
            f'<script type="application/ld+json">\n{new_faq_json}\n</script>',
            html, flags=re.DOTALL
        )

    # ── cross-link banner 교체 ──
    if meta.get('cross_banner_text'):
        html = re.sub(
            r'<span style="font-size:0\.95rem;color:#444;">[^<]*</span>',
            f'<span style="font-size:0.95rem;color:#444;">{meta["cross_banner_text"]}</span>',
            html
        )
        html = re.sub(
            r'<a href="[^"]*" target="_blank" rel="noopener" style="background:#4F6EF7[^>]*>[^<]*</a>',
            f'<a href="{meta["cross_banner_href"]}" target="_blank" rel="noopener" style="background:#4F6EF7;color:#fff;padding:0.5rem 1rem;border-radius:8px;text-decoration:none;font-size:0.9rem;white-space:nowrap;">{meta["cross_banner_link_text"]}</a>',
            html
        )

    # ── Tool header (h1, desc, breadcrumb) ──
    if meta.get('h1'):
        replaced = re.sub(r'<h1 id="toolTitle">[^<]*</h1>', f'<h1 id="toolTitle">{meta["h1"]}</h1>', html)
        if replaced == html:
            replaced = re.sub(r'<h1>([^<]*)</h1>', f'<h1>{meta["h1"]}</h1>', html, count=1)
        html = replaced
    if meta.get('tool_desc'):
        replaced = re.sub(r'<p id="toolDesc">[^<]*</p>', f'<p id="toolDesc">{meta["tool_desc"]}</p>', html)
        html = replaced
    if meta.get('breadcrumb'):
        html = re.sub(r'<span id="breadcrumbTitle">[^<]*</span>', f'<span id="breadcrumbTitle">{meta["breadcrumb"]}</span>', html)

    # ── 공통 문자열 치환 ──
    for ko, en in COMMON:
        html = html.replace(ko, en)

    # ── color-name.html: kr:'...' 필드 영어화 ──
    html = re.sub(r", kr:'[^']*'", ", kr:''", html)

    # ── 한국어 JS 주석 제거 ──
    html = re.sub(r'// ——— [가-힣\w\s·]+ ———', '// ───', html)
    html = re.sub(r'// [가-힣][가-힣\w\s·:()]*$', '//', html, flags=re.MULTILINE)
    html = re.sub(r'/\* ── [가-힣][가-힣\w\s·:()]+ ── \*/', '/* ── */', html)
    html = re.sub(r'<!-- [가-힣][가-힣\w\s·]+ -->', '<!-- -->', html)

    # ── 언어 선택기 CSS 삽입 ──
    if 'lang-switcher' not in html:
        html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)

    # ── 헤더에 언어 선택기 삽입 (기존 header-right 먼저 제거) ──
    html = re.sub(
        r'\s*<div class="header-right">.*</div>(?=\s*\n?\s*</div>\s*\n?</header>)',
        '',
        html, count=1, flags=re.DOTALL
    )
    html = re.sub(
        r'(\s*</div>\s*</header>)',
        f'\n    <div class="header-right">\n'
        f'      <div class="lang-switcher">\n'
        f'        <a href="../{filename}">KO</a>\n'
        f'        <span>|</span>\n'
        f'        <a href="{filename}" class="active">EN</a>\n'
        f'      </div>\n'
        f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</header>',
        html, count=1
    )

    # ── 영어 버전: 쿠팡 완전 제거 ──
    html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
    html = re.sub(
        r'<!-- Coupang Partners -->\s*<div[^>]*>.*?</div>',
        '',
        html, flags=re.DOTALL
    )
    html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
    html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)
    # index 사이드바의 쿠팡 카드 제거
    html = re.sub(
        r'<div class="index-ad-card"[^>]*>\s*<script>\s*new PartnersCoupang\.G\([^)]*\).*?</script>\s*</div>',
        '',
        html, flags=re.DOTALL
    )

    # ── og:locale 교체 ──
    html = html.replace('content="ko_KR"', 'content="en_US"')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  OK en/{filename}')


# ── 4. 실행 ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Building English pages for ColorKit...')
    for filename, meta in PAGE_META.items():
        ko_path = os.path.join(BASE, filename)
        if os.path.exists(ko_path):
            build_page(filename, meta)
        else:
            print(f'  SKIP {filename} not found')

    # about, privacy 처리
    ABOUT_EXTRA = [
        ('<title>서비스 소개 | WooaColor - 무료 온라인 색상 도구 모음</title>',
         '<title>About WooaColor – Free Online Color Tools</title>'),
        ('<meta name="description" content="WooaColor은 HEX·RGB·HSL 변환, 색상 추출, 그라디언트·팔레트 생성, WCAG 대비 검사, CSS 그림자 도구를 무료로 제공하는 서비스입니다.">',
         '<meta name="description" content="WooaColor is a free online color toolkit offering HEX/RGB/HSL conversion, color picker, gradient and palette generation, WCAG contrast checking, and CSS shadow tools.">'),
        ('<meta property="og:title" content="서비스 소개 | WooaColor">',
         '<meta property="og:title" content="About WooaColor – Free Online Color Tools">'),
        ('<meta property="og:description" content="무료 온라인 색상 도구 모음 WooaColor 서비스 소개입니다.">',
         '<meta property="og:description" content="WooaColor is a free online color toolkit for designers and developers. Learn about our tools and features.">'),
        ('<h1 style="font-size:1.8rem;">WooaColor 서비스 소개</h1>',
         '<h1 style="font-size:1.8rem;">About WooaColor</h1>'),
        ('<h1>서비스 소개</h1>', '<h1>About WooaColor</h1>'),
        ('<p>무료 온라인 색상 도구 모음 서비스</p>', '<p>Free Online Color Toolkit</p>'),
        ('<h2>WooaColor이란?</h2>', '<h2>What is WooaColor?</h2>'),
        ('<h2>WooaColor란?</h2>', '<h2>What is WooaColor?</h2>'),
        ('WooaColor은 누구나 쉽게 색상 작업을 할 수 있도록 도와주는 <strong>무료 온라인 색상 도구 서비스</strong>입니다.',
         'WooaColor is a <strong>free online color toolkit</strong> for designers and developers who need fast, accurate color tools.'),
        ('회원가입이나 프로그램 설치 없이 웹 브라우저에서 바로 사용할 수 있으며,',
         'No sign-up or installation needed — open your browser and start working immediately.'),
        ('모든 처리가 사용자의 브라우저 안에서 이루어집니다.',
         'All processing happens entirely within your browser.'),
        ('<h2>제공 서비스</h2>', '<h2>Our Tools</h2>'),
        ('<h2>핵심 특징</h2>', '<h2>Key Features</h2>'),
        ('<strong>🔒 완전한 Privacy Protected</strong>',
         '<strong>🔒 100% Private</strong>'),
        ('업로드한 파일은 서버로 전송되거나 저장되지 않습니다.',
         'No data is ever sent to or stored on any server.'),
        ('모든 처리는 사용자의 컴퓨터(브라우저) 안에서만 이루어집니다.',
         'All processing happens only inside your computer (browser).'),
        ('<strong>⚡ 빠른 처리 속도</strong>',
         '<strong>⚡ Instant Results</strong>'),
        ('서버 업로드 대기 없이 로컬에서 직접 처리하므로',
         'Local processing means'),
        ('인터넷 속도와 관계없이 빠르게 작업할 수 있습니다.',
         'results are instant regardless of internet speed.'),
        ('<strong>💸 완전 무료</strong> — 모든 기능을 제한 없이 무료로 사용할 수 있습니다.',
         '<strong>💸 Completely Free</strong> — All features are available for free with no limitations.'),
        ('회원가입, 로그인, 유료 결제가 전혀 필요하지 않습니다.',
         'No sign-up, no login, no payment required.'),
        ('<strong>📱 모든 기기 지원</strong>',
         '<strong>📱 All Devices</strong>'),
        ('사용할 수 있는 반응형 디자인을 지원합니다.',
         'Responsive design ensures a great experience on any screen.'),
        ('<strong>🌐 설치 불필요</strong> — 별도의 소프트웨어를 설치할 필요 없이',
         '<strong>🌐 No Installation</strong> — No software to install.'),
        ('웹 브라우저만 있으면 어디서든 사용할 수 있습니다.',
         'All you need is a web browser.'),
        ('<h2>이용 방법</h2>', '<h2>How to Use</h2>'),
        ('<p>모든 도구는 동일한 방식으로 사용할 수 있습니다:</p>',
         '<p>All tools are straightforward to use:</p>'),
        ('<h2>기술 정보</h2>', '<h2>Technical Info</h2>'),
        ('WooaColor은 최신 웹 기술을 활용하여 구현되었습니다.',
         'WooaColor is built with modern web technologies.'),
        ('모든 처리는 클라이언트 사이드(브라우저)에서 이루어지며, 어떠한 파일도 서버로 전송되지 않습니다.',
         'All processing is client-side (in the browser) — no data is ever sent to a server.'),
        ('지원 브라우저: Chrome, Edge, Firefox, Safari (최신 버전 권장)',
         'Supported browsers: Chrome, Edge, Firefox, Safari (latest version recommended)'),
        ('<h2>문의</h2>', '<h2>Contact</h2>'),
        ('서비스 이용 중 문제가 발생하거나 개선 제안이 있으시면 언제든지 연락해 주세요.',
         'If you experience any issues or have suggestions, feel free to reach out.'),
        ('더 나은 서비스를 만들기 위해 사용자 여러분의 의견을 소중히 여깁니다.',
         'We value your feedback and are always working to improve WooaColor.'),
        # post-COMMON partial transforms
        ('<li>Complementary·Analogous·Triadic 팔레트 생성</li>',
         '<li>Complementary, Analogous, and Triadic palette generation</li>'),
        ('<li>WCAG AA·AAA 접근성 Contrast Ratio 검사</li>',
         '<li>WCAG AA/AAA accessibility contrast ratio check</li>'),
        ('<li>Opacity 변환 (rgba / 8-digit HEX / hsla)</li>',
         '<li>Opacity conversion (rgba / 8-digit HEX / hsla)</li>'),
        ('도구 추가 요청, Error 제보, 제휴 문의 등은 아래 이메일로 연락 주세요.',
         'For tool requests, bug reports, or partnership inquiries, contact us by email.'),
        # remaining about.html Korean
        ('<li>HEX, RGB, HSL 세 가지 색상 코드 상호 변환</li>',
         '<li>Convert between HEX, RGB, and HSL color codes</li>'),
        ('<li>이미지에서 색상 직접 추출 (캔버스 픽셀 샘플링)</li>',
         '<li>Extract colors from images (canvas pixel sampling)</li>'),
        ('<li>CSS 그라디언트 코드 즉시 생성</li>',
         '<li>Instant CSS gradient code generation</li>'),
        ('<li>모든 처리가 브라우저 안에서 완결 — 서버로 데이터 전송 없음</li>',
         '<li>All processing happens in the browser — no data sent to any server</li>'),
        ('<li>회원가입 없이 무제한 무료 사용</li>',
         '<li>Unlimited free use with no sign-up required</li>'),
        ('<li>PC·태블릿·스마트폰 반응형 지원</li>',
         '<li>Responsive support for PC, tablet, and smartphone</li>'),
        ('<h2>🏠 WooaHouse 네트워크</h2>',
         '<h2>🏠 WooaHouse Network</h2>'),
        ('<p>WooaColor은 WooaHouse가 운영하는 서비스 중 하나입니다. 현재 운영 중인 서비스:</p>',
         '<p>WooaColor is one of the services operated by WooaHouse. Currently running:</p>'),
        ('<h2>📬 문의</h2>', '<h2>📬 Contact</h2>'),
    ]
    PRIVACY_EXTRA = [
        ('<title>개인정보처리방침 | WooaColor</title>',
         '<title>Privacy Policy | WooaColor</title>'),
        ('<meta name="description" content="WooaColor 개인정보처리방침입니다.">',
         '<meta name="description" content="WooaColor Privacy Policy. We do not collect personal data. All color processing happens in your browser.">'),
        ('<h1 style="font-size:1.8rem;">개인정보처리방침</h1>',
         '<h1 style="font-size:1.8rem;">Privacy Policy</h1>'),
        ('<h1>개인정보처리방침</h1>', '<h1>Privacy Policy</h1>'),
        ('시행일:', 'Effective:'),
        ('최종 수정일:', 'Last updated:'),
        ('WooaColor(이하 "당사" 또는 "서비스")은 사용자의 Privacy Protected를 매우 중요하게 생각합니다.',
         'WooaColor ("we" or "the Service") takes your privacy seriously.'),
        ('본 개인정보처리방침은 당사가 제공하는 서비스를 이용하는 과정에서 수집되는 정보와',
         'This Privacy Policy explains what information is collected when you use our service'),
        ('그 처리 방법에 대해 안내합니다.', 'and how it is handled.'),
        ('<h2>1. 수집하는 정보</h2>', '<h2>1. Information We Collect</h2>'),
        ('<h3>1-1. 파일 정보 (서버 미전송)</h3>', '<h3>1-1. Color Data (Never Sent to Server)</h3>'),
        ('<strong>WooaColor에서 처리하는 모든 색상 데이터는 사용자의 브라우저에서만 처리됩니다.</strong>',
         '<strong>All data processed by WooaColor is handled entirely within your browser.</strong>'),
        ('<h3>1-2. 자동 수집 정보</h3>', '<h3>1-2. Automatically Collected Information</h3>'),
        ('<p>서비스 개선 및 통계 목적으로 다음 정보가 자동으로 수집될 수 있습니다:</p>',
         '<p>The following information may be collected automatically for analytics and service improvement:</p>'),
        ('<li>접속 IP 주소 (익명 처리됨)</li>', '<li>IP address (anonymized)</li>'),
        ('<li>브라우저 종류 및 버전</li>', '<li>Browser type and version</li>'),
        ('<li>방문한 pages, 접속 시간</li>', '<li>Pages visited and access time</li>'),
        ('<li>운영체제 정보</li>', '<li>Operating system information</li>'),
        ('<li>유입 경로 (검색어, 이전 방문 사이트)</li>', '<li>Referral source (search terms, referring site)</li>'),
        ('<p>이 정보는 개인을 식별하는 데 사용되지 않으며, 서비스 개선을 위한 통계 분석에만 활용됩니다.</p>',
         '<p>This information is not used to identify individuals and is used only for statistical analysis.</p>'),
        ('<h2>2. 쿠키 및 광고</h2>', '<h2>2. Cookies &amp; Advertising</h2>'),
        ('<h3>2-1. 쿠키</h3>', '<h3>2-1. Cookies</h3>'),
        ('당사는 서비스 편의성 향상을 위해 쿠키를 사용할 수 있습니다.',
         'We may use cookies to improve your experience.'),
        ('<h3>2-2. Google 애드센스</h3>', '<h3>2-2. Google AdSense</h3>'),
        ('당사는 서비스 운영 비용 충당을 위해 Google 애드센스를 통한 광고를 표시할 수 있습니다.',
         'We may display ads via Google AdSense to cover service costs.'),
        ('<h3>2-3. Google 애널리틱스</h3>', '<h3>2-3. Google Analytics</h3>'),
        ('당사는 방문자 통계 분석을 위해 Google 애널리틱스를 사용할 수 있습니다.',
         'We may use Google Analytics to analyze visitor statistics.'),
        ('수집된 데이터는 익명화 처리되어 개인을 식별하는 데 사용되지 않습니다.',
         'Collected data is anonymized and not used to identify individuals.'),
        ('<h2>3. 개인정보의 이용 목적</h2>', '<h2>3. Purpose of Data Use</h2>'),
        ('<p>수집된 정보는 다음 목적으로만 사용됩니다:</p>',
         '<p>Collected information is used only for the following purposes:</p>'),
        ('<li>서비스 제공 및 개선</li>', '<li>Providing and improving the service</li>'),
        ('<li>서비스 이용 통계 분석</li>', '<li>Statistical analysis of service usage</li>'),
        ('<li>기술적 문제 해결</li>', '<li>Troubleshooting technical issues</li>'),
        ('<li>서비스 보안 및 악용 방지</li>', '<li>Service security and abuse prevention</li>'),
        ('<h2>4. 개인정보의 제3자 제공</h2>', '<h2>4. Sharing with Third Parties</h2>'),
        ('당사는 다음의 경우를 제외하고 사용자의 개인정보를 제3자에게 제공하지 않습니다:',
         'We do not share personal information with third parties except in the following cases:'),
        ('<li>사용자의 명시적 동의가 있는 경우</li>', '<li>With explicit user consent</li>'),
        ('<li>법령에 의하거나 수사기관의 요청이 있는 경우</li>',
         '<li>As required by law or requested by law enforcement</li>'),
        ('<h2>5. Privacy Protected 조치</h2>', '<h2>5. Privacy Protection Measures</h2>'),
        ('<li>모든 색상 처리는 사용자 브라우저 내에서만 이루어집니다</li>',
         '<li>All color processing happens only within your browser</li>'),
        ('<li>HTTPS를 통한 암호화 통신을 사용합니다</li>',
         '<li>Encrypted communication via HTTPS</li>'),
        ('<li>불필요한 개인정보를 수집하지 않습니다</li>',
         '<li>We do not collect unnecessary personal information</li>'),
        ('<li>수집된 통계 데이터는 익명화하여 보관합니다</li>',
         '<li>Statistical data is anonymized before storage</li>'),
        ('<h2>6. 사용자의 권리</h2>', '<h2>6. Your Rights</h2>'),
        ('<p>사용자는 언제든지 다음 권리를 행사할 수 있습니다:</p>',
         '<p>You may exercise the following rights at any time:</p>'),
        ('<li>개인정보 수집 및 이용에 대한 동의 철회</li>',
         '<li>Withdraw consent for data collection and use</li>'),
        ('<li>쿠키 사용 거부 (브라우저 설정에서 가능)</li>',
         '<li>Refuse cookies (via browser settings)</li>'),
        ('<li>개인정보 처리 관련 문의 및 이의 제기</li>',
         '<li>Submit inquiries or objections regarding data handling</li>'),
        ('<h2>7. 아동의 Privacy Protected</h2>', '<h2>7. Children\'s Privacy</h2>'),
        ('당사의 서비스는 만 14세 미만 아동을 대상으로 하지 않습니다.',
         'Our service is not directed at children under 14 years of age.'),
        ('만 14세 미만 아동의 개인정보를 의도적으로 수집하지 않습니다.',
         'We do not intentionally collect personal information from children under 14.'),
        ('<h2>8. 개인정보처리방침의 변경</h2>', '<h2>8. Changes to This Policy</h2>'),
        ('본 개인정보처리방침은 법령 또는 서비스 변경에 따라 수정될 수 있습니다.',
         'This Privacy Policy may be updated in response to legal or service changes.'),
        ('<h2>9. 문의</h2>', '<h2>9. Contact</h2>'),
        ('개인정보 처리에 관한 문의 사항이 있으시면 아래로 연락해 주세요.<br>',
         'If you have any questions about this Privacy Policy, please contact us:<br>'),
        ('서비스명: WooaColor<br>', 'Service: WooaColor<br>'),
        ('이메일 문의는 서비스 내 문의 기능을 통해 주시기 바랍니다.',
         'Contact: linker@wooahouse.com'),
    ]

    for f in ['about.html', 'privacy.html']:
        src = os.path.join(BASE, f)
        dst = os.path.join(EN_DIR, f)
        if os.path.exists(src):
            with open(src, encoding='utf-8') as fp:
                html = fp.read()
            for ko, en in COMMON:
                html = html.replace(ko, en)
            html = html.replace('<html lang="ko">', '<html lang="en">')
            html = html.replace('content="ko_KR"', 'content="en_US"')
            extras = ABOUT_EXTRA if f == 'about.html' else PRIVACY_EXTRA
            for ko, en in extras:
                html = html.replace(ko, en)
            # canonical & og:url
            html = re.sub(r'<link rel="canonical" href="[^"]*"',
                          f'<link rel="canonical" href="https://colorkit.wooahouse.com/en/{f}"', html)
            html = re.sub(r'<meta property="og:url" content="[^"]*"',
                          f'<meta property="og:url" content="https://colorkit.wooahouse.com/en/{f}"', html)
            # lang switcher CSS
            if 'lang-switcher' not in html:
                html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)
            # lang switcher HTML: remove existing header-right then insert EN version
            html = re.sub(
                r'\s*<div class="header-right">.*</div>(?=\s*\n?\s*</div>\s*\n?</header>)',
                '',
                html, count=1, flags=re.DOTALL
            )
            html = re.sub(
                r'(\s*</div>\s*</header>)',
                f'\n    <div class="header-right">\n'
                f'      <div class="lang-switcher">\n'
                f'        <a href="../{f}">KO</a>\n'
                f'        <span>|</span>\n'
                f'        <a href="{f}" class="active">EN</a>\n'
                f'      </div>\n'
                f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
                f'    </div>\n'
                f'  </div>\n'
                f'</header>',
                html, count=1
            )
            # 쿠팡 완전 제거
            html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
            html = re.sub(r'<!-- Coupang Partners -->\s*<div[^>]*>.*?</div>', '', html, flags=re.DOTALL)
            html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
            html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)
            with open(dst, 'w', encoding='utf-8') as fp:
                fp.write(html)
            print(f'  OK en/{f}')

    total = len(PAGE_META) + 2
    print(f'\nDone! {total} files generated in en/')
