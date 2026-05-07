param(
    [string]$OutputPath = "print/presentasjoner/2026-05-05-ressursoversikt-og-gapanalyse.pptx"
)

$ErrorActionPreference = "Stop"
$workspaceRoot = Split-Path -Parent $PSScriptRoot

function Get-PythonExe {
    $candidates = @(
        (Join-Path $workspaceRoot ".venv\\Scripts\\python.exe"),
        (Get-Command python -ErrorAction SilentlyContinue | ForEach-Object { $_.Source })
    ) | Where-Object { $_ -and (Test-Path $_) } | Select-Object -Unique

    if (-not $candidates) {
        throw "Fant ingen Python-kjørbar for å generere grafikken."
    }

    return $candidates[0]
}

function U {
    param([string]$Text)
    $escaped = $Text.Replace('"', '\"')
    return ConvertFrom-Json ('"' + $escaped + '"')
}

function Set-Text {
    param(
        $Shape,
        [string]$Text
    )

    $Shape.TextFrame.TextRange.Text = $Text
    return
}

function Add-Textbox {
    param(
        $Slide,
        [single]$Left,
        [single]$Top,
        [single]$Width,
        [single]$Height,
        [string]$Text
    )

    [void]($shape = $Slide.Shapes.AddTextbox(1, $Left, $Top, $Width, $Height))
    Set-Text -Shape $shape -Text $Text
    return $shape
}

function Add-BrandLogo {
    param(
        $Slide,
        [single]$Left,
        [single]$Top,
        [int]$TextColor
    )

    $red = 0x1831C7
    $box = $Slide.Shapes.AddShape(1, $Left, $Top, 22, 22)
    $box.Fill.ForeColor.RGB = $red
    $box.Line.Visible = 0

    $outer = $Slide.Shapes.AddShape(9, $Left + 4, $Top + 3, 14, 14)
    $outer.Fill.ForeColor.RGB = 0xFFFFFF
    $outer.Line.Visible = 0

    $inner = $Slide.Shapes.AddShape(9, $Left + 7.5, $Top + 6, 8, 8)
    $inner.Fill.ForeColor.RGB = $red
    $inner.Line.Visible = 0

    $wordmark = Add-Textbox -Slide $Slide -Left ($Left + 28) -Top ($Top - 1) -Width 120 -Height 24 -Text "Digdir"
}

function Add-FooterBrand {
    param($Slide)

    Add-BrandLogo -Slide $Slide -Left 40 -Top 500 -TextColor 0x2E3A52
}

function Add-CoverStyle {
    param($Slide)

    $navy = 0x3D2C21
    $coral = 0x6160F8

    $slide.Background.Fill.ForeColor.RGB = 0xFFFFFF

    $panel = $Slide.Shapes.AddShape(1, 175, 35, 585, 455)
    $panel.Fill.ForeColor.RGB = $navy
    $panel.Line.Visible = 0
    $panel.Rotation = 11

    $circle = $Slide.Shapes.AddShape(9, -95, 315, 245, 245)
    $circle.Fill.ForeColor.RGB = $coral
    $circle.Line.Visible = 0

    Add-BrandLogo -Slide $Slide -Left 40 -Top 28 -TextColor 0x2E3A52
}

function Add-ContentStyle {
    param(
        $Slide,
        [string]$Section
    )

    $navy = 0x3D2C21
    $red = 0x1831C7
    $yellow = 0x16B7F3

    $slide.Background.Fill.ForeColor.RGB = 0xFFFFFF

    $accent = $Slide.Shapes.AddShape(1, 40, 36, 170, 8)
    $accent.Fill.ForeColor.RGB = $red
    $accent.Line.Visible = 0

    $sectionBox = Add-Textbox -Slide $Slide -Left 40 -Top 18 -Width 240 -Height 18 -Text $Section

    $decor = $Slide.Shapes.AddShape(9, 618, -70, 160, 160)
    $decor.Fill.ForeColor.RGB = $yellow
    $decor.Line.Visible = 0

    Add-FooterBrand -Slide $Slide
}

