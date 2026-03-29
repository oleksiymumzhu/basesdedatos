use db_10000;

db.dispositivo.aggregate([
  { $match: { ID: 2821 } },
  { $lookup: { from: "lectura", localField: "ID", foreignField: "DispositivoID", as: "historial" } }
]);


db.lectura.updateMany(
  { Fecha: "2026-03-27" },
  { $set: { Estado: "Revisado" } }
);

db.lectura.createIndex({ Fecha: 1 });

db.lectura.deleteMany({ Estado: "Activo" });

db.stats();