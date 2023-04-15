$(document).ready(function() {
    $('#scan-form').on('submit', function(e) {
        e.preventDefault();

        var subnet = $('#subnet').val();
        var start = parseInt($('#start').val());
        var end = parseInt($('#end').val());

        // Mengirim permintaan ke server Flask
        $.ajax({
            url: '/scan_ips',
            method: 'POST',
            data: {subnet: subnet, start: start, end: end},
            success: function(response) {
                // Menampilkan hasil scan pada tabel di halaman web
                var tableBody = $('#results-table tbody');
                tableBody.empty();
                for (var i = 0; i < response.active_ips.length; i++) {
                    var ip = response.active_ips[i];
                    var ports = response.active_ports[ip] || [];

                    var row = $('<tr>');
                    row.append($('<td>').text(ip));
                    row.append($('<td>').text(ports.join(', ')));
                    tableBody.append(row);
                }

                $('#results').removeClass('d-none');
            },
            error: function(xhr, status, error) {
                alert('Terjadi kesalahan saat memindai alamat IP.');
            }
        });
    });
});