function Apply-TitleStyle {
    param($Shape)
}

function Apply-BodyStyle {
    param(
        $Shape,
        [int]$Size = 18
    )

}

function Add-BulletSlide {
    param(
        $Presentation,
        [string]$Section,
        [string]$Title,
        [string[]]$Bullets
    )

    $slide = $Presentation.Slides.Add($Presentation.Slides.Count + 1, 12)
    Add-ContentStyle -Slide $slide -Section $Section

    $title = Add-Textbox -Slide $slide -Left 40 -Top 64 -Width 610 -Height 38 -Text $Title
    Apply-TitleStyle -Shape $title

    $body = Add-Textbox -Slide $slide -Left 58 -Top 126 -Width 610 -Height 290 -Text (($Bullets | ForEach-Object { [char]0x2022 + " " + $_ }) -join "`r")
    $tr = $body.TextFrame.TextRange
    Apply-BodyStyle -Shape $body -Size 18

    for ($i = 1; $i -le $Bullets.Count; $i++) {
        $p = $tr.Paragraphs($i)
        $p.ParagraphFormat.SpaceAfter = 10
    }
}

function Add-TwoColumnSlide {
    param(
        $Presentation,
        [string]$Section,
        [string]$Title,
        [string]$LeftTitle,
        [string[]]$LeftBullets,
        [string]$RightTitle,
        [string[]]$RightBullets
    )

    $slide = $Presentation.Slides.Add($Presentation.Slides.Count + 1, 12)
    Add-ContentStyle -Slide $slide -Section $Section

    $title = Add-Textbox -Slide $slide -Left 40 -Top 64 -Width 620 -Height 40 -Text $Title
    Apply-TitleStyle -Shape $title

    $leftPanel = $slide.Shapes.AddShape(1, 40, 126, 290, 288)
    $leftPanel.Fill.ForeColor.RGB = 0xF5F7FA
    $leftPanel.Line.ForeColor.RGB = 0xD8DEE8

    $rightPanel = $slide.Shapes.AddShape(1, 360, 126, 290, 288)
    $rightPanel.Fill.ForeColor.RGB = 0xF5F7FA
    $rightPanel.Line.ForeColor.RGB = 0xD8DEE8

    $leftText = Add-Textbox -Slide $slide -Left 56 -Top 144 -Width 258 -Height 250 -Text ($LeftTitle + "`r" + (($LeftBullets | ForEach-Object { [char]0x2022 + " " + $_ }) -join "`r"))
    $rightText = Add-Textbox -Slide $slide -Left 376 -Top 144 -Width 258 -Height 250 -Text ($RightTitle + "`r" + (($RightBullets | ForEach-Object { [char]0x2022 + " " + $_ }) -join "`r"))

    foreach ($shape in @($leftText, $rightText)) {
        $tr = $shape.TextFrame.TextRange
        Apply-BodyStyle -Shape $shape -Size 16
        for ($i = 2; $i -le $tr.Paragraphs().Count; $i++) {
            $p = $tr.Paragraphs($i)
            $p.ParagraphFormat.SpaceAfter = 8
        }
    }
}

