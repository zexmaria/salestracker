// Função para adicionar uma nova linha de produto
            function addNovoProduto() {
                const container = document.getElementById('produtos-container');
                const row = document.createElement('div');
                row.classList.add('produto-row');
                const produtosOptions = document.getElementById('produtos-options').innerHTML;

                row.innerHTML = `
                    <select name="produtos[]" class="produto-select" required>
                        ${produtosOptions}
                    </select>
                    <input type="number" name="quantidades[]" placeholder="Quantidade" min="1" required>
                    <button type="button" class="add-produto" onclick="adicionarProduto(this)">ADD</button>
                `;
                container.appendChild(row);
            }

            // Função acionada ao clicar em "ADD"
            function adicionarProduto(button) {
                const row = button.parentElement;
                const selectProduto = row.querySelector('.produto-select');
                const inputQuantidade = row.querySelector('input[type="number"]');

                if (!selectProduto.value || inputQuantidade.value <= 0) {
                    alert('Por favor, selecione um produto e insira uma quantidade válida.');
                    return;
                }

                // Criar inputs ocultos para enviar os valores ao backend
                const hiddenProduto = document.createElement('input');
                hiddenProduto.type = 'hidden';
                hiddenProduto.name = 'produtos[]';
                hiddenProduto.value = selectProduto.value;

                const hiddenQuantidade = document.createElement('input');
                hiddenQuantidade.type = 'hidden';
                hiddenQuantidade.name = 'quantidades[]';
                hiddenQuantidade.value = inputQuantidade.value;

                row.appendChild(hiddenProduto);
                row.appendChild(hiddenQuantidade);

                // Tornar os campos visíveis somente leitura
                selectProduto.disabled = true;
                inputQuantidade.disabled = true;

                // Alterar o botão para "Adicionado"
                button.disabled = true;
                button.textContent = 'ADICIONADO';

                // Adicionar uma nova linha de produto
                addNovoProduto();
            }

            // Função para buscar vendas da API
            async function carregarVendas() {
                try {
                    const response = await fetch('/api/vendas/'); // Substitua pelo endpoint real da API
                    if (!response.ok) {
                        throw new Error('Erro ao buscar dados da API.');
                    }
                    const vendas = await response.json();

                    const tabela = document.querySelector('#vendas-table tbody');
                    tabela.innerHTML = ''; // Limpar a tabela antes de adicionar novos dados

                    vendas.forEach(venda => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${venda.cliente_nome}</td>
                            <td>${venda.vendedor_nome}</td>
                            <td>${venda.produtos.map(p => `${p.produto_nome} (${p.quantidade})`).join(', ')}</td>
                            <td>${venda.produtos.reduce((acc, p) => acc + p.quantidade, 0)}</td>
                            <td>R$ ${parseFloat(venda.valor_total).toFixed(2)}</td>
                        `;
                        tabela.appendChild(row);
                    });
                } catch (error) {
                    console.error(error);
                    alert('Erro ao carregar vendas. Tente novamente mais tarde.');
                }
            }

            // Inicializar a página com apenas um campo de produto
            document.addEventListener('DOMContentLoaded', () => {
                addNovoProduto();
                carregarVendas(); // Carregar vendas ao abrir a página
            });