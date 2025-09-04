const expenseData = {
            labels: ['Hyra', 'Mat', 'Transport', 'Nöjen', 'Övrigt'],
            datasets: [{
                label: 'Utgifter',
                data: [9500, 1240, 720, 600, 400],
                backgroundColor: ['#f87171','#fbbf24','#60a5fa','#34d399','#a78bfa']
            }]
        };

        const expenseChart = new Chart(
            document.getElementById('expenseChart'),
            {
                type: 'doughnut',
                data: expenseData
            }
        );

        const incomeExpenseData = {
            labels: ['Inkomster', 'Utgifter'],
            datasets: [{
                label: 'Belopp',
                data: [25000, 12500],
                backgroundColor: ['#22c55e', '#ef4444']
            }]
        };

        const incomeExpenseChart = new Chart(
            document.getElementById('incomeExpenseChart'),
            {
                type: 'bar',
                data: incomeExpenseData,
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: false }
                    }
                }
            }
        );