function Add-TableSlide {
    param(
        $Presentation,
        [string]$Section,
        [string]$Title,
        [string[]]$Headers,
        [object[][]]$Rows,
        [string]$Footer
    )

    $slide = $Presentation.Slides.Add($Presentation.Slides.Count + 1, 12)
    Add-ContentStyle -Slide $slide -Section $Section

    $title = Add-Textbox -Slide $slide -Left 40 -Top 64 -Width 620 -Height 40 -Text $Title
    Apply-TitleStyle -Shape $title

    $tableShape = $slide.Shapes.AddTable($Rows.Count + 1, $Headers.Count, 40, 122, 640, 295)
    $table = $tableShape.Table

    for ($c = 1; $c -le $Headers.Count; $c++) {
        $cell = $table.Cell(1, $c)
        $cell.Shape.TextFrame.TextRange.Text = [string]$Headers[$c - 1]
        $cell.Shape.Fill.ForeColor.RGB = 0x3D2C21
    }

    for ($r = 0; $r -lt $Rows.Count; $r++) {
        for ($c = 0; $c -lt $Headers.Count; $c++) {
            $cell = $table.Cell($r + 2, $c + 1)
            $cell.Shape.TextFrame.TextRange.Text = [string]$Rows[$r][$c]
            if ($r % 2 -eq 0) {
                $cell.Shape.Fill.ForeColor.RGB = 0xF7F8FB
            }
            else {
                $cell.Shape.Fill.ForeColor.RGB = 0xEEF2F6
            }
        }
    }

    $footerBox = Add-Textbox -Slide $slide -Left 42 -Top 430 -Width 610 -Height 24 -Text $Footer
}

function Add-ChartSlide {
    param(
        $Presentation,
        [string]$Section,
        [string]$Title,
        [string]$ImagePath,
        [string[]]$Bullets
    )

    $slide = $Presentation.Slides.Add($Presentation.Slides.Count + 1, 12)
    Add-ContentStyle -Slide $slide -Section $Section

    $title = Add-Textbox -Slide $slide -Left 40 -Top 64 -Width 620 -Height 40 -Text $Title
    Apply-TitleStyle -Shape $title

    $slide.Shapes.AddPicture($ImagePath, $false, $true, 40, 118, 420, 258) | Out-Null

    $panel = $slide.Shapes.AddShape(1, 486, 122, 170, 252)
    $panel.Fill.ForeColor.RGB = 0xF5F7FA
    $panel.Line.ForeColor.RGB = 0xD8DEE8

    $bulletShape = Add-Textbox -Slide $slide -Left 502 -Top 140 -Width 140 -Height 220 -Text (($Bullets | ForEach-Object { [char]0x2022 + " " + $_ }) -join "`r")
    $tr = $bulletShape.TextFrame.TextRange
    for ($i = 1; $i -le $Bullets.Count; $i++) {
        $p = $tr.Paragraphs($i)
        $p.ParagraphFormat.SpaceAfter = 10
    }
}

$outputFile = Join-Path $workspaceRoot $OutputPath
$outputDir = Split-Path -Parent $outputFile
$chartFile = Join-Path $workspaceRoot "print/presentasjoner/ressursvekt-per-kapabilitet.png"

if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$pythonExe = Get-PythonExe
& $pythonExe (Join-Path $workspaceRoot "tools/render_capability_weight_chart.py")
if ($LASTEXITCODE -ne 0 -or -not (Test-Path $chartFile)) {
    throw "Klarte ikke å generere ressursgrafen."
}

$ppt = New-Object -ComObject PowerPoint.Application
$ppt.Visible = -1
$ppt.DisplayAlerts = 1

