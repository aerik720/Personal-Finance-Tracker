fetch('/api/transactions')
  .then(response => response.json())
  .then(transaktioner => {

    let inkomster = 0;
    let utgifter = 0;

    transaktioner.forEach(tx => {
      if (tx.type === "credit") {
        inkomster += tx.amount;
      } else {
        utgifter += Math.abs(tx.amount);
      }
    });

    // Gör en knapp för att hämta excel fil
    const importBtn = document.createElement('button');
    importBtn.textContent = 'Importera Excel-fil';
    importBtn.addEventListener('click', () => {
      window.location.href = '/api/import';
    });
    document.body.appendChild(importBtn);

    document.getElementById('inkomst').textContent = `${Math.round(inkomster)} kr`;
    document.getElementById('utgift').textContent = `${Math.round(utgifter)} kr`;
    document.getElementById('saldo').textContent = `${Math.round(inkomster - utgifter)} kr`;

    // Rita stapeldiagram
    const ctx = document.getElementById('incomeExpenseChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Inkomster', 'Utgifter'],
        datasets: [{
          label: 'Belopp (kr)',
          data: [inkomster, utgifter],
          backgroundColor: ['#4CAF50', '#F44336']
        }]
      },
    });

    // Kategorisera utgifter
    let kategorier = {};
    transaktioner.forEach(tx => {
      if (tx.type === "debit") {
        let kategori = tx.description.split(" ")[0];
        kategorier[kategori] = (kategorier[kategori] || 0) + Math.abs(tx.amount);
      }
    });

    // Rita cirkeldiagram
    const ctx2 = document.getElementById('expenseChart').getContext('2d');
    new Chart(ctx2, {
      type: 'pie',
      data: {
        labels: Object.keys(kategorier),
        datasets: [{
          label: 'Största Utgifterna',
          data: Object.values(kategorier)
        }]
      }
    });

  });