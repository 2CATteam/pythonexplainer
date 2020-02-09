function explain() {
	var code = $('#inCodeTextArea').val();
	$.post('/peter/explain', {code: code}, (data) => {
		console.log(data)
		showCode(JSON.parse(data))
	})
}

function run() {
	var code = $('#inCodeTextArea').val();
	var input = $('#stdinArea').val();
        $.post('/peter/run', {code: code, input: input}, (data) => {
                console.log(data)
                showCode(JSON.parse(data))
		$('#stdoutArea').val(JSON.parse(data).out)
        })
}

function debug() {
	var code = $('#inCodeTextArea').val();
        $.post('/peter/Lowes', {code: code}, (data) => {
                console.log(data)
                showCode(JSON.parse(data))
        })
}

function showCode(data) {
	var code = $('#inCodeTextArea').val();
	var lines = code.split("\n")
	console.log(lines)
	$('.coderow').remove()
	for (var i in lines) {
		console.log(lines[i])
		console.log(data[i])
		let str = `<p class="coderow">${lines[i]}</p>`
		let row = $(str)
		if(data[i]) {
			row.data("data", data[i])
		} else {
			row.data("data", "Nothing to note here!")
		}
		row.click(() => {
			$("#infoTextArea").html(`<p class="coderow">${data[i] ? data[i] : "Nothing to see here!"}</p>`)
		})
		$('#outCodeTextArea').append(row)
	}
}