try {
    $presentation = $ppt.Presentations.Add($true)
    while ($presentation.Slides.Count -gt 0) {
        $presentation.Slides.Item(1).Delete()
    }
    $presentation.PageSetup.SlideSize = 3

    $cover = $presentation.Slides.Add(1, 12)
    Add-CoverStyle -Slide $cover

    $coverTitle = Add-Textbox -Slide $cover -Left 250 -Top 245 -Width 340 -Height 96 -Text (U "Ressursoversikt og gapanalyse")

    $coverBody = Add-Textbox -Slide $cover -Left 250 -Top 345 -Width 330 -Height 84 -Text ((U "Status per 5. mai 2026") + "`r112 registrerte ressurser`r" + (U "Grunnlag: ressursoversikten og analysen av kapabilitetsdekning mot modenhet"))

    Add-BulletSlide -Presentation $presentation -Section "Oversikt" -Title (U "Hva oversikten viser") -Bullets @(
        (U "Repoet har 112 registrerte ressurser i siste versjon p\u00E5 tvers av operative l\u00F8sninger, normerende ressurser og samarbeidsfora.")
        (U "Operative l\u00F8sninger og tjenester dominerer portef\u00F8ljen med 78 ressurser, mens normerende ressurser utgj\u00F8r 25 og samarbeidsfora 9.")
        (U "Oversikten er strukturert slik at register, ressursfiler og kapabilitetskoblinger peker til samme siste versjon.")
        (U "Portef\u00F8ljen gir dermed et reelt grunnlag for \u00E5 analysere hvor NA-arbeidet har dekning og hvor det fortsatt mangler st\u00F8tte.")
    )

    Add-TableSlide -Presentation $presentation -Section (U "Portef\u00F8lje") -Title (U "Ressursmassen i tall") -Headers @(
        (U "Kategori"),
        (U "Antall"),
        (U "Tolkning")
    ) -Rows @(
        @((U "Operative l\u00F8sninger og tjenester"), "78", (U "Tyngdepunktet ligger fortsatt p\u00E5 l\u00F8sninger i bruk, delingsflater og registre.")),
        @((U "Normerende ressurser"), "25", (U "Dekningen er bedre enn f\u00F8r, men fortsatt mindre enn den operative portef\u00F8ljen.")),
        @((U "Samarbeidsfora"), "9", (U "Samordningsarenaer er representert, men fortsatt relativt smalt.")),
        @((U "Andre ressurser"), "0", (U "Strukturen er ryddig; nesten alt er plassert i hovedtypene.")),
        @((U "Totalt"), "112", (U "Totaloversikten er stor nok til \u00E5 brukes som faktisk analysegrunnlag."))
    ) -Footer "Kilde: web/hugo-prototype/content/ressursoversikt/_index.md"

    Add-ChartSlide -Presentation $presentation -Section "Kapabiliteter" -Title (U "Ressursvekt per toppnivå-kapabilitet") -ImagePath $chartFile -Bullets @(
        (U "Datautveksling og integrasjon skiller seg tydelig ut som det tyngste kapabilitetsområdet."),
        (U "Samarbeid, informasjonsforvaltning og datakilder danner et tydelig mellomskikt."),
        (U "Figuren er nyttig som rask porteføljeinngang før vi vurderer modenhet og gap.")
    )

    Add-TableSlide -Presentation $presentation -Section "Kapabiliteter" -Title (U "Hvor dekningen er st\u00F8rst") -Headers @(
        (U "Toppniv\u00E5-kapabilitet"),
        (U "Antall ressurser"),
        (U "Kort lesning")
    ) -Rows @(
        @((U "Datautveksling og integrasjon"), "63", (U "Portef\u00F8ljen er tydelig tyngst rundt deling, bruk og integrasjon.")),
        @((U "Samarbeid"), "32", (U "Samordning og organisatorisk samhandling er godt representert.")),
        @((U "Informasjonsforvaltning"), "28", (U "Mange ressurser ber\u00F8rer styring, begreper og oversikter.")),
        @((U "Datakilder"), "27", (U "Grunndata og nasjonale registre er en sterk del av oversikten.")),
        @((U "Tjenesteutvikling / Sluttbrukertjenester"), "22 / 22", (U "Utvikling og brukerrettet sammenheng er viktige, men svakere enn data- og integrasjonssporene."))
    ) -Footer "Kilde: analyser/Modenhetsanalyser/2026-05-05-prioritering-av-kapabiliteter-basert-pa-modenhet-og-ressursdekning.md"

    Add-BulletSlide -Presentation $presentation -Section (U "M\u00F8nstre") -Title (U "Hva som preger dekningen") -Bullets @(
        (U "De sterkest dekkede delkapabilitetene er \u00E5 dele data med andre, grunndata, bruke data fra andre og organisatorisk samhandling."),
        (U "Det betyr at ressursoversikten allerede er mest moden som beslutningsgrunnlag i problemrom som handler om datadeling, registre og tverrvirksomhetlig samspill."),
        (U "H\u00F8y dekning betyr likevel ikke automatisk at omr\u00E5det er godt nok l\u00F8st; det kan ogs\u00E5 bety at mange ressurser er avhengige av samme svake grunnkapabilitet.")
    )

    Add-TwoColumnSlide -Presentation $presentation -Section "Prioritet" -Title (U "Prioriterte kapabiliteter med st\u00F8rst systemeffekt") -LeftTitle (U "B\u00F8r prioriteres f\u00F8rst") -LeftBullets @(
        (U "Bruke data fra andre: lav modenhet, 20 ber\u00F8rte ressurser"),
        (U "Sammenhengende tjenester: lav modenhet, 20 ber\u00F8rte ressurser"),
        (U "Datastyring: lav modenhet, 17 ber\u00F8rte ressurser")
    ) -RightTitle (U "Hvorfor disse skiller seg ut") -RightBullets @(
        (U "De kombinerer lav modenhet med h\u00F8y ressursdekning."),
        (U "Svikt her rammer mange deler av portef\u00F8ljen samtidig."),
        (U "Tiltak her vil sannsynligvis gi st\u00F8rst effekt p\u00E5 tvers av ressurser og case.")
    )

    Add-TwoColumnSlide -Presentation $presentation -Section "Gap" -Title (U "Viktigste gap og blinde flekker") -LeftTitle (U "Svakt dekkede, men viktige") -LeftBullets @(
        (U "Finansiering: lav modenhet, 0 ressurser"),
        (U "Juridisk samhandling: lav modenhet, 0 ressurser"),
        (U "Sanntidsdata: lav modenhet, 0 ressurser"),
        (U "Testdata: lav modenhet, 0 ressurser")
    ) -RightTitle (U "Hva dette betyr") -RightBullets @(
        (U "Repoet peker p\u00E5 styrings- og samhandlingsproblemer som ikke er oversatt til tydelige ressurser enn\u00E5."),
        (U "Gapene b\u00F8r ikke bare leses som manglende dokumentasjon, men som kandidater for nye normerende ressurser, fora eller eksplisitte analyseobjekter."),
        (U "S\u00E6rlig juridisk samhandling og finansiering framst\u00E5r som underrepresenterte i dagens ressursmasse.")
    )

    Add-BulletSlide -Presentation $presentation -Section "Funn" -Title (U "Viktigste funn for videre arbeid") -Bullets @(
        (U "Ressursoversikten er n\u00E5 stor nok og strukturert nok til \u00E5 brukes som faktisk analysegrunnlag, ikke bare som arbeidsliste."),
        (U "Det st\u00F8rste gevinstomr\u00E5det ligger i kapabiliteter som mange ressurser allerede er avhengige av, men som fortsatt har lav modenhet."),
        (U "Portef\u00F8ljen er sterk p\u00E5 operative og datan\u00E6re ressurser, men svakere p\u00E5 styringsmessige og juridiske gapomr\u00E5der."),
        (U "Neste trinn b\u00F8r kombinere videre ressursbygging med m\u00E5lrettet styrking av kapabilitetene bruke data fra andre, sammenhengende tjenester og datastyring.")
    )

    Add-BulletSlide -Presentation $presentation -Section "Neste steg" -Title (U "Anbefalt oppf\u00F8lging") -Bullets @(
        (U "Bruk de tre prioriterte kapabilitetene som felles inngang til neste analyse- og ressursbatch."),
        (U "Bygg opp bedre ressursdekning for finansiering, juridisk samhandling og sanntids-/testdata som egne gapspor."),
        (U "Bruk ressursoversikten aktivt i presentasjoner og beslutningsunderlag, siden den viser siste versjon per ressurs med konsistent kobling til kapabiliteter.")
    )

    $presentation.SaveAs($outputFile)
    $presentation.Close()
}
finally {
    $ppt.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
