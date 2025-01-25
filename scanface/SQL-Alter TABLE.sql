ALTER TABLE `scanface_tblscanface`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `detected_faces`
--
ALTER TABLE `scanface_tblscanface` MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE scanface_tblscanface MODIFY COLUMN id int(10)