param([string[]]$Files)
# Render DOCX/PPTX to PDF via Office COM (no LibreOffice on this machine).
$ErrorActionPreference = "Stop"
$word = $null; $ppt = $null
try {
  foreach ($f in $Files) {
    $full = (Resolve-Path $f).Path
    $pdf  = [System.IO.Path]::ChangeExtension($full, ".pdf")
    $ext  = [System.IO.Path]::GetExtension($full).ToLower()
    if ($ext -eq ".docx") {
      if ($null -eq $word) { $word = New-Object -ComObject Word.Application; $word.Visible = $false; $word.DisplayAlerts = 0 }
      $doc = $word.Documents.Open($full, $false, $true)
      # 17 = wdExportFormatPDF
      $doc.ExportAsFixedFormat($pdf, 17)
      $doc.Close($false)
      Write-Output "PDF  $pdf"
    } elseif ($ext -eq ".pptx") {
      if ($null -eq $ppt) { $ppt = New-Object -ComObject PowerPoint.Application }
      $pres = $ppt.Presentations.Open($full, $true, $false, $false)
      # 32 = ppSaveAsPDF
      $pres.SaveAs($pdf, 32)
      $pres.Close()
      Write-Output "PDF  $pdf"
    }
  }
} finally {
  if ($word) { $word.Quit() | Out-Null; [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
  if ($ppt)  { $ppt.Quit()  | Out-Null; [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) }
  [System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers()
}
