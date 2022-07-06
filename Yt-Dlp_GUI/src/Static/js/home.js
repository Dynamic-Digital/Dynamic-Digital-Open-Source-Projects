function showDownloadInfo(description, title, thumbnail, views) {
    // btnGrid = document.getElementById("buttonGrid")
    btn = document.createElement("input")
    btn.value = title
    btn.style = "height: 50px; margin: 5px;"
    btn.type = "button"
    btn.onclick = function buttonact(params) {
        document.getElementById("videoTitle").innerHTML = title
        document.getElementById("videoViews").innerHTML = "Total Views: " + views
        document.getElementById("videoInfoThumbnail").src = thumbnail
        document.getElementById("videoDescription").innerHTML = description
        server.PrintInput(description)
    }
    document.getElementById("buttonGrid").appendChild(btn)
}