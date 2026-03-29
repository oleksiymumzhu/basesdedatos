use db_100000000;

db.dispositivo.aggregate([
  { $match: { ID: 16649998 } },
  { $lookup: { from: "lectura", localField: "ID", foreignField: "DispositivoID", as: "historial" } }
]);

db.lectura.updateMany(
  { Fecha: "2026-03-27" },
  { $set: { Estado: "Revisado" } }
);

db.lectura.createIndex({ Fecha: 1 });


db.lectura.deleteMany({ Estado: "Activo" });

db.stats();

EXTRA
db.lectura.aggregate([
  { $group: { _id: "$DispositivoID", TotalLecturas: { $sum: 1 }, Promedio: { $avg: "$Valor" } } }
]);

db.dispositivo.aggregate([
  { $lookup: { from: "lectura", localField: "ID", foreignField: "DispositivoID", as: "historial" } },
  { $unwind: "$historial" },
  { $group: { _id: "$Nombre", Promedio: { $avg: "$historial.Valor" } } },
  { $sort: { Promedio: -1 } },
  { $limit: 5 }
], { allowDiskUse: true });